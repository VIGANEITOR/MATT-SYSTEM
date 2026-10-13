# R0 — Esqueleto

**Estado**: Planificado

## Alcance (Must)
Usuarios y roles, proyectos, registro de experimentos, orquestador con máquina de estados, sandbox sin red,
almacenamiento de artefactos con hash, procedencia básica, UI mínima.

## Requisitos
RF-01 Crear proyecto con jurisdicción y CRS · RF-02 Pregunta e hipótesis antes de ejecutar ·
RF-03 Sandbox aislado · RF-04 Reproducir una ejecución · RF-05 Etiquetar procedencia de cada valor

## Agentes
Análisis, Planificación, Desarrollo científico, Verificación técnica (básica), Despliegue (Brief de Agentes v1.1 §7)

## Decisiones previas
ADR-001 Orquestación · ADR-002 Sandbox · ADR-003 Proveedores de IA · ADR-004 Almacenamiento

## Criterio de salida (gate)
- [ ] Un script Python se ejecuta en sandbox sin red
- [ ] Su resultado queda trazable (hash de entradas, versión de código, imagen, semilla)
- [ ] Una re-ejecución lo reproduce bit a bit (QA-REP-001)
- [ ] Informe de QA emitido; 0 defectos S1/S2 abiertos
