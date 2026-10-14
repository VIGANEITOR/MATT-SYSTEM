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

**Dos productos.** *MATTX plataforma* gestiona usuarios, proyectos, agentes, ejecuciones, permisos, datos, evidencias y
versiones. *MATTX fábrica* transforma ideas en programas científicos, bibliotecas de métodos y aplicaciones
verificadas. El estado real de ambos está solo en [ESTADO.md](ESTADO.md).

## Documentos vigentes

| Documento | Versión | Archivo |
|---|---|---|
| Constitución | 1.0 (provisional) | [CONSTITUCION.md](CONSTITUCION.md) |
| Brief Maestro | 1.6 | [00_Especificacion/Brief_Maestro/v1.6](00_Especificacion/Brief_Maestro/v1.6/MATTX_Brief_Maestro_v1.6.md) |
| Brief de Agentes | 1.2 (cambios ya aceptados; por confirmar) | [00_Especificacion/Brief_Agentes/v1.2](00_Especificacion/Brief_Agentes/v1.2/MATTX_Brief_Agentes_v1.2.md) |
| Brief de Implementación | 2.4 (borrador) | [00_Especificacion/Brief_Implementacion/v2.4](00_Especificacion/Brief_Implementacion/v2.4/MATTX_Brief_Implementacion_v2.4.md) |
| **Estado real de los componentes** | Generado | [ESTADO.md](ESTADO.md) |
| Verificación de la matriz normativa | Revisión 13-oct-2026 | [00_Especificacion/Revisiones](00_Especificacion/Revisiones/2026-10-13_verificacion_matriz_normativa.md) |
| Decisiones de arquitectura | ADR-001…008 (propuestos) | [00_Especificacion/ADR](00_Especificacion/ADR/README.md) |
| Registro de cambios | — | [00_Especificacion/CHANGELOG.md](00_Especificacion/CHANGELOG.md) |
| Pendientes | Revisión 13-oct-2026 | [PENDIENTES.md](PENDIENTES.md) |
| Seguridad | — | [SECURITY.md](SECURITY.md) |

Toda versión anterior de un documento queda **superada** por la vigente y se conserva solo como historial.

## Hoja de ruta

El ámbito científico es **abierto**; cada release cierra solo la prueba de su capacidad, deja un paquete de traspaso
para el siguiente y se mejora con el feedback (Brief Maestro v1.6 §3).

| Release | Capacidad | Casos de referencia (ejemplos) | Estado |
|---|---|---|---|
| R0 — Núcleo reproducible | Núcleo, sandbox sin red y con red controlada, procedencia; **fábrica mínima por capacidad ponderada**, en dos etapas (R0a ruta mínima → R0b); 7 agentes operativos y 14 observadores tras R0a | Programa T1 piloto | Planificado |
| R1 — Ciclo científico completo | Ciclo de punta a punta para cualquier dominio | Drenaje pluvial bajo CE.040 + prueba de generalidad en otro dominio | Planificado |
| R2 — Multidominio e interdisciplina | Incorporación de cualquier dominio y flujos acoplados | Cinco dominios + un área más + 2 flujos acoplados | Planificado |
| R3 — Integraciones y motores propios | Adaptadores abiertos, geomática, motores propios verificados | Motor propio de drenaje contrastado con SWMM | Planificado |
| R4+ — Extensiones | Registro abierto de extensiones | Portable, fablab virtual, GNSS, gemelos digitales, sensores… | Planificado |

## Estructura

```
CONSTITUCION.md      Reglas superiores del proyecto
00_Especificacion/   Briefs versionados (vN.M), ADRs y registro de cambios
01_Releases/         Una carpeta de trabajo por release (R0–R4): alcance, diseño, desarrollo, QA, entregables
02_Agentes/          Contratos, esquemas JSON, evals y perfiles de dominio de los 21 agentes base
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

El repositorio se publica bajo licencia [MIT](LICENSE), creada al inicializar el repositorio en GitHub. [ADR-008](00_Especificacion/ADR/ADR-008-licencia.md) debe confirmarla o reemplazarla (por ejemplo, separando la licencia del código y la de la documentación y los datos).
