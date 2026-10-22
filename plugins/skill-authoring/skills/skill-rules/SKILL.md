---
name: skill-rules
description: "Rules for writing, revising or reviewing a SKILL.md so it stays general across projects. Use when creating, editing or reviewing a skill (including a plugin's skills), turning a workflow into a skill, or when the user corrects a skill's output and the correction may belong in the skill, including whenever skill-creator or another skill- or plugin-building skill is used."
---

# Skill rules

A skill is used across many projects and by people who never saw the conversation it came from. Most skills are drafted inside one project, so that project's audience, names, paths, cases and habits leak in by default. This holds also for a skill stored inside one project: its project-specific content still goes in that project's instructions, so the skill can be moved or shared later. A rule can be correct and still be in the wrong place or the wrong order; both make the skill harder to follow.

Project-specific content lives in **the project's own instructions**: its `CLAUDE.md`, its Project instructions, or files the user points to. The agent already has them in context; a skill only states that they take precedence over its defaults.

This skill has no Project conventions section, because its rules decide what a project may override.

When skill-creator or another skill- or plugin-building skill is loaded as well, use it for the process (interview, test cases, evals, description tuning, packaging). For what goes into a skill, where it goes, in what order, and whether it carries examples, these rules take precedence over its writing guidance. Without such a skill, still run the skill on at least three realistic requests, including one that should not trigger it, and compare the output with a run without the skill before it ships.

## Workflow

1. Read the inputs (Before starting).
2. If the task is folding in a user's correction, classify it first (section 6).
3. Write or revise by sections 1 to 5.
4. Run the review checklist (section 7).

## Before starting

- Read the whole skill folder (SKILL.md, references, scripts, assets) and any README that describes the skill.
- Read the other skills in the same plugin or marketplace: their Project conventions block, their terms and their `description`s, so wording matches and no two descriptions claim the same requests without a stated coupling.
- For a new skill, read the material it is drafted from and note which parts are project-specific.

## 1. Placement: where each piece of content goes

For every line, ask two questions: **would this still be true in a different project?** and **does the agent need it while doing this skill's task?**

| Content | Destination |
|---|---|
| When to use the skill, and what it does in a phrase (not a summary of its rules) | `description` only. The body's opening scope paragraph states boundaries (what the skill covers and leaves to the project), never triggers. |
| When to use it together with another skill ("including whenever X is used") | `description`: the body is read only after the skill loads, so a coupling written there never fires |
| How the work is divided with another skill, or how the skill does its work | The body. `description` does not describe how other skills work or the method. |
| Tools, surfaces or runtimes the skill requires | `compatibility`, requirements only. Omit the field when nothing is required. |
| A general procedure, rule or failure pattern | The skill body |
| Long general reference material, or rules for one of several tools or variants | `references/<topic>.md`, linked from the body with when-to-read guidance |
| Repeated deterministic work | `scripts/`, called or copied when the work is done |
| Files used in the output that hold in any project | `assets/`, referenced from the body |
| Audience, purpose, scenario, section structure, fixed vocabulary, document template files, fonts, colours, sizes for one project | The project's own instructions |
| Pitfalls of one project's environment or tools | The project's own instructions |
| Concrete examples and cases (section 4) | The project's own instructions |
| A project fact needed by several skills (data locations, terminology) | The project's own instructions, stated once for all skills |
| How the user wants replies written (language, length, tone, honesty conventions) | The user's own settings (for example `~/.claude/CLAUDE.md` or account preferences), never a skill |
| The user's personal workflow: where they keep project material, how it gets loaded, how they maintain and release skills | The user's own settings or a private repository, never a shared skill |
| Maintenance guidance the agent needs while doing the task (where to record a correction the user makes) | The skill, in one line |
| The procedure for folding a user's correction into a skill (classifying it, rewriting, checking) | This skill, not the skill being maintained |

When a project case teaches a general lesson, write the lesson into the skill in general form and leave the case itself in the project's own instructions.

Content moved out of a skill is never just deleted. If you can edit its destination (the project's instructions or the user's own settings), add it there; otherwise give the user the exact text and name the file or setting it belongs in.

Output of a skill-building skill's process is still content. A tuned `description` keeps to the rows above (what and when, no method). Test prompts and eval files hold concrete cases, so they stay outside the skill folder.

### Correctness rules, consistency requirements and defaults

Leaving every open choice to the agent makes output vary from run to run, so a skill does fix some choices. Classify each fixed choice by what goes wrong without it:

1. **Correctness rule**: without it the output is wrong or misleading. State it as a rule.
2. **Consistency requirement**: some choice must be made, and any reasonable choice works if it is applied throughout one output and kept when that output is revised. Require the consistency, not a particular choice. Where outputs of separate runs must match each other, the choice needs a default.
3. **Default**: one specific value for a consistency requirement. Keep it, marked as a default with its reason, if the values a competent practitioner would reasonably choose instead give worse output for a reason you can state. If they are merely different, it is personal taste and belongs in the user's own settings.

A value that a bundled script must hold anyway (a corner style, a spacing constant) is a default even when its only reason is that some value is needed; document it as overridable.

Mark each default where it is stated ("Default: …"), so a reader can tell what a project may override. A skill never gives an unmarked value for anything it says belongs to the project; a marked default for such an item is allowed, and the project's conventions override it.

## 2. Required section: Project conventions

Every skill includes this section right after its scope, so the agent knows the project's instructions outrank the skill's defaults. Omit it only when the skill's rules must hold whatever a project says, and say so in the scope paragraph. Within one plugin or marketplace, keep the wording identical across skills, heading included, so a project's instructions and a reviewer can rely on one fixed statement. A new plugin may start from this text:

```markdown
## Project conventions

A project may set its own conventions for this work, in its `CLAUDE.md`, its Project instructions, or files the user points to. Where they conflict with this skill, the project's conventions win; otherwise use the defaults below. A correction that holds only for one project belongs in that project's instructions, not in this skill.
```

After it, a skill may add one line listing what projects commonly set.

The section says only that project conventions win and where single-project corrections go. Where a user keeps project-specific material, and how it is loaded, is the user's own workflow and stays out of shared skills.

## 3. Order

The body follows the order of the work:

1. **Scope**, with definitions of terms used across the skill; a term first needed later is defined at the start of the section that first uses it.
2. **Project conventions** (section 2).
3. **Workflow summary**, if the skill has several stages or entry points: a short numbered list pointing to the sections. It is the only place that refers forward to a later section; a link to a file in `references/` is not a forward reference.
4. **Before starting**: everything that must happen before work begins.
5. **Rules in the order they are applied.**
6. **Review checklist last**, in the same order as the rules.

Within the body:

- Group rules by when they are applied, not by topic. A list of pitfalls is split up and placed with the steps where each one applies.
- One place per rule. If two sections need it, state it once and refer to it. The review checklist names the rules it checks; that is not a second statement of them.
- One term per concept. Once a term is chosen, use it throughout; a synonym reads as a different thing.

## 4. Examples

- A skill carries no examples or cases. An example is a worked instance of a rule: a sample input with its output, a before/after pair, a sentence or figure to imitate, or an account of what happened in a particular project. State each rule so it can be applied without one; if it cannot be, the rule is probably project-specific.
- Concrete examples come from a project and go in that project's own instructions, where they cannot mislead other projects.
- Not examples, and allowed: a list of the generic kinds a rule covers (a scope list), format specifications and output templates, and a short API usage snippet for a bundled script, all written with neutral placeholders (`<name>`, `YYYY-MM`) or invented generic values, never content taken from a project.
- Never include real project names, repository paths, people, internal URLs, project-specific datasets or models, secrets or credentials.

## 5. Content hygiene

- **Contradictions**: no two rules conflict, and `description`, `compatibility`, body, references, scripts and README agree.
- **Necessity**: every correctness rule and default says why unless the reason is obvious. Delete a line only when the agent would make the same choice in every run without it, or cannot act on it; a default that removes run-to-run variation stays. A rule with no action ("be careful with X") is rewritten as an action or removed.
- **Environment pins**: name a specific machine, OS-only path, interpreter version or tool release only when the skill requires it, and then give the minimum version and how to check or install it. Avoid claims about a tool's behaviour that will date; if one is needed, date it ("as of YYYY-MM") and say how to recheck.
- **Frontmatter**: `name` equals the folder name, has at most 64 characters, uses only lowercase letters, digits and hyphens, and does not contain "anthropic" or "claude". `description` has at most 1,024 characters, contains no `<` or `>`, and avoids first and second person ("I can", "you can"), because it is injected into the system prompt. `compatibility`, if present, has at most 500 characters.
- **References and code**: every referenced file exists; paths use forward slashes; instructions say whether each script is run or read; scripts handle their own errors and explain their constants; documented signatures and defaults match the code; MCP tools are named in full (`Server:tool_name`).
- **Size and structure**: the `SKILL.md` body stays under about 500 lines; detail moves to `references/`. Every reference file is linked directly from `SKILL.md`, never only from another reference file, and a reference file longer than 100 lines starts with a table of contents.

## 6. Folding feedback back in

When the user corrects a skill's output, classify the correction before editing:

1. **General**: rewrite the relevant section so the whole class of mistake is prevented. Do not add a narrow special case.
2. **Project-specific**: add it to that project's own instructions and leave the skill unchanged.
3. **The user's own preference**: a reply preference, a matter of personal taste, or the user's personal workflow. It goes in the user's own settings, not in any skill.
4. **Unclear**: ask the user which it is.

State the destination you chose and why in one line. If a rule later turns out to be general, move it from the project's instructions into the skill and delete it there, so it never exists twice.

## 7. Review checklist

Run this on the whole skill before it ships, in this order, and report each finding with its line and the fix. When the user asked for a limited edit, fix findings in the lines you changed and list the others without fixing them.

1. **Placement** (section 1): `description` holds only what (in a phrase) and when, including couplings to other skills, not the method; the body states how work is divided with another skill and does not restate triggers; `compatibility` holds only requirements or is omitted; long or variant-specific material is in `references/` with when-to-read guidance; repeated deterministic code is in `scripts/`; project audience, purpose, structure, vocabulary, document templates, styling, pitfalls, cases and shared facts are moved to the project's instructions; reply preferences, personal taste and personal workflow are moved to the user's settings; each project case is reduced to its general lesson; moved content was added to its destination or handed to the user; every fixed choice is a correctness rule, a consistency requirement or a marked default with its reason.
2. **Project conventions** (section 2): present unless the scope says why the skill is exempt; identical, heading included, to the block in the other skills of the same plugin or marketplace; right after the scope; nothing about where or how a user stores project material.
3. **Order** (section 3): sections follow the order there; forward references occur only in a workflow summary; rules are grouped by when they are applied and pitfalls sit with their steps; no rule is stated twice; one term per concept.
4. **Examples** (section 4): no examples or cases; every rule applies without one; scope lists, format specifications, templates and API snippets use neutral placeholders; no real project names, repository paths, people, internal URLs, project datasets or models, secrets or credentials.
5. **Hygiene** (section 5): contradictions, necessity, environment pins, frontmatter, references and code, size and structure.
6. **Feedback** (section 6): each folded correction was classified and its destination stated; no rule exists both in the skill and in a project's instructions; no narrow special case was added.
