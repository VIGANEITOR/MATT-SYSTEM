# Agentes

Especificación: [Brief de Agentes v1.1](../00_Especificacion/Brief_Agentes/v1.1/MATTX_Brief_Agentes_v1.1.md).
Ningún agente existe sin contrato válido; ningún agente verifica su propio trabajo, reporta un número sin ejecución
registrada ni aprueba resultados o compuertas.

| Grupo | Agentes base (21) |
|---|---|
| A. Orquestación y producto | Análisis, Investigación, Planificación, Desarrollo científico, Diseño técnico, Verificación técnica, Despliegue, Aprendizaje |
| B. Interfaz y diseño (agentes de IA) | Dirección de Arte Digital, Design System, UI/UX Designer, Frontend/UI Engineer, QA Visual y Accesibilidad |
| C. Ciencia | Formulación científica, Métodos numéricos, Incertidumbre y experimentación, Decisión multicriterio, Geomática y BIM, Especialista de dominio, Documentación científica, Forja de herramientas y agentes |

Las instancias de dominio se nombran `<dominio>.<especialidad>` (p. ej., `hidraulica.drenaje_pluvial`) y declaran
`base_agent` y `domain_profile` en su contrato.

Ciclo de vida: Propuesto → Experimental → Supervisado → Activo → Retirado.

## Contenido

| Ruta | Qué es |
|---|---|
| `contratos/*.json` | Un contrato por agente y versión: `<agent_id>@<version>.json` |
| `contratos/schemas/` | Esquemas JSON 2020-12: contrato, mensaje, tipos comunes, entradas y salidas |
| `contratos/ejemplos/` | Instancias **sintéticas** para probar los esquemas (no son datos reales) |
| `validar_contratos.py` | Valida esquemas, contratos y ejemplos |
| `pruebas_contratos.py` | Pruebas negativas: lo que la Constitución prohíbe debe ser rechazado |
| `evals/` | Suites de integridad, contrato, funcional, detección y regresión |
| `perfiles_dominio/` | Conocimiento por dominio |
| `forja/` | Propuestas de herramientas y agentes nuevos |

```bash
pip install -r 02_Agentes/requirements.txt
python 02_Agentes/validar_contratos.py
python 02_Agentes/pruebas_contratos.py
```
