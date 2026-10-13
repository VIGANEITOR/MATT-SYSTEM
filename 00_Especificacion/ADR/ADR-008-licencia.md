# ADR-008 — Propiedad intelectual y licencia

- **Estado**: Propuesto — pendiente de decisión y firma
- **Responsable**: Producto + legal
- **Fecha límite**: Antes de R1 (y antes de hacer público el repositorio)
- **Aprobado por**: _(nombre, rol, fecha)_
- **Revisión legal**: _(sí / no; quién)_

## Contexto

- Brief Maestro v1.1 §15.2 pide decidir entre licencia propietaria, abierta o mixta.
- El repositorio `VIGANEITOR/MATT-SYSTEM` se creó en GitHub con licencia **MIT** (archivo `LICENSE`,
  titular "VIGANEITOR"), que rige de forma provisional (Constitución, Disposición transitoria segunda).
- El repositorio contiene tres tipos de contenido distintos: **código**, **documentación y diagramas** y, más
  adelante, **datos** (casos dorados, datasets). La licencia MIT está pensada para código.
- MATTX dependerá de software de terceros, cada uno con su propia licencia, que ninguna licencia de MATTX puede
  cambiar.
- La búsqueda de antecedentes de la marca "MATTX" en INDECOPI no encontró registros (búsqueda informada por el autor,
  13-oct-2026). Una licencia de código no protege la marca.

## Opciones

| | Opción | Permite | Ventajas | Desventajas |
|---|---|---|---|---|
| **A** | **MIT** para el código + **CC BY 4.0** para documentación, diagramas y datos propios | Cualquiera usa, modifica y vende, citando la autoría | Ya está en el repositorio; máxima adopción académica y profesional; compatible con casi todas las dependencias | Un tercero puede crear un servicio comercial cerrado con el código; no incluye concesión expresa de patentes |
| B | **Apache-2.0** para el código + CC BY 4.0 para documentación y datos | Lo mismo que A | Concesión expresa de patentes; excluye de forma explícita el uso de la marca | Algo más compleja (archivo NOTICE); cambiar desde MIT es sencillo ahora y difícil después |
| C | **AGPL-3.0** para el código + CC BY-SA 4.0 para documentación | Uso libre, pero quien ofrezca MATTX modificado como servicio debe publicar su código | Impide forks comerciales cerrados en la nube | Frena la adopción en consultoras y entidades; complica la integración con software comercial |
| D | **Propietaria** (todos los derechos reservados) | Solo lo que el titular autorice | Control total y modelo de negocio de licencias | Contradice la reproducibilidad pública y la verificación por terceros (Constitución, Arts. 6 y 38); el repositorio debería seguir privado |

## Restricciones de terceros (no dependen de la opción elegida)

| Componente previsto | Licencia | Consecuencia para MATTX |
|---|---|---|
| **OpenSees / OpenSeesPy** (estructural, R2) | Licencia de la Universidad de California: uso libre para educación, investigación y fines no comerciales, y uso interno para otras entidades | Una **aplicación o servicio en la nube** que use OpenSeesPy requiere una **licencia comercial de UC Berkeley**. Decidir antes de R2: obtener esa licencia, ofrecerlo solo como adaptador que el usuario instala, o usar otro motor |
| ODA (lectura de DWG, R3) | Propietaria | Dependencia de licencia ya prevista en el Brief Maestro §6 |
| ETABS, SAP2000, HEC-RAS por adaptador | Propietarias o de uso según el proveedor | Solo con licencia del usuario (Brief Maestro §3.2) |
| PostGIS | GPL-2.0 | Se usa como servidor; no obliga a cambiar la licencia de MATTX mientras no se distribuya modificado dentro de MATTX |
| Resto del stack previsto (SWMM, pyswmm, WNTR, geopandas, pyproj, rasterio, SALib, Pint, NumPy, SciPy, SymPy, React, MapLibre, Potree, Temporal, gVisor, Firecracker) | Permisivas o de dominio público, según sus proyectos | Compatibles con A, B y C. **Verificar cada una con una herramienta de inventario de licencias antes de R0** |
| Normas técnicas (RNE, ASTM, ISO, Eurocódigos, AASHTO…) | Derechos de sus emisores | Se citan con código, edición y artículo; **no se copia su texto** en el repositorio |
| Datos de terceros (SENAMHI, NOAA, Copernicus…) | La licencia de cada productor | Se registran con su licencia (Brief Maestro §3.3.3); CC BY 4.0 solo aplica a datos propios |

## Recomendación

**Opción A**, porque ya rige, maximiza la reproducibilidad y la verificación por terceros, y separa
correctamente código, documentación y datos. Elegir C solo si el objetivo es impedir servicios comerciales cerrados
basados en MATTX; elegir D solo si el repositorio va a seguir privado.

## Consecuencias si se acepta la opción A

1. Se mantiene `LICENSE` (MIT) para el código. Decidir si el titular es "VIGANEITOR", el nombre completo del autor o una
   entidad.
2. Se agrega `LICENSE-docs` (CC BY 4.0) y una sección "Licencias" en el README que indique qué licencia aplica a cada
   carpeta.
3. Cada programa de `08_Programas/` lleva su `LICENSE` y su `CITATION.cff`.
4. Se agrega al CI un inventario de licencias de dependencias que bloquee licencias no aprobadas.
5. La marca "MATTX" queda fuera de la licencia; se recomienda registrarla en INDECOPI (clases 9 y 42 como mínimo).
6. Se actualiza la Disposición transitoria segunda de la Constitución y se registra en el CHANGELOG.

## Decisión

_Pendiente._
