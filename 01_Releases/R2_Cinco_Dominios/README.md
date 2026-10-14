# R2 — Multidominio e interdisciplina

**Estado**: Planificado · Especificación: [Brief Maestro v1.4 §3](../../00_Especificacion/Brief_Maestro/v1.4/MATTX_Brief_Maestro_v1.4.md)

## Capacidad de plataforma (Must)
Perfiles y casos dorados de los cinco dominios; procedimiento para incorporar cualquier dominio o área nueva; acoplamiento entre disciplinas con procedencia completa; incertidumbre completa (Monte Carlo, Sobol); decisión multicriterio; biblioteca de métodos abierta.

## Ámbito científico
Abierto: los cinco dominios son el punto de partida, no el límite.

## Casos de referencia (ejemplos, no límites)
Un caso dorado por dominio (geotecnia, pavimentos, estructural, construcción) y al menos dos flujos acoplados (p. ej., lluvia → infiltración → estabilidad de taludes).

## Agentes
Instancias de Especialista de dominio, Incertidumbre y experimentación completa, Decisión multicriterio, Aprendizaje.

## Requisitos
RF-11 y RF-12.

## Criterio de entrada (§3.5)
- [ ] Paquete de traspaso de R1
- [ ] Especialistas por dominio designados
- [ ] Casos dorados candidatos de los cuatro dominios

## Criterio de salida (gate)
- [ ] 5/5 casos dorados aprobados por revisor independiente
- [ ] 2 flujos acoplados verificados de punta a punta
- [ ] Al menos un dominio o área fuera de los cinco incorporado con el procedimiento
- [ ] 0 defectos S1/S2 abiertos

## Paquete de traspaso al siguiente release (§3.5)
- [ ] Procedimiento de incorporación de dominios probado
- [ ] Perfiles de los cinco dominios y de un área más
- [ ] Contrato de acoplamiento entre flujos
- [ ] Bibliotecas de incertidumbre y multicriterio
- [ ] Métricas de G2
- [ ] Registro de feedback de R2
- [ ] Backlog priorizado de R3

## Feedback (§3.6)
Registro en [`06_Feedback/registro.md`](06_Feedback/registro.md). Al cerrar el release: informe de cierre y punto de
decisión sobre el siguiente (iniciar, ajustar o posponer).
