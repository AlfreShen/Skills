# Generator API

Read when you write or change a generator script that imports `scripts/drawio_gen.py`, or when you run its checks. The script is imported, not read: copy it next to the generator script and call the functions below. Python 3.6 or later; the file uses no f-strings.

## Setup

```python
import drawio_gen
drawio_gen.configure(font="<font>")   # only if the project sets fonts or sizes; before the next line
from drawio_gen import *
```

## Usage rules

- Coordinates are absolute everywhere except `comp`'s `rx`, `ry`, which are relative to its part.
- Label arguments are HTML (`<br>` for line breaks). Wrap literal text containing `<` or `&` in `esc()`. `code` in `lab` and `sub` in `part` are escaped automatically.
- Do not use `e` as a variable name in the generator; it is the edge function.
- No backslashes inside f-string expressions in the generator (a SyntaxError before Python 3.12), so it runs on the Python the user has.
- Compute positions from other elements' geometry (`left`, `right`, `top`, `bot`, `cx`, `cy`). Only the first anchor element on a page takes literal coordinates.
- Define an element before using it as a parent, a port owner or in a geometry call: an unknown id raises `KeyError`. Define ports before the edges that use them: an edge written before its port misses the port constraint (`check_cells()` reports it).

## Functions

| Function | Purpose |
|---|---|
| `configure(font=None, code_font=None, sz_box=None, sz_title=None, sz_small=None)` | Fonts and sizes in px; `None` keeps the current value. Defaults: Helvetica, Courier New, 13, 14, 10 |
| `page(id, name, w, h)`, `page_link(page_id)` | Start a page (w, h in px); link a shape to a page with `link=page_link(...)` |
| `part(id, title, sub, x, y, w, h, extra="", link=None)` | Part container; `sub` (or `None`) is shown in the code font after the title |
| `comp(id, parent, label, rx, ry, w, h, extra="", link=None)` | Component inside a part |
| `doc(id, label, x, y, w, h, extra="", link=None)` | Data store (file shape) at root level |
| `lab(title, code=None, note=None)` | Element label: title, then code name, then note |
| `esc(text)` | Escape literal text for a label |
| `pt(id, parent, side, at)` | Port on a part's side (`north`, `south`, `east`, `west`) at absolute `at` (x for north and south, y for east and west) |
| `e(id, source, target, label="", *parts, parent="1", pos=None)` | Edge. Strings are style fragments, lists are absolute waypoints `[(x, y), ...]`. `parent=<part id>` for internal edges. `pos` (-1 to 1) slides the label along the edge. Port constraints are set automatically |
| `ex(x, y)`, `en(x, y)` | Exit and entry point style fragments (fractions 0 to 1 of the element) |
| `left`, `right`, `top`, `bot`, `cx`, `cy` `(id)` | Absolute geometry of any defined element |
| `legend_columns(name_w=110, caption_w=190, n=4, x0=20)` | Size the legend grid from the longest name and caption; `n` columns starting at `x0`. Call before the legend rows |
| `legend_row(r, name, y0, prefix="lg")`, `legend_item(id, r, c, style, caption, y0)` | Legend row name and swatch; `style=None` draws a port sample; use another `prefix` for a second legend on a page |
| `swatch_header(fill)`, `SWATCH_FILE` | Swatch styles for part-header colours and data stores |
| `check_cells(raise_on_error=False)` | Machine check of the cells built so far (every page); returns a list of issue strings, empty when clean. Call before `save` |
| `check_file(path, raise_on_error=False)` | The same checks on a saved .drawio file, compressed or not; use it when the .drawio is the source of truth. Raises `OSError` if the file cannot be read |
| `save(path)` | Write all pages to one .drawio file |

`check_cells` and `check_file` report: duplicate ids; an edge with no source or target, or one that is not a cell on its page (this includes every port an edge references); an edge to a port that lacks the port constraint; a port no edge uses; a parent that does not exist; two sibling elements that overlap (parts and data stores at the root, components inside one part; ports excluded); an element that extends outside its part. Shared borders are not overlap. They do not check crossings, label placement or text fit: inspect the render for those. With `raise_on_error=True` they raise `ValueError` listing the issues.

## Style constants

`BOX`, `DOC`, `LANE`, `EDGE`, `PORT`, `TXT` (plain text), `H` (label above a horizontal segment), `V` (label right of a vertical one), `COND` (dashed, for conditional elements), `JUMP` (jump on a crossing), and the change-status styles `ORIG`, `MOD`, `NEW`, `MOD_EDGE`, `NEW_EDGE` (see `references/colour.md`).

## Built-in geometry and style

Defaults of the generator, kept so that separate runs give the same diagram. None is a rule; the project's conventions may replace them, and any style key can be overridden for one shape through `extra` (later keys win).

| Item | Value | Reason |
|---|---|---|
| Port | 12 x 12 px circle centred on the border | Large enough to see and grab at 100 % zoom, small enough to stay clear of text |
| Part title bar | 28 px | Fits the default 14 px title; set `startSize=<px>;` in `extra` after raising the title size |
| Collapsed part | 220 x 40 px | Wide enough for a short title |
| Legend swatch, row pitch | 40 x 20 px, 28 px | See `references/legend.md` |
| Corners, dash pattern, jump | square, 8 4, arc of 10 px | Generator constants with no effect on correctness; override freely |
| Edge routing | orthogonal, block arrowheads | See section "Edges and labels" in `SKILL.md` |
