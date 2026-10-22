# Skills

General-purpose skills for Claude, packaged as a plugin marketplace. Each skill describes how to do one kind of task well, with defaults that hold in any project.

## Plugins

| Plugin | Skills | What they do |
|---|---|---|
| `presentation` | `slides`, `arch-diagram` | `slides`: rules for informational slide decks: claims grounded in sources, a title sequence that tells the argument, consistent terms and units, figures that match the system they depict, layout checked before publishing; Claude Slides limits included. `arch-diagram`: an architecture or data-flow diagram of a codebase or system as an editable draw.io file, verified against the code, machine-checked and render-checked; bundles a generator script. |
| `skill-authoring` | `skill-rules` | Rules for writing and reviewing skills: what belongs in a skill and what belongs to a project or to you, which fixed choices are rules and which are defaults, section order, and a review checklist. |

## Install

**Claude (claude.ai or the desktop app)**: Customize → Plugins → Add → Add marketplace → `AlfreShen/skills`, then add the plugins you want.

**Claude Code**

```bash
claude plugin marketplace add AlfreShen/skills
claude plugin install presentation@AlfreShen
claude plugin install skill-authoring@AlfreShen
```

Skills trigger on their own when a task matches. To run one directly: `/slides` on claude.ai, or `/presentation:slides` in Claude Code.

## Adapting to your project

The skills use your project's own instructions when they differ from the defaults: your project's `CLAUDE.md` in Claude Code, or the Project instructions on claude.ai. State there what your project needs, such as audience, templates, fonts or fixed terms, and the skills follow it.

## Requirements

- **Claude (claude.ai or desktop)**: a paid plan; plugins are available on Pro, Max, Team and Enterprise.
- **Claude Code**: a release with plugin support, and `git` to add a GitHub-hosted marketplace.
- **`arch-diagram`**: code execution, Python 3.6+, and the draw.io desktop app or CLI for the render check (on headless Linux also `xvfb`). The skill asks before installing draw.io.

## Updates

Each plugin has its own version; a new release of one plugin does not touch the other.

- **claude.ai**: use **Check for updates** on the marketplace, or turn on **Sync automatically**.
- **Claude Code**: auto-update is off by default for third-party marketplaces. Turn it on in `/plugin` → Marketplaces, or run `claude plugin update <plugin>@AlfreShen`.

Product details above are as of 2026-10.

## License

MIT. See [LICENSE](LICENSE).
