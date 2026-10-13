# Pendientes de MATTX

Revisión: 13-oct-2026. Se marca ✅ solo lo verificado. Cada pendiente indica quién lo cierra y dónde queda la evidencia.

## A. Repositorio e infraestructura

| # | Paso | Estado | Quién | Cómo / evidencia |
|---|---|---|---|---|
| A1 | Iniciar git, commit inicial, remoto y subida a `VIGANEITOR/MATT-SYSTEM` | ✅ Verificado | — | `main` local = `origin/main` |
| A2 | Excepción `safe.directory` para el USB (FAT32) | ✅ Hecho (registrada 5 veces; no afecta) | — | `git config --global --get-all safe.directory` |
| A3 | Decidir la visibilidad del repositorio. Hoy es **privado**; GitHub Pages en repos privados requiere plan de pago | ⬜ | Producto | Antes de hacerlo público: B6 ✅, revisión de datos sensibles ✅ ([informe](00_Especificacion/Revisiones/2026-10-13_revision_datos_sensibles.md)); falta decidir ADR-008 |
| A4 | Activar Pages: *Settings → Pages → Source: GitHub Actions* | ⬜ | Dueño del repo | Requiere A3 |
| A5 | Crear la variable `PAGES_ENABLED = true` en *Settings → Secrets and variables → Actions → Variables* | ⬜ | Dueño del repo | Sin ella el flujo solo compila el sitio y no lo publica |
| A6 | Proteger `main`: PR obligatorio + CI verde (Brief de Implementación §8) | ⬜ | Responsable técnico | Con una sola persona, exigir 1 revisión bloquea los merges propios: activarla cuando haya un segundo revisor |
| A7 | Activar *Private vulnerability reporting*, *Secret scanning* y *Dependabot* en *Settings → Code security* | ⬜ | Dueño del repo | Canal privado de [SECURITY.md](SECURITY.md) (Constitución, Art. 40) |
| A8 | Pasar el USB de FAT32 a exFAT o NTFS | ⬜ | Usuario | FAT32 no admite archivos > 4 GB (RNF-04 pide 2 GB por archivo y nubes de puntos). Formatear borra todo: respaldar y verificar la copia antes |
| A9 | `CITATION.cff` del repositorio y DOI en Zenodo | ⬜ | Producto | Requiere nombre y apellidos del autor como deben citarse, y repositorio público (A3) |
| A10 | Nombre: el producto es **MATTX** y el repositorio **MATT-SYSTEM** | ⬜ | Producto | Decidir si se mantiene la diferencia; se resuelve junto con B6 |

## B. Gobierno

| # | Paso | Estado | Quién | Referencia |
|---|---|---|---|---|
| B1 | Designar responsables de producto, técnico y científico | ⬜ | Autor | Brief Maestro §0; Brief de Agentes §9.3 |
| B2 | Ratificar la Constitución v1.0 (hoy provisional) | ⬜ | B1 | Disposición transitoria primera |
| B3 | Revisar y aprobar el Brief Maestro v1.3, el Brief de Agentes v1.1 y el Brief de Implementación v2.1 (redactados con IA) | ⬜ | B1 | Constitución, Art. 22 |
| B4 | Designar especialistas por dominio y revisores independientes | ⬜ | Responsable científico | Constitución, Art. 37 |
| B5 | Reemplazar la reconstrucción del Brief Maestro v1.0 por el original, si existe | ⬜ | Autor | `00_Especificacion/Brief_Maestro/v1.0/` |
| B6 | Buscar antecedentes de la marca "MATTX" en INDECOPI | ✅ Sin antecedentes (informado por el autor, 13-oct-2026) | Producto + legal | Guardar la constancia de la búsqueda (fecha, tipo fonética/figurativa, clases). Una búsqueda sin resultados no protege la marca: evaluar registrarla (clases 9 y 42 como mínimo) |
| B7 | Revisión de datos sensibles del repositorio y su historial | ✅ Sin hallazgos | Asistida por IA | [Informe](00_Especificacion/Revisiones/2026-10-13_revision_datos_sensibles.md); repetir antes de cada release |
| B8 | Decidir ADR-008 (licencia). Recomendado: opción A, MIT código + CC BY 4.0 documentación y datos | ⬜ | Producto (+ legal) | [ADR-008](00_Especificacion/ADR/ADR-008-licencia.md) |
| B9 | Licencia comercial de OpenSees/OpenSeesPy si MATTX se ofrece como aplicación o servicio en la nube | ⬜ antes de R2 | Producto | ADR-008, restricciones de terceros |

## C. Coherencia entre documentos

| # | Hallazgo | Estado | Resolución |
|---|---|---|---|
| C1 | Faltaba el agente de Documentación científica en el Brief de Agentes | ✅ Resuelto | Brief de Agentes v1.1 §5.2 (ficha, mecanismo, criterio de terminado, evals) y contrato `documentacion_cientifica@1.0.0` |
| C2 | Grupo B: ¿agentes o personas? | ✅ Decidido: **agentes** | Brief de Agentes v1.1 §4 y Brief Maestro v1.3 §7.2; las personas aprueban en G-UI |
| C3 | Nombres distintos entre briefs | ✅ Resuelto | Nombre de mayor especialización (Brief de Agentes v1.1 §2.1); "Incertidumbre y multicriterio" dividido; 21 agentes base |
| C4 | Referencias a versiones antiguas y regla sin fronteras | ✅ Resuelto | Toda versión anterior queda superada; Investigación con matriz nacional e internacional |
| C5 | Esquemas JSON inexistentes | ✅ Resuelto | 7 esquemas, 2 contratos, 3 ejemplos; validador y pruebas negativas en CI (`.github/workflows/spec.yml`) |
| C6 | Matriz normativa redactada con IA | 🔄 En revisión | [Documento de revisión](00_Especificacion/Revisiones/2026-10-13_verificacion_matriz_normativa.md): 95 normas; 6 corregidas en v1.3; 73 por verificar; 13 por precisar |
| C7 | Hallazgos derivados de C6 | ⬜ | Confirmar en fuente oficial: CE.040 (y la modificación del num. 21.2.1), Ley 32069 y su reglamento con modificaciones de 2026, E.030 (RM 183-2026 y su régimen transitorio). Responsable: especialista de cada dominio, antes de R1 |
| C8 | Aprobar el Brief de Agentes v1.1, el Brief Maestro v1.3 y el Brief de Implementación v2.1 | ⬜ | Redactados con asistencia de IA (B3) |

## D. Antes de R0

| # | Paso | Quién | Referencia |
|---|---|---|---|
| D1 | ADR-001 Orquestación | Responsable técnico | [ADR-001](00_Especificacion/ADR/ADR-001-orquestacion.md) |
| D2 | ADR-002 Sandbox | Responsable técnico | [ADR-002](00_Especificacion/ADR/ADR-002-sandbox.md) |
| D3 | ADR-003 Proveedores de IA, incluido si los verificadores usan un modelo distinto al de los autores | Producto + técnico | [ADR-003](00_Especificacion/ADR/ADR-003-proveedores-ia.md); Agentes §9.3 |
| D4 | ADR-004 Almacenamiento | Responsable técnico | [ADR-004](00_Especificacion/ADR/ADR-004-almacenamiento.md) |
| D5 | Esquemas JSON de SPEC, THEORY y manifiesto (contrato y mensaje de agente ya existen) | Responsable técnico | Brief de Implementación §12 |
| D6 | Presupuestos iniciales por agente y por tipo de programa | Producto + técnico | Agentes §9.3 |
| D7 | Programa T1 piloto de G0 y su caso dorado | Responsable científico | Brief de Implementación §10 |
| D8 | Umbrales de cobertura y mutación por tipo de programa; proveedor de CI con sandbox | Responsable técnico | Brief de Implementación §12 |

## E. Antes de R1

| # | Paso | Quién | Referencia |
|---|---|---|---|
| E1 | ADR-005 Frontend, ADR-007 Despliegue (ADR-008: ver B8) | Según ADR | [ADR](00_Especificacion/ADR/README.md) |
| E2 | ADR-006: caso dorado local de drenaje (estudio firmado con datos completos) y su revisor independiente | Responsable científico | Brief Maestro §14.3 |
| E3 | Investigación UX: 8–12 entrevistas por persona, observación en gabinete y obra, línea base de tiempos, prueba de patrones de confianza con 5 usuarios | Producto | Brief Maestro §2.2 |
| E4 | Verificar en fuente oficial cada norma N1 y N2 de la matriz (C6, C7) | Investigación + especialista | Brief Maestro §3.3.1 |
| E5 | Prueba de penetración | Seguridad | Brief Maestro §13.1 |
| E6 | Design system v1 en Storybook | Diseño | Brief Maestro §11.3 |
