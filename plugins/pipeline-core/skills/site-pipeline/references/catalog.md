# The catalog

`catalog/index.tsv` — one tab-separated line per skill: `name · phase · tags · cost · trigger · path`.
`cost` is the rounded token price of reading that skill's `SKILL.md`; a `+` means it carries
further reference files.
268 lines, about 12k tokens if read whole, which is why nothing reads it whole. `find-skill`
scores it and returns ten lines; `grep` works the same way if the shell is unavailable.

`catalog/by-phase/*.tsv` — the skills the pipeline explicitly assigns to a phase. Small enough
to read whole when you are planning that phase (each is a few hundred tokens).

`catalog/tags.txt` — the tag vocabulary with counts. Use it when your words return nothing:
pick the nearest tag and search by tag instead.

## How phase and tags get assigned

Phase comes from `scripts/sources.json` → `phases`: the curated assignment of a skill to a
stage of the pipeline. A skill with `-` is in the library but unassigned — usable, but nothing
in the pipeline vouches for it at a particular moment.

Tags are derived from each skill's own name and description by the regex table at the top of
`scripts/vendor.py`. To retag, edit that table and re-run the vendor script. Do not hand-edit
files under `plugins/` — they are generated and will be overwritten.

## Adding your own

Author it at `authored/pipeline-core/<name>/SKILL.md` and it becomes a registered, always-on
skill — reserve that for things needed in every session. Anything else belongs in the library:
add its repo to `upstream` in `sources.json`, or drop the folder into
`plugins/pipeline-core/library/local/<name>/` and re-run `scripts/vendor.py` after adding
`local` to the manifest.

Promote a library skill to a phase by naming it under `phases.<n>.owners.<upstream>`. That is
the cheap kind of promotion: it changes ranking and `--phase` output, and costs no context.
