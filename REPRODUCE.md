# How this repository was made (João Pessoa)

This file is written by the build on 2026-11-05, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Câmara Municipal de João Pessoa, SAPL: Lei Orgânica do Município, atualizada até a Emenda nº 44/2026 (PDF) | <https://sapl.joaopessoa.pb.leg.br/norma/14101> | 2026-11-05 | Text: Câmara Municipal de João Pessoa, SAPL, Lei Orgânica do Município de João Pessoa (atualizada até a Emenda nº 44/2026), sapl.joaopessoa.pb.leg.br. Lei 9.610/1998 art. 8 IV: the texts of laws and other official acts are not protected by copyright. Non-official text: only the official gazette is authoritative. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `lei-organica` | Lei Orgânica do Município de João Pessoa | 1 | 2026-06-03 to 2026-06-03 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-11-05.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (America/Fortaleza) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Lei Orgânica and its amendments are promulgated by the Mesa da Câmara and take effect on promulgation; this record holds only the updated text, dated by the edition. https://sapl.joaopessoa.pb.leg.br/norma/14101

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `8e8fc61eda25a40c946c08cf7bfd71fe020ace92b8979688e11c8ddc91b442e2` (241407 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `35388bee5aa05369f7da68f5a8fa015ea8d442b8`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Lei Orgânica is given only as the Câmara's updated edition ("atualizado até a Emenda à Lei Orgânica nº 44/2026", junho de 2026), credited to the Câmara as the oldest version available and dated by the edition's own date (the PDF's creation date, 3 June 2026): its notes give only the number and year of each amendment. The text as promulgated on 2 April 1990 and the wordings the amendments replaced are not in the edition.
- Left out: the cover, the table of contents, the page footers and the alteration notes in parentheses ("(Redação dada pela Emenda à Lei Orgânica nº ...)", "(Inciso acrescentado pela ...)", "(Revogado pela ...)"). A paragraph broken across two pages is joined again.
- One file per Art.; headings stand above the first article under them. The signatures of the constituent assembly after the last article stay with it.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text or dates: every word comes from the Câmara's PDF.
