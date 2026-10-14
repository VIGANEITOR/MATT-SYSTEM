"""Registro único de estado de MATTX (FB-R0-003).

Fuentes únicas:
  00_Especificacion/registro/estado_componentes.json   componentes de la plataforma y de la fábrica
  02_Agentes/catalogo.json                              agentes base
  02_Agentes/red_permitida.json                         destinos de red controlada

Genera:
  ESTADO.md (estado real; se regenera libremente)
  Bloques de especificación dentro de los briefs vigentes (00_Especificacion/registro/vigentes.json),
  delimitados por <!-- inicio:generado:NOMBRE --> ... <!-- fin:generado:NOMBRE -->. Esos bloques no contienen
  estados, solo especificación: si cambian, hace falta una versión nueva del brief.

Uso:
  python 00_Especificacion/registro/generar.py --check              (CI: falla si algo está desalineado)
  python 00_Especificacion/registro/generar.py --write              (regenera ESTADO.md)
  python 00_Especificacion/registro/generar.py --write --incluir-briefs   (solo al crear una versión nueva de un brief)
"""
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

RAIZ = Path(__file__).resolve().parents[2]
REG = RAIZ / '00_Especificacion' / 'registro'
PESO = {'critica': 3, 'alta': 2, 'media': 1, 'baja': 0.5}
NOMBRE_CRIT = {'critica': 'Crítica', 'alta': 'Alta', 'media': 'Media', 'baja': 'Baja'}
NOMBRE_ESTADO = {'planificado': 'Planificado', 'en_desarrollo': 'En desarrollo', 'probado': 'Probado',
                 'operativo': 'Operativo', 'degradado': 'Degradado', 'no_disponible': 'No disponible'}
NOMBRE_CLASE = {'nucleo': '**Núcleo**', 'must': 'Must', 'should': 'Should', 'posterior': '—'}
errores = []


def num(x):
    return f'{x:g}'.replace('.', ',')


def cargar(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def validar(inst, esquema, etiqueta):
    for e in Draft202012Validator(cargar(esquema)).iter_errors(inst):
        errores.append(f'{etiqueta}: {"/".join(map(str, e.path)) or "(raíz)"}: {e.message}')


comp = cargar(REG / 'estado_componentes.json')
validar(comp, REG / 'estado_componentes.schema.json', 'estado_componentes.json')
cat = cargar(RAIZ / '02_Agentes' / 'catalogo.json')
red = cargar(RAIZ / '02_Agentes' / 'red_permitida.json')
C = comp['componentes']
ids = [c['id'] for c in C]
if len(ids) != len(set(ids)):
    errores.append('estado_componentes.json: IDs repetidos')
for c in C:
    if c['estado'] in ('probado', 'operativo') and not c.get('evidencia'):
        errores.append(f'{c["id"]}: estado {c["estado"]} sin evidencia')
FAB = [c for c in C if c.get('inventario')]


def tabla(cab, filas):
    return '\n'.join(['| ' + ' | '.join(cab) + ' |', '|' + '---|' * len(cab)] + ['| ' + ' | '.join(map(str, f)) + ' |' for f in filas])


def pct(a, b):
    return f'{100 * a / b:.0f} %' if b else '—'


# ---------------------------------------------------------------- bloques de especificación
def bloque_resumen_peso():
    tot = sum(PESO[c['criticidad']] for c in FAB)
    filas, acum = [], 0
    for clase in ('nucleo', 'must', 'should'):
        sel = [c for c in FAB if c['clase_r0'] == clase]
        p = sum(PESO[c['criticidad']] for c in sel)
        acum += p
        filas.append([NOMBRE_CLASE[clase], len(sel), num(p), f'{num(acum)} ({pct(acum, tot)})'])
    post = [c for c in FAB if c['clase_r0'] == 'posterior']
    filas.append(['Releases posteriores', len(post), num(sum(PESO[c['criticidad']] for c in post)), '—'])
    nc = [c for c in FAB if c['no_compensable'] and c['clase_r0'] != 'posterior']
    pie = (f'\n\nPeso total del inventario: **{num(tot)}** ({len(FAB)} elementos). Pesos: crítica 3, alta 2, media 1, baja 0,5. '
           f'Elementos **no compensables** en el alcance de R0: **{len(nc)}** (deben estar todos operativos).')
    return tabla(['Clase en R0', 'Elementos', 'Peso', 'Peso acumulado'], filas) + pie


def bloque_inventario():
    filas = []
    for c in FAB:
        filas.append([c['id'], c['seccion'], c['nombre'], NOMBRE_CLASE[c['clase_r0']], c.get('etapa_r0', '—'),
                      NOMBRE_CRIT[c['criticidad']], num(PESO[c['criticidad']]), 'Sí' if c['no_compensable'] else '—',
                      f'{c["prueba_aceptacion"]["id"]}: {c["prueba_aceptacion"]["criterio"]}', c.get('agentes', '—')])
    return tabla(['ID', 'Sección', 'Elemento', 'En R0', 'Etapa', 'Criticidad', 'Peso', 'No compensable', 'Prueba de aceptación', 'Agente(s)'], filas)


def bloque_agentes_por_release():
    rel = {}
    for a in cat['agentes']:
        rel.setdefault(a['release_operativo'], []).append(a['nombre'])
    return tabla(['Release', 'Agentes que pasan a operativos'], [[r, ', '.join(v)] for r, v in sorted(rel.items())])


def bloque_catalogo_maestro():
    return tabla(['Grupo', 'Agente', 'Función', 'Release operativo'],
                 [[a['grupo'], a['nombre'], a['funcion'], a['release_operativo']] for a in cat['agentes']])


BLOQUES = {'resumen_peso': bloque_resumen_peso, 'inventario_fabrica': bloque_inventario,
           'agentes_por_release': bloque_agentes_por_release, 'catalogo_agentes_maestro': bloque_catalogo_maestro}


# ---------------------------------------------------------------- ESTADO.md
def estado_md():
    out = ['# Estado de MATTX', '',
           f'> **Archivo generado** por `00_Especificacion/registro/generar.py` a partir del registro único '
           f'(`estado_componentes.json`, actualizado el {comp["actualizado"]}). No editar a mano.', '',
           'Es la **única** fuente pública del estado real de cada componente (Constitución, Art. 13). Los briefs '
           'especifican; no declaran estados.', '',
           'Estados: Planificado · En desarrollo · Probado (con evidencia local o de pruebas) · Operativo (en uso, con evidencia) · Degradado · No disponible.', '']
    for prod, titulo in (('plataforma', 'Plataforma'), ('fabrica', 'Fábrica')):
        sel = [c for c in C if c['producto'] == prod]
        cuenta = {}
        for c in sel:
            cuenta[c['estado']] = cuenta.get(c['estado'], 0) + 1
        out += [f'## {titulo}', '', ' · '.join(f'{NOMBRE_ESTADO[k]}: {v}' for k, v in cuenta.items()), '',
                tabla(['ID', 'Componente', 'Release', 'Criticidad', 'Estado', 'Evidencia'],
                      [[c['id'], c['nombre'], c['release'], NOMBRE_CRIT[c['criticidad']], NOMBRE_ESTADO[c['estado']], c.get('evidencia', '—')] for c in sel]), '']
    tot = sum(PESO[c['criticidad']] for c in FAB)
    op = sum(PESO[c['criticidad']] for c in FAB if c['estado'] == 'operativo')
    nc = [c for c in FAB if c['no_compensable'] and c['clase_r0'] != 'posterior']
    nc_ok = [c for c in nc if c['estado'] == 'operativo']
    out += ['## Avance de R0 respecto al Brief de Implementación', '',
            tabla(['Indicador', 'Valor', 'Requisito para cerrar R0'],
                  [['Peso del inventario operativo', f'{num(op)} de {num(tot)} ({pct(op, tot)})', '≥ 50 %'],
                   ['Elementos no compensables de R0 operativos', f'{len(nc_ok)} de {len(nc)}', 'Todos'],
                   ['Ruta mínima (R0a) completa', 'Sí' if all(c['estado'] == 'operativo' for c in FAB if c.get('etapa_r0') == 'R0a') else 'No', 'Sí']]), '',
            '## Agentes', '',
            tabla(['Agente', 'Grupo', 'Release operativo', 'Estado en el ciclo de vida'],
                  [[a['nombre'], a['grupo'], a['release_operativo'], a['estado']] for a in cat['agentes']]), '',
            '## Red controlada: lista permitida', '',
            tabla(['ID', 'Destino', 'Hosts', 'Uso', 'Requiere credencial'],
                  [[d['id'], d['nombre'], ', '.join(d['hosts']), d['uso'], 'Sí' if d['requiere_credencial'] else 'No'] for d in red['destinos']]), '']
    return '\n'.join(out)


# ---------------------------------------------------------------- comprobación y escritura
def procesar(escribir, incluir_briefs):
    vig = cargar(REG / 'vigentes.json')
    for doc, bloques in vig['bloques'].items():
        p = RAIZ / doc
        texto = p.read_text(encoding='utf-8')
        nuevo = texto
        for b in bloques:
            patron = re.compile(rf'(<!-- inicio:generado:{b} -->\n)(.*?)(\n<!-- fin:generado:{b} -->)', re.S)
            if not patron.search(nuevo):
                errores.append(f'{doc}: falta el bloque generado "{b}"')
                continue
            nuevo = patron.sub(lambda m: m.group(1) + BLOQUES[b]() + m.group(3), nuevo)
        if nuevo != texto:
            if escribir and incluir_briefs:
                p.write_text(nuevo, encoding='utf-8')
            else:
                errores.append(f'{doc}: los bloques generados no coinciden con el registro. Si cambió la especificación, cree una versión nueva del brief')
    e = RAIZ / 'ESTADO.md'
    contenido = estado_md() + '\n'
    if escribir:
        e.write_text(contenido, encoding='utf-8')
    elif not e.exists() or e.read_text(encoding='utf-8') != contenido:
        errores.append('ESTADO.md está desactualizado: ejecute generar.py --write')


procesar('--write' in sys.argv, '--incluir-briefs' in sys.argv)
if errores:
    print('ERRORES:\n  ' + '\n  '.join(errores))
    sys.exit(1)
print(f'Registro coherente: {len(C)} componentes, {len(cat["agentes"])} agentes, {len(red["destinos"])} destinos de red.')
