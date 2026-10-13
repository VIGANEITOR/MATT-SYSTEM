# Casos dorados

Datos de entrada fijos, resultado de referencia conocido y tolerancia declarada. Sin caso dorado aprobado,
el dominio no se libera. Las tolerancias son propuestas iniciales que el especialista DEBE confirmar.

| Carpeta | Caso propuesto | Tolerancia inicial | Release |
|---|---|---|---|
| hidraulica | Ejemplos oficiales del manual de SWMM (EPA) + caso local firmado bajo CE.040 | ±2 % caudal pico; continuidad < 1 % | R1 |
| geotecnia | Problemas resueltos de literatura de referencia | ±3 % capacidad; ±0,02 FS | R2 |
| pavimentos | Ejemplo de diseño de la guía AASHTO 93 | ±1 % número estructural | R2 |
| estructural | Pórtico de referencia con solución analítica o benchmark | ±2 % periodos; ±5 % derivas | R2 |
| construccion | Cronograma de prueba con ruta crítica conocida | Ruta crítica idéntica; ±0 días holguras | R2 |
| ahp | Ejemplo de Saaty publicado | Pesos ±0,005; RC idéntica | R2 |

Cada caso: `entradas/`, `referencia/` (resultado y fuente), `README.md` (tolerancia, revisor, estado).
