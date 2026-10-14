# MATTX — Brief de Implementación v2.2

La fábrica de programas científicos · Oct 14, 2026 · @Chris

## 0. Control del documento

| Campo | Definición |
|---|---|
| Producto | MATTX |
| Documento | Brief de Implementación: cómo se construye MATTX y cómo MATTX construye programas científicos |
| Versión | 2.2 (reemplaza a 2.1 del 13-oct-2026) |
| Vigencia | Toda versión anterior queda superada por esta y se conserva solo como historial |
| Estado | Borrador. Incorpora la solicitud del autor del 14-oct-2026 (≥ 50 % desde R0 y modo observador). Redactado con asistencia de IA; pendiente de aprobación |
| Rige sobre | Tipos de programa (T1–T5), compuertas (G-SPEC … G-RELEASE, G-DOC), plantilla de programa, flujo Git, CI/CD y fases de la fábrica (G0–G3) |
| Subordinado a | [Constitución de MATTX](../../../CONSTITUCION.md), [Brief Maestro v1.5](../../Brief_Maestro/v1.5/MATTX_Brief_Maestro_v1.5.md) |
| Agentes | [Brief de Agentes v1.1](../../Brief_Agentes/v1.1/MATTX_Brief_Agentes_v1.1.md) |
| Aprobadores | Pendiente: responsable técnico, responsable científico |

**Cambios respecto a v2.1**

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
| **G0 — Arranque** | R0 | Fábrica con al menos el 50 % de este brief operativo (§12); un programa T1 piloto recorre las compuertas de núcleo; 14 agentes en modo observador (§13) | Programa T1 liberado; ≥ 23/45 elementos operativos con evidencia, incluidos los 19 de núcleo; tiempo idea → T1 medido como línea base; informe de observadores |
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

**Solicitud del autor (14-oct-2026):** implementar **al menos el 50 %** de este brief desde R0 (solicitud de cambio
[SC-001](../../../01_Releases/R0_Esqueleto/01_Alcance/SC-001_fabrica_minima_y_observadores.md)).

### 12.1 Cómo se mide

El brief se descompone en **45 elementos implementables**. Un elemento cuenta como **operativo** solo si funciona en
R0 con evidencia en `01_Releases/R0_Esqueleto/04_Verificacion_QA/`; estar documentado no basta (Constitución, Art. 13).

| Clase en R0 | Elementos | Acumulado | Significado |
|---|---|---|---|
| **Núcleo** | 19 | 19 (42 %) | Obligatorios para cerrar R0: sin ellos R1 no tiene punto de partida (Brief Maestro §3.5) |
| Must | 9 | 28 (62 %) | Comprometidos para R0 |
| Should | 4 | 32 (71 %) | Se hacen si el núcleo y los Must están asegurados |
| Releases posteriores | 13 | — | Sus agentes trabajan en R0 como **observadores** (§13) |

**Criterio de salida de R0 para este brief:** al menos **23 de 45 elementos (50 %) operativos con evidencia,
incluidos los 19 de núcleo**. Objetivo planificado: 28 (62 %). Este criterio se fija antes de iniciar
R0 y no se relaja durante el release (Brief Maestro §3.6, regla 3).

### 12.2 Inventario

| # | Sección | Elemento | En R0 | Agente(s) | Evidencia de "operativo" |
|---|---|---|---|---|---|
| 1 | §2 Tipos | T1 — Cálculo | **Núcleo** | Desarrollo científico | Programa T1 piloto liberado |
| 2 | §2 Tipos | T2 — Biblioteca de métodos | Should | Desarrollo científico | Primer método T2 liberado y reutilizado por el T1 |
| 3 | §2 Tipos | T3 — Aplicación con interfaz | R1 | Grupo B (observan en R0) | — |
| 4 | §2 Tipos | T4 — Flujo integrado | R1 | Especialista de dominio (observa en R0) | — |
| 5 | §2 Tipos | T5 — Experimento publicable | R2 | Incertidumbre (observa en R0) | — |
| 6 | §3 Pipeline | Etapa 1 — Solicitud estructurada | Must | Análisis | Solicitud del T1 registrada |
| 7 | §3 Pipeline | Etapa 2 — Estado del arte | Should | Investigación | Matriz de fuentes del T1 obtenida por red controlada (OpenAlex/Crossref) |
| 8 | §3 Pipeline | Etapa 3 — Especificación (SPEC.md) | **Núcleo** | Planificación | SPEC del T1 aprobado en G-SPEC |
| 9 | §3 Pipeline | Etapa 4 — Teoría (THEORY.md) | Must | Formulación científica | THEORY del T1 aprobado en G-THEORY |
| 10 | §3 Pipeline | Etapa 5 — Método numérico (NUMERICS.md) | Must | Métodos numéricos | NUMERICS del T1 con criterio de convergencia |
| 11 | §3 Pipeline | Etapa 6 — Arquitectura | R1 | Diseño técnico (observa en R0) | — |
| 12 | §3 Pipeline | Etapa 7 — Implementación | **Núcleo** | Desarrollo científico | Pull request del T1 aprobado en G-CODE |
| 13 | §3 Pipeline | Etapa 8 — Verificación y validación | **Núcleo** | Verificación técnica | Informe V&V del T1 |
| 14 | §3 Pipeline | Etapa 9 — Interfaz | R1 | Grupo B (observan en R0) | — |
| 15 | §3 Pipeline | Etapa 10 — Documentación | R1 | Documentación científica (observa en R0) | — |
| 16 | §3 Pipeline | Etapa 10b — Empaquetado | **Núcleo** | Despliegue | Imagen con digest, manifiesto y CITATION.cff del T1 |
| 17 | §3 Pipeline | Etapa 11 — Aprobación humana | **Núcleo** | Persona autorizada | Aprobación nominal registrada |
| 18 | §3 Pipeline | Etapa 12 — Aprendizaje | R2 | Aprendizaje (observa en R0) | — |
| 19 | §4 Compuertas | G-SPEC | **Núcleo** | Planificación + persona | Lista de verificación aplicada al T1 |
| 20 | §4 Compuertas | G-THEORY | Must | Formulación + especialista | Lista de verificación aplicada al T1 |
| 21 | §4 Compuertas | G-CODE | **Núcleo** | Revisor humano | Lista de verificación aplicada al T1 |
| 22 | §4 Compuertas | G-VERIFY | **Núcleo** | Verificación técnica + responsable científico | Lista de verificación aplicada al T1 |
| 23 | §4 Compuertas | G-UI | R1 | QA Visual (observa en R0) | — |
| 24 | §4 Compuertas | G-DOC | R1 | Documentación científica (observa en R0) | — |
| 25 | §4 Compuertas | G-RELEASE | **Núcleo** | Despliegue + responsable técnico | T1 re-ejecutado fuera de MATTX |
| 26 | §5 Registro | Registro de programas | **Núcleo** | Despliegue | T1 registrado con estado y versión |
| 27 | §5 Registro | Biblioteca de métodos | Should | Desarrollo científico | Biblioteca con el primer T2 |
| 28 | §6 Plantilla | Plantilla de programa | **Núcleo** | Planificación | T1 creado desde la plantilla |
| 29 | §6 Plantilla | Secciones obligatorias de SPEC.md (con esquema) | Must | Planificación | Esquema de SPEC validado en CI |
| 30 | §6 Plantilla | Secciones obligatorias de THEORY.md (con esquema) | Must | Formulación científica | Esquema de THEORY validado en CI |
| 31 | §7 Repositorio | Estructura del monorepo MATT-SYSTEM | **Núcleo** | — | ✅ Ya existe |
| 32 | §8 Git | Flujo de trabajo con Git (rama protegida, Conventional Commits, etiquetas) | Must | Responsable técnico | Rama main protegida; etiqueta r0.x.y |
| 33 | §9 CI | Pipeline docs | Must | — | ✅ Ya compila el sitio en cada cambio |
| 34 | §9 CI | Pipeline spec | **Núcleo** | — | ✅ Ya valida contratos y esquemas |
| 35 | §9 CI | Pipeline code | **Núcleo** | — | Lint, tipado, pruebas, SAST y secretos en cada PR |
| 36 | §9 CI | Pipeline verify | **Núcleo** | — | Casos dorados y propiedades del T1 en CI |
| 37 | §9 CI | Pipeline evals | Must | — | Evals de integridad de los 21 agentes en CI |
| 38 | §9 CI | Pipeline e2e-ui | R1 | — | — |
| 39 | §9 CI | Pipeline rep (reproducibilidad) | **Núcleo** | — | QA-REP en CI |
| 40 | §9 CI | Pipeline pages | Should | — | Sitio publicado (requiere activar Pages) |
| 41 | §10 Fases | G0 — Arranque | **Núcleo** | Todos | Criterio de salida de G0 cumplido |
| 42 | §10 Fases | G1 — Primer dominio | R1 | — | — |
| 43 | §10 Fases | G2 — Multidominio | R2 | — | — |
| 44 | §10 Fases | G3 — Escala | R3 | — | — |
| 45 | §11 Terminado | Definición de terminado | **Núcleo** | Todos | Aplicada a cada artefacto de R0 |

### 12.3 Agentes en R0

| Modo | Agentes | Cantidad |
|---|---|---|
| **Operativos** | Análisis, Planificación, Formulación científica, Métodos numéricos, Desarrollo científico, Verificación técnica, Despliegue | 7 |
| **Observadores** | Investigación (pasa a operativo si se cumple su Should), Diseño técnico, Aprendizaje, los cinco del grupo B, Incertidumbre y experimentación, Decisión multicriterio, Geomática y BIM, Especialista de dominio, Documentación científica, Forja | 14 |

La asignación vigente está en `02_Agentes/asignaciones/R0.json` y el CI comprueba que cubre los 21 agentes base, sin
repetir ninguno.

**Riesgo:** R0 crece respecto al Brief Maestro v1.4: 9 elementos más y contratos y evals de integridad para 21 agentes,
no para 5. **Mitigación:** los observadores comparten una suite común de evals de integridad y un presupuesto
acotado; si el núcleo está en riesgo, se sacrifican primero los Should.

## 13. Modo observador

**Solicitud del autor (14-oct-2026):** los agentes que aún no interactúan en un release actúan como **observadores** y
analizan posibles errores; sus hallazgos sirven para la versión siguiente.

### 13.1 Qué hace un observador

Recibe copia de solo lectura de los artefactos publicados que corresponden a su especialidad y emite un **informe de
observación** con posibles errores, riesgos, brechas, inconsistencias normativas y mejoras. Por ejemplo: Documentación
científica revisa si los resultados del T1 piloto bastarían para redactar una memoria trazable; QA Visual revisa la UI
mínima; Investigación revisa si las referencias de THEORY.md son verificables.

### 13.2 Límites (no negociables)

| Regla | Detalle |
|---|---|
| Solo lectura | Lee los artefactos por su hash; no modifica artefactos, estados ni compuertas |
| Escritura | Solo en `observaciones/<agent_id>/` |
| Red | Denegada |
| No bloquea ni aprueba | Sus hallazgos son propuestas; no detienen el pipeline ni cuentan como la revisión cruzada de una compuerta (Constitución, Art. 27) |
| Números | Si afirma un error numérico, lo respalda con una ejecución propia en un sandbox P0 aislado, que nunca alimenta los resultados del proyecto |
| Permisos | El orquestador aplica el perfil `observador`, que **reemplaza** los permisos del contrato y nunca los amplía |
| Presupuesto | Acotado por release; el gasto de los observadores se contabiliza aparte |
| Requisitos | Contrato válido y 100 % en la suite común de evals de integridad (no inventar números ni citas, resistir inyección) |

### 13.3 Destino de los hallazgos

1. Cada informe valida contra `observation_report.schema.json`. El esquema no admite campos de decisión ni de aprobación.
2. Cada hallazgo entra al registro de feedback del release (`06_Feedback/registro.md`) y una persona lo clasifica (Brief Maestro §3.6).
3. **Un release no puede cerrarse mientras haya hallazgos con severidad sugerida S1 o S2 sin clasificar.** El observador no bloquea por sí mismo: lo que se exige es que una persona revise esos hallazgos.
4. El informe de cierre incluye un **informe de observadores** con hallazgos confirmados, descartados y diferidos, que alimenta el alcance del release siguiente.
5. La precisión de cada observador (hallazgos confirmados sobre emitidos) se mide y sirve como evidencia para su promoción en el ciclo de vida (Brief de Agentes v1.1 §9) y para calibrar sus instrucciones. Un observador con muchos falsos positivos se ajusta antes de pasar a operativo.

### 13.4 Transición

Cuando un agente pasa a operativo en un release, deja de observar ese tramo del pipeline y su contrato operativo pasa
por el ciclo de vida normal. La experiencia acumulada como observador (informes, precisión) forma parte de su
evidencia para salir del estado Experimental.

## 14. Decisiones pendientes

- Umbrales finales de cobertura y de mutación por tipo de programa.
- Esquemas JSON de SPEC, THEORY y manifiesto. Los de contrato y mensaje de agente ya existen en `02_Agentes/contratos/schemas/`.
- Primer programa T1 piloto de G0 y su caso dorado.
- Presupuesto de los observadores por release.
- Esquemas de SPEC.md y THEORY.md (elementos 29 y 30 del inventario).
- Proveedor de CI para pipelines con sandbox (GitHub Actions u otro con ejecutores propios).
