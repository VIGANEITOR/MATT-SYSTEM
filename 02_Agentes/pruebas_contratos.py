"""Pruebas negativas de los esquemas: lo que la Constitución prohíbe debe ser rechazado.

Uso: python 02_Agentes/pruebas_contratos.py   (termina con código 1 si alguna prueba falla)
"""
import copy
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

DIR = Path(__file__).resolve().parent / 'contratos'
sch = {p.name: json.loads(p.read_text(encoding='utf-8')) for p in (DIR / 'schemas').glob('*.json')}
reg = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in sch.values())


def valido(nombre, instancia):
    return not list(Draft202012Validator(sch[nombre], registry=reg).iter_errors(instancia))


def leer(rel):
    return json.loads((DIR / rel).read_text(encoding='utf-8'))


out, inp = leer('ejemplos/drenaje_output.ejemplo.json'), leer('ejemplos/drenaje_input.ejemplo.json')
con = leer('hidraulica.drenaje_pluvial@1.0.0.json')
obs = leer('ejemplos/potential_defect_report.ejemplo.json')
Z = 'sha256:' + '0' * 64
doc = {'entregable': {'fuente_md': Z, 'version': '0.1.0'}, 'trazabilidad': [], 'valores_faltantes': [],
       'bibliografia': [], 'anexo_ia': {'secciones': []}, 'estado': 'listo_para_revision'}


def mod(base, f):
    x = copy.deepcopy(base)
    f(x)
    return x


# (descripción, esquema, instancia, debe_ser_valida)
casos = [
    ('Valor Calculado sin ejecución (Art. 8)', 'drenaje_output.json',
     mod(out, lambda x: x['subcuencas'][0]['caudal_pico'].pop('ejecucion_id')), False),
    ('Agente marca un resultado como aprobado (Art. 11)', 'drenaje_output.json',
     mod(out, lambda x: x.update(estado_verificacion='aprobado')), False),
    ('Valor de IA sin marcar como no verificado', 'drenaje_output.json',
     mod(out, lambda x: x['subcuencas'][0].update(area={'valor': 1, 'unidad': 'm2', 'procedencia': 'Generado por IA'})), False),
    ('Falta la curva IDF (RF-07)', 'drenaje_input.json', mod(inp, lambda x: x['datasets'].pop('lluvia')), False),
    ('Norma de cumplimiento etiquetada como referencia (RF-16)', 'drenaje_input.json',
     mod(inp, lambda x: x['criterios_diseno']['norma_cumplimiento'].update(rol='referencia')), False),
    ('Contrato con red abierta', 'agent_contract.schema.json',
     mod(con, lambda x: x['permissions'].update(network='allow_all')), False),
    ('Instancia de dominio sin perfil', 'agent_contract.schema.json', mod(con, lambda x: x.update(base_agent='especialista_dominio')), False),
    ('Entregable listo con valores faltantes', 'documentacion_output.json', dict(doc, valores_faltantes=['r1']), False),
    ('Entregable listo con un valor de IA', 'documentacion_output.json',
     dict(doc, trazabilidad=[{'marcador': '{{resultado:r1}}', 'resultado_id': 'r1', 'procedencia': 'Generado por IA'}]), False),
    ('Control: entregable listo y completo', 'documentacion_output.json', doc, True),
    ('Observador incluye una decisión o aprobación', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].update(decision='aprobado')), False),
    ('Observador sin evidencia en un hallazgo', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].pop('evidencia')), False),
    ('Observador con valor Calculado sin ejecución', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].update(valores=[{'valor': 1, 'unidad': 'm3/s', 'procedencia': 'Calculado'}])), False),
    ('Observador reporta una mejora como defecto', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].update(tipo='mejora')), False),
    ('Observador sin prioridad', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].pop('prioridad_sugerida')), False),
    ('Observador con ejecución propia', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0].update(ejecucion_observador='run-obs-1')), False),
    ('Observador sin lo esperado frente a lo observado', 'potential_defect_report.schema.json',
     mod(obs, lambda x: x['hallazgos'][0]['evidencia'].pop('esperado')), False),
    ('Control: informe de defectos potenciales válido', 'potential_defect_report.schema.json', obs, True),
    ('Control: ejemplo de salida de drenaje', 'drenaje_output.json', out, True),
]
fallos = 0
for desc, nombre, inst, esperado in casos:
    ok = valido(nombre, inst) == esperado
    fallos += not ok
    print(('OK   ' if ok else 'FALLA'), desc)
sys.exit(1 if fallos else 0)
