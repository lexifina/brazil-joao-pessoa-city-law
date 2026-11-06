# How this repository was made (João Pessoa)

This file is written by the build on 2026-11-06, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Câmara Municipal de João Pessoa, SAPL: Lei Orgânica do Município, atualizada até a Emenda nº 44/2026 (PDF) | <https://sapl.joaopessoa.pb.leg.br/norma/14101> | 2026-11-05 | Text: Câmara Municipal de João Pessoa, SAPL, Lei Orgânica do Município de João Pessoa (atualizada até a Emenda nº 44/2026), sapl.joaopessoa.pb.leg.br. Lei 9.610/1998 art. 8 IV: the texts of laws and other official acts are not protected by copyright. Non-official text: only the official gazette is authoritative. |
| Câmara Municipal de João Pessoa, SAPL: records of the municipal laws and their PDFs (newest first) | <https://sapl.joaopessoa.pb.leg.br/norma/pesquisar> | 2026-11-06 | Texts: Câmara Municipal de João Pessoa, SAPL (Sistema de Apoio ao Processo Legislativo), sapl.joaopessoa.pb.leg.br; SAPL: "Conteúdo e dados sob licença Creative Commons 4.0 Atribuir Fonte - Compartilhar Igual". Lei 9.610/1998 art. 8 IV: the texts of laws and other official acts are not protected by copyright. Non-official text: only the official gazette is authoritative. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `lei-organica` | Lei Orgânica do Município de João Pessoa | 1 | 2026-06-03 to 2026-06-03 |
| `lei-2025-15465` | Lei nº 15.465, de 4 de fevereiro de 2025 | 1 | 2025-02-06 to 2025-02-06 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-11-06.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (America/Fortaleza) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Lei Orgânica and its amendments are promulgated by the Mesa da Câmara and take effect on promulgation; this record holds only the updated text, dated by the edition. https://sapl.joaopessoa.pb.leg.br/norma/14101

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `fb6ca3b4e986ab51fa21fd8f023c4d63df8eab6cb4b1351139d8bc491e2954da` (254482 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `35388bee5aa05369f7da68f5a8fa015ea8d442b8`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Lei Orgânica is given only as the Câmara's updated edition ("atualizado até a Emenda à Lei Orgânica nº 44/2026", junho de 2026), credited to the Câmara as the oldest version available and dated by the edition's own date (the PDF's creation date, 3 June 2026): its notes give only the number and year of each amendment. The text as promulgated on 2 April 1990 and the wordings the amendments replaced are not in the edition.
- Left out: the cover, the table of contents, the page footers and the alteration notes in parentheses ("(Redação dada pela Emenda à Lei Orgânica nº ...)", "(Inciso acrescentado pela ...)", "(Revogado pela ...)"). A paragraph broken across two pages is joined again.
- One file per Art.; headings stand above the first article under them. The signatures of the constituent assembly after the last article stay with it.
- Each municipal law ("Lei" and "Lei Complementar") is given as enacted, from the PDF the Câmara's SAPL holds for it, credited to the law itself and dated by the publication date SAPL records for it (else by the law's own date). Later amendments by other laws are not worked into earlier laws: each law is its own file set as enacted. Laws are taken newest first, in parts.
- Left out: scans (with or without an OCR layer), PDFs whose heading does not carry the record's number, texts with no article or no closing date line, texts carrying alteration notes, and laws whose vigência clause sets another day than their publication (or that have none, so that the 45 days of the LINDB apply).
- The text runs from the law's heading to its closing date line (signatures after it are left out); lines repeated at the top or bottom of two or more pages (letterheads, footers) and page numbers are left out. Lines are joined into paragraphs: a new paragraph starts at a provision label, a heading line, or after a line ending in ".", ";" or ":". One file per Art.; "000-titulo" holds what comes before the first article.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text or dates: every word comes from the Câmara's PDF.
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text or dates: every word comes from the Câmara's SAPL.
