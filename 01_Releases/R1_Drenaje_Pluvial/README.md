# R1 — Primer flujo científico: drenaje pluvial urbano (RNE OS.060)

**Estado**: Planificado

## Alcance (Must)
Flujo de drenaje pluvial de punta a punta (Brief Maestro §14), agentes de análisis, hidráulica, verificación y
documentación, patrones de confianza en UI, design system v1.

## Requisitos
RF-06 Impedir números sin ejecución · RF-07 Detectar datos faltantes · RF-08 Citar norma con edición ·
RF-09 Aprobación por rol autorizado · RF-10 Exportar paquete reproducible ·
RF-15 Cobertura bibliográfica internacional · RF-16 Separar norma de cumplimiento y referencia

## Marco de referencia
RNE OS.060 como norma de cumplimiento; referencias internacionales (EPA SWMM, FHWA HEC-22, ASCE/EWRI MOP 77, EN 752, CIRIA C753, entre otras) según Brief Maestro v1.2 §3.3.

## Decisiones previas
ADR-005 Frontend · ADR-006 Caso dorado local · ADR-007 Despliegue · ADR-008 Licencia

## Criterio de salida (gate)
- [ ] Caso dorado reproducido dentro de ±2 % en caudal pico
- [ ] Error de continuidad de la simulación < 1 %
- [ ] 100 % de valores de la memoria con procedencia; 0 "Generado por IA" en la versión aprobada
- [ ] Paquete exportado re-ejecutado por un tercero fuera de MATTX con el mismo resultado
- [ ] Aprobación nominal registrada del ingeniero responsable
- [ ] Tiempo de producción −40 % frente a la línea base
- [ ] SUS ≥ 75 con 5 usuarios; 0 defectos S1/S2 abiertos

## Pendiente
Elegir el caso dorado local y el revisor independiente que lo valida.
