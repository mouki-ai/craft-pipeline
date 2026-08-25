# Attribution

Everything under `plugins/*/skills/` and `plugins/pipeline-core/library/` except the
skills in `authored/` is third-party work, vendored unmodified at a pinned commit.
Each vendored folder carries a `_source.json` naming its upstream repo, commit,
licence and copyright holder.

| Upstream | Holder | Licence | Pinned commit |
|---|---|---|---|
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | Jakub Krehel | MIT | `ca483852de` |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Emil Kowalski | MIT | `d23d7f88a2` |
| [codeswithroh/tastemaker](https://github.com/codeswithroh/tastemaker) | codeswithroh | MIT | `45313ce9f6` |
| [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | Elaya | MIT | `1c1e97cb98` |
| [MengTo/Skills](https://github.com/MengTo/Skills) | Meng To | MIT | `4c716b516b` |
| [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) | MC Dean | MIT | `20e34c4a58` |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | ConardLi | MIT | `aaf9a82f5e` |

All of the above are MIT-licensed. Their licence text and copyright notices travel
with the vendored files; this file and each `_source.json` carry the attribution the
MIT licence requires. Nothing here is relicensed: the vendored files remain under
their original terms, and this repository's own MIT licence covers only the parts
written for it (`authored/`, `scripts/`, `docs/` and the READMEs).

## Referenced but deliberately not vendored

`github.com/mouki-ai/chatgpt-scrollcraft` @ `1eb8f930` carries no LICENSE file, so it
is not redistributable. The `site-pipeline` skill hands the build to it when it is
installed, and runs the phases itself when it is not. Install it separately.

If you own that repository, add a licence to it and it can be vendored here like
the rest.
