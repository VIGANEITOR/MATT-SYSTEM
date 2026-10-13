# Sitio público

Sitio de documentación construido con MkDocs Material a partir del Markdown del repositorio.
Se publica en GitHub Pages con el flujo `.github/workflows/sitio.yml` en cada cambio a `main`.

Construir en local:

```bash
pip install -r 06_Sitio_Publico/requirements.txt
python 06_Sitio_Publico/ensamblar_docs.py
mkdocs serve -f 06_Sitio_Publico/mkdocs.yml
```

`ensamblar_docs.py` copia los documentos a `06_Sitio_Publico/docs/` (carpeta generada, ignorada por git).
