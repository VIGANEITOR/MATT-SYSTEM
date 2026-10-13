# Pendientes de MATTX

Revisión: 13-oct-2026. Se marca ✅ solo lo verificado. Cada pendiente indica quién lo cierra y dónde queda la evidencia.

## A. Repositorio e infraestructura

| # | Paso | Estado | Quién | Cómo / evidencia |
|---|---|---|---|---|
| A1 | Iniciar git, commit inicial, remoto y subida a `VIGANEITOR/MATT-SYSTEM` | ✅ Verificado | — | `main` local = `origin/main` |
| A2 | Excepción `safe.directory` para el USB (FAT32) | ✅ Hecho (registrada 5 veces; no afecta) | — | `git config --global --get-all safe.directory` |
| A3 | Decidir la visibilidad del repositorio. Hoy es **privado**; GitHub Pages en repos privados requiere plan de pago | ⬜ | Producto | Antes de hacerlo público: A10, B6, ADR-008 y revisar que no haya datos sensibles (Constitución, Art. 39) |
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
| B3 | Revisar y aprobar el Brief Maestro v1.2 y el Brief de Implementación v2.0 (redactados con IA) | ⬜ | B1 | Constitución, Art. 22 |
| B4 | Designar especialistas por dominio y revisores independientes | ⬜ | Responsable científico | Constitución, Art. 37 |
| B5 | Reemplazar la reconstrucción del Brief Maestro v1.0 por el original, si existe | ⬜ | Autor | `00_Especificacion/Brief_Maestro/v1.0/` |
| B6 | Buscar antecedentes de la marca "MATTX" en INDECOPI | ⬜ | Producto + legal | Brief Maestro §11.4 y §15.1 |

## C. Coherencia entre documentos (detectada en esta revisión)

| # | Hallazgo | Propuesta |
|---|---|---|
| C1 | El **agente de Documentación científica** está en el catálogo del Brief Maestro (§7.2, R1) y lo usa el paso 8 del flujo R1, pero **no figura** entre los 17 agentes del Brief de Agentes | Agregarlo en un Brief de Agentes v1.1 |
| C2 | El Brief Maestro §7.2 dice que los 5 roles de diseño son "roles del equipo, no agentes del producto"; el Brief de Agentes los define como agentes (grupo B) | Decidir en un ADR: agentes de la fábrica para programas T3, o roles humanos |
| C3 | El Brief Maestro llama "Desarrollo científico" y "Verificación" a los agentes que el Brief de Agentes llama "Desarrollo/automatización" y "Verificación técnica" | Unificar nombres en Agentes v1.1 |
| C4 | El Brief de Agentes cita el "Brief v1.1 §7.1"; la versión vigente es la v1.2 y la ficha del agente de Investigación no recoge "conocimiento sin fronteras" (DOI, país, nivel de evidencia, RF-15/16) | Actualizar en Agentes v1.1 |
| C5 | El contrato de ejemplo `hidraulica.drenaje_pluvial@1.0.0.json` referencia `schemas/drenaje_input.json` y `schemas/drenaje_output.json`, que no existen | Crearlos junto con D5 |
| C6 | La matriz normativa internacional del Brief Maestro v1.2 §3.3.1 se redactó con asistencia de IA | Verificar nombre, edición y vigencia de cada norma antes de R1 (D9) |

## D. Antes de R0

| # | Paso | Quién | Referencia |
|---|---|---|---|
| D1 | ADR-001 Orquestación | Responsable técnico | [ADR-001](00_Especificacion/ADR/ADR-001-orquestacion.md) |
| D2 | ADR-002 Sandbox | Responsable técnico | [ADR-002](00_Especificacion/ADR/ADR-002-sandbox.md) |
| D3 | ADR-003 Proveedores de IA, incluido si los verificadores usan un modelo distinto al de los autores | Producto + técnico | [ADR-003](00_Especificacion/ADR/ADR-003-proveedores-ia.md); Agentes §9.3 |
| D4 | ADR-004 Almacenamiento | Responsable técnico | [ADR-004](00_Especificacion/ADR/ADR-004-almacenamiento.md) |
| D5 | Esquemas JSON: contrato de agente, mensaje entre agentes, SPEC, THEORY, manifiesto | Responsable técnico | Brief de Implementación §12 |
| D6 | Presupuestos iniciales por agente y por tipo de programa | Producto + técnico | Agentes §9.3 |
| D7 | Programa T1 piloto de G0 y su caso dorado | Responsable científico | Brief de Implementación §10 |
| D8 | Umbrales de cobertura y mutación por tipo de programa; proveedor de CI con sandbox | Responsable técnico | Brief de Implementación §12 |

## E. Antes de R1

| # | Paso | Quién | Referencia |
|---|---|---|---|
| E1 | ADR-005 Frontend, ADR-007 Despliegue, ADR-008 Licencia (hoy rige MIT de forma provisional) | Según ADR | [ADR](00_Especificacion/ADR/README.md) |
| E2 | ADR-006: caso dorado local de drenaje (estudio firmado con datos completos) y su revisor independiente | Responsable científico | Brief Maestro §14.3 |
| E3 | Investigación UX: 8–12 entrevistas por persona, observación en gabinete y obra, línea base de tiempos, prueba de patrones de confianza con 5 usuarios | Producto | Brief Maestro §2.2 |
| E4 | Verificar edición vigente de cada norma N1 y N2 de la matriz (C6) | Investigación + especialista | Brief Maestro §3.3.1 |
| E5 | Prueba de penetración | Seguridad | Brief Maestro §13.1 |
| E6 | Design system v1 en Storybook | Diseño | Brief Maestro §11.3 |
