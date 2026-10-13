# Verificación de la matriz normativa — revisión 13-oct-2026

Documento de revisión del pendiente **C6** ([PENDIENTES.md](../../PENDIENTES.md)). Cubre la matriz del
[Brief Maestro v1.3 §3.3.1](../Brief_Maestro/v1.3/MATTX_Brief_Maestro_v1.3.md), que se redactó con asistencia de IA.

**Regla:** ninguna norma de esta lista se cita como N1 (cumplimiento) ni como N2 (referencia de diseño) en una memoria
hasta que una persona la marque como verificada **en la fuente oficial**, anotando el dispositivo o la edición, la fecha
de consulta y su nombre.

## Resumen

| Estado | Significado | Cantidad |
|---|---|---|
| ✅ Verificada* | Confirmada en búsqueda web del 13-oct-2026 (fuentes secundarias u oficiales). *Falta confirmarla en la fuente oficial (El Peruano, SPIJ, portal del emisor) | 3 |
| ⚠️ Corregida | Tenía un error de nombre, edición o pertinencia; ya se corrigió en el Brief Maestro v1.3 | 6 |
| ⬜ Por verificar | Nombre plausible; falta confirmar edición y vigencia | 73 |
| 🔶 Imprecisa | Demasiado genérica para verificarse; hay que precisar qué documento exacto se usa | 13 |
| **Total** | | **95** |

**Hallazgos críticos para R1**

1. **La RNE OS.060 Drenaje Pluvial Urbano ya no existe con ese nombre.** Es la **CE.040 Drenaje Pluvial** (DS 012-2020-VIVIENDA y RM 126-2021-VIVIENDA). Todo el flujo R1 pasa a basarse en la CE.040.
2. **La Ley 30225 de Contrataciones del Estado está derogada.** Rige la Ley N.° 32069 y su reglamento (DS 009-2025-EF), con modificaciones de 2026.
3. **La E.030 se modificó en mayo de 2026** (RM 183-2026-VIVIENDA), con un régimen transitorio que también fue modificado.
4. **ASME V&V 40 no corresponde** a la ingeniería civil (es para dispositivos médicos) y se retiró.

## Cómo verificar cada norma

1. Buscar la norma en la fuente oficial: El Peruano o SPIJ para Perú; el portal del organismo emisor para las internacionales.
2. Anotar el código exacto, el título, la edición o el dispositivo de aprobación, la fecha de vigencia y las modificatorias.
3. Revisar si existe un régimen transitorio que afecte a proyectos en curso.
4. Cambiar el estado a **✅ Verificada (fuente oficial)** con fecha y nombre de quien verificó.
5. Si algo cambia, corregirlo en una versión nueva del Brief Maestro y en el perfil de dominio correspondiente.

Quién verifica: el agente de Investigación prepara la evidencia y una persona (especialista del dominio) la confirma
(Constitución, Art. 27).

## A. Perú — jurisdicción de cumplimiento (N1)

| # | Norma | Organismo · país | Dispositivo o edición | Estado | Observación |
|---|---|---|---|---|---|
| 1 | CE.040 Drenaje Pluvial | MVCS · PE | DS 012-2020-VIVIENDA (cambio de nombre y ubicación); RM 126-2021-VIVIENDA (contenido) | ⚠️ Corregida | La OS.060 ya no existe con ese nombre. Hubo un proyecto de modificación del numeral 21.2.1 publicado para aportes: confirmar si se aprobó |
| 2 | Ley General de Drenaje Pluvial y su reglamento | MVCS · PE | DL 1356; DS 016-2018-VIVIENDA | ✅ Verificada* | Proyecto de nuevo reglamento en consulta (RM 013-2026-VIVIENDA): seguir su estado |
| 3 | OS.050 Redes de distribución de agua | MVCS · PE | — | ⬜ Por verificar | Confirmar dispositivo vigente y si fue renombrada como la OS.060 |
| 4 | OS.070 Redes de aguas residuales | MVCS · PE | — | ⬜ Por verificar | Ídem |
| 5 | Demás normas OS del RNE | MVCS · PE | — | 🔶 Imprecisa | Listar solo las que use cada programa y verificarlas una por una |
| 6 | Manual de Hidrología, Hidráulica y Drenaje | MTC · PE | — | ⬜ Por verificar | No se encontró el dispositivo de aprobación vigente |
| 7 | ANA (criterios y datos) | ANA · PE | — | 🔶 Imprecisa | Precisar qué documentos de la ANA se usan |
| 8 | E.050 Suelos y Cimentaciones | MVCS · PE | RM 406-2018-VIVIENDA | ✅ Verificada* | No se confirmó si hubo modificaciones posteriores a 2018 |
| 9 | Manual de Suelos, Geología, Geotecnia y Pavimentos | MTC · PE | — | ⬜ Por verificar |  |
| 10 | CE.010 Pavimentos Urbanos | MVCS · PE | — | ⬜ Por verificar |  |
| 11 | Manual de Carreteras: Diseño Geométrico DG | MTC · PE | DG-2018, RD 03-2018-MTC/14 | ✅ Verificada* | No se encontró actualización posterior |
| 12 | Especificaciones Técnicas Generales para Construcción (EG) | MTC · PE | EG-2013 y su actualización | ⬜ Por verificar | Confirmar el dispositivo de la última actualización |
| 13 | E.020 Cargas | MVCS · PE | — | ⬜ Por verificar |  |
| 14 | E.030 Diseño Sismorresistente | MVCS · PE | RM 183-2026-VIVIENDA (mayo 2026) | ⚠️ Corregida | Tiene régimen transitorio para proyectos en curso, modificado por un dispositivo posterior cuyo número falta confirmar. Antecedentes: RM 355-2018 y RM 043-2019 |
| 15 | E.060 Concreto Armado | MVCS · PE | — | ⬜ Por verificar | No se encontraron modificaciones 2024–2026; confirmar el texto vigente. Revisar su coherencia con la E.030 de 2026 |
| 16 | E.070 Albañilería | MVCS · PE | — | ⬜ Por verificar |  |
| 17 | E.090 Estructuras Metálicas | MVCS · PE | — | ⬜ Por verificar |  |
| 18 | Ley N.° 32069, Ley General de Contrataciones Públicas, y su reglamento | MEF / OECE · PE | Ley 32069 (2024), vigente desde abril de 2025; DS 009-2025-EF | ⚠️ Corregida | Deroga la Ley 30225. Modificada por el DL 1715 (feb. 2026) y la Ley 32732 (jul. 2026), cuya vigencia depende de un cambio en el reglamento |
| 19 | Obras por Impuestos | MEF · PE | — | ⬜ Por verificar | Confirmar la ley y el reglamento vigentes |
| 20 | Invierte.pe | MEF · PE | — | ⬜ Por verificar | Confirmar la norma marco y las directivas vigentes |
| 21 | G.050 Seguridad durante la Construcción | MVCS · PE | — | ⬜ Por verificar |  |
| 22 | IGN, REGGEN | IGN · PE | — | ⬜ Por verificar |  |
| 23 | Normas de catastro (SUNARP/COFOPRI) | PE | — | 🔶 Imprecisa | Precisar qué normas |
| 24 | Directivas de Invierte.pe (evaluación de alternativas) | MEF · PE | — | 🔶 Imprecisa | Precisar qué directivas |

## B. Internacional y referentes comparados (N2)

La columna "Edición candidata" viene del **conocimiento del modelo de IA y no está verificada**. Sirve solo como punto de
partida.

### Hidráulica, hidrología y saneamiento

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | SWMM Reference Manuals (Vol. I–III) | US EPA · US | 2016–2017 | ⬜ Por verificar |  |
| 2 | HEC-22 Urban Drainage Design Manual | FHWA · US | 3.ª ed. 2009 / 4.ª ed. 2024 | ⬜ Por verificar | Confirmar la edición vigente |
| 3 | HEC-RAS / HEC-HMS | USACE · US | Versión de software 6.x / 4.x | ⬜ Por verificar | Registrar como software con versión, no como norma |
| 4 | Manual of Practice 77 (Urban Stormwater) | ASCE/EWRI · US | 1992 | ⬜ Por verificar |  |
| 5 | Guide to Hydrological Practices (WMO-No. 168) | OMM · INT | 6.ª ed. | ⬜ Por verificar |  |
| 6 | EN 752 Drain and sewer systems outside buildings | CEN · INT | 2017 | ⬜ Por verificar |  |
| 7 | ISO 4373 / ISO 748 (medición de nivel y caudal) | ISO · INT | — | ⬜ Por verificar |  |
| 8 | Guías para la calidad del agua de consumo humano | OMS · INT | 4.ª ed. con adendas | ⬜ Por verificar |  |
| 9 | RAS (Resolución 0330 de 2017) | MinVivienda · CO | 2017 y modificatorias | ⬜ Por verificar |  |
| 10 | MAPAS | CONAGUA · MX | — | ⚠️ Corregida | Antes figuraba como "NTC/CONAGUA MAPAS"; NTC es un prefijo colombiano |
| 11 | Manual de Carreteras Vol. 3 | MOP · CL | Edición anual | ⬜ Por verificar |  |
| 12 | ABNT NBR | ABNT · BR | — | 🔶 Imprecisa | Precisar las normas (p. ej., redes de alcantarillado y aguas pluviales) |
| 13 | CIRIA C753 The SuDS Manual | CIRIA · GB | 2015 | ⬜ Por verificar |  |
| 14 | DWA-A 118 | DWA · DE | — | ⬜ Por verificar | Confirmar si hay edición nueva |

### Geotecnia

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | Eurocódigo 7 (EN 1997) | CEN · INT | 2004; segunda generación en publicación | ⬜ Por verificar | Definir qué generación se usa |
| 2 | ASTM D-series (ensayos de suelos) | ASTM · INT | — | 🔶 Imprecisa | Listar cada norma con su año (p. ej., clasificación, límites, SPT) |
| 3 | FHWA Geotechnical Engineering Circulars | FHWA · US | — | 🔶 Imprecisa | Precisar qué GEC (número y edición) |
| 4 | AASHTO LRFD Bridge Design Specifications §10–11 | AASHTO · US | 10.ª ed. | ⬜ Por verificar |  |
| 5 | ISO 22475 / ISO 22476 | ISO · INT | Varias partes | ⬜ Por verificar | Precisar las partes |
| 6 | NSR-10 Título H | MinVivienda · CO | 2010 y modificatorias | ⬜ Por verificar |  |
| 7 | NCh 1508 | INN · CL | — | ⬜ Por verificar |  |
| 8 | Japanese Geotechnical Society Standards | JGS · JP | — | 🔶 Imprecisa | Precisar qué normas |
| 9 | Canadian Foundation Engineering Manual | CGS · CA | — | ⬜ Por verificar | Confirmar la edición vigente |

### Pavimentos y vías

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | AASHTO Guide for Design of Pavement Structures | AASHTO · US | 1993 | ⬜ Por verificar | Es la base del caso dorado de pavimentos |
| 2 | Mechanistic-Empirical Pavement Design Guide (MEPDG) | AASHTO · US | Manual of Practice, edición a confirmar | ⬜ Por verificar |  |
| 3 | A Policy on Geometric Design (Green Book) | AASHTO · US | 7.ª ed. 2018 | ⬜ Por verificar |  |
| 4 | ASTM D6433 (PCI) | ASTM · INT | — | ⬜ Por verificar |  |
| 5 | HDM-4 | PIARC / Banco Mundial · INT | — | ⬜ Por verificar | Es software; registrar versión |
| 6 | INVIAS | INVIAS · CO | — | 🔶 Imprecisa | Precisar el manual (diseño de pavimentos) |
| 7 | Manual de Carreteras | MOP · CL | Edición anual | ⬜ Por verificar |  |
| 8 | Guide to Pavement Technology | Austroads · AU | Varias partes | ⬜ Por verificar |  |
| 9 | TRL Road Notes (p. ej., Road Note 31) | TRL · GB | — | ⬜ Por verificar |  |

### Estructural y sísmica

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | ACI 318 | ACI · US | 318-19 / 318-25 | ⬜ Por verificar | Confirmar la edición vigente |
| 2 | ASCE 7 | ASCE · US | 7-22 | ⬜ Por verificar |  |
| 3 | ASCE 41 | ASCE · US | 41-23 | ⬜ Por verificar |  |
| 4 | AISC 360 / AISC 341 | AISC · US | 2022 | ⬜ Por verificar |  |
| 5 | FEMA P-58 / FEMA P-695 | FEMA · US | — | ⬜ Por verificar |  |
| 6 | Eurocódigos 2 y 8 (EN 1992 / EN 1998) | CEN · INT | 2004–2005; segunda generación en publicación | ⬜ Por verificar |  |
| 7 | ISO 2394 (confiabilidad estructural) | ISO · INT | 2015 | ⬜ Por verificar |  |
| 8 | NCh 433 | INN · CL | Of.1996 Mod.2009 + DS 61 | ⬜ Por verificar |  |
| 9 | NSR-10 | MinVivienda · CO | 2010 y modificatorias | ⬜ Por verificar |  |
| 10 | NTC-CDMX | Gobierno CDMX · MX | — | ⬜ Por verificar | Confirmar la edición vigente |
| 11 | NZS 1170.5 | Standards NZ · NZ | 2004 + enmiendas | ⬜ Por verificar |  |
| 12 | Building Standard Law | MLIT · JP | — | ⬜ Por verificar |  |

### Construcción y gestión

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | AACE RP 29R-03 Forensic Schedule Analysis | AACE International · INT | 2011 | ⬜ Por verificar |  |
| 2 | PMBOK Guide | PMI · INT | — | ⬜ Por verificar | Confirmar la edición vigente |
| 3 | Practice Standard for Scheduling | PMI · INT | — | ⬜ Por verificar |  |
| 4 | ISO 21500 / ISO 21502 | ISO · INT | 2021 / 2020 | ⬜ Por verificar |  |
| 5 | ISO 19650 (BIM) | ISO · INT | Partes 1–6 | ⬜ Por verificar |  |
| 6 | FIDIC (contratos) | FIDIC · INT | Suite 2017 | ⬜ Por verificar | Precisar qué libro |
| 7 | Delay and Disruption Protocol | SCL · GB | 2.ª ed. 2017 | ⬜ Por verificar |  |
| 8 | NEC4 | NEC · GB | 2017 + enmiendas | ⬜ Por verificar |  |
| 9 | Guías de contratación pública | BID / Banco Mundial · INT | — | 🔶 Imprecisa | Precisar qué guías |

### Geomática y GIS

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | EPSG Geodetic Parameter Dataset | IOGP · INT | Versión del dataset | ⬜ Por verificar | Registrar la versión usada (RF-14) |
| 2 | ISO 19100 (información geográfica) | ISO · INT | Serie | 🔶 Imprecisa | Precisar qué normas |
| 3 | OGC GeoPackage / WMS / WFS | OGC · INT | — | ⬜ Por verificar |  |
| 4 | ASPRS Positional Accuracy Standards for Digital Geospatial Data | ASPRS · US | 2.ª ed. | ⚠️ Corregida | Antes figuraba como "ASPRS LiDAR Accuracy Standards" |
| 5 | IHO S-44 (levantamientos hidrográficos) | OHI · INT | 6.ª ed. | ⬜ Por verificar |  |
| 6 | SIRGAS | SIRGAS · INT | Marco de referencia vigente | ⬜ Por verificar |  |
| 7 | INSPIRE | UE · INT | — | ⬜ Por verificar |  |

### Verificación, validación e incertidumbre

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | ASME V&V 10 | ASME · US | 2019 | ⬜ Por verificar |  |
| 2 | ASME V&V 20 | ASME · US | 2009 (reafirmada) | ⬜ Por verificar |  |
| 3 | ASME V&V 40 | ASME · US | — | ⚠️ Corregida | **Retirada de la matriz**: es para dispositivos médicos |
| 4 | JCGM 100 (GUM) / JCGM 101 (Monte Carlo) | JCGM · INT | 2008 | ⬜ Por verificar |  |
| 5 | ISO/IEC 25010 | ISO/IEC · INT | 2023 | ⬜ Por verificar |  |
| 6 | ISO/IEC 17025 | ISO/IEC · INT | 2017 | ⬜ Por verificar |  |
| 7 | NASA-STD-7009 | NASA · US | — | ⬜ Por verificar | Confirmar la revisión vigente |
| 8 | AIAA G-077 | AIAA · US | 1998 | ⬜ Por verificar |  |

### Decisión multicriterio

| # | Norma | Organismo · país | Edición candidata (no verificada) | Estado | Observación |
|---|---|---|---|---|---|
| 1 | Saaty (AHP) y literatura MCDA | Literatura | — | 🔶 Imprecisa | Registrar las referencias exactas con DOI o ISBN |
| 2 | ISO 31000 (gestión del riesgo) | ISO · INT | 2018 | ⬜ Por verificar |  |
| 3 | Guías de evaluación de inversión pública | MDSF · CL / DNP · CO | — | 🔶 Imprecisa | Precisar qué guías |

## Fuentes consultadas en esta revisión

- Ley N.° 32069 y su reglamento (OECE): https://www.gob.pe/institucion/oece/colecciones/45029-ley-n-32069-ley-general-de-contrataciones-publicas-y-su-reglamento
- Cambios de la Ley General de Contrataciones Públicas (LP Derecho): https://lpderecho.pe/principales-cambios-introducidos-por-la-ley-general-de-contrataciones-publicas/
- Reglamento de la Ley 32069 (CMS): https://cms.law/es/per/publication/publican-el-reglamento-de-la-ley-general-de-contrataciones-publicas
- CE.040 y la OS.060 (vLex): https://vlex.com.pe/vid/864974428
- Proyecto de modificación de la CE.040 (MVCS): https://cdn.www.gob.pe/uploads/document/file/7047026/6064162-anexo-rm-385-rm-modif-nt-ce040.pdf
- Consulta del nuevo reglamento de drenaje pluvial (El Peruano): https://elperuano.pe/noticia/287447-ejecutivo-inicia-consulta-sobre-propuesta-de-nuevo-reglamento-de-la-ley-de-drenaje-pluvial
- RM 183-2026-VIVIENDA, modificación de la E.030 (MVCS): https://cdn.www.gob.pe/uploads/document/file/9902956/8081915-rm-183-2026-vivienda-modifica-norma-tecnica-e-030.pdf
- RM 406-2018-VIVIENDA, E.050 (SBN): https://sbn.gob.pe/Repositorio/Normas_Legales/NORMA_LEGAL_1821_b9ae.pdf
- DG-2018 (SNI): https://sni.org.pe/aprueban-manual-de-carreteras-diseno-geometrico-dg-2018/

Revisión asistida por IA (Constitución, Art. 22). Las búsquedas se hicieron el 13-oct-2026 y pueden no reflejar
cambios posteriores.
