"""Helpers for generating editable draw.io architecture diagrams.

Copy this file next to the diagram's generator script, then:

    import drawio_gen
    drawio_gen.configure(...)        # optional: project fonts and sizes, before the next line
    from drawio_gen import *

Coordinates are ABSOLUTE everywhere except comp()'s rx, ry, which are relative to its part.
Label arguments are HTML (use <br> for line breaks). Wrap literal text that contains < or & in esc().
`code` (in lab) and `sub` (in part) are escaped automatically.
Do not use `e` as a variable name in the generator; it is the edge function.

Before save(), run check_cells() (generator state) or check_file(path) (any .drawio file): they report
missing edge endpoints, missing or unused ports, duplicate ids and overlapping elements as a list of strings.
Requires Python 3.6+ (no f-strings or newer syntax are used).
"""
import base64
import html
import urllib.parse
import xml.etree.ElementTree as ET
import zlib

__all__ = [
    "configure", "page", "page_link", "part", "comp", "doc", "lab", "esc", "pt", "e", "ex", "en",
    "left", "right", "top", "bot", "cx", "cy",
    "legend_columns", "legend_row", "legend_item", "swatch_header", "save",
    "check_cells", "check_file",
    "BOX", "DOC", "LANE", "EDGE", "TXT", "PORT", "H", "V", "COND", "JUMP",
    "ORIG", "MOD", "NEW", "MOD_EDGE", "NEW_EDGE", "SWATCH_FILE",
]

# ---------------------------------------------------------------- style settings
# Call configure() before drawing to apply the project's fonts and sizes.
# These are defaults, not rules. Helvetica is draw.io's own default font, so shapes the user adds by hand
# in the editor match. Courier New is a monospace font from draw.io's font list. The sizes (px) fit the
# fixed geometry below (28 px title bar, 20 px legend cells); after raising them, check that part titles
# and legend captions still fit (a taller title bar: put `startSize=<px>;` in the part's `extra`).
FONT = "Helvetica"
CODE_FONT = "Courier New"
SZ_BOX, SZ_TITLE, SZ_SMALL = 13, 14, 10


def configure(font=None, code_font=None, sz_box=None, sz_title=None, sz_small=None):
    """Set fonts and sizes (from the project's conventions) and rebuild the styles.

    font: text font; code_font: monospace font for code names; sz_box: component and data-store text size;
    sz_title: part title size; sz_small: subtitle, code-name, edge-label and legend size (all in px).
    An argument left as None keeps its current value. Call before drawing anything.
    """
    global FONT, CODE_FONT, SZ_BOX, SZ_TITLE, SZ_SMALL
    FONT = font or FONT
    CODE_FONT = code_font or CODE_FONT
    SZ_BOX = sz_box or SZ_BOX
    SZ_TITLE = sz_title or SZ_TITLE
    SZ_SMALL = sz_small or SZ_SMALL
    _build_styles()


def _build_styles():
    global F, BOX, DOC, LANE, EDGE, TXT
    F = "fontFamily=%s;fontSize=%s;" % (FONT, SZ_BOX)
    BOX = "rounded=0;whiteSpace=wrap;html=1;" + F
    DOC = "shape=document;whiteSpace=wrap;html=1;boundedLbl=1;size=0.15;" + F
    LANE = ("swimlane;startSize=28;align=left;spacingLeft=8;fontStyle=1;whiteSpace=wrap;html=1;"
            "fontFamily=%s;fontSize=%s;collapsible=1;" % (FONT, SZ_TITLE))
    EDGE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;fontSize=%s;endArrow=block;endFill=1;"
            "jettySize=auto;orthogonalLoop=1;labelBackgroundColor=none;fontFamily=%s;" % (SZ_SMALL, FONT))
    TXT = "text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;" + F


_build_styles()

# Fixed shape styles. Square corners (rounded=0) and the 8/4 dash pattern are generator defaults, not rules;
# override any of them for one shape through the `extra` argument (later keys win).
PORT = "ellipse;aspect=fixed;html=1;fillColor=default;"
H = "verticalLabelPosition=top;verticalAlign=bottom;spacingBottom=2;"   # label above a horizontal segment
V = "labelPosition=right;align=left;spacingLeft=4;"                     # label right of a vertical segment
COND = "dashed=1;dashPattern=8 4;"   # conditional element or edge
JUMP = "jumpStyle=arc;jumpSize=10;"  # on the later edge of a forced crossing

# Change status (component fill channel). Fill and stroke pairs are draw.io's preset palette; NEW has a
# heavier outline so it stays distinguishable from ORIG in greyscale.
ORIG = "fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;"
MOD = "fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#000000;"
NEW = "fillColor=#d5e8d4;strokeColor=#82b366;strokeWidth=2.5;fontColor=#000000;"
MOD_EDGE = "strokeColor=#d6b656;"
NEW_EDGE = "strokeColor=#4d8a3a;"

# Swatch styles for the legend
SWATCH_FILE = "shape=document;whiteSpace=wrap;html=1;size=0.25;"


def swatch_header(fill):
    """Small swimlane swatch for a part-header colour."""
    return LANE.replace("startSize=28", "startSize=6").replace("collapsible=1", "collapsible=0") + fill


# ---------------------------------------------------------------- pages and geometry
_pages = []
_cur = None
SIDE = {}
G = {}   # id -> absolute (x, y, w, h)
OPP = {"west": "east", "east": "west", "north": "south", "south": "north"}


def page(id, name, w, h):
    """Start a new page. Later cells go on it. Link to it with link=page_link(id)."""
    global _cur
    _cur = {"id": id, "name": name, "w": w, "h": h, "cells": []}
    _pages.append(_cur)


def page_link(page_id):
    """Link value for a shape: `link=page_link(<page id>)` jumps to that page."""
    return "data:page/id," + page_id


def _g(i):
    """Absolute geometry of element i, with a clear error when it was not defined yet."""
    try:
        return G[i]
    except KeyError:
        raise KeyError("unknown element id %r: define it before using it as a parent or for geometry" % (i,))


def _cells():
    if _cur is None:
        page("p1", "Overview", 1600, 900)
    return _cur["cells"]


def esc(text):
    """Escape literal text for use inside an HTML label (also used for the XML layer)."""
    return html.escape(text, quote=True)


def lab(title, code=None, note=None):
    """Box label: title (HTML), optional code name (escaped, code font), optional note (HTML)."""
    out = title
    if code:
        out += '<br><font face="%s" style="font-size:%spx">%s</font>' % (CODE_FONT, SZ_SMALL, html.escape(code))
    if note:
        out += '<br><font style="font-size:%spx">%s</font>' % (SZ_SMALL, note)
    return out


def v(id, val, style, x, y, w, h, parent="1", alt=None, link=None):
    """Raw vertex. x, y are relative to `parent`."""
    a = ""
    if alt:
        a = '<mxRectangle x="%s" y="%s" width="%s" height="%s" as="alternateBounds"/>' % alt
    geo = '<mxGeometry x="%s" y="%s" width="%s" height="%s" as="geometry">%s</mxGeometry>' % (x, y, w, h, a)
    if link:
        _cells().append('<UserObject label="%s" link="%s" id="%s"><mxCell style="%s" vertex="1" parent="%s">%s'
                        '</mxCell></UserObject>' % (esc(val), esc(link), id, style, parent, geo))
    else:
        _cells().append('<mxCell id="%s" value="%s" style="%s" vertex="1" parent="%s">%s</mxCell>'
                        % (id, esc(val), style, parent, geo))


def part(id, title, sub, x, y, w, h, extra="", link=None):
    """Part container. `sub` (e.g. the entry file for code-reading readers) is shown in the code font."""
    if sub:
        title += '&nbsp;&nbsp;&nbsp;<font face="%s" style="font-size:%spx;font-weight:normal">%s</font>' % (
            CODE_FONT, SZ_SMALL, html.escape(sub))
    # alt = bounds shown when the part is collapsed: same corner, 220 x 40 px, wide enough for a short title
    v(id, title, LANE + extra, x, y, w, h, alt=(x, y, 220, 40), link=link)
    G[id] = (x, y, w, h)


def comp(id, parent, label, rx, ry, w, h, extra="", link=None):
    """Component inside `parent`; rx, ry relative to the parent."""
    px, py = _g(parent)[0], _g(parent)[1]
    v(id, label, BOX + extra, rx, ry, w, h, parent, link=link)
    G[id] = (px + rx, py + ry, w, h)


def doc(id, label, x, y, w, h, extra="", link=None):
    """File or data store at the root level."""
    v(id, label, DOC + extra, x, y, w, h, link=link)
    G[id] = (x, y, w, h)


def pt(id, parent, side, at):
    """Port on `side` of `parent` at absolute coordinate `at` (x for north/south, y for east/west)."""
    if side not in OPP:
        raise ValueError("port %s: side must be north, south, east or west, not %r" % (id, side))
    x, y, w, h = _g(parent)
    cx_, cy_ = {"north": (at - x, 0), "south": (at - x, h),
                "west": (0, at - y), "east": (w, at - y)}[side]
    SIDE[id] = side
    v(id, "", PORT, cx_ - 6, cy_ - 6, 12, 12, parent)
    G[id] = (x + cx_ - 6, y + cy_ - 6, 12, 12)


def left(i): return _g(i)[0]
def right(i): return _g(i)[0] + _g(i)[2]
def top(i): return _g(i)[1]
def bot(i): return _g(i)[1] + _g(i)[3]
def cx(i): return _g(i)[0] + _g(i)[2] / 2.0
def cy(i): return _g(i)[1] + _g(i)[3] / 2.0


def e(id, source, target, label="", *parts, parent="1", pos=None):
    """Edge. parts: str = style fragment, list = ABSOLUTE waypoints [(x, y), ...].
    Internal edges pass parent=<part id>; port constraints are set automatically."""
    for p in parts:
        if not isinstance(p, (str, list)):
            raise TypeError("edge %s: style must be str, waypoints must be a list" % id)
    style = "".join(p for p in parts if isinstance(p, str))
    pts = [q for p in parts if isinstance(p, list) for q in p]
    if parent != "1":
        px, py = _g(parent)[0], _g(parent)[1]
        pts = [(a - px, b - py) for a, b in pts]
    for end, node in (("source", source), ("target", target)):
        if node in SIDE:
            side = SIDE[node] if parent == "1" else OPP[SIDE[node]]
            style += "%sPortConstraint=%s;" % (end, side)
    g = '<mxGeometry%s relative="1" as="geometry">' % ("" if pos is None else ' x="%s"' % pos)
    if pts:
        g += '<Array as="points">' + "".join('<mxPoint x="%s" y="%s"/>' % tuple(p) for p in pts) + "</Array>"
    _cells().append('<mxCell id="%s" value="%s" style="%s%s" edge="1" parent="%s" source="%s" target="%s">%s'
                    '</mxGeometry></mxCell>' % (id, esc(label), EDGE, style, parent, source, target, g))


def ex(x, y):
    return "exitX=%s;exitY=%s;exitDx=0;exitDy=0;" % (x, y)


def en(x, y):
    return "entryX=%s;entryY=%s;entryDx=0;entryDy=0;" % (x, y)


# ---------------------------------------------------------------- legend
LCOL = []
LROW_PITCH = 28      # px between legend rows (constant, so rows line up); fits the 20 px swatch height
_LNAME_W = 110
_LCAP_W = 190


def legend_columns(name_w=110, caption_w=190, n=4, x0=20):
    """Size the legend grid from the longest dimension name and caption (in px)."""
    global _LNAME_W, _LCAP_W
    _LNAME_W, _LCAP_W = name_w, caption_w
    LCOL[:] = [x0 + name_w + 5 + (50 + caption_w + 10) * i for i in range(n)]


legend_columns()


def legend_row(r, name, y0, prefix="lg"):
    """Bold dimension name at the start of legend row r. Use a different prefix for a second legend on a page."""
    v("%sr%d" % (prefix, r), name, TXT + "fontSize=%s;fontStyle=1;" % (SZ_SMALL + 1),
      LCOL[0] - _LNAME_W - 5, y0 + r * LROW_PITCH, _LNAME_W, 20)


def legend_item(id, r, c, style, caption, y0):
    """Swatch (40 x 20) in row r, column c; style=None draws a port sample."""
    x, y = LCOL[c], y0 + r * LROW_PITCH
    if style is None:
        v(id, "", PORT, x + 14, y + 4, 12, 12)
    else:
        v(id, "", style, x, y, 40, 20)
    v(id + "t", caption, TXT + "fontSize=%s;" % (SZ_SMALL + 1), x + 50, y, _LCAP_W, 20)


# ---------------------------------------------------------------- machine checks
def _cell_records(elements):
    """Flatten parsed <mxCell>/<UserObject> elements into plain dicts (root cells 0 and 1 are skipped)."""
    recs = []
    for el in elements:
        cell = el.find("mxCell") if el.tag == "UserObject" else el
        if cell is None or cell.tag != "mxCell":
            continue
        cid = el.get("id")
        if cid in ("0", "1") or cid is None:
            continue
        geo = cell.find("mxGeometry")
        rec = {"id": cid, "edge": cell.get("edge") == "1", "vertex": cell.get("vertex") == "1",
               "parent": cell.get("parent", "1"), "source": cell.get("source"), "target": cell.get("target"),
               "style": cell.get("style", ""), "box": None}
        if geo is not None and not rec["edge"]:
            try:
                rec["box"] = tuple(float(geo.get(k, 0)) for k in ("x", "y", "width", "height"))
            except ValueError:
                rec["box"] = None
        recs.append(rec)
    return recs


def _check_records(where, recs):
    """Run the checks on the flattened cells of one page and return a list of issue strings."""
    issues = []
    ids = {}
    for r in recs:
        if r["id"] in ids:
            issues.append("%s: duplicate id %s" % (where, r["id"]))
        ids[r["id"]] = r
    used = set()
    for r in recs:
        if r["vertex"] and r["parent"] != "1" and r["parent"] not in ids:
            issues.append("%s: %s has a parent %s that does not exist" % (where, r["id"], r["parent"]))
        if not r["edge"]:
            continue
        for end in ("source", "target"):
            node = r[end]
            if not node:
                issues.append("%s: edge %s has no %s" % (where, r["id"], end))
            elif node not in ids:
                issues.append("%s: edge %s %s %s does not exist" % (where, r["id"], end, node))
            else:
                used.add(node)
    for r in recs:
        if r["edge"]:
            for end in ("source", "target"):
                node = ids.get(r[end])
                if node and node["vertex"] and node["style"].startswith(PORT) and node["parent"] != "1" \
                        and end + "PortConstraint=" not in r["style"]:
                    issues.append("%s: edge %s %s is port %s but has no %sPortConstraint (define ports before "
                                  "their edges)" % (where, r["id"], end, node["id"], end))
    # A port is a PORT-styled vertex inside a part (PORT-styled vertices at the root are legend samples).
    for r in recs:
        if r["vertex"] and r["style"].startswith(PORT) and r["parent"] != "1" and r["id"] not in used:
            issues.append("%s: port %s is not used by any edge" % (where, r["id"]))
    # Overlap and containment, compared among siblings (same coordinate space). Ports sit on borders by design.
    groups = {}
    for r in recs:
        if r["vertex"] and r["box"] and not r["style"].startswith(PORT):
            groups.setdefault(r["parent"], []).append(r)
    for parent, members in groups.items():
        for i, a in enumerate(members):
            ax, ay, aw, ah = a["box"]
            if parent in ids and ids[parent]["box"]:
                _, _, pw, ph = ids[parent]["box"]
                if ax < 0 or ay < 0 or ax + aw > pw or ay + ah > ph:
                    issues.append("%s: %s extends outside its part %s" % (where, a["id"], parent))
            for b in members[i + 1:]:
                bx, by, bw, bh = b["box"]
                if ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah:
                    issues.append("%s: %s and %s overlap" % (where, a["id"], b["id"]))
    return issues


def _raise_or_return(issues, raise_on_error):
    if issues and raise_on_error:
        raise ValueError("\n".join(issues))
    return issues


def check_cells(raise_on_error=False):
    """Check the cells built so far, on every page, before save(). Returns a list of issue strings (empty = OK).

    Reports: duplicate ids; an edge with no source or target, or whose source or target is not a cell on its
    page (this covers every port an edge references); an edge to a port without its port constraint; a port
    that no edge uses; a parent that does not exist;
    two sibling elements that overlap (parts and data stores at the root, components inside one part; ports
    excluded); an element that extends outside its part. Touching edges do not count as overlap.
    Not checked: edge crossings, label placement and text fit (inspect the render for those).
    With raise_on_error=True, raises ValueError listing the issues instead of returning them.
    """
    issues = []
    for p in _pages:
        where = "page %s" % p["name"]
        try:
            root = ET.fromstring("<root>" + "".join(p["cells"]) + "</root>")
        except ET.ParseError as exc:
            issues.append("%s: XML is not well-formed (%s)" % (where, exc))
            continue
        issues.extend(_check_records(where, _cell_records(list(root))))
    return _raise_or_return(issues, raise_on_error)


def check_file(path, raise_on_error=False):
    """Run the same checks on a saved .drawio file (also one edited by hand, compressed or not).

    Use it when the .drawio file is the source of truth and there is no generator state. Returns a list of
    issue strings (empty = OK); see check_cells for what is reported. Raises OSError when the file cannot
    be read; raises ValueError instead of returning when raise_on_error=True and there are issues.
    """
    issues = []
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        return _raise_or_return(["%s: XML is not well-formed (%s)" % (path, exc)], raise_on_error)
    top_el = tree.getroot()
    diagrams = [top_el] if top_el.tag == "mxGraphModel" else list(top_el.iter("diagram"))
    for d in diagrams:
        where = "page %s" % (d.get("name") or d.get("id") or "?")
        model = d if d.tag == "mxGraphModel" else d.find("mxGraphModel")
        try:
            if model is None:   # compressed page: base64 of raw-deflated, URL-encoded XML
                text = urllib.parse.unquote(zlib.decompress(base64.b64decode((d.text or "").strip()), -15).decode("utf-8"))
                model = ET.fromstring(text)
        except (ValueError, zlib.error, ET.ParseError) as exc:
            issues.append("%s: cannot read page content (%s)" % (where, exc))
            continue
        root = model.find("root")
        if root is None:
            issues.append("%s: no <root> element" % where)
            continue
        issues.extend(_check_records(where, _cell_records(list(root))))
    return _raise_or_return(issues, raise_on_error)


# ---------------------------------------------------------------- output
def save(path):
    """Write all pages to one .drawio file."""
    if not _pages:
        _cells()
    diagrams = []
    for p in _pages:
        diagrams.append(
            '<diagram id="%s" name="%s"><mxGraphModel grid="1" gridSize="10" page="1" pageWidth="%s" '
            'pageHeight="%s"><root><mxCell id="0"/><mxCell id="1" parent="0"/>%s</root></mxGraphModel></diagram>'
            % (p["id"], esc(p["name"]), p["w"], p["h"], "\n".join(p["cells"])))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write('<mxfile host="app.diagrams.net">' + "".join(diagrams) + "</mxfile>")
