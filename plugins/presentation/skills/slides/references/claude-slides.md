# Claude Slides: tool limits

Read before editing a deck in Claude Slides. These are properties of the tool, observed as of 2026-10. Recheck one by trying it on a scratch slide in a copy of the deck, and against the tool's current documentation, whenever the tool behaves differently from what is written here. The main skill's rules still apply.

## Text and boxes

- `line-height` accepts only 0.5–4 times the font size. Larger values are clamped, and a fixed-height box shrinks.
- `<span>` can change colour only, not size or font. Place subscripts as a separate small `<p>`.
- A `<p>` element's width includes its padding and border, so its right edge is at its `left + width`. End connectors there.
- Tables usually render taller than estimated. Confirm on the rendered slide that elements below a table do not overlap it.

## Connectors

- An x-connector is covered by elements drawn after it. End it at the box outline, or place the connector later in the source.
- When moving a group of elements, adjust `top` together with the connector's `y1` and `y2`.

## Transitions

- The tool's morph transition is called Magic. It matches elements by id: an element moves between adjacent slides only when it has the same id on both.

## Deck files

- To delete a slide, remove it from `order` in `deck.json` and delete its file. A file removed only from `order` still appears at the end of the editor.
- The editor reformats files the user edited, so re-read a file before patching it rather than applying a diff made against your earlier copy.
