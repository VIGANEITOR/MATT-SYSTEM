# SC-002 — Ruta mínima primero, métrica ponderada y permisos en 4 dimensiones

| Campo | Valor |
|---|---|
| Fecha | 2026-10-14 |
| Solicitante | Autor (revisión aportada por el autor; FB-R0-003 a FB-R0-007) |
| Tipo | Cambio de alcance de un release futuro (R0 aún no se inicia) |
| Estado | **Aceptada** el 2026-10-14 por el autor ("ok, aplícalos"), ejerciendo provisionalmente los roles de responsable |

## Cambios

| # | Cambio | Origen |
|---|---|---|
| 1 | R0 en dos etapas: **R0a ruta mínima completa** y R0b; los observadores se activan al superar R0a | FB-R0-004 |
| 2 | El 50 % del Brief de Implementación se mide por **peso de capacidad**; cada elemento tiene prueba de aceptación; 10 elementos no compensables | FB-R0-005 |
| 3 | **Registro único de estado** de componentes; los briefs no declaran estados | FB-R0-003 |
| 4 | Permisos en **4 dimensiones**; credenciales fuera del alcance de agentes y procesos; proxy de salida (ADR-009) | FB-R0-006 |
| 5 | Plataforma y fábrica separadas en documentos y registro | FB-R0-007 |

## Impacto en el criterio de salida de R0

| Antes (SC-001) | Después (SC-002) |
|---|---|
| ≥ 23 de 45 elementos, incluidos 19 de núcleo | R0a superada + núcleo y no compensables al 100 % + ≥ 50 % del peso (el núcleo ya es el 57 % del peso) |
| Objetivo 28 elementos (62 % por conteo) | Objetivo núcleo + Must: 74 % del peso |
| Observadores desde el inicio de R0 | Observadores tras superar R0a |
| Permisos de red, lectura y escritura | + ejecución como dimensión separada; ADR-009 como criterio de entrada de R0 |

El criterio no se relaja: se exige todo el núcleo, como antes, y además la ruta mínima y los no compensables.

## Documentos modificados

Brief Maestro v1.6, Brief de Agentes v1.2, Brief de Implementación v2.4, `00_Especificacion/registro/`, `ESTADO.md`,
`02_Agentes/red_permitida.json`, esquemas de contrato, catálogo y asignación, contratos 1.1.0 y ADR-009.
