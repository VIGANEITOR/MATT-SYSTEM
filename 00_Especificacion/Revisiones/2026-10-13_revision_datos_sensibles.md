# Revisión de datos sensibles — 13-oct-2026

Objetivo: comprobar que el repositorio no contiene información que la Constitución (Art. 39) prohíbe publicar, antes
de decidir su visibilidad (PENDIENTES.md, A3).

**Alcance:** los 99 archivos versionados en `main` (commit `44fbc62`) y **todas las versiones de cada archivo en los
4 commits del historial**. Lo que está en el historial sigue visible aunque se borre después, por eso se revisó también.

**Método:** búsqueda automática con expresiones regulares (`git grep` sobre todas las revisiones), inspección de las
partes internas de los `.docx` y de los metadatos de las imágenes PNG, y revisión de las identidades de los commits.
Revisión asistida por IA.

## Resultados

| Verificación | Resultado |
|---|---|
| Claves, tokens y credenciales (GitHub, AWS, OpenAI, Slack, claves privadas PEM, "password/token/secret =") | ✅ Ninguno. Única coincidencia: `id-token: write`, un permiso del flujo de GitHub Pages, no un secreto |
| Correos electrónicos | ✅ Ninguno real. Coincidencias: `dominio.nombre@MAYOR.MENOR.PARCHE` y `hidraulica.drenaje_pluvial@1.0.0.json` (formatos de versión) |
| DNI (8 dígitos), RUC (11 dígitos), teléfonos móviles | ✅ Ninguno |
| Rutas locales del equipo o nombre de usuario de Windows | ✅ Ninguna |
| Identidades de commit | ✅ Solo correos `noreply` de GitHub (`VIGANEITOR@users.noreply.github.com` y el del commit inicial de GitHub) |
| `.docx`: autor, comentarios, cambios controlados, texto oculto, enlaces externos | ✅ Metadatos solo con título y "Claude Docs"; sin comentarios, sin cambios controlados, sin texto oculto, sin enlaces externos |
| Imágenes PNG: metadatos de texto o EXIF | ✅ Ninguno |
| Contratos, expedientes, planos, estudios de clientes, datos de obra | ✅ Ninguno. Las carpetas de casos dorados y de investigación UX están vacías |
| Datos personales | Solo el nombre de autor "Chris (Ingeniero civil-sanitario)", incluido a propósito como autoría |

## Conclusión

No se encontraron datos sensibles. El repositorio puede hacerse público en lo que a este punto respecta.

## Controles para que siga así

1. `.gitignore` ya bloquea `.env`, claves (`*.pem`, `*.key`) y carpetas `privado/` y `confidencial/`.
2. Activar *Secret scanning* y *Push protection* en GitHub (PENDIENTES.md, A7).
3. Antes de subir un caso dorado o un dataset: confirmar que su licencia permite publicarlo y que no identifica a
   personas ni contiene información reservada del cliente o de la entidad.
4. Repetir esta revisión antes de cada release.
