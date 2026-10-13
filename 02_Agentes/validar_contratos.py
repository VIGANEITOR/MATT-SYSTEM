"""Valida esquemas, contratos de agente y ejemplos de 02_Agentes/contratos.

Uso: python 02_Agentes/validar_contratos.py
Requiere: jsonschema (ver 02_Agentes/requirements.txt). Termina con código 1 si hay errores.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

DIR = Path(__file__).resolve().parent / 'contratos'
SCH = DIR / 'schemas'
EJ = DIR / 'ejemplos'
errores = []


def cargar(p):
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        errores.append(f'{p.name}: JSON inválido ({e})')
        return None


# 1. Esquemas válidos y registro por $id
esquemas = {}
for p in sorted(SCH.glob('*.json')):
    s = cargar(p)
    if s is None:
        continue
    try:
        Draft202012Validator.check_schema(s)
    except Exception as e:  # noqa: BLE001
        errores.append(f'{p.name}: esquema inválido ({e.message if hasattr(e, "message") else e})')
        continue
    esquemas[p.name] = s
registro = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in esquemas.values())


def validar(instancia, nombre_esquema, etiqueta):
    v = Draft202012Validator(esquemas[nombre_esquema], registry=registro)
    for e in sorted(v.iter_errors(instancia), key=lambda e: list(e.path)):
        ruta = '/'.join(str(x) for x in e.path) or '(raíz)'
        errores.append(f'{etiqueta}: {ruta}: {e.message}')


# 2. Contratos
for p in sorted(DIR.glob('*.json')):
    c = cargar(p)
    if c is None:
        continue
    validar(c, 'agent_contract.schema.json', p.name)
    esperado = f"{c.get('agent_id')}@{c.get('contract_version')}.json"
    if p.name != esperado:
        errores.append(f'{p.name}: el nombre debe ser {esperado}')
    for lado in ('inputs', 'outputs'):
        destino = (c.get(lado) or {}).get('$ref', '')
        if destino and (DIR / destino).name not in esquemas:
            errores.append(f'{p.name}: {lado} apunta a {destino}, que no existe o no es un esquema válido')

# 3. Ejemplos: <nombre>.ejemplo.json se valida contra schemas/<nombre>.json o <nombre>.schema.json
for p in sorted(EJ.glob('*.ejemplo.json')):
    base = p.name.removesuffix('.ejemplo.json')
    nombre = next((n for n in (f'{base}.json', f'{base}.schema.json') if n in esquemas), None)
    if nombre is None:
        errores.append(f'{p.name}: no hay esquema {base}.json ni {base}.schema.json')
        continue
    e = cargar(p)
    if e is not None:
        validar(e, nombre, p.name)

print(f'Esquemas: {len(esquemas)} · contratos: {len(list(DIR.glob("*.json")))} · ejemplos: {len(list(EJ.glob("*.ejemplo.json")))}')
if errores:
    print('ERRORES:\n  ' + '\n  '.join(errores))
    sys.exit(1)
print('Todo válido.')
