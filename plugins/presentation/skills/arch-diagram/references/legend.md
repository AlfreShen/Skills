# Legend rules

Read before drawing the legend of a diagram, and when checking it in the render.

## Rows

- One row per encoding dimension in use: shape, condition (conditional elements), and each colour channel. Each row starts with the dimension's name in bold.
- Each row varies only its own dimension. Never put two dimensions on one row, even when one of them has a single value.
- A colour row also shows the default value ("other"), so the contrast is visible.
- A part-header colour is shown with a small swimlane swatch, a component colour with a box swatch. A port is shown with a port sample.
- Every encoding that appears in the diagram has a row, and every row's value appears in the diagram.

## Grid

- All rows share one set of columns. Every swatch has the same size and sits at its column's x, so swatches line up vertically across rows; a port sample is centred in its cell. The row pitch is constant.
- Size the columns from the longest name and the longest caption, so no text runs into the next column.

Defaults of the generator (the project's conventions may replace them): swatch 40 x 20 px, row pitch 28 px, dimension names in bold and captions in regular weight at the same size. Reason: the 28 px pitch leaves a gap between rows of 20 px swatches, and the bold weight sets a dimension name apart from its values.

## Generator functions

Call `legend_columns` first, then `legend_row` and `legend_item`; signatures are in `references/generator-api.md`. Placeholders below.

```python
legend_columns(name_w=<longest name in px>, caption_w=<longest caption in px>)
legend_row(0, "<dimension name>", y0)
legend_item("<id>", 0, 0, <style>, "<caption>", y0)      # row 0, column 0
legend_item("<id>", 0, 1, None, "<caption>", y0)          # None draws a port sample
```

A second legend on the same page uses another `prefix` in `legend_row`, so its ids stay unique.
