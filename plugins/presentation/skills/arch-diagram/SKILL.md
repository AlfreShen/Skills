---
name: arch-diagram
description: "Draw an architecture or data-flow diagram of a codebase or system as an editable draw.io file. Use when the user asks for an architecture, system, pipeline, component or data-flow diagram or a .drawio file, including updating or redrawing an existing one, and when the user asks to show how the parts of a system connect even without naming draw.io or architecture."
compatibility: "Code execution with Python 3.6+, and the draw.io desktop app or CLI for the render check (on headless Linux also xvfb)."
---

# draw.io architecture and data-flow diagrams

Diagrams of systems, pipelines or components that the user keeps editing in draw.io. The diagram's language, fonts, sizes, colour meanings, vocabulary and destination format are set per project; the rules here hold for any system.

Terms used throughout. A **part** is a unit that runs on its own (program, process, service) and is drawn as a container. A **component** is a role inside a part. A **data store** is a file, database or queue drawn at the root level. An **element** is any of these three. An **edge** is a line with an arrowhead between two elements or ports. A **port** is a small circle on a part's border, where edges enter or leave the part. A **stub** is the first edge segment between a port and the element it connects to. The **delivery note** is the text delivered with the diagram that lists what it simplifies, omits or could not check.

## Project conventions

A project may set its own conventions for this work, in its `CLAUDE.md`, its Project instructions, or files the user points to. Where they conflict with this skill, the project's conventions win; otherwise use the defaults below. A correction that holds only for one project belongs in that project's instructions, not in this skill.

Projects commonly set: diagram text language, fonts and sizes, colour meanings, fixed component and field names, target format, scale and aspect ratio, element budget, file locations, and quirks of the local draw.io install.

## Workflow

A summary; each step points to the section with the details.

1. Settle the setup and prepare the generator (section 1).
2. Fix the question and the reader, then choose the parts and the level of detail (section 2).
3. Verify every claim against the code (section 3).
4. Model the system, decide colour, draw edges and labels, add the legend, lay it out (sections 4 to 9).
5. Build or change the diagram file (section 10).
6. Check by code, render, inspect and deliver (section 11).
7. When the code changes after delivery, start again from section 3.

## 1. Before starting

- **Previous version.** Look for an earlier .drawio, PNG, generator, or a past conversation about the same system. If one exists, it is the base: keep its parts, layout and level of detail, and change only what is wrong or what the user asks for. Redrawing from scratch throws away decisions the user already made. Inherited content is not pre-verified: audit every inherited label, subtitle, edge style and legend entry as if it were new. Note a checksum of each existing file before you change anything.
- **Source of truth.** Ask the user which file is authoritative before the first change: the generator (changes go through the script) or the .drawio (the user edits by hand and the generator is retired). Regenerating overwrites hand edits.
- **Destination.** Settle the target format, scale and aspect ratio from the project's conventions, or ask. Default for a slide: PNG at 300 %, with an aspect ratio matching the slide's free area (a full 16:9 slide is about 1.78 : 1). Reason: 300 % keeps text sharp when projected or printed, and a matching ratio avoids cropping or empty bands in the slide. Prefer PNG over SVG (`references/drawio-cli.md` explains why).
- **Slide decks.** When the diagram goes into a deck, the `slides` skill governs the deck (captions, numbering, figure-to-system correspondence) and this skill governs how the diagram is drawn.
- **Tools.** Check that Python 3.6 or later (`python3 --version`) and a draw.io CLI (`references/drawio-cli.md`: locating it, installing it, export flags) are available. If draw.io is missing, ask now whether to install it. If it cannot be installed, the diagram can still be built but the render check cannot be done: say so before starting, and at delivery list which checks were not done.
- **Language.** Diagram text uses the language in the project's conventions; without one, the language of the user's request.
- **Generator.** Used when the generator is the source of truth or no previous version exists; when the .drawio is the source of truth, skip this. Copy `scripts/drawio_gen.py` from this skill's folder next to the diagram's generator script, and read `references/generator-api.md` (usage rules, functions, built-in geometry) before writing the script. The script is imported, not read.

## 2. Choosing the level of detail

Granularity follows the question and the reader, never the amount of detail available.

1. **Write the question in one sentence**, naming the system and what the reader must learn from the diagram. If it cannot be written, ask the user one question before drawing. One diagram per question and reader.
2. **Set the unit of an element by what the reader does with it.**
   - Readers who do not read code: an element is something that could be replaced or deployed on its own (a service, a capability). Merge steps the reader does not need to tell apart; use plain-language subtitles; mark everything not running for real (simulated, offline, planned) so the diagram does not overstate what exists.
   - Readers who review code: an element is something they would open in an editor (a function or file); subtitles carry code names.
   - Every element in one diagram sits at the same level.
3. **Deletion test, for every component and every edge.** Keep it only if removing it would leave the question unanswerable or make the reader believe something false about the system. "True and more complete" is not a reason to keep it.
4. **Separate the system the diagram is about from the tooling that runs or tests it** (orchestration, deployment, retries, test harnesses, feature switches). That tooling goes in a separate diagram or in the delivery note, unless the question is about it.
5. **Conditional paths** (flags, alternative policies or modes) are drawn only when the question is about them or the user asks; otherwise list them in the delivery note. When drawn, they use a dashed outline and dashed edges (`COND`) with their own legend row; keep them few, since each adds edges. A component that is active only under a condition says so in its subtitle. A path that is unverified rather than conditional is drawn solid, with "unverified" in its label: a dashed outline or edge means conditional and nothing else.
6. **Budget per diagram.** Default for a slide: about 5 parts, 15 components and 20 edges (the project's conventions may change it). Reason: beyond this, text at slide size drops below a legible size and forced crossings multiply. Over budget, split into an overview plus drill-down pages linked within the same file (`page`, `page_link`) rather than collapsing parts.
7. **Coarse first.** Deliver the coarse version, then add detail where the user asks. Adding detail is easy to judge; removing it is not.

## 3. Verify against the code

Read the project's own overview documents first, then the code. Check every claim the diagram will make:

- the data crossing every boundary and every edge: the actual fields, not the message type;
- every output: whether it overwrites its input, and who reads it (search for the consumers). Every output the diagram shows being written needs a drawn consumer in scope, or the delivery note says why not; a write-back with no visible reader leaves the reader asking why it exists;
- which paths are always on and which are conditional, and what triggers each part;
- what each component's subtitle says it does and when it is active. A subtitle that overstates what the code does is a mismatch.

Treat documentation as a claim to check. Report each mismatch, separating what the code shows from what you infer. Code reading yields far more true facts than one diagram can carry; selection (section 2) is the main design step.

When the code changes after a diagram was delivered, redo this section before touching the layout, then state whether the diagram changed and recheck its colours.

When given another reviewer's critique, check each point against the code and state for each whether you agree, partly agree or disagree, with the reason.

## 4. Modeling

- **Part**: every part is a container; all parts at the same level get the same treatment.
- **Component**: named by role. State when components are logical groupings rather than code units. A step a component performs beyond what its name says is stated in its subtitle.
- **Elements are structure, edges are data flow**, pointing from producer to consumer. Every edge is a data-flow edge; never draw an edge that only associates two elements. A request and its response are two edges when both carry data the reader needs. When only the response matters (polling, health checks, metric scrapes), draw the response alone and state the trigger and its period in a subtitle.
- **Shape encodes kind** (component, data store, part).
- **Ownership is named in text, not drawn**: the owner's name is part of the component or data-store name, or of its subtitle. Give ownership a graphic encoding only when it is part of the diagram's question, and then show it on every shape kind that carries it in the legend. Never use dashed outlines or edges for it: section 2 reserves them for conditional paths, which is what readers expect a dashed outline or edge to mean.
- An output that overwrites its own input is drawn as a return edge labelled "<content> (overwrite)". A data store written by one part and patched by another gets one edge from each, the patch labelled "<field> (overwrite)".
- Collapsing or expanding a part changes granularity, not the type of diagram.
- An elements-and-edges diagram has no time axis. Write triggers and frequencies in subtitles, say in the delivery note what order or timing is not shown, and offer a sequence diagram when order matters to the reader.

## 5. Ports and collapsing

- Every part has ports on its border, all the same size and centred on the border. Ports are the only place edges enter or leave a part.
- External edges (root layer) connect port to port or port to data store. Internal edges are parented to their part, so they hide when it collapses and external edges re-attach to the collapsed part.
- Every edge touching a port meets the border perpendicularly: external edges are constrained to the side the port is on, internal edges to the opposite side. The generator sets both.
- Ports are placed so no edge crosses a part's title text (no north ports under the title).
- Align the internal stub with the port (set the exit or entry point from the port position) so the edge leaves the port straight, without a jog.

## 6. Colour

Default: no colour (the default fills). Colour only when a dimension is worth seeing at a glance for the diagram's question. Pick the dimension from the question and agree it with the user before colouring; if the user cannot be asked, keep the default colours. Do not colour a dimension that maps one-to-one onto parts, since their titles already carry it. Read `references/colour.md` before colouring: channels, rules, the default palette and change-status colours.

## 7. Edges and labels

**Edges**
- No edge crosses a part or its title bar, and no edge runs along a part's border. Leave gutters between parts and rows for routing.
- Orthogonal edges only (the port and fork rules depend on it), with block arrowheads. Default arrowhead: block, because a filled head keeps the direction readable when the diagram is reduced to slide size.
- A fork or merge shares one branching point, forming a T.
- A stub is long enough that the arrowhead and the port do not touch. Default minimum: 30 px (arrowhead, port and a visible gap).
- Edge crossings that topology forces are allowed if perpendicular; put a jump (`JUMP`) on the edge drawn later and list the crossings in the delivery note. Many forced crossings are a sign the diagram is over budget (section 2).
- Route return edges (overwrites, feedback) so they do not enclose a data store or component that other edges must leave; an enclosed node forces every new edge to cross the loop.

**Labels**
- Every edge between components states the data it carries. An edge may stay unlabelled only when one of its endpoints already names that content.
- A label names the content, as a noun phrase listing the fields or payload the edge carries. Never a generic message type (request, response, data), an endpoint or path, a function name, or a verb; those read as actions and hide what moves. Use the same wording for the same data everywhere in the diagram.
- Lack of space is never a reason to omit a label: reroute, move the exit point or widen the gap. Any label still omitted is listed in the delivery note.
- Labels never sit on the edge and carry no background, so the edge stays unobstructed. Default placement: above a horizontal segment (`H`), right of a vertical one (`V`). Slide a label along its edge (`pos`) when it comes near another edge.
- A labelled segment is at least the label width plus a margin, so labels never cover ports or arrowheads. Default margin: 20 px.

**Notation.** Default: plain-language notation in the diagram's language, so no notation legend is needed. A comma (or the language's list separator) separates list items, the word for "or" marks alternatives, parentheses add an annotation and always follow what they annotate, a colon introduces a value, an en dash marks a range, "*" is a filename glob, "&" may join two names in a title. Do not invent symbols for "sent together", "one or the other" or "then": items on one edge already travel together. This applies to labels, subtitles and legend captions alike.

A comma means a list and nothing else. In a subtitle, put each step, alternative or fact on its own line, starting alternatives with the word for "or" and later steps with the word for "then"; never join them with commas or semicolons.

## 8. Legend

The legend has one row per encoding dimension in use (shape, condition, each colour channel). Read `references/legend.md` before drawing it: row content, the shared column grid, and the generator functions.

## 9. Layout and style

- Flow in the reading direction of the diagram's language (Default: left to right); wrapped rows start at the same margin as the first.
- Default stroke and font colours unless section 6 applies. Fonts and sizes come from the project's conventions; without them use the generator's defaults (`references/generator-api.md`). Use one font for text, one monospace font for code names, and the same three sizes (element text, part title, small text for subtitles and labels) in the whole diagram; keep them when the diagram is revised.
- Element text stays inside the element; widen the element rather than shrink text.
- Part title inside the title bar, on one line: the part's name, followed for code-reading readers by its entry file in the code font. All part titles share one alignment and weight. Default: left-aligned, bold, so a title is set apart from the component text below it. Number parts only when the delivery note or slides refer to them by number.

## 10. Build or change the diagram file

- **Generator is the source of truth**: change the script, run it to a temporary path, and compare the existing .drawio with the checksum noted in section 1. If the existing file changed since then, stop and tell the user what changed instead of replacing it. Otherwise replace it.
- **The .drawio is the source of truth**: never regenerate. Edit only the affected cells in its XML with a small script, computing positions from the existing geometry.

## 11. Check by code, render and deliver

**Machine checks first.** Verify with code rather than by eye wherever code can decide. Run these before rendering and fix every issue:
- every edge's source and target exist, and every port an edge references exists (and every port is used);
- no two elements at the same level overlap (parts and data stores at the root, components inside one part), and no component leaves its part;
- ids are unique and the XML is well-formed;
- the counts of parts, components and edges, read from the cells, against the budget in section 2;
- the exported image's width and height, read from the file, against the destination's aspect ratio.

With the generator, call `check_cells()` before `save` (it covers the first three); for a .drawio edited by hand call `check_file(path)`; both are in `references/generator-api.md`. Without them, write a short script over the parsed XML (`xml.etree.ElementTree`). A clean result does not replace the inspection below; the inspection judges only what code cannot decide (crossings, label placement, text fit, greyscale legibility, whether labels name the right fields).

Then render every page with the draw.io CLI (`references/drawio-cli.md`), and inspect each page in full and a crop of every part, in this order:

1. Section 2: every element at the same level; no element that fails the deletion test.
2. Section 3: every label names the actual fields; no subtitle overstates what the code does; every written output has a drawn consumer or a note.
3. Section 4: no edges that only associate; overwrites drawn as return edges.
4. Section 5: edges meet ports perpendicularly; no edge crosses a title.
5. Section 6: colour legible, including a greyscale copy when colour is used (`references/colour.md`).
6. Section 7: no edge crosses a part, title bar or border; T-shaped forks; stub lengths; label placement and coverage; every label and subtitle read once more against the notation rules.
7. Section 8: legend swatches line up in columns (`references/legend.md`).
8. Section 9: text inside elements.
9. Destination: the aspect ratio of the exported image (draw.io crops to content), legend included, against the target from section 1. For slides, export one part per image when needed (draw.io "Selection only").

Deliver the diagram and the rendered previews. When the generator is the source of truth, also deliver it together with `drawio_gen.py`, so the user can rerun it without this skill.

- If files reach the user through a copy or sync step, verify them at the destination (checksum, or search for a string only the new version contains); a tool reporting success is not proof.
- In the delivery note, state what is simplified or omitted, what the diagram cannot show (section 4), forced crossings, omitted labels, removed elements, which file is the source of truth, and any check above that could not be done.
