import re
from pathlib import Path
p = Path('MATHSYS_oefeningen.tex')
s = p.read_text(encoding='utf-8', errors='replace')

replacements = [
    (r'reel', 'reëel'),
    (r'rele', 'reële'),
    (r'rel', 'reëel'),
    (r're', 'reëe'),
    (r'coficint', 'coëfficiënt'),
    (r'coficinten', 'coëfficiënten'),
]

# Actually use the replacement char \ufffd for matches
patterns = {
    're\uFFFDel': 'reëel',
    're\uFFFDele': 'reële',
    're\uFFFDel': 'reëel',
    'co\uFFFDffici\uFFFDnt': 'coëfficiënt',
    'co\uFFFDffici\uFFFDnten': 'coëfficiënten',
    'parti\uFFFDle': 'partiële',
    'Ge\uFFFDnspireerd': 'Geïnspireerd',
    'ge\uFFFDnspireerd': 'geïnspireerd',
    'sinuso\uFFFDdaal': 'sinusoïdaal',
    'sinuso\uFFFDdale': 'sinusoïdale',
    'amplitudeverst\uFFFDrking': 'amplitudeversterking',
    'verst\uFFFDrking': 'versterking',
    'verifi\uFFFDren': 'verifiëren',
    'Verifi\uFFFDring': 'Verificering',
    'initi\uFFFDle': 'initiële',
    '\uFFFD Starter Level': '— Starter Level',
    'parti\uFFFDle integratie': 'partiële integratie',
    'parti\uFFFDle breuken': 'partiële breuken',
    'ge\uFFFDnspireerd': 'geïnspireerd',
    'parti\uFFFDle': 'partiële',
}

orig = s
for pat, repl in patterns.items():
    s = s.replace(pat, repl)

if s != orig:
    p.write_text(s, encoding='utf-8')
    print('Applied unicode fixes')
else:
    print('No changes made')
