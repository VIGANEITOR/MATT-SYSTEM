# R1 — Primer flujo científico: drenaje pluvial urbano (RNE CE.040)

**Estado**: Planificado

> La norma de cumplimiento es la **CE.040 Drenaje Pluvial**, que reemplazó a la OS.060 (DS 012-2020-VIVIENDA,
> RM 126-2021-VIVIENDA). Su vigencia debe confirmarse en la fuente oficial antes de iniciar R1
> ([revisión](../../00_Especificacion/Revisiones/2026-10-13_verificacion_matriz_normativa.md)).

## Alcance (Must)
Flujo de drenaje pluvial de punta a punta (Brief Maestro v1.3 §14), patrones de confianza en UI, design system v1.

## Agentes (Brief de Agentes v1.1 §7)
Investigación, Formulación científica, Métodos numéricos, Diseño técnico, `hidraulica.drenaje_pluvial`,
Incertidumbre y experimentación (sensibilidad ±20 %), Documentación científica y los cinco agentes de interfaz y diseño.

## Requisitos
RF-06 Impedir números sin ejecución · RF-07 Detectar datos faltantes · RF-08 Citar norma con edición ·
RF-09 Aprobación por rol autorizado · RF-10 Exportar paquete reproducible ·
RF-15 Cobertura bibliográfica internacional · RF-16 Separar norma de cumplimiento y referencia

## Marco de referencia
RNE CE.040 como norma de cumplimiento; referencias internacionales (EPA SWMM, FHWA HEC-22, ASCE/EWRI MOP 77,
EN 752, CIRIA C753, entre otras) según Brief Maestro v1.3 §3.3, una vez verificadas.

## Decisiones previas
ADR-005 Frontend · ADR-006 Caso dorado local · ADR-007 Despliegue · ADR-008 Licencia

## Criterio de salida (gate)
- [ ] Caso dorado reproducido dentro de ±2 % en caudal pico
- [ ] Error de continuidad de la simulación < 1 %
- [ ] 100 % de valores de la memoria con procedencia; 0 "Generado por IA" en la versión aprobada (G-DOC)
- [ ] Paquete exportado re-ejecutado por un tercero fuera de MATTX con el mismo resultado
- [ ] Aprobación nominal registrada del ingeniero responsable
- [ ] Tiempo de producción −40 % frente a la línea base
- [ ] SUS ≥ 75 con 5 usuarios; 0 defectos S1/S2 abiertos

## Pendiente
Elegir el caso dorado local (estudio firmado bajo CE.040) y el revisor independiente que lo valida.
