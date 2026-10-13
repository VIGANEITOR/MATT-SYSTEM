"""Copia el Markdown del repositorio a 06_Sitio_Publico/docs para que MkDocs lo publique."""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / '06_Sitio_Publico' / 'docs'
CARPETAS = ['00_Especificacion', '01_Releases', '02_Agentes', '03_Casos_Dorados', '07_Plataforma', '08_Programas']

if DOCS.exists():
    shutil.rmtree(DOCS)
DOCS.mkdir(parents=True)

shutil.copy(ROOT / 'README.md', DOCS / 'index.md')
shutil.copy(ROOT / 'CONSTITUCION.md', DOCS / 'CONSTITUCION.md')
for carpeta in CARPETAS:
    for f in (ROOT / carpeta).rglob('*'):
        if f.is_file() and f.suffix.lower() in {'.md', '.png', '.jpg', '.svg', '.json'}:
            destino = DOCS / f.relative_to(ROOT)
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, destino)

# Los README de carpeta se publican como index.md de esa carpeta
for f in DOCS.rglob('README.md'):
    f.rename(f.with_name('index.md'))
for f in DOCS.rglob('*.md'):
    texto = f.read_text(encoding='utf-8')
    texto = re.sub(r'\]\(([^)#]*?)README\.md', r'](\1index.md', texto)
    f.write_text(texto, encoding='utf-8')
print('Docs ensamblados en', DOCS)
