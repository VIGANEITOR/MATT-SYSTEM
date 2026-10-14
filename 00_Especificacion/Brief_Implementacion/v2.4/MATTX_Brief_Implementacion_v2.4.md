# MATTX — Brief de Implementación v2.4

La fábrica de programas científicos · Oct 14, 2026 · @Chris

## 0. Control del documento

| Campo | Definición |
|---|---|
| Producto | MATTX |
| Documento | Brief de Implementación: cómo se construye MATTX y cómo MATTX construye programas científicos |
| Versión | 2.4 (reemplaza a 2.3 del 14-oct-2026) |
| Vigencia | Toda versión anterior queda superada por esta y se conserva solo como historial |
| Estado | Borrador. Incorpora SC-001, SC-002 y FB-R0-002 a 006. Redactado con asistencia de IA; pendiente de aprobación |
| Rige sobre | Tipos de programa (T1–T5), compuertas (G-SPEC … G-RELEASE, G-DOC), plantilla de programa, flujo Git, CI/CD y fases de la fábrica (G0–G3) |
| Subordinado a | [Constitución de MATTX](../../../CONSTITUCION.md), [Brief Maestro v1.6](../../Brief_Maestro/v1.6/MATTX_Brief_Maestro_v1.6.md) |
| Agentes | [Brief de Agentes v1.2](../../Brief_Agentes/v1.2/MATTX_Brief_Agentes_v1.2.md) |
| Aprobadores | Pendiente: responsable técnico, responsable científico |

**Cambios respecto a v2.3**

| Cambio | Origen | Sección |
|---|---|---|
| R0 en dos etapas: **R0a ruta mínima completa** y R0b; los observadores se activan tras R0a | FB-R0-004, SC-002 | 12.2 |
| El 50 % pasa a **capacidad ponderada**: ID, prueba de aceptación, criticidad y peso por elemento; 10 elementos **no compensables** | FB-R0-005, SC-002 | 12.1 |
| El inventario se genera desde el registro único; el estado de cada elemento vive solo en `ESTADO.md` | FB-R0-003 | 12.3 |
| La plataforma y la fábrica se gobiernan por separado | FB-R0-007 | 1 |

**Cambios de v2.2 a v2.3 (historial)**

| Cambio | Sección |
|---|---|
| Los observadores producen **informes de defectos potenciales** con evidencia, severidad y prioridad; las mejoras no son defectos | 13.1 |
| Matriz de permisos del observador: sin ejecución, sin red, sin credenciales, sin acciones privilegiadas (se elimina la ejecución propia en sandbox que permitía la v2.2) | 13.2 |
| La reproducción de un hallazgo la ejecuta Verificación técnica por decisión humana | 13.3 |
| El observador no aprueba, confirma ni prioriza su propia propuesta; informes inmutables | 13.4 |
| Utilidad medida por **defectos reales** confirmados; el volumen no cuenta | 13.5 |

**Cambios de v2.1 a v2.2 (historial)**

| Cambio | Sección |
|---|---|
| R0 implementa al menos el 50 % de este brief: inventario de 45 elementos, clases núcleo, Must y Should, criterio de salida medible | 12 (nuevo) |
| Modo observador para los agentes que aún no operan, con límites, destino de hallazgos y transición | 13 (nuevo) |
| Fase G0 actualizada con el nuevo alcance | 10 |
| Formulación científica y Métodos numéricos operan desde R0 | 12.3 |

**Cambios de v2.0 a v2.1 (historial)**

| Cambio | Sección |
|---|---|
| Nombres de agentes unificados (Desarrollo científico, Verificación técnica) | 3 |
| Nueva etapa de Documentación científica y compuerta **G-DOC** para entregables escritos | 2, 3, 4 |
| Los agentes emiten informes; **solo personas aprueban** compuertas (corrige G-UI y G-VERIFY) | 4 |
| El grupo B son agentes de IA que diseñan e implementan interfaces | 3 |
| Esquemas de contrato y mensaje de agente creados y validados en CI | 9, 12 |
| Ejemplo T3 actualizado a la norma CE.040 | 2 |

**Convención normativa.** DEBE, DEBERÍA y PUEDE según el Artículo 4 de la Constitución.

## 1. Propósito

MATTX entrega dos cosas distintas, con ciclos de vida distintos:

| Producto | Qué es | Quién lo construye | Cómo se libera |
|---|---|---|---|
| **Plataforma** | Núcleo: orquestador, sandbox, procedencia, registro, interfaz (Brief Maestro §6) | Equipo de ingeniería de software | Releases R0–R4 |
| **Programas científicos** | Herramientas de cálculo, bibliotecas de métodos, aplicaciones y flujos verificados | La *fábrica*: agentes del Brief de Agentes v1.1 + aprobación humana | Registro de programas, versión semántica por programa |

Son los dos productos de MATTX (Brief Maestro v1.6 §1.2) y se gobiernan por separado: componentes `PLA-xx` y `FAB-xx`
en el registro único, con su estado publicado en [`ESTADO.md`](../../../ESTADO.md).

Este brief especifica la fábrica: el camino que lleva una idea de ingeniería civil a un programa verificado,
empaquetado, citable y reproducible fuera de MATTX.

## 2. Tipos de programa

| Tipo | Qué es | Ejemplo | Compuertas obligatorias | Agentes de diseño (grupo B) |
|---|---|---|---|---|
| **T1 — Cálculo** | Script o cuaderno determinista con entradas y salidas tipadas | Caudal por método racional | G-SPEC, G-THEORY, G-CODE, G-VERIFY, G-RELEASE | No |
| **T2 — Biblioteca de métodos** | Módulo reutilizable con API estable y documentada, usado por otros programas | Curvas IDF; equilibrio límite de Bishop; AASHTO 93 | T1 + API documentada y pruebas de propiedad | No |
| **T3 — Aplicación con interfaz** | Programa T1/T2 con interfaz de usuario | Calculadora de cunetas con verificación CE.040 | T2 + G-UI | Sí, cadena completa |
| **T4 — Flujo integrado** | Orquesta varios programas, datasets y conectores de punta a punta | Flujo R1 de drenaje pluvial urbano | T3 (si tiene interfaz) + pruebas E2E del flujo y de conectores + G-DOC si produce entregable escrito | Si tiene interfaz |
| **T5 — Experimento publicable** | Paquete de investigación con cuantificación de incertidumbre, dataset y artículo o memoria | Sensibilidad del caudal pico al cambio de uso de suelo | Todas las del tipo base + incertidumbre en G-VERIFY + G-DOC + aprobación del responsable científico | Si tiene interfaz |

Regla de clasificación: el agente de Análisis propone el tipo; el tipo determina las compuertas. Cambiar de tipo
durante el desarrollo exige volver a G-SPEC.

## 3. Pipeline de la fábrica

| # | Etapa | Agente (Brief de Agentes) | Artefacto de salida | Compuerta |
|---|---|---|---|---|
| 1 | Idea → solicitud estructurada | Análisis | Solicitud: dominio, tipo T1–T5, entradas faltantes, hipótesis, riesgos | — |
| 2 | Estado del arte | Investigación | Matriz de fuentes nacional e internacional (Brief Maestro §3.3) | — |
| 3 | Especificación | Planificación | `SPEC.md` + plan de tareas | **G-SPEC** |
| 4 | Teoría | Formulación científica | `THEORY.md` | **G-THEORY** |
| 5 | Método numérico | Métodos numéricos | `NUMERICS.md` | (parte de G-THEORY) |
| 6 | Arquitectura | Diseño técnico | `ARCHITECTURE.md` | (revisada en G-CODE) |
| 7 | Implementación | Desarrollo científico | Código, pruebas, pull request | **G-CODE** |
| 8 | Verificación y validación | Verificación técnica (+ Incertidumbre en T5) | Informe V&V | **G-VERIFY** |
| 9 | Interfaz (T3+) | Agentes del grupo B: Dirección de Arte → Design System → UI/UX → Frontend → QA Visual | Interfaz implementada e informe de aceptación | **G-UI** |
| 10 | Documentación (T4 con entregable, T5) | Documentación científica | Memoria, informe o artículo con valores por referencia, bibliografía y anexo de IA | **G-DOC** |
| 10b | Empaquetado | Despliegue | Imagen con digest, manifiesto, `CITATION.cff`, versión | **G-RELEASE** |
| 11 | Aprobación | Persona con rol autorizado | Aprobación nominal registrada | — |
| 12 | Aprendizaje | Aprendizaje | Lecciones propuestas | Aprobación humana |

Las etapas que todavía no operan en el release vigente tienen a su agente en **modo observador** (§13).

Cada etapa termina cuando su artefacto se publica con hash; la siguiente parte de ese artefacto, no de un resumen
(Brief de Agentes §6.2). Una compuerta fallida devuelve el trabajo a la etapa que la produjo, con el informe de
defectos.

## 4. Compuertas

Cada compuerta es una lista de verificación ejecutada por CI y por un verificador distinto del autor. Ninguna se
aprueba por declaración. **Los agentes emiten informes; solo personas aprueban** (Constitución, Art. 27).

### G-SPEC — Especificación verificable

- [ ] `SPEC.md` valida contra su esquema (secciones obligatorias de §6.1).
- [ ] Pregunta, hipótesis o criterio de aceptación registrados.
- [ ] 100 % de los requisitos con criterio Given/When/Then y prueba vinculada.
- [ ] Jurisdicción de cumplimiento declarada y matriz de fuentes con al menos una fuente nacional y una internacional por criterio crítico (RF-15).
- [ ] Tipo de programa, entradas, salidas con unidades SI y presupuesto declarados.

Aprueba: responsable de producto (alcance) y especialista del dominio (pertinencia técnica).

### G-THEORY — Teoría y método

- [ ] `THEORY.md` con ecuaciones, supuestos, rango de validez, condiciones de borde y referencias con página.
- [ ] Análisis dimensional sin errores (verificación automática con Pint/SymPy).
- [ ] Toda derivación nueva paso a paso y revisable.
- [ ] `NUMERICS.md` con método elegido, justificación y criterio de convergencia.
- [ ] Orden de convergencia observado = teórico ± 0,2, o estudio de soluciones manufacturadas.

Aprueba: especialista del dominio.

### G-CODE — Código

- [ ] Pruebas unitarias verdes; cobertura de líneas ≥ 90 % en el núcleo de cálculo.
- [ ] Ningún número de diseño fijo en el código sin fuente citada.
- [ ] Reutiliza la biblioteca de métodos cuando el método existe.
- [ ] Lint, tipado estático, SAST y escaneo de dependencias sin hallazgos críticos o altos.
- [ ] Coherencia entre `ARCHITECTURE.md` y la estructura real del repositorio.

Aprueba: persona revisora distinta del autor (puede apoyarse en la revisión automática de un agente distinto del autor).

### G-VERIFY — Verificación y validación

- [ ] Casos dorados dentro de la tolerancia declarada.
- [ ] Balances (masa, energía, continuidad) y chequeos dimensionales.
- [ ] Pruebas de propiedad (hypothesis) y de mutación (mutmut) con puntuación de mutación ≥ 80 % en el núcleo.
- [ ] Validación contra datos medidos cuando existan, reportada por separado de la verificación.
- [ ] T5: incertidumbre con semilla registrada y tamaño de muestra justificado por convergencia del estimador.
- [ ] 0 defectos S1/S2 abiertos.

Informe: agente de Verificación técnica. Aprueba: responsable científico.

### G-UI — Interfaz (T3 en adelante)

- [ ] Cada requisito del SPEC tiene una pantalla o interacción que lo cubre.
- [ ] Insignia de procedencia en todo valor calculado; "¿De dónde sale este número?" operativo.
- [ ] Solo componentes del design system; el cliente no recalcula lo que calcula el núcleo.
- [ ] Pruebas E2E verdes; WCAG 2.2 AA con 0 violaciones críticas de axe-core.

Informe: agente de QA Visual y Accesibilidad. Aprueba: responsable de producto.

### G-DOC — Entregable escrito (T4 con entregable, T5)

- [ ] 100 % de los valores numéricos insertados por referencia a un Resultado; 0 valores tecleados.
- [ ] 0 valores "Generado por IA" o "no verificado" en la versión enviada a aprobación (RF-06).
- [ ] 100 % de las citas resuelven a una Fuente registrada; normas con código, organismo, país, edición y artículo (RF-08).
- [ ] Normas etiquetadas como cumplimiento o referencia (RF-16); cobertura nacional e internacional (RF-15).
- [ ] Verificación y validación en secciones separadas; incertidumbre o etiqueta "determinístico".
- [ ] Ejecuciones descartadas con motivo; anexo de uso de IA.

Informe: agente de Documentación científica (borrador) y agente de Verificación técnica (revisión cruzada de
trazabilidad). Aprueba: ingeniero responsable, con firma nominal.

### G-RELEASE — Liberación

- [ ] Imagen reconstruida con digest idéntico o reproducible; manifiesto y `CITATION.cff` completos.
- [ ] Re-ejecución externa, fuera de MATTX, con resultado idéntico o dentro de tolerancia.
- [ ] Versión semántica y `CHANGELOG.md` actualizados.
- [ ] Anexo de uso de IA generado (Constitución, Art. 22).

Aprueba: responsable técnico.

## 5. Registro de programas y biblioteca de métodos

| Estado del programa | Significado |
|---|---|
| Borrador | En la fábrica; no ha pasado G-VERIFY |
| Verificado | Pasó G-VERIFY; aún no liberado |
| Liberado | Pasó G-RELEASE y tiene aprobación nominal |
| Obsoleto | Reemplazado por una versión mayor; se conserva para reproducir resultados anteriores |
| Retirado | No se usa en trabajo nuevo; queda en el registro para trazabilidad |

- Cada programa tiene identificador `dominio.nombre@MAYOR.MENOR.PARCHE`.
- MAYOR cambia si cambian resultados para las mismas entradas; MENOR si se agregan capacidades compatibles; PARCHE si se corrigen defectos sin cambiar resultados verificados.
- La biblioteca de métodos es el conjunto de programas T2 liberados; los agentes de Desarrollo DEBEN reutilizarla.

## 6. Plantilla de programa

```
<dominio>.<nombre>/
├─ SPEC.md              Especificación (G-SPEC)
├─ THEORY.md            Teoría y referencias (G-THEORY)
├─ NUMERICS.md          Método numérico y convergencia (G-THEORY)
├─ ARCHITECTURE.md      Módulos, interfaces y modelo de datos
├─ src/                 Núcleo de cálculo
├─ ui/                  Interfaz (solo T3+)
├─ tests/
│  ├─ unit/
│  ├─ properties/       Pruebas de propiedad
│  ├─ golden/           Casos dorados con tolerancia
│  └─ e2e/              Solo T3+ y T4
├─ data/                Solo datos abiertos y con licencia; nunca datos sensibles
├─ environment.lock     Dependencias fijadas
├─ Dockerfile
├─ manifest.json        Hashes de entradas, código, imagen y resultados
├─ CITATION.cff
├─ CHANGELOG.md
└─ LICENSE              Según ADR-008
```

### 6.1 Secciones obligatorias de SPEC.md

1. Pregunta científica, hipótesis y criterio de aceptación.
2. Tipo de programa y justificación.
3. Jurisdicción de cumplimiento y normas aplicables (N1).
4. Matriz de fuentes nacional e internacional (resumen; enlace a la matriz completa).
5. Entradas: nombre, tipo, unidad SI, rango válido, fuente.
6. Salidas: nombre, tipo, unidad SI, tolerancia, procedencia.
7. Requisitos con Given/When/Then y prueba vinculada.
8. Casos dorados y tolerancias.
9. Fuera de alcance.
10. Presupuesto (tiempo, coste de IA) y riesgos.

### 6.2 Secciones obligatorias de THEORY.md

1. Modelo físico y ecuaciones gobernantes.
2. Supuestos y su justificación.
3. Rango de validez y condiciones de borde.
4. Derivaciones nuevas paso a paso (si existen).
5. Análisis dimensional.
6. Referencias con página o ecuación citada, con nivel de evidencia.

## 7. Repositorio MATT-SYSTEM

El repositorio público `VIGANEITOR/MATT-SYSTEM` contiene la especificación y, a partir de R0, el código.

| Carpeta | Contenido | Desde |
|---|---|---|
| `CONSTITUCION.md` | Reglas superiores del proyecto | Ya |
| `00_Especificacion/` | Briefs versionados, ADR, registro de cambios | Ya |
| `01_Releases/` | Alcance, evidencias de compuerta y entregables por release | Ya |
| `02_Agentes/` | Contratos, evals, perfiles de dominio, forja | Ya (contratos desde R0) |
| `03_Casos_Dorados/` | Benchmarks por dominio | Ya (datos desde R1) |
| `04_Design_System/` | Tokens, componentes, guía de arte | R1 |
| `05_Investigacion_UX/` | Resultados de investigación (sin datos personales) | Antes de R1 |
| `06_Sitio_Publico/` | Sitio de documentación pública | Ya |
| `07_Plataforma/` | Código del núcleo: orquestador, sandbox, procedencia, API, interfaz | R0 |
| `08_Programas/` | Programas de la fábrica, uno por carpeta según §6 | R0 (piloto T1) |
| `99_Archivo/` | Versiones retiradas | Ya |

## 8. Flujo de trabajo con Git

- `main` está protegida: solo recibe cambios por pull request con CI verde y una revisión aprobada de alguien distinto del autor.
- Ramas: `feat/…`, `fix/…`, `docs/…`, `adr/NNN-…`, `programa/<id>`, `release/rN`.
- Mensajes de commit según Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).
- Etiquetas: `rN.x.y` para la plataforma; `<id-programa>@x.y.z` para cada programa.
- Una enmienda constitucional va en su propia rama y pull request, con la etiqueta `enmienda-constitucional`.
- Nunca se suben secretos, credenciales, datos personales ni documentos de perfil P3; el CI DEBE ejecutar un escáner de secretos.

## 9. Integración y despliegue continuos

| Pipeline | Qué ejecuta | Cuándo | Bloquea |
|---|---|---|---|
| `docs` | Enlaces rotos, formato Markdown, construcción del sitio | Cada pull request | Sí |
| `spec` | Validación de contratos y mensajes de agente (`02_Agentes/validar_contratos.py`, ya operativo); SPEC, THEORY y manifiesto cuando existan sus esquemas | Cada pull request | Sí |
| `code` | Lint, tipado, pruebas unitarias, SAST, dependencias, secretos | Cada pull request | Sí |
| `verify` | Casos dorados, balances, propiedades, mutación | Cambios en `src/` o `tests/golden/` | Sí |
| `evals` | Suites de integridad, contrato, funcional, detección y regresión de agentes | Cambio de prompt, modelo o contrato | Sí |
| `e2e-ui` | Playwright, regresión visual, axe-core | Cambios en `ui/` o `07_Plataforma/` | Sí |
| `rep` | Reproducibilidad (QA-REP) | Semanal y en cada release | En release |
| `pages` | Publicación del sitio | Merge a `main` | No |

## 10. Fases de la fábrica (G0–G3)

Las fases miden la madurez de la fábrica; corren en paralelo a los releases de la plataforma.

| Fase | Release asociado | Alcance | Criterio de salida |
|---|---|---|---|
| **G0 — Arranque** | R0 | R0a: ruta mínima completa con el T1 piloto; R0b: resto del alcance y activación de los observadores (§12, §13) | R0a superada; núcleo y 10 no compensables operativos; ≥ 50 % del peso del inventario operativo; tiempo idea → T1 medido; informe de observadores |
| **G1 — Primer dominio** | R1 | Agentes del grupo A en Experimental/Supervisado; programas T1–T4 del flujo de drenaje | Flujo R1 liberado; iteraciones promedio hasta G-VERIFY medidas |
| **G2 — Multidominio** | R2 | Agentes del grupo C en Supervisado; programas T5 habilitados; un T2 por dominio | ≥ 60 % de programas pasan todas las compuertas al primer intento humano; 0 defectos S1 detectados por humanos y no por agentes |
| **G3 — Escala** | R3 | Forja operativa; conectores; biblioteca de métodos estable | Iteraciones hasta G-VERIFY −30 % frente a G1; coste por programa T1/T3 fijado y dentro de presupuesto |

## 11. Definición de terminado

Un trabajo está terminado solo si:

1. Su artefacto está publicado con hash y enlazado en el grafo de procedencia.
2. Pasó la compuerta correspondiente con evidencia, no por declaración.
3. No dejó defectos S1/S2 abiertos.
4. Su documentación y su registro de cambios están actualizados.
5. Una persona con rol autorizado lo aprobó cuando la Constitución lo exige.

## 12. Alcance de implementación por release

**Solicitud del autor (SC-001):** al menos el 50 % de este brief desde R0. **Refinamiento (SC-002):** el 50 % se mide
como **capacidad ponderada**, la **ruta mínima completa va primero** y los elementos críticos **no se compensan**.

### 12.1 Cómo se mide

- Cada elemento del inventario tiene **ID, prueba de aceptación, criticidad y peso** (crítica 3, alta 2, media 1, baja 0,5).
- Un elemento es **operativo** solo si pasa su prueba de aceptación con evidencia en `01_Releases/R0_Esqueleto/04_Verificacion_QA/`. Su estado se registra únicamente en el registro único y se publica en [`ESTADO.md`](../../../ESTADO.md).
- Son **no compensables** los elementos de seguridad, procedencia, reproducibilidad, verificación independiente y aprobación humana. Deben estar todos operativos; ningún avance en interfaz o documentación los compensa.

<!-- inicio:generado:resumen_peso -->
| Clase en R0 | Elementos | Peso | Peso acumulado |
|---|---|---|---|
| **Núcleo** | 19 | 50,5 | 50,5 (57 %) |
| Must | 9 | 15,5 | 66 (74 %) |
| Should | 4 | 4,5 | 70,5 (79 %) |
| Releases posteriores | 13 | 18,5 | — |

Peso total del inventario: **89** (45 elementos). Pesos: crítica 3, alta 2, media 1, baja 0,5. Elementos **no compensables** en el alcance de R0: **10** (deben estar todos operativos).
<!-- fin:generado:resumen_peso -->

**Criterio de salida de R0 para este brief:**

1. Etapa **R0a** superada (12.2).
2. Todos los elementos de **núcleo** y todos los **no compensables** del alcance de R0 operativos.
3. Al menos el **50 % del peso total** del inventario operativo.

El núcleo equivale al 57 % del peso, por lo que cumplir (2) cumple también (3). Objetivo planificado: núcleo + Must
(74 %). Este criterio se fija antes de iniciar R0 y no se relaja durante el release (Brief Maestro §3.6, regla 3).

### 12.2 Etapas de R0

| Etapa | Contenido | Puerta |
|---|---|---|
| **R0a — Ruta mínima** | Idea → especificación → código → ejecución aislada → prueba independiente → resultado trazable → aprobación humana → paquete reproducible, con el programa T1 piloto. 16 elementos de la fábrica marcados R0a y los componentes de plataforma PLA-01 a PLA-05 y PLA-07 a PLA-09 | El T1 recorre la ruta completa una vez, con evidencia de cada eslabón y re-ejecución bit a bit. **Sin R0a superada no se activan observadores ni se agregan agentes** |
| **R0b — Resto del alcance** | Must y Should de la fábrica; red controlada con proxy de salida (PLA-06); aislamiento de credenciales (PLA-10, ADR-009); registro de agentes con permisos en 4 dimensiones (PLA-11); UI mínima (PLA-12); **activación de los 14 observadores** | Criterio de salida completo de R0 |

Motivo (FB-R0-004): si la ruta mínima no funciona, agregar más agentes no resuelve el problema.

### 12.3 Inventario

Especificación generada desde `00_Especificacion/registro/estado_componentes.json`. El **estado** de cada elemento no
figura aquí: está en `ESTADO.md`.

<!-- inicio:generado:inventario_fabrica -->
| ID | Sección | Elemento | En R0 | Etapa | Criticidad | Peso | No compensable | Prueba de aceptación | Agente(s) |
|---|---|---|---|---|---|---|---|---|---|
| FAB-01 | §2 Tipos | T1 — Cálculo | **Núcleo** | R0a | Crítica | 3 | — | QA-IMP-001: Programa T1 piloto liberado | Desarrollo científico |
| FAB-02 | §2 Tipos | T2 — Biblioteca de métodos | Should | R0b | Media | 1 | — | QA-IMP-002: Primer método T2 liberado y reutilizado por el T1 | Desarrollo científico |
| FAB-03 | §2 Tipos | T3 — Aplicación con interfaz | — | — | Media | 1 | — | QA-IMP-003: Se define al planificar su release | Grupo B (observan en R0) |
| FAB-04 | §2 Tipos | T4 — Flujo integrado | — | — | Alta | 2 | — | QA-IMP-004: Se define al planificar su release | Especialista de dominio (observa en R0) |
| FAB-05 | §2 Tipos | T5 — Experimento publicable | — | — | Media | 1 | — | QA-IMP-005: Se define al planificar su release | Incertidumbre (observa en R0) |
| FAB-06 | §3 Pipeline | Etapa 1 — Solicitud estructurada | Must | R0b | Alta | 2 | — | QA-IMP-006: Solicitud del T1 registrada | Análisis |
| FAB-07 | §3 Pipeline | Etapa 2 — Estado del arte | Should | R0b | Alta | 2 | — | QA-IMP-007: Matriz de fuentes del T1 obtenida por red controlada (OpenAlex/Crossref) | Investigación |
| FAB-08 | §3 Pipeline | Etapa 3 — Especificación (SPEC.md) | **Núcleo** | R0a | Crítica | 3 | — | QA-IMP-008: SPEC del T1 aprobado en G-SPEC | Planificación |
| FAB-09 | §3 Pipeline | Etapa 4 — Teoría (THEORY.md) | Must | R0b | Alta | 2 | — | QA-IMP-009: THEORY del T1 aprobado en G-THEORY | Formulación científica |
| FAB-10 | §3 Pipeline | Etapa 5 — Método numérico (NUMERICS.md) | Must | R0b | Alta | 2 | — | QA-IMP-010: NUMERICS del T1 con criterio de convergencia | Métodos numéricos |
| FAB-11 | §3 Pipeline | Etapa 6 — Arquitectura | — | — | Media | 1 | — | QA-IMP-011: Se define al planificar su release | Diseño técnico (observa en R0) |
| FAB-12 | §3 Pipeline | Etapa 7 — Implementación | **Núcleo** | R0a | Crítica | 3 | — | QA-IMP-012: Pull request del T1 aprobado en G-CODE | Desarrollo científico |
| FAB-13 | §3 Pipeline | Etapa 8 — Verificación y validación | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-013: Informe V&V del T1 | Verificación técnica |
| FAB-14 | §3 Pipeline | Etapa 9 — Interfaz | — | — | Media | 1 | — | QA-IMP-014: Se define al planificar su release | Grupo B (observan en R0) |
| FAB-15 | §3 Pipeline | Etapa 10 — Documentación | — | — | Alta | 2 | — | QA-IMP-015: Se define al planificar su release | Documentación científica (observa en R0) |
| FAB-16 | §3 Pipeline | Etapa 10b — Empaquetado | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-016: Imagen con digest, manifiesto y CITATION.cff del T1 | Despliegue |
| FAB-17 | §3 Pipeline | Etapa 11 — Aprobación humana | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-017: Aprobación nominal registrada | Persona autorizada |
| FAB-18 | §3 Pipeline | Etapa 12 — Aprendizaje | — | — | Baja | 0,5 | — | QA-IMP-018: Se define al planificar su release | Aprendizaje (observa en R0) |
| FAB-19 | §4 Compuertas | G-SPEC | **Núcleo** | R0a | Crítica | 3 | — | QA-IMP-019: Lista de verificación aplicada al T1 | Planificación + persona |
| FAB-20 | §4 Compuertas | G-THEORY | Must | R0b | Alta | 2 | — | QA-IMP-020: Lista de verificación aplicada al T1 | Formulación + especialista |
| FAB-21 | §4 Compuertas | G-CODE | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-021: Lista de verificación aplicada al T1 | Revisor humano |
| FAB-22 | §4 Compuertas | G-VERIFY | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-022: Lista de verificación aplicada al T1 | Verificación técnica + responsable científico |
| FAB-23 | §4 Compuertas | G-UI | — | — | Media | 1 | — | QA-IMP-023: Se define al planificar su release | QA Visual (observa en R0) |
| FAB-24 | §4 Compuertas | G-DOC | — | — | Alta | 2 | — | QA-IMP-024: Se define al planificar su release | Documentación científica (observa en R0) |
| FAB-25 | §4 Compuertas | G-RELEASE | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-025: T1 re-ejecutado fuera de MATTX | Despliegue + responsable técnico |
| FAB-26 | §5 Registro | Registro de programas | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-026: T1 registrado con estado y versión | Despliegue |
| FAB-27 | §5 Registro | Biblioteca de métodos | Should | R0b | Media | 1 | — | QA-IMP-027: Biblioteca con el primer T2 | Desarrollo científico |
| FAB-28 | §6 Plantilla | Plantilla de programa | **Núcleo** | R0a | Alta | 2 | — | QA-IMP-028: T1 creado desde la plantilla | Planificación |
| FAB-29 | §6 Plantilla | Secciones obligatorias de SPEC.md (con esquema) | Must | R0b | Media | 1 | — | QA-IMP-029: Esquema de SPEC validado en CI | Planificación |
| FAB-30 | §6 Plantilla | Secciones obligatorias de THEORY.md (con esquema) | Must | R0b | Media | 1 | — | QA-IMP-030: Esquema de THEORY validado en CI | Formulación científica |
| FAB-31 | §7 Repositorio | Estructura del monorepo MATT-SYSTEM | **Núcleo** | R0b | Baja | 0,5 | — | QA-IMP-031: Estructura del monorepo publicada y documentada | — |
| FAB-32 | §8 Git | Flujo de trabajo con Git (rama protegida, Conventional Commits, etiquetas) | Must | R0b | Alta | 2 | — | QA-IMP-032: Rama main protegida; etiqueta r0.x.y | Responsable técnico |
| FAB-33 | §9 CI | Pipeline docs | Must | R0b | Baja | 0,5 | — | QA-IMP-033: Ya compila el sitio en cada cambio | — |
| FAB-34 | §9 CI | Pipeline spec | **Núcleo** | R0b | Alta | 2 | — | QA-IMP-034: Ya valida contratos y esquemas | — |
| FAB-35 | §9 CI | Pipeline code | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-035: Lint, tipado, pruebas, SAST y secretos en cada PR | — |
| FAB-36 | §9 CI | Pipeline verify | **Núcleo** | R0a | Crítica | 3 | — | QA-IMP-036: Casos dorados y propiedades del T1 en CI | — |
| FAB-37 | §9 CI | Pipeline evals | Must | R0b | Crítica | 3 | Sí | QA-IMP-037: Evals de integridad de los 21 agentes en CI | — |
| FAB-38 | §9 CI | Pipeline e2e-ui | — | — | Media | 1 | — | QA-IMP-038: Se define al planificar su release | — |
| FAB-39 | §9 CI | Pipeline rep (reproducibilidad) | **Núcleo** | R0a | Crítica | 3 | Sí | QA-IMP-039: QA-REP en CI | — |
| FAB-40 | §9 CI | Pipeline pages | Should | R0b | Baja | 0,5 | — | QA-IMP-040: Sitio publicado (requiere activar Pages) | — |
| FAB-41 | §10 Fases | G0 — Arranque | **Núcleo** | R0b | Alta | 2 | — | QA-IMP-041: Criterio de salida de G0 cumplido | Todos |
| FAB-42 | §10 Fases | G1 — Primer dominio | — | — | Alta | 2 | — | QA-IMP-042: Se define al planificar su release | — |
| FAB-43 | §10 Fases | G2 — Multidominio | — | — | Alta | 2 | — | QA-IMP-043: Se define al planificar su release | — |
| FAB-44 | §10 Fases | G3 — Escala | — | — | Alta | 2 | — | QA-IMP-044: Se define al planificar su release | — |
| FAB-45 | §11 Terminado | Definición de terminado | **Núcleo** | R0a | Alta | 2 | — | QA-IMP-045: Aplicada a cada artefacto de R0 | Todos |
<!-- fin:generado:inventario_fabrica -->

### 12.4 Agentes en R0

| Modo | Agentes | Cantidad |
|---|---|---|
| **Operativos** | Análisis, Planificación, Formulación científica, Métodos numéricos, Desarrollo científico, Verificación técnica, Despliegue | 7 |
| **Observadores** (se activan tras R0a) | Investigación (pasa a operativo si se cumple su Should), Diseño técnico, Aprendizaje, los cinco del grupo B, Incertidumbre y experimentación, Decisión multicriterio, Geomática y BIM, Especialista de dominio, Documentación científica, Forja | 14 |

La asignación vigente está en `02_Agentes/asignaciones/R0.json`; el CI comprueba que cubre los 21 agentes del catálogo
sin repetir ninguno.

**Riesgo:** R0 crece respecto al Brief Maestro v1.4. **Mitigación:** R0a primero; los observadores comparten una suite
común de evals de integridad y un presupuesto acotado; si el núcleo está en riesgo, se sacrifican primero los Should.

## 13. Modo observador

**Definición (autor, 14-oct-2026):** los observadores producen **informes de defectos potenciales**, con evidencia y
prioridad, **sin modificar código, ejecutar acciones privilegiadas ni aprobar su propia propuesta**. Su utilidad se mide
por los **defectos reales** que detectan.

### 13.1 Qué producen

Un **informe de defectos potenciales** que valida contra `potential_defect_report.schema.json`. Cada hallazgo lleva:

| Campo | Contenido | Obligatorio |
|---|---|---|
| Tipo | Posible error, riesgo de seguridad, brecha de trazabilidad, inconsistencia normativa o inconsistencia entre documentos | Sí |
| Severidad sugerida | S1–S4: impacto si el defecto es real (Brief Maestro §13.3) | Sí |
| Prioridad sugerida | P0–P3: urgencia de revisarlo | Sí |
| Evidencia | Artefacto por hash, ubicación exacta, qué se esperaba y qué se observa | Sí |
| Recomendación | Qué revisar o corregir | Sí |
| Confianza | Alta, media o baja | Sí |
| Requiere reproducción | Si para confirmarlo hay que ejecutar algo (lo ejecuta otro agente, ver 13.3) | No |

Las mejoras y sugerencias de diseño **no son defectos** y no van en este informe. Si un observador las tiene, se
canalizan como feedback ordinario revisado por una persona.

### 13.2 Permisos

El orquestador aplica el perfil `observador`, que **reemplaza** los permisos del contrato y nunca los amplía.

| Permiso | Observador | Agente operativo (referencia) |
|---|---|---|
| Lectura | Solo artefactos publicados de su especialidad, por hash | Según su contrato |
| Escritura | Solo su informe, en `observaciones/<agent_id>/` | Según su contrato |
| Ejecución | **Ninguna**: no ejecuta código, ni siquiera en sandbox | En sandbox según su perfil |
| Red | Denegada | Sin red o red controlada |
| Credenciales | Ninguna | Nunca expuestas (Brief Maestro §12.2) |
| Acciones privilegiadas | **Ninguna**: no cambia estados, compuertas, permisos ni asignaciones; no dispara despliegues; no envía mensajes que bloqueen | Solo las de su contrato, con aprobación humana cuando corresponda |

Todo intento de salir del perfil se bloquea, queda en el log de auditoría y se registra como defecto del propio
observador.

### 13.3 Reproducción de un hallazgo

Si un hallazgo necesita una ejecución para confirmarse (por ejemplo, un posible error numérico), el observador lo
marca como *requiere reproducción*. Una persona decide si se reproduce; en ese caso lo ejecuta **Verificación técnica**
(operativa) en su sandbox, y el resultado queda como evidencia de la confirmación o del descarte. Los valores que cite
un observador solo pueden referirse a ejecuciones ya existentes.

### 13.4 No aprueba su propia propuesta

1. La clasificación (confirmado, descartado, duplicado, diferido) la hace **una persona**, no el observador.
2. Confirmar un hallazgo exige evidencia revisada por alguien distinto del observador: la reproducción de 13.3 o la comprobación directa del artefacto.
3. El informe es **inmutable** una vez publicado (identificado por su hash). Una corrección es un informe nuevo que referencia al anterior.
4. Un observador no confirma, cierra ni prioriza hallazgos propios ni de otros observadores.
5. Sus hallazgos no detienen el pipeline ni cuentan como la revisión cruzada de una compuerta (Constitución, Art. 27). Sí se exige que **una persona clasifique** todo hallazgo con severidad sugerida S1 o S2 antes de cerrar el release.

### 13.5 Cómo se mide su utilidad

La utilidad de un observador se mide por los **defectos reales** que detecta, no por la cantidad de informes o
hallazgos que emite.

| Métrica | Definición | Uso |
|---|---|---|
| **Defectos reales detectados** | Hallazgos confirmados como defectos y registrados con un ID de defecto, por severidad | **Métrica principal** |
| Defectos críticos detectados primero | Defectos S1/S2 confirmados que el observador reportó antes de que los encontraran QA, otro agente o una persona | Valor diferencial |
| Precisión | Confirmados ÷ (confirmados + descartados) | Costo de triaje que impone |
| Defectos escapados | Defectos reales de su especialidad encontrados después por otros, que el observador no reportó | Cobertura |

**No cuentan como utilidad:** número de informes, número de hallazgos, extensión de los informes, hallazgos pendientes
o descartados.

**Consecuencias:**

- Al cerrar cada release, el informe de observadores presenta estas métricas por agente.
- Un observador sin defectos reales confirmados en todo el release y con baja precisión se reajusta (instrucciones, alcance o presupuesto) por decisión del responsable técnico. Los umbrales se fijan con los datos de R0.
- Solo los defectos **confirmados** cuentan como evidencia para su promoción en el ciclo de vida (Brief de Agentes v1.2 §9).

Registro: `01_Releases/Rn_*/06_Feedback/observadores.md`.

### 13.6 Transición

Cuando un agente pasa a operativo en un release, deja de observar ese tramo del pipeline y su contrato operativo pasa
por el ciclo de vida normal. Sus métricas de utilidad como observador forman parte de su evidencia para salir del
estado Experimental.

## 14. Decisiones pendientes

- Umbrales finales de cobertura y de mutación por tipo de programa.
- Esquemas JSON de SPEC, THEORY y manifiesto. Los de contrato y mensaje de agente ya existen en `02_Agentes/contratos/schemas/`.
- Primer programa T1 piloto de G0 y su caso dorado.
- Presupuesto de los observadores por release.
- Esquemas de SPEC.md y THEORY.md (elementos 29 y 30 del inventario).
- Proveedor de CI para pipelines con sandbox (GitHub Actions u otro con ejecutores propios).
