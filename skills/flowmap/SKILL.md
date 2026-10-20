---
name: flowmap
description: Flow map: design a diagram of entities and what flows between them. Use when mapping work, data, goods or money between people, teams or systems, showing handoffs or intermediaries, or comparing current and future states.
---

# Flow map

A flow map shows entities, the flows between them, and an overlay that makes one argument. You produce a spec (`flowmap.yaml`), not a picture; renderers draw it. Every rule in this skill's files is a default: when the user overrides one, follow them and record it under `overrides:` with the reason.

## 1. Grill for the goal

Run `/grilling` on the diagram until you hold three answers: what it illustrates, what it should achieve, and the decision the reader leaves with. Write the goal as one sentence, **Show that ___**. It becomes the action title.

Done when: the user has accepted a "Show that" sentence carrying one claim. Two claims → the user picks the primary one; the other becomes overlay or a second view.

## 2. Classify the takeaway

Name what the reader's eye must compare: **steps**, **handoffs**, **layers** or **relationships**. Map it to a layout with the table and tie-breakers in `LAYOUTS.md`.

Done when: one layout is chosen and every tie-breaker has been checked against it. Still ambiguous → put the choice to the user.

## 3. Match an archetype

Use the archetype in `LAYOUTS.md` that fits the goal, with its presets. Record any hybrid structure in `layout.modifiers`.

Done when: `layout.archetype` names an archetype or `generic`.

## 4. Write the spec

Write `flowmap.yaml` in the shape of `SPEC-FORMAT.md`, drawing entities, flows, overlays and scenarios by the rules in `ENCODING.md`. **Pin** every overlay to an entity, flow, group or zone. Quantify overlays carry only numbers the user or a source supplied; mark any other value as a placeholder.

Done when: every entity, flow, overlay and scenario from the grilling is in the spec.

## 5. Validate

Run `python scripts/validate.py flowmap.yaml`. Fix and re-run until it goes **green**, then walk each warning with the user. Then check what the script can't:

- The layout carries the primary takeaway; the overlay carries the secondary one.
- The action title states the "Show that" claim.
- Every quantify number traces to the user or a cited source.
- Every override has a reason the user agreed to.

Done when: zero errors, every warning is fixed or recorded under `overrides:`, and all four checks hold.
