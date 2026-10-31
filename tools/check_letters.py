"""Independent letters-and-digits check of the Lei Orgânica against the PDF, read with a second PDF reader (PyMuPDF,
not the builder's pdftotext) and none of the builder's code.

    python -X utf8 check_letters.py [part.json ...]

The PDF text from the first page that starts "TÍTULO I" without a table-of-contents leader ("....."), with the page
footers ("Câmara Municipal | Lei Orgânica do Município <n>") and every note in parentheses that cites "pela Emenda à
Lei Orgânica nº ..." removed, reduced to letters and digits, must equal the version's unit files reduced the same way,
each unit found at its place in document order.
"""
import hashlib, json, re, sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def ld(s):
    return ''.join(ch for ch in s if ch.isalnum())


def pdf_text(raw):
    # the footer comes first on each page in this reader
    pages = [re.sub(r'Câmara\s+Municipal\s*\|\s*Lei\s+Orgânica\s+do\s+Município\s+\d+', ' ', p.get_text())
             for p in pymupdf.open(stream=raw, filetype='pdf')]
    start = next(i for i, t in enumerate(pages) if t.lstrip().startswith('TÍTULO I') and '.....' not in t)
    t = '\n'.join(pages[start:])
    return re.sub(r'\([^()]*pela\s+Emenda\s+à\s+Lei\s+Orgânica\s*nº\s*[\d/]+\s*\)', ' ', t)


def main(paths):
    bad = total = 0
    for p in paths:
        for a in json.load(open(p, encoding='utf-8'))['acts']:
            for v in a['versions']:
                raw = (HERE / '.cache' / 'sapl' / 'raw' / hashlib.sha256(v['source_url'].encode()).hexdigest()).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == v['sha256'], (a['slug'], 'sha256')
                src = ld(pdf_text(raw))
                rest = {k: ld(re.sub(r'(?m)^#+ ', '', u['text'])) for k, u in v['units'].items()}
                pos = 0
                while rest:
                    hit = None
                    for k, t in rest.items():
                        if t and src.startswith(t, pos) and (hit is None or len(t) > len(rest[hit])):
                            hit = k
                    if hit is None:
                        break
                    pos += len(rest.pop(hit))
                total += 1
                if rest or pos != len(src):
                    bad += 1
                    print(f'MISMATCH {a["slug"]} {v["from"]}: matched {pos}/{len(src)}; next source: '
                          f'{src[pos:pos + 80]!r}; unplaced: {list(rest)[:5]}')
    print(f'{total} versions checked, {bad} mismatches')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or sorted(str(p) for p in (HERE / 'corpus.d').glob('*.json'))) else 0)
