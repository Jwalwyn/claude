"""Validate a flowmap.yaml spec. Exit 0 = green (no errors); warnings are printed either way."""
import sys
import yaml

LIMITS = {"linear": ("entities", 7), "swimlane": ("entities", 8), "tiered": ("entities", 8), "network": ("entities", 10)}


def main(path):
    s = yaml.safe_load(open(path))
    errors, warnings = [], []
    ents = {e["id"] for e in s.get("entities", [])}
    flows = {f["id"]: f for f in s.get("flows", [])}
    types = {t["id"] for t in s.get("flow_types", [])}
    zones = {z["id"] for z in s.get("zones", [])}
    scen = {x["id"] for x in s.get("scenarios", [])}
    ids = ents | set(flows)

    if not s.get("meta", {}).get("goal", "").lower().startswith("show that"):
        errors.append("meta.goal must be a 'Show that ___' sentence")
    for e in s.get("entities", []):
        if not e.get("label") or not e.get("role"):
            errors.append(f"entity {e['id']}: needs label and role")
    for f in flows.values():
        for end in ("from", "to"):
            if f[end] not in ents:
                errors.append(f"flow {f['id']}: unknown {end} '{f[end]}'")
        if f.get("type") not in types:
            errors.append(f"flow {f['id']}: unknown type '{f.get('type')}'")
    for o in s.get("overlays", []):
        t = o.get("target") or {}
        if len(t) != 1:
            errors.append(f"overlay {o['id']}: pin to exactly one target")
        pools = {"entity": ents, "entities": ents, "flow": set(flows), "zone": zones}
        for k, v in t.items():
            for x in v if isinstance(v, list) else [v]:
                if x not in pools.get(k, set()):
                    errors.append(f"overlay {o['id']}: unknown {k} '{x}'")
        for sc in o.get("scenarios", []):
            if sc not in scen:
                errors.append(f"overlay {o['id']}: unknown scenario '{sc}'")
    for sc in s.get("scenarios", []):
        for state, lst in (sc.get("states") or {}).items():
            for x in lst:
                if x not in ids:
                    errors.append(f"scenario {sc['id']}: {state} has unknown id '{x}'")

    # Warnings: defaults the user may override
    if len(types) >= 2 and not all(t.get("label") for t in s.get("flow_types", [])):
        warnings.append("2+ flow types: every type needs a legend label")
    if len(types) >= 3 and not any(t.get("hero") for t in s.get("flow_types", [])):
        warnings.append("3+ flow types: mark one as hero")
    for e in s.get("entities", []):
        if len(e.get("details") or []) > 4:
            warnings.append(f"entity {e['id']}: {len(e['details'])} details, keep to 4 or fewer")
    layout = s.get("layout", {}).get("type")
    if layout == "tiered" and len(s.get("tiers", [])) > 4:
        warnings.append(f"tiered: {len(s['tiers'])} tiers exceeds soft limit 4")
    if layout in LIMITS and len(ents) > LIMITS[layout][1]:
        warnings.append(f"{layout}: {len(ents)} entities exceeds soft limit {LIMITS[layout][1]}")
    for sc in scen or {None}:
        active = [o for o in s.get("overlays", []) if sc is None or sc in o.get("scenarios", scen)]
        pinned = sum(o.get("scope") == "pinned" for o in active)
        bubbles = sum(o.get("scope") == "system" for o in active)
        if pinned > 4:
            warnings.append(f"scenario {sc}: {pinned} pinned callouts, switch to numbered markers")
        if bubbles > 2:
            warnings.append(f"scenario {sc}: {bubbles} system bubbles, max 2")

    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    print("green" if not errors else f"red: {len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(sys.argv[1])
