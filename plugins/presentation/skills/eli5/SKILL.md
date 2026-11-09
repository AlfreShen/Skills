---
name: eli5
description: "Explain a topic to someone who knows nothing about it, as one HTML page built from large visuals and very few words. Use only when the user names eli5 explicitly (as eli5 or /eli5, in any language). Do not use it for other requests to explain, simplify, summarise or break something down, even when they ask for an explanation "like I'm five" without naming eli5; answer those in the conversation."
compatibility: "An environment that can create an HTML artifact, or write an HTML file the user opens in a browser."
---

# eli5

Explains one topic to a reader with no prior knowledge of it, as a single self-contained HTML page in which the visuals carry the explanation and the words are labels. Everything below serves that one page. The page's language, palette, fonts and where it is published are set per project.

## Project conventions

A project may set its own conventions for this work, in its `CLAUDE.md`, its Project instructions, or files the user points to. Where they conflict with this skill, the project's conventions win; otherwise use the defaults below. A correction that holds only for one project belongs in that project's instructions, not in this skill.

Projects commonly set: the reader, the language of the text, palette and fonts, reading-time target, and where the page is saved or published.

## 1. The reader

Assume zero prior knowledge, not low intelligence. Remove the jargon and the prerequisites, not the substance. No baby talk and no "imagine you are a little child" framing, because they talk down to the reader without making anything clearer.

## 2. The visuals

- Carry the meaning in the visual: diagrams, shapes, arrows, spatial layout, colour, size and motion do the explaining.
- Draw with inline SVG or CSS. Do not load external images, because the page must work on its own wherever it is opened. Do not use emoji as the diagram, because they render differently on each system and cannot show structure.
- Choose analogies whose failure points do not matter for the point being made, and do not extend an analogy past where it holds: an analogy pushed past its limit teaches something false.

## 3. The words

- One short label per visual, at most one line of text. If a section needs a paragraph, the visual is not doing its job: redraw it instead of adding text.
- Language: the language in the project's conventions; without one, the language of the user's request.

## 4. Layout

- One idea per screen, so the reader takes in each idea before the next.
- Default: vertical scroll, large type and generous whitespace, because a page read top to bottom one screen at a time needs no navigation. Every block earns its place or is cut.
- Default: the whole page readable in under a minute, because a longer page stops being a first explanation.

## 5. After the page

If the topic resists compression, say so briefly after delivering the page, instead of shipping a confident oversimplification.

## 6. Review checklist

1. Reader (section 1): no jargon or prerequisite left unexplained; no baby talk.
2. Visuals (section 2): every idea is carried by a visual; only inline SVG or CSS; no external images or emoji diagrams; every analogy holds for the point it is used for.
3. Words (section 3): at most one line of text per visual; no paragraphs; language as set.
4. Layout (section 4): one idea per screen; readable within the reading-time target.
5. After the page (section 5): any loss from compression is stated.
