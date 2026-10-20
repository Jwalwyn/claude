# Encoding

Used in step 4. Every rule is a default; record overrides in the spec.

## Entities and flows

**Entities**
- Every entity carries a **name** (`label`) and a **role** (one line under the name, e.g. "Warehouse" / "Receives and re-ships stock").
- Bullet content inside a box goes in `details:`, three or four short lines at most.
- **Icon = what it is** (person, team, organisation, system, service, data store).
- **Role shape = what it does or which group it belongs to**: a tier band, a dashed ring for an intermediary, a container for "our organisation", an accent ring when emphasised in a scenario.
- Icons are the default; add a role shape where it carries meaning.
- Name channels and networks (an API, email, a courier network, a payment rail) as text on the flow with `via:`, and keep third-party logos off the map.

**Flows**
- Every flow has a type, a direction and, ideally, a label.
- Draw up to two flow types at full weight. With three or more, mark one type `hero` and draw the rest muted (thin grey, dashed or dotted).
- Two or more flow types → a legend, directly below the subtitle or at the bottom of the page.
- Pair each flow-type colour with a line style (solid, dashed, dotted) so the map reads in greyscale.


## Overlays

| Kind | Purpose | Drawing |
|---|---|---|
| **Diagnose** | Pain points, risks, frictions | `pain` role; severity high / medium / low sets intensity |
| **Prescribe** | Target or optimal path | Hero weight in the `improvement` role; other paths muted |
| **Compare** | Current vs future, option A vs B | One view per scenario on one base map, or ≤3 small multiples |
| **Quantify** | Volumes, costs, times | Numbers on flows or entities; line weight or node size scaled to value |

**Placement**
- **Pin** every overlay to exactly one target: an entity, a flow, a group of entities or a zone.
- Specific target → callout with a leader line. Several items on one target merge into one callout list.
- System-wide → a bubble anchored to a zone; up to two per view.
- More than four pinned callouts → numbered markers on the map, text in a side panel.
- Quantify overlays carry only numbers the user or a cited source supplied; mark any other value as a placeholder.


## Scenarios

- One **base map** holds every entity and flow across all scenarios, with positions locked.
- Each scenario is a **delta** of states on that map:

| State | Drawing |
|---|---|
| `emphasised` | Accent colour, full weight |
| `unchanged` | Neutral (the default for anything unlisted) |
| `muted` | Thin grey, dashed or dotted |
| `added` | Accent colour plus a small "new" marker |
| `removed` | **Ghosted**: dotted outline, left in place, labels faded |
| *(introduced later)* | Hidden, position reserved (`introduced_in`) |

- Each scenario carries its own action title.
- Show one view per scenario, all on the same base map: one slide each in a deck; tabs, a click-through build or an animation in HTML.


## Arrow geometry and labels

| Geometry | Meaning |
|---|---|
| Straight | One-off transfer or step |
| Right-angled (elbow) | One-off, routed around an obstacle |
| **Curved loop** | Recurring or iterative: top-ups, reconciliation, review cycles, feedback (`recurring: true`) |
| Parallel pair | Two directions or two types between the same pair |
| Double-headed | Both directions carry the same thing |

Route around obstacles with right angles, and keep curves for cycles, so a curve always means "this repeats".

**Labels.** One direction: label on or over the line. Two directions, or several flows between the same pair: parallel arrows, each labelled on its outer side.


## Colour roles

The spec names roles; the renderer maps them to the house style or template.

| Role | Use |
|---|---|
| `neutral` | Default entities and unchanged flows |
| `hero` | The emphasised flow or entity |
| `muted` | De-emphasised flows and entities |
| `pain` | Diagnose overlays |
| `improvement` | Prescribe overlays and target paths |
| `flow-type-1`, `flow-type-2`, … | One per flow type, explained in the legend |
| `ghost` | Removed items, outline only |


## Icons

Use the house style's icon library when there is one; otherwise one MIT-licensed set per map, Tabler or Lucide.

| Entity type | Tabler | Lucide |
|---|---|---|
| Person | `user` | `user` |
| Team / group | `users` | `users` |
| Organisation | `building` | `building-2` |
| Shop / merchant | `building-store` | `store` |
| Factory / supplier | `building-factory-2` | `factory` |
| System / platform | `server` | `server` |
| Service / API | `api` | `plug` |
| Data store | `database` | `database` |
| Agent / bot | `robot` | `bot` |
| Authority / regulator | `scale` | `scale` |
| Network / channel | `network` | `network` |
| Document / message | `file-text` | `file-text` |
| Goods / parcel | `package` | `package` |
| Money | `coins` | `coins` |
| Global / remote | `world` | `globe` |
