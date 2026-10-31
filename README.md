# João Pessoa (city): law history in git

The municipal law of the Município de João Pessoa, the city of João Pessoa (Paraíba) (Brazil) as a git history: one file per Artigo, one paragraph per line, so `git blame`, `git log` and `git diff` work line by line. The text is Portuguese, the only official language.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

| Folder | Act | Versions |
| --- | --- | ---: |
| `lei-organica/` | Lei Orgânica do Município de João Pessoa (1990), updated up to Emenda nº 44/2026 | 1 |

**Lei Orgânica only, for now.** The text is given **only as the Câmara's updated edition**, credited to the Câmara as the oldest version available. State law is in [brazil-paraiba-law](https://github.com/lexifina/brazil-paraiba-law); federal law in [brazil-law](https://github.com/lexifina/brazil-law).

## Source

[Câmara Municipal de João Pessoa, SAPL](https://sapl.joaopessoa.pb.leg.br/norma/14101), published by the Câmara Municipal de João Pessoa. Each version names the page it was taken from and that page's sha256, in `data/versions.json`.

## Dates

The one version is dated by the edition itself: the PDF "atualizado até a Emenda à Lei Orgânica nº 44/2026" was created on 3 June 2026 (its notes give each amendment's number and year only). Commits are at noon in João Pessoa.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The PDF's text layer is read with pdftotext from the first page of the text; the cover, the table of contents, the page footers and the alteration notes in parentheses ("(Redação dada pela Emenda à Lei Orgânica nº 12/2008)", "(Inciso acrescentado pela ...)") are left out, and a paragraph broken across two pages is joined again. One file per Art.; headings stand above the first article under them.

## How it is checked

Every version is read back from git on the day it took effect (`tools/check_repo.py`) and must match the corpus; an independent letters-and-digits comparison of every version against the source page must show no difference. Results are in `REPRODUCE.md`.

## What "author" means

The author of each commit is the law that made the text, or, for a consolidated text, the publisher, with an e-mail address that cannot exist; the committer is always Lexifina.

## Limits

Not a history: the Lei Orgânica as promulgated on 2 April 1990 and the wordings its amendments replaced are not in the edition, and the notes that say which amendment changed which provision are left out. The text is not the official version.

## Licence

See [LICENSE](LICENSE): Brazilian law texts are not protected by copyright (Lei 9.610/1998, art. 8, IV). Fonte: Câmara Municipal de João Pessoa, SAPL, Câmara Municipal de João Pessoa.
