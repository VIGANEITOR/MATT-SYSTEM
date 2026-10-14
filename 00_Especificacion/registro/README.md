# Registro único de estado

Fuente única de qué componentes existen, en qué estado están y cómo se aceptan (FB-R0-003).

| Archivo | Contenido |
|---|---|
| `estado_componentes.json` | Componentes de la **plataforma** y de la **fábrica**: release, criticidad, peso, no compensable, prueba de aceptación, **estado** y evidencia |
| `estado_componentes.schema.json` | Esquema; un estado *probado* u *operativo* exige evidencia |
| `vigentes.json` | Briefs vigentes y bloques que se generan desde el registro |
| `generar.py` | Genera `ESTADO.md` y comprueba en CI que los briefs vigentes coincidan con el registro |

**Regla:** los briefs especifican, no declaran estados. El estado real se publica solo en [`ESTADO.md`](../../ESTADO.md).
Si cambia la especificación de un componente (release, criticidad, clase), el CI falla hasta que se crea una versión nueva
del brief afectado.

```bash
python 00_Especificacion/registro/generar.py --check
python 00_Especificacion/registro/generar.py --write
```
