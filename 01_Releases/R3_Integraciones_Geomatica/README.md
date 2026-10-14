# R3 — Integraciones, geomática y motores propios

**Estado**: Planificado · Especificación: [Brief Maestro v1.4 §3](../../00_Especificacion/Brief_Maestro/v1.4/MATTX_Brief_Maestro_v1.4.md)

## Capacidad de plataforma (Must)
Adaptadores de formatos abiertos (IFC, LandXML, GeoTIFF, GeoPackage), topografía y nubes de puntos, paquete de proyecto cifrado, motores propios verificados y software de terceros "no confiable hasta verificar".

## Ámbito científico
Abierto. Prioridad a motores propios abiertos y auditables; software licenciado solo opcional y con licencia del usuario.

## Casos de referencia (ejemplos, no límites)
Primer motor propio: solucionador de redes de drenaje, contrastado con EPA SWMM. Segundo previsto: análisis estructural.

## Agentes
Geomática y BIM, Forja de herramientas y agentes, Desarrollo científico y Verificación técnica para los motores propios.

## Requisitos
RF-13 y RF-14.

## Criterio de entrada (§3.5)
- [ ] Paquete de traspaso de R2
- [ ] Matriz de conectores inicial
- [ ] Casos dorados de drenaje de R1 disponibles para contrastar

## Criterio de salida (gate)
- [ ] Matriz de conectores con estado real publicada
- [ ] Pruebas de recuperación aprobadas
- [ ] Motor propio de drenaje verificado dentro de tolerancia frente a SWMM en los casos dorados de R1
- [ ] 0 defectos S1/S2 abiertos

## Paquete de traspaso al siguiente release (§3.5)
- [ ] Motor propio de drenaje verificado
- [ ] Adaptadores de formatos abiertos
- [ ] Geomática con CRS trazable
- [ ] Matriz de conectores con estado real
- [ ] Forja operativa
- [ ] Métricas de G3
- [ ] Registro de feedback de R3

## Feedback (§3.6)
Registro en [`06_Feedback/registro.md`](06_Feedback/registro.md). Al cerrar el release: informe de cierre y punto de
decisión sobre el siguiente (iniciar, ajustar o posponer).
