# MATTX — Brief de Implementación v2.0

La fábrica de programas científicos · Oct 13, 2026 · @Chris

## 0. Control del documento

| Campo | Definición |
|---|---|
| Producto | MATTX |
| Documento | Brief de Implementación: cómo se construye MATTX y cómo MATTX construye programas científicos |
| Versión | 2.0 |
| Estado | Borrador. Redactado con asistencia de IA a partir del Brief Maestro v1.2 y el Brief de Agentes v1.0, que ya lo citaban; pendiente de revisión y aprobación humana |
| Rige sobre | Tipos de programa (T1–T5), compuertas (G-SPEC … G-RELEASE), plantilla de programa, flujo Git, CI/CD y fases de la fábrica (G0–G3) |
| Subordinado a | [Constitución de MATTX](../../../CONSTITUCION.md), Brief Maestro v1.2 |
| Aprobadores | Pendiente: responsable técnico, responsable científico |

**Numeración.** Es la primera versión registrada en el repositorio. Se numera 2.0 para mantener la referencia que ya
hace el Brief de Agentes v1.0.

**Convención normativa.** DEBE, DEBERÍA y PUEDE según el Artículo 4 de la Constitución.

## 1. Propósito

MATTX entrega dos cosas distintas, con ciclos de vida distintos:

| Producto | Qué es | Quién lo construye | Cómo se libera |
|---|---|---|---|
| **Plataforma** | Núcleo: orquestador, sandbox, procedencia, registro, interfaz (Brief Maestro §6) | Equipo de ingeniería de software | Releases R0–R4 |
| **Programas científicos** | Herramientas de cálculo, bibliotecas de métodos, aplicaciones y flujos verificados | La *fábrica*: agentes del Brief de Agentes + revisión humana | Registro de programas, versión semántica por programa |

Este brief especifica la fábrica: el camino que lleva una idea de ingeniería civil a un programa verificado,
empaquetado, citable y reproducible fuera de MATTX.

## 2. Tipos de programa

| Tipo | Qué es | Ejemplo | Compuertas obligatorias | Agentes de diseño (grupo B) |
|---|---|---|---|---|
| **T1 — Cálculo** | Script o cuaderno determinista con entradas y salidas tipadas | Caudal por método racional | G-SPEC, G-THEORY, G-CODE, G-VERIFY, G-RELEASE | No |
| **T2 — Biblioteca de métodos** | Módulo reutilizable con API estable y documentada, usado por otros programas | Curvas IDF; equilibrio límite de Bishop; AASHTO 93 | T1 + API documentada y pruebas de propiedad | No |
| **T3 — Aplicación con interfaz** | Programa T1/T2 con interfaz de usuario | Calculadora de cunetas con verificación OS.060 | T2 + G-UI | Sí, cadena completa |
| **T4 — Flujo integrado** | Orquesta varios programas, datasets y conectores de punta a punta | Flujo R1 de drenaje pluvial urbano | T3 (si tiene interfaz) + pruebas E2E del flujo y de conectores | Si tiene interfaz |
| **T5 — Experimento publicable** | Paquete de investigación con cuantificación de incertidumbre, dataset y artículo o memoria | Sensibilidad del caudal pico al cambio de uso de suelo | Todas las del tipo base + incertidumbre en G-VERIFY + revisión del responsable científico | Si tiene interfaz |

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
| 7 | Implementación | Desarrollo/automatización | Código, pruebas, pull request | **G-CODE** |
| 8 | Verificación y validación | Verificación técnica (+ Incertidumbre en T5) | Informe V&V | **G-VERIFY** |
| 9 | Interfaz (T3+) | Dirección de Arte → Design System → UI/UX → Frontend → QA Visual | Interfaz implementada e informe de aceptación | **G-UI** |
| 10 | Empaquetado | Despliegue | Imagen con digest, manifiesto, `CITATION.cff`, versión | **G-RELEASE** |
| 11 | Aprobación | Persona con rol autorizado | Aprobación nominal registrada | — |
| 12 | Aprendizaje | Aprendizaje | Lecciones propuestas | Aprobación humana |

Cada etapa termina cuando su artefacto se publica con hash; la siguiente parte de ese artefacto, no de un resumen
(Brief de Agentes §6.2). Una compuerta fallida devuelve el trabajo a la etapa que la produjo, con el informe de
defectos.

## 4. Compuertas

Cada compuerta es una lista de verificación ejecutada por CI y por un verificador distinto del autor. Ninguna se
aprueba por declaración.

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

Aprueba: revisor de código distinto del autor.

### G-VERIFY — Verificación y validación

- [ ] Casos dorados dentro de la tolerancia declarada.
- [ ] Balances (masa, energía, continuidad) y chequeos dimensionales.
- [ ] Pruebas de propiedad (hypothesis) y de mutación (mutmut) con puntuación de mutación ≥ 80 % en el núcleo.
- [ ] Validación contra datos medidos cuando existan, reportada por separado de la verificación.
- [ ] T5: incertidumbre con semilla registrada y tamaño de muestra justificado por convergencia del estimador.
- [ ] 0 defectos S1/S2 abiertos.

Aprueba: agente de Verificación técnica emite el informe; lo acepta el responsable científico.

### G-UI — Interfaz (T3 en adelante)

- [ ] Cada requisito del SPEC tiene una pantalla o interacción que lo cubre.
- [ ] Insignia de procedencia en todo valor calculado; "¿De dónde sale este número?" operativo.
- [ ] Solo componentes del design system; el cliente no recalcula lo que calcula el núcleo.
- [ ] Pruebas E2E verdes; WCAG 2.2 AA con 0 violaciones críticas de axe-core.

Aprueba: QA Visual y Accesibilidad + responsable de producto.

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
| `spec` | Validación de SPEC, THEORY y contratos de agente contra esquema | Cada pull request | Sí |
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
| **G0 — Arranque** | R0 | Fábrica asistida manualmente; un programa T1 piloto (método racional) recorre todas las compuertas | Programa T1 liberado; tiempo idea → T1 medido como línea base |
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

## 12. Decisiones pendientes

- Umbrales finales de cobertura y de mutación por tipo de programa.
- Esquemas JSON de SPEC, THEORY y manifiesto (se publicarán en `02_Agentes/contratos/schemas/`).
- Primer programa T1 piloto de G0 y su caso dorado.
- Proveedor de CI para pipelines con sandbox (GitHub Actions u otro con ejecutores propios).
