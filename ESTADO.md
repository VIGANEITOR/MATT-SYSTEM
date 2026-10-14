# Estado de MATTX

> **Archivo generado** por `00_Especificacion/registro/generar.py` a partir del registro único (`estado_componentes.json`, actualizado el 2026-10-14). No editar a mano.

Es la **única** fuente pública del estado real de cada componente (Constitución, Art. 13). Los briefs especifican; no declaran estados.

Estados: Planificado · En desarrollo · Probado (con evidencia local o de pruebas) · Operativo (en uso, con evidencia) · Degradado · No disponible.

## Plataforma

Planificado: 23

| ID | Componente | Release | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|
| PLA-01 | Usuarios y roles | R0 | Crítica | Planificado | — |
| PLA-02 | Proyectos con jurisdicción y CRS | R0 | Alta | Planificado | — |
| PLA-03 | Registro de experimentos con pregunta e hipótesis | R0 | Alta | Planificado | — |
| PLA-04 | Orquestador con máquina de estados | R0 | Crítica | Planificado | — |
| PLA-05 | Sandbox sin red | R0 | Crítica | Planificado | — |
| PLA-06 | Sandbox con red controlada mediante proxy de salida | R0 | Crítica | Planificado | — |
| PLA-07 | Almacenamiento de artefactos direccionado por hash | R0 | Crítica | Planificado | — |
| PLA-08 | Procedencia básica (W3C PROV) | R0 | Crítica | Planificado | — |
| PLA-09 | Log de auditoría inmutable | R0 | Crítica | Planificado | — |
| PLA-10 | Aislamiento de credenciales | R0 | Crítica | Planificado | — |
| PLA-11 | Registro de agentes y contratos con permisos en 4 dimensiones | R0 | Alta | Planificado | — |
| PLA-12 | UI mínima | R0 | Media | Planificado | — |
| PLA-13 | Patrones de confianza en la UI | R1 | Alta | Planificado | — |
| PLA-14 | Design system v1 en Storybook | R1 | Media | Planificado | — |
| PLA-15 | Bandeja de revisión y aprobación | R1 | Alta | Planificado | — |
| PLA-16 | Exportación de paquete reproducible del proyecto | R1 | Crítica | Planificado | — |
| PLA-17 | Procedimiento de incorporación de dominios y áreas | R2 | Alta | Planificado | — |
| PLA-18 | Acoplamiento entre flujos con procedencia | R2 | Alta | Planificado | — |
| PLA-19 | Adaptadores de formatos abiertos (IFC, LandXML, GeoTIFF, GeoPackage) | R3 | Alta | Planificado | — |
| PLA-20 | Ingesta de topografía y nubes de puntos | R3 | Media | Planificado | — |
| PLA-21 | Paquete de proyecto cifrado | R3 | Alta | Planificado | — |
| PLA-22 | Matriz de conectores con estado real | R3 | Alta | Planificado | — |
| PLA-23 | Registro de extensiones | R4+ | Media | Planificado | — |

## Fábrica

Planificado: 43 · Operativo: 1 · Probado: 2

| ID | Componente | Release | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|
| PRG-01 | Motor propio: solucionador de redes de drenaje (T2) | R3 | Alta | Planificado | — |
| FAB-01 | T1 — Cálculo | R0 | Crítica | Planificado | — |
| FAB-02 | T2 — Biblioteca de métodos | R0 | Media | Planificado | — |
| FAB-03 | T3 — Aplicación con interfaz | R1 | Media | Planificado | — |
| FAB-04 | T4 — Flujo integrado | R1 | Alta | Planificado | — |
| FAB-05 | T5 — Experimento publicable | R2 | Media | Planificado | — |
| FAB-06 | Etapa 1 — Solicitud estructurada | R0 | Alta | Planificado | — |
| FAB-07 | Etapa 2 — Estado del arte | R0 | Alta | Planificado | — |
| FAB-08 | Etapa 3 — Especificación (SPEC.md) | R0 | Crítica | Planificado | — |
| FAB-09 | Etapa 4 — Teoría (THEORY.md) | R0 | Alta | Planificado | — |
| FAB-10 | Etapa 5 — Método numérico (NUMERICS.md) | R0 | Alta | Planificado | — |
| FAB-11 | Etapa 6 — Arquitectura | R1 | Media | Planificado | — |
| FAB-12 | Etapa 7 — Implementación | R0 | Crítica | Planificado | — |
| FAB-13 | Etapa 8 — Verificación y validación | R0 | Crítica | Planificado | — |
| FAB-14 | Etapa 9 — Interfaz | R1 | Media | Planificado | — |
| FAB-15 | Etapa 10 — Documentación | R1 | Alta | Planificado | — |
| FAB-16 | Etapa 10b — Empaquetado | R0 | Crítica | Planificado | — |
| FAB-17 | Etapa 11 — Aprobación humana | R0 | Crítica | Planificado | — |
| FAB-18 | Etapa 12 — Aprendizaje | R2 | Baja | Planificado | — |
| FAB-19 | G-SPEC | R0 | Crítica | Planificado | — |
| FAB-20 | G-THEORY | R0 | Alta | Planificado | — |
| FAB-21 | G-CODE | R0 | Crítica | Planificado | — |
| FAB-22 | G-VERIFY | R0 | Crítica | Planificado | — |
| FAB-23 | G-UI | R1 | Media | Planificado | — |
| FAB-24 | G-DOC | R1 | Alta | Planificado | — |
| FAB-25 | G-RELEASE | R0 | Crítica | Planificado | — |
| FAB-26 | Registro de programas | R0 | Crítica | Planificado | — |
| FAB-27 | Biblioteca de métodos | R0 | Media | Planificado | — |
| FAB-28 | Plantilla de programa | R0 | Alta | Planificado | — |
| FAB-29 | Secciones obligatorias de SPEC.md (con esquema) | R0 | Media | Planificado | — |
| FAB-30 | Secciones obligatorias de THEORY.md (con esquema) | R0 | Media | Planificado | — |
| FAB-31 | Estructura del monorepo MATT-SYSTEM | R0 | Baja | Operativo | Estructura publicada en el repositorio (README.md, carpetas 00–08) |
| FAB-32 | Flujo de trabajo con Git (rama protegida, Conventional Commits, etiquetas) | R0 | Alta | Planificado | — |
| FAB-33 | Pipeline docs | R0 | Baja | Probado | mkdocs build --strict sin advertencias en local (14-oct-2026); ejecución en GitHub Actions no verificada |
| FAB-34 | Pipeline spec | R0 | Alta | Probado | 02_Agentes/validar_contratos.py y pruebas_contratos.py en verde en local (14-oct-2026); ejecución en GitHub Actions no verificada |
| FAB-35 | Pipeline code | R0 | Crítica | Planificado | — |
| FAB-36 | Pipeline verify | R0 | Crítica | Planificado | — |
| FAB-37 | Pipeline evals | R0 | Crítica | Planificado | — |
| FAB-38 | Pipeline e2e-ui | R1 | Media | Planificado | — |
| FAB-39 | Pipeline rep (reproducibilidad) | R0 | Crítica | Planificado | — |
| FAB-40 | Pipeline pages | R0 | Baja | Planificado | — |
| FAB-41 | G0 — Arranque | R0 | Alta | Planificado | — |
| FAB-42 | G1 — Primer dominio | R1 | Alta | Planificado | — |
| FAB-43 | G2 — Multidominio | R2 | Alta | Planificado | — |
| FAB-44 | G3 — Escala | R3 | Alta | Planificado | — |
| FAB-45 | Definición de terminado | R0 | Alta | Planificado | — |

## Avance de R0 respecto al Brief de Implementación

| Indicador | Valor | Requisito para cerrar R0 |
|---|---|---|
| Peso del inventario operativo | 0,5 de 89 (1 %) | ≥ 50 % |
| Elementos no compensables de R0 operativos | 0 de 10 | Todos |
| Ruta mínima (R0a) completa | No | Sí |

## Agentes

| Agente | Grupo | Release operativo | Estado en el ciclo de vida |
|---|---|---|---|
| Análisis | A | R0 | especificado |
| Investigación | A | R1 | especificado |
| Planificación | A | R0 | especificado |
| Desarrollo científico | A | R0 | especificado |
| Diseño técnico | A | R1 | especificado |
| Verificación técnica | A | R0 | especificado |
| Despliegue | A | R0 | especificado |
| Aprendizaje | A | R2 | especificado |
| Dirección de Arte Digital | B | R1 | especificado |
| Design System | B | R1 | especificado |
| UI/UX Designer | B | R1 | especificado |
| Frontend/UI Engineer | B | R1 | especificado |
| QA Visual y Accesibilidad | B | R1 | especificado |
| Formulación científica | C | R0 | especificado |
| Métodos numéricos | C | R0 | especificado |
| Incertidumbre y experimentación | C | R1 | especificado |
| Decisión multicriterio | C | R2 | especificado |
| Geomática y BIM | C | R3 | especificado |
| Especialista de dominio | C | R1 | propuesto |
| Documentación científica | C | R1 | propuesto |
| Forja de herramientas y agentes | C | R3 | especificado |

## Red controlada: lista permitida

| ID | Destino | Hosts | Uso | Requiere credencial |
|---|---|---|---|---|
| pypi | PyPI | pypi.org, files.pythonhosted.org | Paquetes de Python con versiones fijadas y escaneo de dependencias | No |
| senamhi | SENAMHI | senamhi.gob.pe | Datos hidrometeorológicos del Perú | No |
| noaa | NOAA | ncei.noaa.gov | Datos climáticos y meteorológicos globales | No |
| copernicus | Copernicus | cds.climate.copernicus.eu, dataspace.copernicus.eu | Observación de la Tierra y reanálisis climático | Sí |
| openalex | OpenAlex | api.openalex.org | Metadatos de literatura científica | No |
| crossref | Crossref | api.crossref.org | Verificación de DOI y metadatos bibliográficos | No |

