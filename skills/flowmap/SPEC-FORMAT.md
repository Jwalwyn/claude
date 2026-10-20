# Spec format

Used in step 4. Write `flowmap.yaml` in this shape; `scripts/validate.py` checks it.

## Schema

```yaml
flowmap: 1                      # schema version

meta:
  title: string                 # action title
  subtitle: string              # optional
  goal: string                  # "Show that ___"
  illustrate: string            # grilling answer 1
  achieve: string               # grilling answer 2
  decision: string              # grilling answer 3
  audience: string
  out_of_scope: [string]        # optional

layout:
  type: linear | swimlane | tiered | network
  archetype: string | generic   # from LAYOUTS.md
  modifiers: [string]           # optional, for hybrids
  direction: string             # optional; for tiered, name the focal entity

style:
  entity_style: icons | shapes | hybrid      # default icons
  icon_set: template | tabler | lucide

flow_types:
  - id: string
    label: string               # legend text
    role: flow-type-1 | flow-type-2 | ...
    line: solid | dashed | dotted
    hero: bool                  # one type, when there are 3+

tiers:                          # tiered layouts; optional elsewhere
  - {id: string, label: string, level: int}   # 1 = closest to the focal entity

zones:                          # optional regions for bubbles and grouping
  - id: string
    label: string
    contains: [entity ids]      # or
    tier: tier id

entities:
  - id: string
    label: string               # name
    role: string                # one line under the name
    type: person | group | organisation | system | service | store | network | document
    details: [string]           # optional bullets inside the box, ≤4
    icon: string                # optional override of the type's icon
    role_shape: intermediary | own | external | none
    tier: tier id
    side: origin | destination | centre        # U-shape and chains
    lane: string                # swimlane layouts
    order: int                  # position within tier or lane
    introduced_in: scenario id  # hidden before this scenario

flows:
  - id: string
    from: entity id
    to: entity id
    type: flow type id
    label: string
    via: [string]               # rails / channels
    order: int                  # sequence number
    recurring: bool             # true → curved loop
    introduced_in: scenario id

overlays:
  - id: string
    kind: diagnose | prescribe | compare | quantify
    scope: pinned | system      # pinned → callout; system → bubble
    target:                     # exactly one of: entity, flow, entities, zone
      entity: id
    items: [string]
    severity: high | medium | low    # diagnose only
    scenarios: [scenario ids]   # default = all

scenarios:
  - id: string
    label: string
    title: string               # this scenario's action title
    base: bool                  # true for the scenario drawn as-is
    states:                     # the delta; unlisted = unchanged
      emphasised: [ids]
      muted: [ids]
      added: [ids]
      removed: [ids]

overrides:
  - {rule: string, choice: string, reason: string}
```

## Example

A trimmed spec: an online order through a marketplace warehouse, with one pain point and a second scenario that ghosts the warehouse.

```yaml
flowmap: 1
meta:
  title: Every order waits in the marketplace warehouse before the customer gets it
  goal: Show that the marketplace warehouse adds a wait to every order
  illustrate: How an online order reaches a customer through a marketplace
  achieve: Diagnose where delivery time is lost
  decision: Test shipping direct from the seller
  audience: Operations leadership
layout: {type: tiered, archetype: intermediary-chain, direction: distance from the customer}
flow_types:
  - {id: data, label: Order data, role: flow-type-1, line: dashed}
  - {id: goods, label: Goods, role: flow-type-2, line: solid}
tiers:
  - {id: ends, label: Customer and seller, level: 1}
  - {id: middle, label: Fulfilment layer, level: 2}
entities:
  - {id: customer, label: Customer, role: Orders online, type: person, tier: ends, side: origin}
  - {id: seller, label: Seller, role: Makes and packs the goods, type: organisation, tier: ends, side: destination}
  - {id: warehouse, label: Marketplace warehouse, role: Receives and re-ships stock, type: organisation, role_shape: intermediary, tier: middle}
flows:
  - {id: order, from: customer, to: seller, type: data, label: Order}
  - {id: restock, from: seller, to: warehouse, type: goods, label: Restock, recurring: true}
  - {id: ship, from: warehouse, to: customer, type: goods, label: Parcel}
  - {id: direct, from: seller, to: customer, type: goods, label: Parcel, introduced_in: direct}
overlays:
  - id: o_wait
    kind: diagnose
    scope: pinned
    target: {entity: warehouse}
    items: [Orders wait for a pick-and-pack slot]
    severity: high
    scenarios: [today]
scenarios:
  - {id: today, label: Today, base: true, title: Every order waits in the marketplace warehouse before the customer gets it}
  - id: direct
    label: Ship direct
    title: Shipping direct removes the warehouse wait but moves packing onto the seller
    states: {removed: [warehouse, restock, ship], added: [direct]}
```
