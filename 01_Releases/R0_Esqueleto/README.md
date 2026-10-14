# R0 — Núcleo reproducible

**Estado**: Planificado · Especificación: [Brief Maestro v1.5 §3](../../00_Especificacion/Brief_Maestro/v1.5/MATTX_Brief_Maestro_v1.5.md)

## Capacidad de plataforma (Must)
Usuarios y roles, proyectos, registro de experimentos, orquestador con máquina de estados, sandbox con perfiles sin red y con red controlada, almacenamiento de artefactos con hash, procedencia básica, registro de agentes y contratos con validación de esquema, UI mínima.

**Fábrica mínima (SC-001):** al menos el 50 % del Brief de Implementación operativo con evidencia; objetivo 62 %
([inventario](../../00_Especificacion/Brief_Implementacion/v2.2/MATTX_Brief_Implementacion_v2.2.md)).

## Ámbito científico
Independiente del dominio: cualquier cálculo en los lenguajes soportados (Python primero).

## Casos de referencia (ejemplos, no límites)
Programa T1 piloto (fase G0).

## Agentes
**Operativos (7):** Análisis, Planificación, Formulación científica, Métodos numéricos, Desarrollo científico,
Verificación técnica, Despliegue.

**Observadores (14):** el resto de los agentes base; leen, informan posibles errores y no bloquean ni aprueban
([asignación](../../02_Agentes/asignaciones/R0.json)).

## Requisitos
RF-01 a RF-05.

## Criterio de entrada (§3.5)
- [ ] ADR-001 a ADR-004 aceptados
- [ ] Briefs vigentes aprobados (PENDIENTES B3)
- [ ] Constitución ratificada o vigente en forma provisional
- [ ] Esquemas de contrato y mensaje de agente (✅ ya existen)
- [ ] Contratos de los 21 agentes (operativos y observadores) con 100 % en evals de integridad

## Criterio de salida (gate)
- [ ] Un script se ejecuta en sandbox sin red y otro en red controlada
- [ ] Toda conexión queda registrada y la que esté fuera de la lista permitida se bloquea
- [ ] La conexión exige aprobación humana registrada
- [ ] El resultado queda trazable (hash de entradas, versión de código, imagen, semilla)
- [ ] Una re-ejecución lo reproduce bit a bit (QA-REP-001)
- [ ] Informe de QA emitido; 0 defectos S1/S2 abiertos
- [ ] Al menos 23 de los 45 elementos del Brief de Implementación operativos con evidencia, incluidos los 19 de núcleo
- [ ] Informe de observadores incluido en el informe de cierre; ningún hallazgo S1/S2 sugerido sin clasificar

## Paquete de traspaso al siguiente release (§3.5)
- [ ] Núcleo desplegable
- [ ] API documentada del orquestador, del sandbox y de la procedencia
- [ ] Registro de agentes
- [ ] Suite de reproducibilidad (QA-REP)
- [ ] Informe de QA
- [ ] Línea base de métricas
- [ ] Registro de feedback de R0
- [ ] Informe de observadores con hallazgos clasificados
- [ ] Backlog priorizado de R1

## Solicitudes de cambio
- [SC-001](01_Alcance/SC-001_fabrica_minima_y_observadores.md) — Fábrica mínima en R0 y agentes observadores (aceptada)

## Feedback (§3.6)
Registro en [`06_Feedback/registro.md`](06_Feedback/registro.md). Al cerrar el release: informe de cierre y punto de
decisión sobre el siguiente (iniciar, ajustar o posponer).
