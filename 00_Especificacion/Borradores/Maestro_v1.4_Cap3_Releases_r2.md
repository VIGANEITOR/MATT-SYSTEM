# Borrador — Brief Maestro v1.4 · Capítulo 3: Alcance, releases y áreas complementarias

| Campo | Valor |
|---|---|
| Revisión de trabajo | r2 · 14-oct-2026 |
| Base | Revisión r1 + respuesta del autor del 14-oct-2026 |
| Estado | **Integrado** en el [Brief Maestro v1.4](../Brief_Maestro/v1.4/MATTX_Brief_Maestro_v1.4.md). Sigue abierto a feedback (§3.6) |
| Redacción | Asistida por IA |

## Respuesta del autor a la r1

> "Estoy de acuerdo con las propuestas del brief maestro, siempre y cuando cada versión o release sea suficiente como
> punto de partida de la siguiente versión; asimismo, que permita modificaciones conforme se tenga el feedback de cada
> versión para su mejora."

## Decisiones de esta revisión

| # | Pregunta de la r1 | Decisión | Dónde queda |
|---|---|---|---|
| 1 | ¿Prueba de generalidad en R1? | **Sí, en R1**: un programa T1 de otro dominio pasa todas sus compuertas sin cambiar el código de la plataforma | §3.1, R1, criterio (5) |
| 2 | ¿Primer motor propio? | **Solucionador de redes de drenaje**, contrastado con EPA SWMM (continúa R1 y SWMM es de dominio público). Segundo previsto: **análisis estructural** | §3.1 R3 y §3.1.2 |
| 3 | ¿Áreas complementarias? | Lista y orden aprobados; la lista sigue abierta y el orden se ajusta con el feedback | §3.4 |
| 4 | ¿Lista permitida de red controlada? | PyPI, SENAMHI, NOAA, Copernicus, OpenAlex y Crossref; ampliable solo con aprobación registrada | §3.1.1 |
| 5 | Condición del autor: cada release debe servir de punto de partida del siguiente | Criterio de entrada y paquete de traspaso obligatorios por release; compatibilidad hacia adelante | §3.5 (nuevo) |
| 6 | Condición del autor: permitir modificaciones según el feedback de cada versión | Registro de feedback por release, clasificación y destino, informe de cierre y punto de decisión antes del siguiente; versiones Rn.x | §3.6 (nuevo) |

## Texto del capítulo

La sección 3.3 (jurisdicción de cumplimiento y marco bibliográfico universal) no cambia respecto a la v1.3 y no se
repite aquí.

## 3. Alcance, releases, jurisdicción, áreas complementarias y mejora continua

La arquitectura objetivo conserva todos los subsistemas de v1.0. Cada release entrega una **capacidad general** de la
plataforma con un criterio de salida medible, deja lo necesario para iniciar el siguiente (§3.5) y se mejora con el
feedback recibido (§3.6). Un subsistema diferido sigue en la arquitectura como punto de extensión con interfaz definida.

### 3.0 Principio: alcance científico abierto, liberaciones verificables

MATTX no limita **qué** ciencia se puede hacer: cualquier pregunta de ingeniería civil o de un área complementaria
puede entrar a la plataforma. Lo que sí se cierra en cada release es **la prueba de que una capacidad funciona**.

| Concepto | Abierto o cerrado | Significado |
|---|---|---|
| Ámbito científico | **Abierto** | Ningún release restringe los dominios, métodos ni preguntas que se pueden abordar |
| Capacidad de plataforma | Cerrada por release | Lo que la plataforma sabe hacer de forma general (ejecutar, verificar, documentar, acoplar, integrar) |
| Casos de referencia | Ejemplos | Demuestran la capacidad; **no son su límite** |
| Criterio de salida | Cerrado y medible | Evidencia de que la capacidad funciona en los casos de referencia y en un caso fuera de ellos |
| Carril abierto | Continuo | Desde R1, cualquier flujo nuevo entra por la fábrica en cualquier momento, sin esperar a un release, y opera como *experimental* hasta pasar sus compuertas |
| Base para el siguiente | Obligatoria | Cada release entrega un paquete de traspaso que es el punto de partida del siguiente (§3.5) |
| Mejora por feedback | Continua | El alcance de los releases futuros se ajusta con el feedback de los anteriores (§3.6) |

Por qué la prueba debe ser cerrada: un criterio de salida abierto no se puede verificar, y una capacidad no verificada
no se puede declarar como existente (Constitución, Art. 13).

### 3.1 Releases

| Release | Capacidad de plataforma (Must) | Ámbito científico | Casos de referencia (ejemplos) | Áreas complementarias que se integran | Criterio de salida (gate) |
|---|---|---|---|---|---|
| **R0 — Núcleo reproducible** | Usuarios y roles, proyectos, registro de experimentos, orquestador con máquina de estados, **sandbox con perfiles sin red y con red controlada** (§3.1.1), almacenamiento de artefactos con hash, procedencia básica, registro de agentes y contratos con validación de esquema, UI mínima | Independiente del dominio: cualquier cálculo en los lenguajes soportados (Python primero) | Programa T1 piloto (fase G0) | Ciencia de datos y computación científica | (1) Un script se ejecuta en sandbox sin red y otro en red controlada; (2) toda conexión queda registrada y la que esté fuera de la lista se bloquea; (3) la conexión exige aprobación humana registrada; (4) resultado trazable; (5) re-ejecución idéntica bit a bit |
| **R1 — Ciclo científico completo** | Ciclo de punta a punta para **cualquier dominio**: pregunta → investigación nacional e internacional → teoría → código → V&V → incertidumbre local → documentación → aprobación humana → paquete reproducible. Patrones de confianza en UI, design system v1, agentes de R1, compuertas G-SPEC a G-RELEASE y G-DOC | **Abierto.** Toda pregunta de ingeniería civil o de un área complementaria puede entrar por el carril abierto | **Demostrador:** drenaje pluvial urbano bajo RNE CE.040 (sección 14). **Prueba de generalidad:** un programa T1 de un dominio distinto (p. ej., capacidad portante o número estructural de pavimento) | Hidrometeorología y clima, geología y suelos, urbanismo, ingeniería ambiental y sanitaria, gestión del riesgo de inundación, economía | (1) Caso dorado del demostrador dentro de tolerancia; (2) 100 % de valores trazables; (3) revisión del ingeniero registrada; (4) SUS ≥ 75; (5) **la prueba de generalidad pasa todas sus compuertas sin cambiar el código de la plataforma** |
| **R2 — Multidominio e interdisciplina** | Perfiles de dominio y casos dorados para los cinco dominios; **procedimiento para incorporar cualquier dominio o área nueva** (perfil + caso dorado + especialista); **acoplamiento entre disciplinas** (salida de un flujo como entrada de otro, con procedencia completa); incertidumbre completa (Monte Carlo, Sobol); decisión multicriterio; biblioteca de métodos abierta | **Abierto.** Los cinco dominios son el punto de partida, no el límite | Un caso dorado por dominio (geotecnia, pavimentos, estructural, construcción) **y** al menos dos flujos acoplados, p. ej.: lluvia → infiltración → estabilidad de taludes; interacción suelo-estructura; drenaje de pavimentos | Geología e ingeniería geológica, sismología, ciencia de materiales, clima, economía y evaluación de proyectos, ingeniería ambiental, ciencias sociales | (1) 5/5 casos dorados aprobados por revisor independiente; (2) 2 flujos acoplados verificados de punta a punta; (3) **al menos un dominio o área fuera de los cinco** incorporado con el procedimiento, como prueba |
| **R3 — Integraciones, geomática y motores propios** | Adaptadores de formatos abiertos (IFC, LandXML, GeoTIFF, GeoPackage), ingesta de topografía y nubes de puntos, paquete de proyecto cifrado. **Motores propios** (§3.1.2): la fábrica genera aplicaciones y software propios, verificados. **Software de terceros "no confiable hasta verificar"**: se usa solo mediante adaptadores, se contrasta con casos dorados o con un motor propio, y su estado queda en la matriz de conectores | Abierto. Prioridad: motores propios en código abierto y auditable; software licenciado solo opcional, con licencia del usuario | **Primer motor propio: solucionador de redes de drenaje**, contrastado con EPA SWMM. Segundo previsto: análisis estructural (reduce la dependencia de la licencia de OpenSees). Geomática con CRS trazable | Geodesia y teledetección, ciencia de la computación (HPC, nube), BIM | (1) Matriz de conectores con estado real; (2) pruebas de recuperación aprobadas; (3) **el motor propio de drenaje verificado** dentro de la tolerancia frente a SWMM en los casos dorados de R1 |
| **R4+ — Extensiones (registro abierto)** | Mecanismo de **registro de extensiones**: cualquier capacidad nueva entra con mini-brief, ADR y criterio de salida | **Ilimitado** | Entorno portable arrancable, fablab virtual, visión móvil y cámara, receptores GNSS RTK/PPK, gemelos digitales, monitoreo estructural con sensores (SHM e IoT), drones, realidad aumentada en obra, impresión 3D de construcción, cómputo de alto rendimiento | Mecatrónica y robótica, electrónica y sensores, telecomunicaciones, ciencia de datos | Cada extensión tiene su propio criterio de salida. La plataforma no declara ninguna extensión como disponible hasta que lo cumpla |

Cada release puede tener versiones de mejora **Rn.x** con correcciones y mejoras compatibles que provengan del
feedback (§3.6).

#### 3.1.1 Perfiles de red del sandbox (detalle de R0)

| Perfil | Red | Requisitos |
|---|---|---|
| Sin red | Denegada | Por defecto para todo cálculo |
| Red controlada | Solo a destinos de una **lista permitida** | Aprobación humana registrada por proyecto y por destino; registro de cada conexión; escaneo de lo descargado; los datos descargados entran como Datasets con procedencia y licencia |
| Red abierta | **Prohibida** | Constitución, Arts. 29 y 32 |

**Lista permitida inicial** (ampliable solo con aprobación del responsable técnico, registrada):

| Destino | Uso |
|---|---|
| PyPI | Paquetes de Python, con versiones fijadas y escaneo de dependencias |
| SENAMHI | Datos hidrometeorológicos del Perú |
| NOAA | Datos climáticos y meteorológicos globales |
| Copernicus | Datos de observación de la Tierra y reanálisis climático |
| OpenAlex | Metadatos de literatura científica |
| Crossref | Verificación de DOI y metadatos bibliográficos |

#### 3.1.2 Motores propios y software de terceros (detalle de R3)

| Regla | Detalle |
|---|---|
| Preferencia | Ante dos caminos equivalentes, se prefiere el motor propio, abierto y verificado |
| No confiable hasta verificar | Un resultado de software de terceros se etiqueta *Importado* y no se usa como base de diseño hasta pasar el caso dorado del dominio o la comparación con un motor propio |
| Verificación cruzada | Cuando existan un motor propio y uno de terceros para el mismo problema, se contrastan; una diferencia fuera de tolerancia es un defecto que se investiga, no un dato que se descarta |
| Origen legítimo | Los motores propios se implementan a partir de teoría publicada (THEORY.md con referencias). Nunca mediante ingeniería inversa ni copia de software licenciado |
| Ritmo realista | Un motor propio es un programa T2 con todas sus compuertas. Se construyen de a uno: primero drenaje (R3), luego análisis estructural (R3.x o R4) |

### 3.2 Fuera de alcance

- Emitir planos "para construcción" o firmar en nombre de un profesional.
- Ejecutar software licenciado sin licencia válida del usuario.
- Operar máquinas físicas reales o cámaras de vigilancia (el fablab de R4+ es virtual hasta que una extensión defina su capa de seguridad).
- Reemplazar ensayos de laboratorio o de campo con estimaciones de IA.
- Dar acceso de red abierta a un sandbox.

### 3.4 Áreas complementarias

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
4. La lista es abierta: un área nueva entra con el procedimiento de incorporación de R2, y el orden de la columna "Desde" se puede ajustar con el feedback (§3.6).

### 3.5 Continuidad entre releases

**Regla:** cada release DEBE dejar un **paquete de traspaso** suficiente para iniciar el siguiente. Un release solo se
inicia cuando el anterior cumplió su criterio de salida y entregó ese paquete. Iniciar sin ello exige una excepción
aprobada por el responsable técnico y el científico, con los riesgos registrados.

| Release | Criterio de entrada | Paquete de traspaso (lo que deja) | Qué habilita en el siguiente |
|---|---|---|---|
| R0 | ADR-001 a ADR-004 aceptados; briefs vigentes aprobados; Constitución ratificada o vigente en forma provisional; esquemas de contrato y mensaje de agente (ya existen) | Núcleo desplegable; API documentada del orquestador, del sandbox y de la procedencia; registro de agentes; suite de reproducibilidad (QA-REP); informe de QA; línea base de métricas; registro de feedback de R0; backlog priorizado de R1 | R1 construye el ciclo científico completo sobre el núcleo, sin rehacerlo |
| R1 | Paquete de traspaso de R0; ADR-005 a ADR-008; caso dorado local (ADR-006); investigación UX; normas de cumplimiento de R1 verificadas en fuente oficial (C7) | Fábrica operativa con todas las compuertas; plantilla de programa; primeros métodos de la biblioteca (hidrología y drenaje); perfil de dominio de hidráulica; design system v1; programa de la prueba de generalidad; métricas de G1; feedback de usuarios (SUS, entrevistas); registro de feedback de R1 | R2 replica el ciclo en cada dominio y acopla flujos, reutilizando la fábrica |
| R2 | Paquete de traspaso de R1; especialistas por dominio designados; casos dorados candidatos de los cuatro dominios | Procedimiento de incorporación de dominios probado; perfiles de los cinco dominios y de un área más; contrato de acoplamiento entre flujos; bibliotecas de incertidumbre y multicriterio; métricas de G2; registro de feedback de R2 | R3 contrasta motores propios contra una biblioteca y casos dorados ya verificados |
| R3 | Paquete de traspaso de R2; matriz de conectores inicial; casos dorados de drenaje de R1 disponibles para contrastar el motor propio | Motor propio de drenaje verificado; adaptadores de formatos abiertos; geomática con CRS trazable; matriz de conectores con estado real; forja operativa; métricas de G3; registro de feedback de R3 | R4+ incorpora extensiones sobre adaptadores, motores y forja ya probados |
| R4+ | Paquete de traspaso de R3; mini-brief y ADR de cada extensión | Cada extensión deja su propio paquete de traspaso | Extensiones posteriores |

**Compatibilidad hacia adelante.** Un release no rompe lo liberado por el anterior. Si un cambio rompe la
compatibilidad (contrato, esquema, formato de paquete), exige versión mayor del componente, migración documentada y
que los paquetes reproducibles ya aprobados sigan re-ejecutándose con su entorno original (Constitución, Art. 6).

### 3.6 Feedback y mejora continua

Cada versión se mejora con lo que se aprende de la anterior. El feedback **puede modificar el alcance de los releases
futuros**; no reescribe los ya liberados.

**Fuentes de feedback:** usuarios (SUS, entrevistas, reportes), revisores y entidades (observaciones), defectos de QA,
métricas de las fases G0–G3, evals de agentes, lecciones del agente de Aprendizaje, cambios normativos y, si el
repositorio es público, la comunidad (issues).

**Registro:** cada release tiene `01_Releases/Rn_*/06_Feedback/registro.md`. Cada entrada lleva ID, fecha, fuente,
descripción, evidencia, clasificación, decisión, destino y responsable.

| Clasificación | Destino | Aprueba |
|---|---|---|
| Defecto en un release liberado | Versión de corrección **Rn.x** | Responsable técnico |
| Mejora dentro del alcance vigente | Backlog del release siguiente o de una Rn.x | Responsable de producto |
| Cambio de alcance de un release futuro | Solicitud de cambio → capítulo 3 en una versión nueva del Brief Maestro | Producto + científico |
| Cambio de arquitectura | ADR nuevo | Responsable técnico |
| Cambio normativo | Matriz normativa y perfil de dominio; aviso a los proyectos con resultados afectados | Especialista del dominio |
| Cambio de principio o regla superior | Enmienda constitucional (Arts. 43–45) | Tres responsables |

**Cierre de cada release:** un informe de cierre con la evidencia del criterio de salida, las métricas frente a sus
objetivos, el feedback recibido y su clasificación, las lecciones y la **propuesta de ajuste del siguiente release**.
Antes de iniciar el siguiente hay un punto de decisión: iniciar tal como está, ajustar su alcance o posponerlo.

**Reglas**

1. El alcance de un release futuro es una propuesta hasta que se inicia, y se ajusta con el feedback.
2. Una vez iniciado, su alcance solo cambia por solicitud de cambio registrada.
3. Un criterio de salida no se relaja durante un release para poder aprobarlo. Si se demuestra inadecuado, se cambia con justificación registrada y se aplica a todos los casos por igual (Constitución, Art. 45).
4. Un release liberado no se reescribe: las mejoras van en una Rn.x o en el release siguiente.
5. Todo feedback recibe una respuesta registrada: aceptado (con destino), diferido (con fecha o release) o rechazado (con motivo).
6. Un resultado aprobado no se reabre automáticamente por un cambio posterior; se marca como afectado y se avisa al proyecto, que decide si lo revisa.

