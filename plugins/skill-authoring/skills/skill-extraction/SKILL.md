---
name: skill-extraction
description: "Turn a way of working that has settled through repeated correction into a skill or a rule document. Use when a piece of work (troubleshooting, design, analysis, coordination) has converged after back-and-forth and is worth following directly next time, when the user asks to record a method, workflow, preference or principle as a skill or rule document, and whenever skill-rules (skill-authoring:skill-rules) is used to turn a workflow into a skill."
---

# Skill extraction

Covers the path from raw material to a verified draft in its final place: recording the material, choosing where it goes, abstracting it, writing it and having it checked by someone who did not write it. What goes into a skill, in what order and with which review checklist is governed by `skill-rules` (`skill-authoring:skill-rules`); load it as well and follow it wherever this skill says "write".

Terms used throughout:

- **Method**: a procedure for doing some kind of work (troubleshooting, design, analysis, coordination). Its output is steps, each with a done condition, and pitfalls.
- **Preference**: one person's taste, principles or rules about a kind of work. Its output is general rules, each with a check question and the person's own words.
- **Pitfall**: a point where the work went wrong, stated as what was first believed, what was actually true, and what to do instead.
- **Done condition**: a test that shows whether a step is finished.
- **Record file**: the file holding the raw material and its sources, which the draft is built from.
- **Draft folder**: a working location outside every folder the tool loads skills from, holding the record file and the draft until verification ends. A draft placed in a skill folder can trigger before it has been checked.
- **Shared skill**: a skill meant for use across projects and by people who never saw the material.

When one task produces both a method and a preference, extract them as two separate outputs.

## Project conventions

A project may set its own conventions for this work, in its `CLAUDE.md`, its Project instructions, or files the user points to. Where they conflict with this skill, the project's conventions win; otherwise use the defaults below. A correction that holds only for one project belongs in that project's instructions, not in this skill.

Projects commonly set: where the draft folder and record files are kept, the record file's name, where the project stores preferences, and who verifies drafts.

## Workflow

1. Write the material into a record file (section 1).
2. Decide where each piece goes, and whether it extends an existing skill or starts a new one (section 2).
3. Abstract the material into general steps, pitfalls or rules (section 3).
4. Write the draft (section 4).
5. Have a fresh agent verify it, then move it into place (section 5).

## Before starting

- Load `skill-rules`; sections 2 to 5 of this skill depend on its placement rules and review checklist.
- Decide whether the material is a method, a preference or both, by the definitions above.

## 1. Record the material

Write all raw material into a record file in the draft folder before writing any skill text; the draft quotes from this file. Copy in material that exists only in the conversation too: conversations get compressed and sessions restart, and text rewritten from memory turns into paraphrase.

- **Method**: the steps finally used; every wrong turn, with what was believed at the time and what was actually true; who or what revealed the wrong turn.
- **Preference**: the person's own words, verbatim. Where only someone else's paraphrase can be found, copy it as given and mark it as paraphrase, naming who paraphrased.

Give every entry a source: date and location (a file path, or the conversation it came from). Write file paths without line numbers, because line numbers drift as files change; the quoted words themselves serve as the search anchor.

Default record file name: `SOURCES.md`, so the record is found by name beside what it supports.

**Done when** the record file exists and every entry has a source.

## 2. Decide placement, and extend or create

### Placement

For each entry, ask whether it would still hold in another project:

| Entry | Destination |
|---|---|
| A method that holds in other projects | A shared skill |
| Parts of a method that hold only in this project (its tools, conventions, environment pitfalls) | The project's own instructions |
| A method whose generality cannot yet be judged | The project's own instructions first; move it to a shared skill when it recurs in another project |
| A preference about how a kind of work is done (taste) | The project's own instructions (a taste skill, as `skill-rules` defines it, counts), never a shared skill |
| A preference about how replies are written, or the person's own way of working | The user's own settings, never a shared skill |
| A taste the person states holds everywhere | The project's own instructions, like any other taste. Bringing it to other projects follows the user's own process for changes that span projects (stated in the user's settings or the project's instructions); never a shared skill |

Preferences stay out of shared skills because a shared skill is used by people whose taste differs, and `skill-rules` places personal taste outside them.

When one extraction has entries for both a shared skill and the project, split it: the shared skill holds the general part, and the project's instructions hold the specific part and point to the shared skill.

When the user names a document to write into (for example a project's rule file), write there instead of making a skill, and skip the trigger decision in section 4.

Decide here where the record file goes when verification ends, so that section 3 can point to its final location:

- Destination in the project's own instructions: the project's notes or reports location, by its conventions.
- Destination is a document the user named: the same folder as that document, named `<document-name>-SOURCES.md`.
- Destination is a shared skill: outside the skill folder, in a location the project's conventions name, or that the user names when asked. The record holds project cases and names, which never ship in a shared skill.
- When the extraction is split, each part takes its own entries.

### Find the closest existing skill

List the skills already at the destination, plus the skills available in the current session (skills installed by plugins appear only in that list).

- **Method**: put the two sets of steps side by side. They are the same skill only if each could be used to do the other's work.
- **Preference**: draft a check question for each quoted rule first (finalised in section 3). They are the same skill only if both come from the same person and the check question also makes sense when applied to the kind of work the existing skill covers.

| Found | Action |
|---|---|
| The same skill | Add to it (new steps, pitfalls, quotes) |
| Same shape of procedure, but this domain has a part no other domain uses | Add a supplementary section to the existing skill. If the supplement outgrows the main text, make a separate supplementary skill whose opening line names the skill it supplements |
| The closest skill comes from a plugin | Create a new skill whose opening line names the plugin skill it supplements |
| Nothing | Create a new skill |

**Done when** every entry has a destination (shared skill, project's instructions, user's settings or named document) and a target skill or document, or a reason for a new one.

## 3. Abstract

A skill states how to find the answer. An answer that belongs only to this one occasion (this fix, the identifier hit this time, this occasion's numbers) stays in the record file. Values the subject always uses (a tool path the project runs every time, the numeric value a preference itself sets) are part of the rule and go wherever the rule goes.

- **Method**: write each wrong turn as a pitfall. Wrong first guesses are the most valuable part of a method. State each pitfall as one general sentence (it may be a negative statement) followed by what to do instead, and place it with the step where it applies. The date and numbers of the occasion stay in the record file.
- **Preference**: write each rule as one general sentence, followed by:
  - **Check question**: one question the person doing the work asks of their own output before handing it over.
  - **Own words**: the verbatim quote with its source, or the paraphrase marked as such. The specific object the person was talking about goes in the source, not in the rule.
  - The rule has the same strength as the words: words that say "may", "even" or "usually" give a rule that says may or usually, not "always". When the words speak of one object only, ask before generalising whether applying the rule to other objects would remove something reasonable; if it would, keep it to that object.
  - Refer to the person by a role word instead of a pronoun or a name, because a pronoun lets another session pick the wrong person. Choose a role word not already used for a different role in the same skill. The name stays only in the record file's sources.
- Lists that change over time (open questions, an object's current state, decisions about a single object) stay in the record file.
- Pointers to the record file: the project's own instructions may follow a rule or pitfall with a pointer to its record entry, so later readers can confirm it was real. A shared skill carries no pointer, because the path and the case would leave the project (`skill-rules` section 4).

**Done when** the text of the rules and steps (quotes and sources excluded) contains no file name, number or identifier that belongs only to this occasion, and a shared skill also contains no project name, path or person.

## 4. Write

Write in the draft folder; move into place only after section 5.

First decide how the skill is triggered:

- **Model-triggered** (most extracted skills): the `description` names the topic, then lists only the situations that call for it, stated as general situations ("something that used to work has broken") rather than the occasion it came from.
- **Manual only**: use the tool's setting for skills that run only when called by name. The `description` still follows `skill-rules` section 1: what the skill does and when to call it.

Then write by `skill-rules` sections 1 to 5 and run its review checklist (section 7), including its test run on realistic requests. Its rules on wording apply to the instructions the skill gives; quoted own words stay verbatim, and pitfalls keep the form section 3 gave them.

For a destination that is a document rather than a skill, follow that document's conventions and `skill-rules` section 1 for what belongs there.

**Done when** the trigger mode is decided and every finding of the `skill-rules` review checklist is fixed or listed with a reason.

## 5. Verify with a fresh agent

Hand the draft to a newly started agent that has not seen this conversation, not a copy of the current one: a copy carries the same assumptions and misses the same gaps. Ask it to act as if following the draft. For a preference, ask it to take an existing real piece of work and apply each rule to it in turn, because reading the rules alone does not show where they reach too far. Ask it to report:

- steps it does not know how to carry out;
- terms with two readings;
- rules that conflict;
- rules that hold only for one specific object.

Write the handling of every reported item into the record file: what was changed, or why nothing was changed.

If a fix changes what a step does or a rule's criterion, have another newly started agent verify again. Items about wording only, which do not change what is done, need no new round.

**Done when** every item in the last round has its handling recorded, and every confirmed item of the four kinds is fixed. Then move the draft to the destination chosen in section 2, and the record file to the location chosen there.

## 6. Review checklist

1. Record (section 1): the record file exists in the draft folder; every entry has a source without line numbers; own words are verbatim or marked as paraphrase.
2. Placement (section 2): every entry has a destination; no preference is in a shared skill; the record file's final location is decided; the closest existing skill was compared and the extend-or-create choice is recorded.
3. Abstraction (section 3): no occasion-only names, numbers or identifiers in rules and steps; every pitfall says what to do instead and sits with its step; every preference rule has a check question, own words and matching strength; the person is named by a role word; a shared skill has no pointer to the record file.
4. Writing (section 4): trigger mode decided; `skill-rules` review checklist run.
5. Verification (section 5): a fresh agent ran on the draft; every item has recorded handling; a new round followed every change to a step or criterion; the draft and record file are in their final locations.
