# Borrador — Brief Maestro v1.4 · Capítulo 3: Alcance, releases y áreas complementarias

| Campo | Valor |
|---|---|
| Revisión de trabajo | r1 · 13-oct-2026 |
| Base | Brief Maestro v1.3 §3 + observaciones del autor sobre la tabla 3.1 |
| Estado | Borrador en iteración. Cuando se apruebe, reemplazará el capítulo 3 en el Brief Maestro v1.4 |
| Redacción | Asistida por IA |

## Observaciones del autor que este borrador atiende

| Release | Observación | Cómo se atiende |
|---|---|---|
| R0 | Sandbox **con red y sin red** | Se agrega un perfil de red **controlada** (lista permitida, registro de conexiones y aprobación humana). La red abierta sigue prohibida (Constitución, Arts. 29 y 32) |
| R1 | El drenaje pluvial es **un ejemplo**; el alcance del flujo científico es ilimitado | R1 entrega el **ciclo científico completo para cualquier dominio**. El drenaje es el caso demostrador, y un segundo caso de otro dominio prueba que no está atado a él |
| R2 | El alcance científico es ilimitado | R2 entrega el **mecanismo para incorporar cualquier dominio o área complementaria**, y flujos acoplados entre disciplinas |
| R3 | Generar aplicaciones y software **propios**, sin fiarse de terceros | Se agrega la línea de **motores propios** y la regla de que el software de terceros es "no confiable hasta verificar" |
| R4+ | Más extensiones; el ámbito es ilimitado | Las extensiones pasan a un **registro abierto**; las de la tabla son ejemplos |
| General | Relacionarse con áreas complementarias | Nueva sección 3.2 de **áreas complementarias** |

## 3.0 Principio: alcance científico abierto, liberaciones verificables

MATTX no limita **qué** ciencia se puede hacer: cualquier pregunta de ingeniería civil o de un área complementaria
puede entrar a la plataforma. Lo que sí se cierra en cada release es **la prueba de que una capacidad funciona**.

| Concepto | Abierto o cerrado | Significado |
|---|---|---|
| Ámbito científico | **Abierto** | Ningún release restringe los dominios, métodos ni preguntas que se pueden abordar |
| Capacidad de plataforma | Cerrada por release | Lo que la plataforma sabe hacer de forma general (ejecutar, verificar, documentar, acoplar, integrar) |
| Casos de referencia | Ejemplos | Demuestran la capacidad; **no son su límite** |
| Criterio de salida | Cerrado y medible | Evidencia de que la capacidad funciona en los casos de referencia y en un caso fuera de ellos |
| Carril abierto | Continuo | Desde R1, cualquier flujo nuevo entra por la fábrica en cualquier momento, sin esperar a un release, y opera como *experimental* hasta pasar sus compuertas |

Por qué la prueba debe ser cerrada: un criterio de salida abierto no se puede verificar, y una capacidad no verificada
no se puede declarar como existente (Constitución, Art. 13).

## 3.1 Releases

| Release | Capacidad de plataforma (Must) | Ámbito científico | Casos de referencia (ejemplos) | Áreas complementarias que se integran | Criterio de salida (gate) |
|---|---|---|---|---|---|
| **R0 — Núcleo reproducible** | Usuarios y roles, proyectos, registro de experimentos, orquestador con máquina de estados, **sandbox con perfiles sin red y con red controlada**, almacenamiento de artefactos con hash, procedencia básica, registro de agentes y contratos con validación de esquema, UI mínima | Independiente del dominio: cualquier cálculo en los lenguajes soportados (Python primero) | Programa T1 piloto (fase G0) | Ciencia de datos y computación científica | (1) Un script se ejecuta en sandbox sin red y otro en red controlada; (2) toda conexión queda registrada y la que esté fuera de la lista se bloquea; (3) la conexión exige aprobación humana registrada; (4) resultado trazable; (5) re-ejecución idéntica bit a bit |
| **R1 — Ciclo científico completo** | Ciclo de punta a punta para **cualquier dominio**: pregunta → investigación nacional e internacional → teoría → código → V&V → incertidumbre local → documentación → aprobación humana → paquete reproducible. Patrones de confianza en UI, design system v1, agentes de R1, compuertas G-SPEC a G-RELEASE y G-DOC | **Abierto.** Toda pregunta de ingeniería civil o de un área complementaria puede entrar por el carril abierto | **Demostrador:** drenaje pluvial urbano bajo RNE CE.040. **Prueba de generalidad:** un programa T1 de un dominio distinto (p. ej., capacidad portante o número estructural de pavimento) | Hidrometeorología y clima (curvas IDF, escenarios climáticos), geología y suelos (infiltración), urbanismo, ingeniería ambiental y sanitaria (calidad de la escorrentía), gestión del riesgo de inundación, economía (costo de alternativas) | (1) Caso dorado del demostrador dentro de tolerancia; (2) 100 % de valores trazables; (3) revisión del ingeniero registrada; (4) SUS ≥ 75; (5) **la prueba de generalidad pasa todas sus compuertas sin cambiar el código de la plataforma** |
| **R2 — Multidominio e interdisciplina** | Perfiles de dominio y casos dorados para los cinco dominios; **procedimiento para incorporar cualquier dominio o área nueva** (perfil + caso dorado + especialista); **acoplamiento entre disciplinas** (salida de un flujo como entrada de otro, con procedencia completa); incertidumbre completa (Monte Carlo, Sobol); decisión multicriterio; biblioteca de métodos abierta | **Abierto.** Los cinco dominios son el punto de partida, no el límite | Un caso dorado por dominio (geotecnia, pavimentos, estructural, construcción) **y** al menos dos flujos acoplados, p. ej.: lluvia → infiltración → estabilidad de taludes; interacción suelo-estructura; drenaje de pavimentos | Geología e ingeniería geológica, sismología, ciencia de materiales, clima, economía y evaluación de proyectos, ingeniería ambiental, ciencias sociales | (1) 5/5 casos dorados aprobados por revisor independiente; (2) 2 flujos acoplados verificados de punta a punta; (3) **al menos un dominio o área fuera de los cinco** incorporado con el procedimiento, como prueba |
| **R3 — Integraciones, geomática y motores propios** | Adaptadores de formatos abiertos (IFC, LandXML, GeoTIFF, GeoPackage), ingesta de topografía y nubes de puntos, paquete de proyecto cifrado. **Motores propios:** la fábrica genera aplicaciones y software propios, verificados. **Software de terceros "no confiable hasta verificar":** se usa solo mediante adaptadores, se contrasta con casos dorados o con un motor propio, y su estado queda en la matriz de conectores | Abierto. Prioridad: motores propios en código abierto y auditable; software licenciado solo opcional, con licencia del usuario | Un motor propio verificado contra una referencia de terceros (p. ej., un solucionador de redes de drenaje contrastado con SWMM); geomática con CRS trazable | Geodesia y teledetección, ciencia de la computación (HPC, nube), BIM | (1) Matriz de conectores con estado real; (2) pruebas de recuperación aprobadas; (3) **al menos un motor propio verificado** dentro de la tolerancia frente a la referencia de terceros |
| **R4+ — Extensiones (registro abierto)** | Mecanismo de **registro de extensiones**: cualquier capacidad nueva entra con mini-brief, ADR y criterio de salida | **Ilimitado** | Entorno portable arrancable, fablab virtual, visión móvil y cámara, receptores GNSS RTK/PPK, gemelos digitales, monitoreo estructural con sensores (SHM e IoT), drones, realidad aumentada en obra, impresión 3D de construcción, cómputo de alto rendimiento | Mecatrónica y robótica, electrónica y sensores, telecomunicaciones, ciencia de datos | Cada extensión tiene su propio criterio de salida. La plataforma no declara ninguna extensión como disponible hasta que lo cumpla |

### 3.1.1 Perfiles de red del sandbox (detalle de R0)

| Perfil | Red | Requisitos |
|---|---|---|
| Sin red | Denegada | Por defecto para todo cálculo |
| Red controlada | Solo a destinos de una **lista permitida** (repositorios de paquetes, servicios de datos abiertos, APIs de normas o metadatos) | Aprobación humana registrada por proyecto y por destino; registro de cada conexión; escaneo de lo descargado; los datos descargados entran como Datasets con procedencia y licencia |
| Red abierta | **Prohibida** | Constitución, Arts. 29 y 32 |

### 3.1.2 Motores propios y software de terceros (detalle de R3)

| Regla | Detalle |
|---|---|
| Preferencia | Ante dos caminos equivalentes, se prefiere el motor propio, abierto y verificado |
| No confiable hasta verificar | Un resultado de software de terceros se etiqueta *Importado* y no se usa como base de diseño hasta pasar el caso dorado del dominio o la comparación con un motor propio |
| Verificación cruzada | Cuando existan un motor propio y uno de terceros para el mismo problema, se contrastan; una diferencia fuera de tolerancia es un defecto que se investiga, no un dato que se descarta |
| Origen legítimo | Los motores propios se implementan a partir de teoría publicada (THEORY.md con referencias). Nunca mediante ingeniería inversa ni copia de software licenciado |
| Ritmo realista | Un motor propio es un programa T2 con todas sus compuertas. Se construyen de a uno, empezando por donde la dependencia de terceros sea más crítica (licencia, costo o falta de transparencia) |

## 3.2 Áreas complementarias (nuevo)

La ingeniería civil se apoya en otras disciplinas para que sus implementaciones sean correctas. MATTX las integra
con el mismo mecanismo que los dominios: **perfil de conocimiento + fuentes + casos de referencia + especialista humano**.

| Área complementaria | Qué aporta | Ejemplo de interrelación | Desde |
|---|---|---|---|
| Hidrometeorología y clima | Lluvia, curvas IDF, escenarios de cambio climático | Caudales de diseño bajo clima futuro | R1 |
| Geología e ingeniería geológica | Modelo geológico, peligros geológicos | Estabilidad de taludes, cimentaciones en roca | R1 (suelos) / R2 |
| Sismología e ingeniería sísmica | Peligro sísmico, registros, microzonificación | Espectros para la E.030 y estudios de sitio | R2 |
| Ciencia de materiales | Propiedades y durabilidad del concreto, el acero, los asfaltos y los suelos estabilizados | Vida útil de pavimentos y estructuras | R2 |
| Ingeniería ambiental y sanitaria | Calidad del agua, impacto ambiental, saneamiento | Calidad de la escorrentía; redes de agua y desagüe | R1 |
| Salud pública | Riesgos sanitarios de la infraestructura | Drenaje y enfermedades de transmisión hídrica | R2 |
| Gestión del riesgo de desastres | Peligro, vulnerabilidad, riesgo | Inundaciones, huaicos, sismos | R1 |
| Economía y evaluación de proyectos | Costo del ciclo de vida, evaluación social | Comparación de alternativas (Invierte.pe, MCDA) | R1 |
| Urbanismo y transporte | Usos del suelo, demanda, movilidad | Coeficientes de escorrentía; diseño vial | R1 |
| Ciencias sociales | Participación, aceptación, impacto social | Criterios sociales en la decisión multicriterio | R2 |
| Sostenibilidad y ciclo de vida (LCA) | Huella de carbono, energía incorporada | Selección de materiales y alternativas | R2 |
| Geodesia y teledetección | Marcos de referencia, imágenes satelitales, LiDAR | MDT, cambios de uso del suelo | R3 |
| Ciencia de datos y computación | Estadística, aprendizaje automático, HPC | Modelos sustitutos, calibración, Monte Carlo masivo | R0 |
| Derecho y contratos | Contratación pública, responsabilidad | Análisis forense de plazos (AACE) | R2 |
| Mecatrónica, sensores y robótica | Medición, automatización | Monitoreo estructural, fablab | R4+ |

**Reglas para las áreas complementarias**

1. Siguen las mismas reglas que los dominios: procedencia, marco bibliográfico universal, niveles de evidencia y casos de referencia.
2. Un resultado que dependa de un área complementaria declara qué área aportó qué dato o modelo.
3. La aprobación de los aportes de un área complementaria corresponde a un **profesional competente de esa área** (p. ej., un geólogo para el modelo geológico), no solo al ingeniero civil.
4. La lista es abierta: un área nueva entra con el procedimiento de incorporación de R2.

## 3.3 Fuera de alcance (sin cambios de fondo respecto a v1.3)

- Emitir planos "para construcción" o firmar en nombre de un profesional.
- Ejecutar software licenciado sin licencia válida del usuario.
- Operar máquinas físicas reales o cámaras de vigilancia (el fablab de R4+ es virtual hasta que una extensión defina su capa de seguridad).
- Reemplazar ensayos de laboratorio o de campo con estimaciones de IA.
- Dar acceso de red abierta a un sandbox.

## Preguntas abiertas para la siguiente revisión (r2)

1. **Prueba de generalidad en R1:** ¿se exige ya en R1 un segundo caso de otro dominio, o se deja para R2? Exigirlo amplía R1 pero demuestra desde el inicio que el alcance es abierto.
2. **Primer motor propio en R3:** ¿en qué dominio conviene empezar? Propuesta: red de drenaje (contrastable con SWMM) o análisis estructural (por la licencia de OpenSees).
3. **Áreas complementarias:** ¿falta o sobra alguna? ¿El orden de entrada (columna "Desde") es el correcto?
4. **Red controlada:** ¿qué destinos deberían estar en la lista permitida inicial? (p. ej., PyPI, SENAMHI, NOAA, Copernicus, OpenAlex/Crossref)
