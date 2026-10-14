# SC-001 — Fábrica mínima en R0 y agentes observadores

| Campo | Valor |
|---|---|
| Fecha | 2026-10-14 |
| Solicitante | Autor (Chris) |
| Tipo | Cambio de alcance de un release futuro (R0 aún no se inicia; Brief Maestro v1.4 §3.6) |
| Estado | **Aceptada** el 2026-10-14 por el autor, ejerciendo provisionalmente los roles de responsable (Constitución, Disposición transitoria primera) |

## Solicitud

> "Para el [Brief] de implementación se solicita que se implemente al menos el 50 % del brief desde el R0 y que los
> agentes que aún no interactúan sean observadores y analicen posibles errores, lo cual servirá para la siguiente versión."

## Análisis de impacto

| Aspecto | Impacto |
|---|---|
| Alcance de R0 | De 19 a 28 elementos comprometidos del Brief de Implementación (62 % del inventario de 45); mínimo exigido 23 (50 %) incluidos 19 de núcleo |
| Agentes | De 5 a 7 operativos (Formulación científica y Métodos numéricos se adelantan desde R1) y 14 observadores |
| Contratos y evals | Se necesitan contratos y evals de integridad para los 21 agentes antes de iniciar R0 |
| Presupuesto de IA | Aumenta por los observadores; se acota por release y se contabiliza aparte |
| Riesgo | R0 más largo. Mitigación: suite común de evals para observadores; los Should se sacrifican primero |
| Beneficio | Llega a R1 una fábrica ya probada y un primer informe de observadores para mejorar R1 |

## Documentos modificados

- Brief Maestro v1.5 (R0 en §3.1 y §3.5, fuentes de feedback en §3.6, catálogo y modo observador en §7.2).
- Brief de Implementación v2.2 (§12 alcance por release, §13 modo observador, fase G0).
- `02_Agentes/catalogo.json` y `02_Agentes/asignaciones/R0.json`.
- Esquemas `observation_report` (reemplazado por `potential_defect_report` en FB-R0-002), `agent_catalog` y `release_assignment`.

## Seguimiento

- FB-R0-002: definición de los observadores del autor, aplicada en el Brief de Implementación v2.3 §13.
- FB-R0-001: incorporar el modo observador y el adelanto de Formulación y Métodos numéricos en el Brief de Agentes v1.2.
