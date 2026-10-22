# Rendering .drawio files from the command line

Read when you need to install draw.io or render a diagram to an image.

The flag descriptions below were checked as of 2026-10 against the draw.io desktop source (`src/main/args.js` and `src/main/electron.js` on the main branch of jgraph/drawio-desktop, `package.json` version 32.5.5) and the CLI notes of the drawio skill in jgraph/drawio-mcp. Recheck on the installed version with `<drawio> --version` and `<drawio> --help`; the help output lists every option the installed build accepts.

## Find the CLI

| System | Command |
|---|---|
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Windows | `"C:\Program Files\draw.io\draw.io.exe"` (confirm the install path first) |
| Linux, desktop app installed | `drawio` (check with `command -v drawio`) |
| Linux, headless | the .deb below, run under `xvfb-run` |

## Export flags

| Flag | Behaviour |
|---|---|
| `-x`, `--export` | Export mode. Takes one or more input files or folders as positional arguments. |
| `-f`, `--format <format>` | `pdf` (the default when nothing is given), `png`, `jpg`, `svg`, `xml` or `html`. Ignored when the `-o` file name has an extension: the extension decides. |
| `-o`, `--output <file or folder>` | Output file or folder. When omitted, the input name is used with the format as extension. Exporting several inputs needs a folder. |
| `-p`, `--page-index <n>` | Page to export, counted from 1 (tab order). Before draw.io 27.0.2 it counted from 0; `0` now fails with "Invalid page index". Without it, an image export renders the first page. |
| `-a`, `--all-pages` | All pages, for `pdf` and `html` only. An image export always renders one page, so export each page of a multi-page file with its own `-p`. |
| `-s`, `--scale <factor>` | Scale factor on the diagram's size: `3` is 300 %. |
| `-b`, `--border <px>` | Border around the content (default 0). |
| `-t`, `--transparent` | Transparent background for PNG and SVG (otherwise white). |
| `--theme <dark\|light\|auto>` | Appearance of the export. With `auto`, PNG, JPEG and PDF render light and SVG stays adaptive to the viewer. Not present in older builds: look for it in `--help`. |
| `--size <diagram\|page>` | `diagram` (the default) crops an image to the content, `page` exports the full page. |

Unknown flags are dropped silently by the argument parser, so a misspelled or unsupported flag does not fail: confirm in the output image that an option took effect.

## Flags for headless Linux

`--no-sandbox` and `--disable-gpu` are not draw.io options. They are Chromium switches that the Electron-based app passes on.

- `--no-sandbox`: needed when running as root or in a container, where Chromium refuses to start its sandbox. The draw.io source explicitly excludes this flag from the list of input files, so it is safe next to the export options.
- `--disable-gpu`: not in draw.io's own documentation; third-party draw.io export wrappers use it for machines without a usable GPU (an option to try when an export hangs or logs GPU errors). draw.io's own switch for the same purpose is `--disable-acceleration`, which calls Electron's `disableHardwareAcceleration`.

## Render

Default: preview at `-s 1.5` (large enough to read labels when inspecting, small enough to be quick). The destination scale comes from the project's conventions or section "Before starting" of `SKILL.md`.

```bash
<drawio> -x -f png -s 1.5 -o out.png in.drawio       # preview, first page
<drawio> -x -f png -s 3 -p 2 -o page2.png in.drawio  # 300 % export of page 2
<drawio> -x -f pdf -a -o all.pdf in.drawio           # every page, PDF only
```

To render every page of a multi-page file as images, count the `<diagram>` elements in the file and run the second command for each page number from 1. If the draw.io build is older than 27.0.2, page numbers start at 0: render `-p 1` and `-p 2` of a two-page file and compare the images to see which convention applies.

## Headless Linux install

Needs root and the `xvfb` package. Download the current `drawio-amd64-<version>.deb` from https://github.com/jgraph/drawio-desktop/releases (asset name and install location not rechecked as of 2026-10), then:

```bash
sudo apt-get install -y ./drawio-amd64-<version>.deb xvfb   # resolves dependencies
command -v drawio || ls /opt/*/drawio                       # locate the executable
xvfb-run -a drawio --no-sandbox -x -f png -s 1.5 -o "$PWD/out.png" "$PWD/in.drawio"
```

- `xvfb-run` supplies the virtual display the app needs without a desktop.
- `--no-sandbox` is required when running as root.
- Use absolute paths for `-o` and the input.

## Why PNG rather than SVG

draw.io's SVG stores box text as HTML (foreignObject). PowerPoint, Keynote and system previews render it inconsistently (lost text or lost lines). Offer SVG only when the user must edit shapes in the slide tool, and ask them to check it after inserting.

As observed on dark-themed editors (not in draw.io's documentation, as of 2026-10), default colours (`fillColor=default` and similar) follow the editor's appearance, so such a diagram can export with white lines and text. Export PNG and PDF with the light appearance (`--theme light` where the build has it) and check the image on a white background.
