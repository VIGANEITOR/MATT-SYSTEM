# Agentes

Ningún agente existe sin contrato válido (Brief Maestro v1.1 §7.1). Ningún agente verifica su propio trabajo,
reporta un número sin ejecución registrada ni aprueba resultados.

| Grupo | Agentes |
|---|---|
| A. Orquestación y producto | Análisis, Investigación, Planificación, Desarrollo/automatización, Diseño técnico, Verificación técnica, Despliegue, Aprendizaje |
| B. Interfaz y diseño | UI/UX Designer, Design System, Frontend/UI Engineer, QA Visual y Accesibilidad, Dirección de Arte Digital |
| C. Ciencia | Formulación científica, Métodos numéricos, Incertidumbre y experimentación, Forja de herramientas y agentes |

Ciclo de vida: Propuesto → Experimental → Supervisado → Activo → Retirado (Brief de Agentes v1.0 §8).

- `contratos/` — un JSON por agente y versión (`<agent_id>@<version>.json`)
- `evals/` — suites de integridad, contrato, funcional, detección y regresión
- `perfiles_dominio/` — conocimiento por dominio que se carga en Formulación, Investigación y Verificación
- `forja/` — propuestas de herramientas y agentes nuevos
