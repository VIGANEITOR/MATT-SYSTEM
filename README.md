# MATTX

Plataforma de IA para el desarrollo científico de la ingeniería civil.

> **Estado: especificación objetivo.** Ningún componente se considera implementado por estar descrito
> (Constitución, Art. 13). El estado real de cada módulo se publica en la hoja de ruta.

MATTX es un laboratorio digital donde una pregunta de ingeniería civil se convierte en un experimento
numérico reproducible, validado contra evidencia y documentado para revisión por pares o por la entidad
competente. La IA acelera la investigación, la codificación y la redacción; **no es fuente de verdad numérica**.

**Conocimiento sin fronteras.** MATTX usa bibliografía científica, técnica y normativa nacional e internacional.
La jurisdicción de cada proyecto solo define qué norma es de cumplimiento obligatorio; nunca limita qué conocimiento
se consulta (Constitución, Título III).

## Documentos vigentes

| Documento | Versión | Archivo |
|---|---|---|
| Constitución | 1.0 (provisional) | [CONSTITUCION.md](CONSTITUCION.md) |
| Brief Maestro | 1.2 | [00_Especificacion/Brief_Maestro/v1.2](00_Especificacion/Brief_Maestro/v1.2/MATTX_Brief_Maestro_v1.2.md) |
| Brief de Agentes | 1.0 | [00_Especificacion/Brief_Agentes/v1.0](00_Especificacion/Brief_Agentes/v1.0/MATTX_Brief_Agentes_v1.0.md) |
| Brief de Implementación | 2.0 (borrador) | [00_Especificacion/Brief_Implementacion/v2.0](00_Especificacion/Brief_Implementacion/v2.0/MATTX_Brief_Implementacion_v2.0.md) |
| Decisiones de arquitectura | ADR-001…008 (propuestos) | [00_Especificacion/ADR](00_Especificacion/ADR/README.md) |
| Registro de cambios | — | [00_Especificacion/CHANGELOG.md](00_Especificacion/CHANGELOG.md) |

## Hoja de ruta

| Release | Alcance (Must) | Criterio de salida | Estado |
|---|---|---|---|
| R0 — Esqueleto | Usuarios, proyectos, registro de experimentos, orquestador, sandbox sin red, artefactos con hash, procedencia básica | Script Python en sandbox, trazable y reproducible bit a bit | Planificado |
| R1 — Drenaje pluvial | Flujo RNE OS.060 de punta a punta con referencias internacionales, patrones de confianza, design system v1 | Caso dorado ±2 %, 100 % valores trazables, firma del ingeniero, SUS ≥ 75 | Planificado |
| R2 — Cinco dominios | Geotecnia, pavimentos, estructural, construcción, incertidumbre, AHP | 5/5 casos dorados aprobados por revisor independiente | Planificado |
| R3 — Integraciones | CAD/BIM/GIS, conectores licenciados, nubes de puntos, paquete cifrado | Matriz de conectores con estado real y pruebas de recuperación | Planificado |
| R4+ — Extensiones | Portable, fablab virtual, visión móvil, GNSS | Mini-brief + ADR + criterio de salida propios | Planificado |

## Estructura

```
CONSTITUCION.md      Reglas superiores del proyecto
00_Especificacion/   Briefs versionados (vN.M), ADRs y registro de cambios
01_Releases/         Una carpeta de trabajo por release (R0–R4): alcance, diseño, desarrollo, QA, entregables
02_Agentes/          Contratos, evals y perfiles de dominio de los 17 agentes
03_Casos_Dorados/    Benchmarks con datos fijos, resultado de referencia y tolerancia por dominio
04_Design_System/    Tokens, componentes y guía de arte
05_Investigacion_UX/ Entrevistas, personas, JTBD y métricas de línea base (sin datos personales)
06_Sitio_Publico/    Fuente del sitio de documentación pública (MkDocs)
07_Plataforma/       Código del núcleo (desde R0)
08_Programas/        Programas científicos de la fábrica (desde R0)
99_Archivo/          Versiones retiradas (nunca se borran)
```

## Convención de versiones

- **Documentos**: cada versión vive en su propia carpeta `vN.M`; una versión publicada no se sobrescribe.
  Los cambios se registran en [`00_Especificacion/CHANGELOG.md`](00_Especificacion/CHANGELOG.md).
- **Releases**: `01_Releases/Rn_*` guarda alcance, evidencias de compuerta y entregables de cada release.
  El código se versiona con git y etiquetas `rN.x.y`; los programas con `<id>@x.y.z`.
- **ADRs**: numerados e inmutables una vez aceptados; un cambio se hace con un ADR nuevo que reemplaza al anterior.
- **Commits**: Conventional Commits (`feat:`, `fix:`, `docs:` …). Ver Brief de Implementación §8.

## Uso de IA

Parte de esta documentación fue redactada o convertida con asistencia de IA y está pendiente de revisión humana,
según se indica en el control de cada documento (Constitución, Art. 22).

## Licencia

Pendiente de [ADR-008](00_Especificacion/ADR/ADR-008-licencia.md). Hasta su aprobación: todos los derechos reservados.
