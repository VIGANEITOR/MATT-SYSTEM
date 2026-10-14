# R0 — Núcleo reproducible

**Estado**: Planificado · Especificación: [Brief Maestro v1.4 §3](../../00_Especificacion/Brief_Maestro/v1.4/MATTX_Brief_Maestro_v1.4.md)

## Capacidad de plataforma (Must)
Usuarios y roles, proyectos, registro de experimentos, orquestador con máquina de estados, sandbox con perfiles sin red y con red controlada, almacenamiento de artefactos con hash, procedencia básica, registro de agentes y contratos con validación de esquema, UI mínima.

## Ámbito científico
Independiente del dominio: cualquier cálculo en los lenguajes soportados (Python primero).

## Casos de referencia (ejemplos, no límites)
Programa T1 piloto (fase G0).

## Agentes
Análisis, Planificación, Desarrollo científico, Verificación técnica (básica), Despliegue.

## Requisitos
RF-01 a RF-05.

## Criterio de entrada (§3.5)
- [ ] ADR-001 a ADR-004 aceptados
- [ ] Briefs vigentes aprobados (PENDIENTES B3)
- [ ] Constitución ratificada o vigente en forma provisional
- [ ] Esquemas de contrato y mensaje de agente (✅ ya existen)

## Criterio de salida (gate)
- [ ] Un script se ejecuta en sandbox sin red y otro en red controlada
- [ ] Toda conexión queda registrada y la que esté fuera de la lista permitida se bloquea
- [ ] La conexión exige aprobación humana registrada
- [ ] El resultado queda trazable (hash de entradas, versión de código, imagen, semilla)
- [ ] Una re-ejecución lo reproduce bit a bit (QA-REP-001)
- [ ] Informe de QA emitido; 0 defectos S1/S2 abiertos

## Paquete de traspaso al siguiente release (§3.5)
- [ ] Núcleo desplegable
- [ ] API documentada del orquestador, del sandbox y de la procedencia
- [ ] Registro de agentes
- [ ] Suite de reproducibilidad (QA-REP)
- [ ] Informe de QA
- [ ] Línea base de métricas
- [ ] Registro de feedback de R0
- [ ] Backlog priorizado de R1

## Feedback (§3.6)
Registro en [`06_Feedback/registro.md`](06_Feedback/registro.md). Al cerrar el release: informe de cierre y punto de
decisión sobre el siguiente (iniciar, ajustar o posponer).
