# R1 — Ciclo científico completo

**Estado**: Planificado · Especificación: [Brief Maestro v1.4 §3](../../00_Especificacion/Brief_Maestro/v1.4/MATTX_Brief_Maestro_v1.4.md)

## Capacidad de plataforma (Must)
Ciclo de punta a punta para cualquier dominio: pregunta → investigación nacional e internacional → teoría → código → V&V → incertidumbre local → documentación → aprobación humana → paquete reproducible. Patrones de confianza en UI, design system v1, compuertas G-SPEC a G-RELEASE y G-DOC.

## Ámbito científico
Abierto: toda pregunta de ingeniería civil o de un área complementaria puede entrar por el carril abierto.

## Casos de referencia (ejemplos, no límites)
Demostrador: drenaje pluvial urbano bajo RNE CE.040 (Brief Maestro §14). Prueba de generalidad: un programa T1 de un dominio distinto.

## Agentes
Investigación, Formulación científica, Métodos numéricos, Diseño técnico, `hidraulica.drenaje_pluvial`, Incertidumbre y experimentación (sensibilidad ±20 %), Documentación científica y los cinco agentes de interfaz y diseño.

## Requisitos
RF-06 a RF-10, RF-15 y RF-16.

## Criterio de entrada (§3.5)
- [ ] Paquete de traspaso de R0
- [ ] ADR-005 a ADR-008 aceptados
- [ ] Caso dorado local bajo CE.040 y su revisor independiente (ADR-006)
- [ ] Investigación UX con línea base de tiempos
- [ ] Normas de cumplimiento de R1 verificadas en fuente oficial (PENDIENTES C7)

## Criterio de salida (gate)
- [ ] Caso dorado del demostrador dentro de ±2 % en caudal pico; continuidad < 1 %
- [ ] 100 % de valores de la memoria con procedencia; 0 "Generado por IA" en la versión aprobada (G-DOC)
- [ ] Paquete exportado re-ejecutado por un tercero fuera de MATTX con el mismo resultado
- [ ] Aprobación nominal registrada del ingeniero responsable
- [ ] Tiempo de producción −40 % frente a la línea base; SUS ≥ 75 con 5 usuarios
- [ ] La prueba de generalidad pasa todas sus compuertas sin cambiar el código de la plataforma
- [ ] 0 defectos S1/S2 abiertos

## Paquete de traspaso al siguiente release (§3.5)
- [ ] Fábrica operativa con todas las compuertas
- [ ] Plantilla de programa
- [ ] Primeros métodos de la biblioteca (hidrología y drenaje)
- [ ] Perfil de dominio de hidráulica
- [ ] Design system v1
- [ ] Programa de la prueba de generalidad
- [ ] Métricas de G1
- [ ] Feedback de usuarios (SUS, entrevistas)
- [ ] Registro de feedback de R1
- [ ] Backlog priorizado de R2

## Feedback (§3.6)
Registro en [`06_Feedback/registro.md`](06_Feedback/registro.md). Al cerrar el release: informe de cierre y punto de
decisión sobre el siguiente (iniciar, ajustar o posponer).
