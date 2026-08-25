# Adding, removing and authoring skills

## Promote a library skill into the core

Edit `scripts/sources.json` → `core.<plugin>.skills.<upstream>` and add the skill's
name. Re-run `python3 scripts/vendor.py`. It moves out of the library automatically —
nothing is ever in both tiers, and `validate.py` fails the build if it is.

Promote sparingly. Every core skill costs context in every session and adds one more
description that can collide with another. Before promoting, add a row to the
conflict table in `authored/pipeline-core/site-pipeline/references/conflicts.md`
saying which question it owns and which skill it takes that question from.

## Demote a core skill

Remove its name from `scripts/sources.json` and re-run the vendor script. It reappears
in the library.

## Add a new upstream

Append to `upstream` in `scripts/sources.json` with the repo URL, a pinned commit, its
licence and holder. Re-run the vendor script; every skill it finds lands in the library
unless you also name it under `core`. Check the licence first: only redistribute what
the licence allows, and add it to `NOTICE.md`.

## Author your own

Create `authored/<plugin>/<skill-name>/SKILL.md` with `name` and `description`
frontmatter. The vendor script copies it into that plugin on every build, so it
survives regeneration. This is where project-specific skills belong — brand rules, a
client's component conventions, a deploy runbook.
