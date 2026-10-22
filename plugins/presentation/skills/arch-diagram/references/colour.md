# Colour rules

Read before colouring any part or component, and again when checking the colours of a rendered diagram. `SKILL.md` decides whether to colour at all; this file says how.

## Channels

Colour is used when a dimension is worth seeing at a glance; otherwise the default colours stay.

Candidate dimensions:
- new or in-scope parts versus existing infrastructure (only the new or in-scope parts are coloured)
- stage or layer
- where it runs
- owner or team
- change status, when the diagram reviews a change (see Change status)

At most two dimensions per diagram, each on its own channel and with its own legend row:
- **Part header** (the swimlane fill; the body stays white): for a dimension that is constant within a part, such as stage or location.
- **Component fill**: for a dimension that varies inside a part, such as contribution or change status.

Never put two dimensions on the same channel, and keep the two palettes apart in hue. Do not tint whole container bodies: coloured components on a coloured body lose contrast.

## Rules

Correctness rules (without them the diagram misleads or cannot be read):
- Colour never repeats a meaning already carried by shape or outline, and never replaces it (a conditional element stays dashed).
- Fills are light, so that black text stays readable; coloured components and headers fix the font colour to black, so text stays readable in either editor theme.
- 2 to 4 values per channel plus the default; more hues cannot be told apart.
- Files, data stores and edges stay default unless the dimension is change status.
- Check a greyscale copy of the export (`python3 -c "from PIL import Image; Image.open('out.png').convert('L').save('out-grey.png')"`, or ImageMagick `magick out.png -colorspace Gray out-grey.png`). Fills of similar lightness are indistinguishable in greyscale; that is acceptable only when the same information is readable from part titles or position. Otherwise vary lightness, not only hue, and tell the user if the diagram may be printed in black and white.

Consistency requirements:
- Diagrams of the same system keep the same colour for the same meaning, and a revision keeps the colours of the previous version.
- Each channel has one legend row (see `references/legend.md` for the legend).

Default fills (fill / stroke). Reason: they are draw.io's own preset palette, so shapes the user adds by hand match and the editor's style presets give the same colours. The project's conventions may replace them.

| Name | Fill | Stroke |
|---|---|---|
| blue | `#dae8fc` | `#6c8ebf` |
| green | `#d5e8d4` | `#82b366` |
| yellow | `#fff2cc` | `#d6b656` |
| red | `#f8cecc` | `#b85450` |
| purple | `#e1d5e7` | `#9673a6` |
| grey | `#f5f5f5` | `#666666` |

## Change status

For a diagram that reviews a change; it uses the component-fill channel.

- Default colours (the project's conventions may replace them): original blue (`ORIG`), modified yellow (`MOD`), added green with a heavier outline (`NEW`). Reason: three separate hues from the preset palette, and the heavier outline keeps added elements distinguishable from original ones in greyscale.
- Edges take the status of what they carry (`MOD_EDGE`, `NEW_EDGE`). Edges of different status never share a segment, because the shared segment would have two colours.
- Removed elements are not drawn; list them in the delivery note.
- The criterion for "modified" follows the reader, and is agreed with the user before colouring. At service level a component is modified when what it exchanges with other components changes (inputs, outputs, fields); changes not visible at that level stay original. At code-review level it is modified when its code changed in a way the reviewer must read. Decide per component from the diff, and name added data in the subtitle as "(new: x)".
