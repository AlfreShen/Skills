---
name: slides
description: "Rules for building or revising an informational slide deck (a report, briefing, review, or explanation of a system, study or result). Use whenever creating or editing such a deck in any tool, including whenever a tool-specific deck skill or artifact type is used, such as pptx or Claude Slides."
---

# Slides

Rules for decks that inform. Three terms are used throughout: the **claim lines** are the lines under a slide's title stating what the slide shows, the **source line** is the short line naming where the slide's content comes from, and the **notes** are the speaker notes. Audience, purpose, section structure, slide types, fixed vocabulary and visual style are set per project, not here.

## Project conventions

A project may set its own conventions for this work, in its `CLAUDE.md`, its Project instructions, or files the user points to. Where they conflict with this skill, the project's conventions win; otherwise use the defaults below. A correction that holds only for one project belongs in that project's instructions, not in this skill.

Projects commonly set: audience and purpose, register, section structure, slide types with fixed fields (cover, divider, closing), title form, fixed block titles and status words, template, palette, font sizes, text-per-slide limit and element positions, claim-line length and style, figure numbering, speaker-notes format, notation conventions, storyboard location, source locations and tool scripts.

## Workflow

1. Prepare (section 1).
2. Plan in the storyboard (section 2).
3. Build or revise the slides by sections 3 to 9.
4. Answer questions and apply corrections as they arise (section 10).
5. Run the checks in section 11 before publishing.

## 1. Before starting

- Know the deck's question: what the audience must understand or decide after it. Take it from the project's conventions, or ask the user once. Content that does not serve that question stays out.
- If the deck already exists, start from its current live version rather than a local copy, and keep any edits the user made.
- If a storyboard already exists, read it. Its location comes from the project's conventions. Default: next to the deck, so the two are found and kept together.
- If a source exists in several versions, use the one the user names (ask if none is named), compare the versions before planning, and keep the list of differences.
- If a tool-specific skill or artifact type is also in use (such as pptx or Claude Slides), follow its instructions for how files are built and edited, and these rules for content, figures and layout. Where they disagree about how the tool works, the tool's instructions win.
- If the tool is Claude Slides, read `references/claude-slides.md` (its limits on text, connectors, transitions and deck files) before editing.

## 2. Storyboard

Plan in a storyboard before building slides: changing a row is cheaper than rebuilding a slide.

- One row per slide: slide, id, title, block title (if the template uses titled blocks), claim lines, figure with its number, source, animation, transition.
- Title-sequence test: reading only the titles in order, section names included, tells the deck's argument: its answer to the deck's question, the steps that support it, and its conclusion. A title that only names a topic fails when the sequence then loses the argument. Fix titles or order until it passes, and repeat the test on the final titles before publishing.
- Attach a symbol table (symbol, meaning, the source's own notation), the differences between source versions if any, and a detailed-sources section (file names, identifiers of the runs, builds or documents used, scripts, data locations). Detailed sources stay off the slides.
- Update the storyboard first whenever slides are added or changed, then save it at the location from section 1.
- Number figures with one scheme across the storyboard and the deck, and keep it when slides are added. Default: by section, N-M for the M-th figure of section N, because an insertion then renumbers only its own section.
- After inserting or deleting a slide or figure, renumber everything after it (items, figures) and update the counts on overview, contents and section slides.

## 3. Structure and order

- Default slide types (the project's conventions may replace them): the cover's title is the topic and its subtitle the purpose, so a reader can identify the deck; section divider slides carry only the section number and name, so they work as navigation without repeating the overview.
- Concepts and effects come before details.
- A slide showing only part of a mechanism never follows the slide that explains the whole of it; it would read as an incomplete summary.
- A slide that explains how something works does not also evaluate it. Evaluations go on their own slides; observations about them may go in the notes. Differences between configurations are findings, not properties of the thing described.
- An overview slide listing N items is followed by N detail slides, one item each, whose titles carry the same number and name.
- The main line ends on the deck's conclusion, or on the decision or next step that conclusion supports, so the audience leaves with what section 1 says they must understand or decide. A closing slide may add thanks or an invitation for questions, but it still carries the conclusion; one that holds only those is not an ending.
- Material outside the main line follows it, introduced by one overview slide that uses the deck's terms.

## 4. Content

### Grounding

- Write only what the source material supports. Where the sources are silent, say so in the notes instead of filling the gap.
- Do not invent numbers. Leave an uncertain number out, or show a symbol in the figure; never placeholder text.
- State a disagreement with a source as evidence (what the source says versus what the evidence shows), not as a verdict on its author.
- Name the exact version, configuration or edition of anything compared, instead of writing "same settings".
- Keep observation and inference apart. Mark inference as such on the slide and in the notes.
- When the deck reports measured or computed results:
  - ratios and values come from the source's own statistics, not from one instance, and each statistic's scope is stated on the slide;
  - every number traces back to the underlying data; a number computed for this deck rather than taken from a source is marked as such in the source line, with the data location in the notes;
  - recompute any number whose origin is unknown.

### Consistent terms

- If the template uses titled blocks, block titles come from one fixed set in the project's conventions, with no extra sub-headings.
- Keep proper nouns in their original form. When two sources name the same thing differently, give both.
- Define a term, parameter or symbol once in full; later slides use the same name or symbol. A slide likely to be viewed on its own repeats a short gloss rather than the full definition.
- Unless the audience reads code, no code variable names on slides; use the symbols the deck defines.
- One name per metric throughout, matching the slide that defines it. Only a quantity that differs from that definition is explained again.
- One unit per quantity throughout. Put units in table headers, and say whether a difference is relative or absolute.
- Default register: formal, without slang, in figure labels and notes too, because slang and colloquial wording is ambiguous to readers outside the author's circle. Expand an abbreviation at first use unless the audience already knows it. Text the user typed themselves is kept as written.
- Default: no file names or paths on slides; name the kind of document instead, because the audience cannot use them and they go out of date. They belong in the notes and the storyboard. A project whose audience works with those files may allow them.

### Sentences

- Write a sequence as numbered steps or as one declarative sentence joined by →. → joins two stated items in cause or time order, never items of a list.
- One claim per sentence, so that each claim can be checked alone. Split a line that joins two claims, in the notes as well.
- Parallel items (flow boxes, legend entries, bullets, table columns) share one level and one grammatical form.
- No pointers to other slides; put what the slide needs on the slide.
- Describe status neutrally and factually; fixed status words come from the project's conventions. Avoid labels that read as blame or failure.
- Every table cell states its content and does not refer to another cell.
- An illustrative case shown on a slide states what it demonstrates, not only its outcome.
- Table column names are readable by someone seeing the table for the first time.

### Figures, axes and notation

- Every figure gets a numbered figure caption.
- Axes have names and units. A unitless quantity gets its definition.
- When a slide draws on an external method, the figure or table shows how its values correspond to the slide's, not only the method's name.
- Follow the source's notation. Define your own symbol only when the source gives none, and define it on the slide.
- Typeset math normally (stacked fractions, italic variables) and write formulas as the source does.
- Replace vague comparisons with a quantity (a number, ratio or formula), defining each symbol where it first appears.

## 5. Claim lines and source line

Claim lines follow the assertion-evidence principle: the claim is stated in full, and the figure or table below carries the evidence.

- Line 1: the claim. Line 2: the mechanism, condition or result that supports it.
- Default: at most two lines, one sentence per line, each fitting on one line at the deck's claim-line size (length set per project), because claim lines are read at a glance and longer text belongs in the figure or the notes.
- Use one claim-line style (alignment, closing punctuation) throughout the deck, and keep it when slides are revised.
- Definitions, thresholds and formulas go into the figure, not the claim lines.
- Claim lines never refer to a rule or threshold the deck has not yet introduced.
- Sources go in the source line, not in the claim lines: one per content slide, naming sections or kinds of documents.

## 6. Figure-to-system correspondence

A figure whose counts, flows or states differ from the real system teaches the reader something false. Check every figure item by item:

1. **Counts**: the number of elements matches reality; nothing is duplicated to fill the picture.
2. **Data flow**: every piece of data has a source and a destination, and leaves only from the element that really produces it. Arrow labels name what is actually passed.
3. **Composition**: an object has the same parts, order and colour on every slide.
4. **State**: a state change applies to every part of the object it affects.
5. **Context and rules**: elements absent from the depicted situation are not drawn; values shown obey the system's rules; an apparent contradiction is explained in the claim lines.
6. **Legend**: every legend entry appears in the figure, and every colour or line style in the figure is in the legend.
7. **Text**: everything the claim lines and notes describe is visible in the figure; when the figure changes, claim lines and notes change with it.
8. **Numbers**: counts, totals, percentages and analysis scope agree across the slide.
9. **Overview**: overview and detail slides match as section 3 requires.

## 7. Layout

- Default density limits, because smaller or denser text is hard to read when projected: at most about 50 words of running text per slide (claim lines, bullets and captions; figure and table labels excluded), and no visible text below 12 pt at a slide width of 13.33 in (scale in proportion for other widths). Move overflow to another slide or the notes instead of shrinking text below the minimum.
- Title, claim lines, source line and page number keep fixed positions and sizes across the deck (values set per project).
- Shared elements (legend, components of one recurring diagram) stay in the same place across related slides, so they can be compared and animated between slides.
- Legends do not cover data. Spread content across the content region rather than packing it to one side.
- No large empty areas in the content region, especially at the bottom. Fix in this order, so that content is never added only to fill space: move the content down and centre it, widen the spacing, then add content that carries meaning. Never add unrelated content.
- Labels do not wrap and get enough width; crowded boxes get spare room, because the final font may render wider than the preview. If the preview font differs from the final font, ask the user to check crowded boxes in the real view.
- A visual code (outline style, colour, line style) has one meaning only.
- Grouped elements sit in a titled container that appears together with its members.
- Many compared items go in a table. Default: when a figure and a table sit side by side, align the top of the table's header with the top of the figure, because misaligned tops read as unintended.
- Slides of the same kind use the same presentation: tables of the same kind share columns, order and format.
- Overview and detail use the same figure: a reduced version first, then the same figure expanded, rather than a new drawing.
- A setup or architecture figure shows only the elements and parameters the slide's claim needs. A second setup of the same kind marks only its differences and names the rest.

## 8. Speaker notes

Default format, because notes serve as the record of what each slide rests on, not as a script; the project's conventions may replace it:

- Formal written prose summarising the slide.
- Three parts: "Summary:" the key points; "Details:" calculations and inferences, marked as such; "Sources:" source sections and data locations.

## 9. Animation

- Builds and morph transitions (a transition that moves matching elements from one slide to the next) show sequence. How elements are matched depends on the tool; for Claude Slides see `references/claude-slides.md`.
- Only elements with an order or causal relation appear one after another; parallel elements appear together.
- A moving element follows the path the data takes in the figure.
- Show a state change by placing the new state over the old one, so the reader sees what changed in place.

## 10. Questions and corrections

- When the user asks what a source says, check the source, code or data before answering.
- When the user points out one error, fix every instance of the same kind across the deck.
- Confirm a file actually changed before reporting that it did.

## 11. Before publishing

1. Reread the live version. If it changed since you started, reapply your edits on top of it.
2. Storyboard: matches the deck; figures and items are numbered in sequence; counts on overview slides are right.
3. Structure: order follows section 3, including the ending; the title-sequence test (section 2) passes on the final titles; every slide serves the deck's question.
4. Grounding: no invented numbers or placeholder text; inference marked; computed numbers marked in the source line.
5. Visible text (not the notes): terms outside the fixed vocabulary, inconsistent metric names or units, code variable names for a non-code audience, file names or paths, lines joining two claims, blame labels, cells that refer to other cells, pointers to other slides.
6. Claim lines and source line: within the claim-line limit and one style, no sources in them, no reference to anything not yet introduced; a source line on every content slide.
7. Every figure passes section 6.
8. Every changed slide viewed at full size, not as a thumbnail: connectors and arrows, box heights, overflow, overlap, balance, empty space at the bottom, density limits, and fixed elements aligned with neighbouring slides. Crowded boxes checked in the final font (section 7).
9. Notes follow section 8; animation order follows section 9.
10. Every file you report as changed was actually changed.
