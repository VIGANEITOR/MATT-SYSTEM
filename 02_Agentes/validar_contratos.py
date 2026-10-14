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
red = cargar(DIR.parent / 'red_permitida.json') or {'destinos': []}
validar(red, 'allowlist.schema.json', 'red_permitida.json')
destinos = {d['id']: d for d in red.get('destinos', [])}
for p in sorted(DIR.glob('*.json')):
    c = cargar(p)
    if c is None:
        continue
    perm = c.get('permissions', {})
    for d in perm.get('network_allowlist', []):
        if d not in destinos:
            errores.append(f'{p.name}: destino de red {d!r} no está en red_permitida.json')
    for d in c.get('credenciales', []):
        if d not in perm.get('network_allowlist', []):
            errores.append(f'{p.name}: credencial de {d!r} sin ese destino en network_allowlist')
        elif not destinos.get(d, {}).get('requiere_credencial'):
            errores.append(f'{p.name}: {d!r} no requiere credencial según red_permitida.json')
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

# 4. Catálogo de agentes y asignaciones por release
RAIZ = DIR.parent
catalogo = cargar(RAIZ / 'catalogo.json')
if catalogo is not None:
    validar(catalogo, 'agent_catalog.schema.json', 'catalogo.json')
    ids = [x['id'] for x in catalogo.get('agentes', [])]
    if len(ids) != len(set(ids)):
        errores.append('catalogo.json: hay agentes repetidos')
    release_de = {x['id']: x['release_operativo'] for x in catalogo.get('agentes', [])}
    for p in sorted((RAIZ / 'asignaciones').glob('*.json')):
        asig = cargar(p)
        if asig is None:
            continue
        validar(asig, 'release_assignment.schema.json', p.name)
        oper = set(asig.get('operativos', []))
        obs = [o['agent_id'] for o in asig.get('observadores', [])]
        if oper & set(obs):
            errores.append(f'{p.name}: agentes operativos y observadores a la vez: {sorted(oper & set(obs))}')
        if len(obs) != len(set(obs)):
            errores.append(f'{p.name}: observadores repetidos')
        faltan = set(ids) - oper - set(obs)
        sobran = (oper | set(obs)) - set(ids)
        if faltan:
            errores.append(f'{p.name}: agentes del catálogo sin modo asignado: {sorted(faltan)}')
        if sobran:
            errores.append(f'{p.name}: agentes que no están en el catálogo: {sorted(sobran)}')
        rel = asig.get('release')
        for a in ids:
            if release_de[a] == rel and a not in oper:
                errores.append(f'{p.name}: {a} opera desde {rel} según el catálogo y debe ser operativo')
        for a in oper:
            if a in release_de and release_de[a] != rel and a not in asig.get('adelantados', []):
                errores.append(f'{p.name}: {a} es operativo antes de su release ({release_de[a]}) sin figurar en "adelantados"')

print(f'Esquemas: {len(esquemas)} · contratos: {len(list(DIR.glob("*.json")))} · ejemplos: {len(list(EJ.glob("*.ejemplo.json")))}')
if errores:
    print('ERRORES:\n  ' + '\n  '.join(errores))
    sys.exit(1)
print('Todo válido.')
