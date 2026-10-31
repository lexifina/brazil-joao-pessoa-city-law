"""Builds corpus.d/10-lei-organica.json for the Município de João Pessoa from the Câmara Municipal's updated edition of
the Lei Orgânica in its SAPL (PDF with a text layer; no network).

    python -X utf8 parse.py --today YYYY-MM-DD

The edition ("Texto promulgado em 02 de abril de 1990 (atualizado até a Emenda à Lei Orgânica nº 44/2026)", João
Pessoa, junho de 2026) is read with pdftotext (poppler) page by page, from the page that starts "TÍTULO I" after the
table of contents. Left out: the cover and table of contents, each page's footer ("Câmara Municipal | Lei Orgânica do
Município <page>") and the alteration notes in parentheses ("(Redação dada pela Emenda à Lei Orgânica nº 12/2008)",
"(Inciso acrescentado pela ...)", "(Revogado pela ...)"). A paragraph broken across two pages is joined again.
"""
import argparse, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from br_lib import units_of, write_part, sha, norm  # noqa: E402

BASE = 'https://sapl.joaopessoa.pb.leg.br'
PDF_URL = 'http://sapl.joaopessoa.pb.leg.br/media/sapl/public/normajuridica/1990/14101/lei_organica.pdf'
PAGE_URL = BASE + '/norma/14101'
PDF = HERE / '.cache' / 'sapl' / 'raw' / sha(PDF_URL.encode())
FOOTER = re.compile(r'(?:^|\s)Câmara Municipal \| Lei Orgânica do Município \d+$')  # alone, or glued to a line's end
NOTE = re.compile(r'\([^()]*\bpela\s+Emenda\s+à\s+Lei\s+Orgânica\s*nº\s*[\d/]+\s*\)')
STARTS = re.compile(r'^(?:Art\.|§|Par[áa]grafo|[IVXLC]+\s*[-–]|[a-z]\)|T[ÍI]TULO|CAP[ÍI]TULO|Se[çc][ãa]o|SE[ÇC][ÃA]O|ATO\b)')


def lines_of_pdf():
    s = subprocess.run(['pdftotext', '-enc', 'UTF-8', str(PDF), '-'], capture_output=True, check=True).stdout.decode()
    ps = s.split('\f')
    start = next(i for i, p in enumerate(ps) if p.lstrip().startswith('TÍTULO I') and '.....' not in p)
    out = []
    for p in ps[start:]:
        ls = [FOOTER.sub('', norm(l)).strip() for l in p.split('\n')]
        ls = [l for l in ls if l]
        page = []
        for l in ls:
            l = norm(NOTE.sub(' ', l))
            if l and re.search(r'\w', l):
                page.append(l)
        if page and out and not re.search(r'[.;:!?)"”]$', out[-1]) and not STARTS.match(page[0]):
            out[-1] = out[-1] + ' ' + page.pop(0)
        out += page
    return out


COUNTRY = {
    'code': 'BR-PB-JOAO-PESSOA', 'name': 'João Pessoa', 'slug': 'brazil-joao-pessoa-city', 'lang': 'pt',
    'tz': 'America/Fortaleza', 'future_branch': 'futuro',
    'publisher': {'name': 'Câmara Municipal de João Pessoa', 'email': 'sapl@joaopessoa.pb.leg.br.invalid'},
    'default_in_force_rule': {
        'text': 'The Lei Orgânica and its amendments are promulgated by the Mesa da Câmara and take effect on '
                'promulgation; this record holds only the updated text, dated by the edition.',
        'source': PAGE_URL},
    'licence_note': 'Text: Câmara Municipal de João Pessoa, SAPL, Lei Orgânica do Município de João Pessoa (atualizada '
                    'até a Emenda nº 44/2026), sapl.joaopessoa.pb.leg.br. Lei 9.610/1998 art. 8 IV: the texts of laws '
                    'and other official acts are not protected by copyright. Non-official text: only the official '
                    'gazette is authoritative.',
}
DECISIONS = [
    'The Lei Orgânica is given only as the Câmara\'s updated edition ("atualizado até a Emenda à Lei Orgânica nº '
    '44/2026", junho de 2026), credited to the Câmara as the oldest version available and dated by the edition\'s own '
    'date (the PDF\'s creation date, 3 June 2026): its notes give only the number and year of each amendment. The text '
    'as promulgated on 2 April 1990 and the wordings the amendments replaced are not in the edition.',
    'Left out: the cover, the table of contents, the page footers and the alteration notes in parentheses ("(Redação '
    'dada pela Emenda à Lei Orgânica nº ...)", "(Inciso acrescentado pela ...)", "(Revogado pela ...)"). A paragraph '
    'broken across two pages is joined again.',
    'One file per Art.; headings stand above the first article under them. The signatures of the constituent '
    'assembly after the last article stay with it.',
]
AI = ["Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal "
      "text or dates: every word comes from the Câmara's PDF."]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--today', required=True)
    a = ap.parse_args()
    units = units_of([('p', l) for l in lines_of_pdf()], adt=True)
    b = PDF.read_bytes()
    key = 'lei-organica-1990'
    laws = {key: {'label': 'Lei Orgânica do Município de João Pessoa, de 2 de abril de 1990',
                  'title': 'Lei Orgânica do Município de João Pessoa', 'kind': 'law', 'enacted': '1990-04-02',
                  'published': None, 'url': PAGE_URL, 'temporary_until': None, 'restores': None, 'note': None}}
    v = {'from': '2026-06-03', 'source_url': PDF_URL, 'sha256': sha(b), 'units': units,
         'note': 'Text in force as updated by the Câmara Municipal de João Pessoa up to Emenda nº 44/2026 (edition of '
                 'June 2026).'}
    act = {'slug': 'lei-organica', 'short': 'LOM-JP', 'title': 'Lei Orgânica do Município de João Pessoa',
           'url': PAGE_URL, 'first_law': None, 'earlier_laws': [key], 'versions': [v]}
    c = {'country': COUNTRY,
         'sources': [{'name': 'Câmara Municipal de João Pessoa, SAPL: Lei Orgânica do Município, atualizada até a '
                              'Emenda nº 44/2026 (PDF)', 'url': PAGE_URL, 'retrieved': a.today,
                      'licence': COUNTRY['licence_note'], 'notes': '1 act.'}],
         'laws': laws, 'acts': [act], 'applies': [], 'decisions': DECISIONS, 'ai_use': AI}
    print(write_part(HERE / 'corpus.d', '10-lei-organica', c), len(units))


if __name__ == '__main__':
    main()
