# Layouts

Used in steps 2–3. Every rule is a default; record overrides in the spec.

## Content model

A flow map has three content layers and one layout decision:

1. **Entities**: who or what is involved.
2. **Flows**: what moves between them, and in which direction.
3. **Overlay**: the argument: diagnose, prescribe, compare or quantify.
4. **Layout**: chosen last, from what the reader must compare (below).


## Layouts

| Reader must compare… | Layout | Telltale | Reading direction | Soft limit |
|---|---|---|---|---|
| **Steps**: what happens, in order | Linear | One path; who does each step doesn't matter | Left → right | ≤7 steps |
| **Handoffs**: who does what, where work passes between parties | Swimlane | Order *and* ownership matter | Left → right, one lane per actor | ≤5 lanes, ≤8 steps |
| **Layers**: how many intermediaries or levels sit between two ends | Tiered | Entities group into levels | Top → bottom by distance from the focal entity | ≤4 tiers, ≤8 entities |
| **Relationships**: who depends on or connects to whom | Network | Order weak or absent | Most important entity at the centre | ≤10 nodes |

**Tie-breakers**
- **Handoffs vs layers.** Counting actions, messages or checks *per party* → swimlane. Counting *parties* between the two ends → tiered.
- **Steps that are really layers.** When each step is owned by a different kind of organisation and participation narrows at each step, use tiered (funnel archetype).
- **Many-to-many links → network**, even when the takeaway sounds layered.
- **Compare is a modifier.** Draw the same layout twice: one view per scenario, or ≤3 small multiples.

**Tier depth.** `level: 1` is the tier closest to the **focal entity**: the customer in a supply chain, the end user in a product map, the worker in an enablement map. Name the focal entity in `layout.direction`.

**Soft limits** keep a diagram legible at a glance, on a slide or a page. When the spec exceeds one, the validator warns; propose a split or a second scenario and follow the user's call.


## Archetypes

Use the archetype that fits the goal, with its presets. Hybrids record their secondary structure in `layout.modifiers`.

| Archetype | Layout | Typical goal | Presets |
|---|---|---|---|
| **Linear value chain** | Linear | Where value is added or lost | 4–7 stages; chevrons or boxes; overlay on the stage |
| **Approval chain** | Swimlane | Where handoffs stall | Lanes by role; decision points; pain at lane crossings |
| **U-shape origin-to-destination** | Tiered | The intermediary layers between two ends | Origin column left (down), intermediary layer at the bottom (across), destination column right (up); mirror-symmetric |
| **Intermediary chain** | Tiered | Same as U-shape, where space is tight | Horizontal hops; intermediaries marked with a dashed ring so they still read as a tier |
| **Funnel** | Tiered | Participation narrowing to a central party | Wide top tier narrowing to the central party (a platform, a clearing house, an approval board) |
| **Disintermediation** | Tiered | A tier removed | Two scenarios on one base map; the removed tier ghosted |
| **Hub-and-spoke** | Network | Concentration on, or dependency on, one party | Hub centred; spokes evenly spaced; optional ring modifier for direct participants |

**Candidates** (one example each; an archetype joins the table at its second real example):
- **Foundation stack**: the worker on top, layers of enablement below, owners at the base.
