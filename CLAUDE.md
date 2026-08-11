# Laboratorio de Métodos Cuantitativos Aplicados a la Gestión (FCE UBA)

Repositorio de la cátedra: notebooks de clase, datasets y material de apoyo.
Los alumnos lo abren en **Google Colab** desde GitHub.

## Contexto

- **Cuatrimestre en curso:** 2C-2026 (14-ago a 1-dic-2026).
- **Equipo docente:** Juan, Manu, Rita + colaboradores. Rama de git por docente.
- **Alumnos:** de la Facultad de Ciencias Económicas, en general **sin experiencia previa de
  programación**. Todo se explica desde cero y en castellano rioplatense.

## Documentos que hay que leer antes de tocar nada

| Archivo | Para qué |
|---|---|
| [`notebooks/README.md`](notebooks/README.md) | Mapa clase → notebook + convenciones de escritura |
| [`CuestionesAdministrativas/Plan_2C2026.md`](CuestionesAdministrativas/Plan_2C2026.md) | Plan de migración al cronograma nuevo |

## Reglas al escribir o editar notebooks

1. **Idioma:** castellano, con acentos correctos. Tono cercano pero preciso.
2. **Nivel:** explicar como a alguien que nunca programó. Analogía concreta antes de la fórmula.
3. **Datos por URL, nunca rutas locales.** Todos los datasets se leen así:
   ```python
   URL = "https://raw.githubusercontent.com/Datso653/Laboratorio-de-metodos-Cuantitativos-Aplicados-a-la-gestion/main/DF/"
   ```
   Nunca `C:\Users\...`, nunca `/content/drive/...`. El notebook tiene que correr en Colab sin editar nada.
4. **Estructura fija:** encabezado de la cátedra → Complemento (PDF) → "¿Qué vamos a hacer en esta
   clase?" → imports → contenido → 📝 Ejercicios → 🧭 Para llevarse.
5. **Verificar antes de entregar:** el notebook tiene que correr de arriba a abajo sin errores.
6. **Colores de gráficos:** `#243b5e` (azul) y `#e07b39` (naranja).

## Estructura

```
notebooks/          Clases, numeradas según el cronograma (ver notebooks/README.md)
  Complemento/      Material extra opcional
  Backup/           Versiones viejas — no se usan en clase
Integradoras/       Trabajos prácticos integradores
DF/                 Datasets
PPT's/              Presentaciones teóricas que acompañan cada notebook
Paper Teorico/      Apunte teórico en LaTeX
CuestionesAdministrativas/   Cronogramas, pautas de examen, plan del cuatrimestre
```

## Trampas conocidas

- **Los notebooks son JSON**: dos personas editando el mismo archivo generan conflictos de git muy
  difíciles de resolver. Una rama por clase, y avisar antes de tocar un notebook ajeno.
- **La numeración de archivos y los títulos internos no coinciden** en varios notebooks heredados
  del cuatrimestre pasado (hay tres que dicen "Clase 17"). Al editar uno, corregir el título.
- **`.xls` requiere `xlrd`**, que no siempre está en Colab. Preferir `.csv` o `.xlsx`.
- **En SQLite, dividir dos enteros da un entero.** Usar `100.0` en vez de `100` al calcular porcentajes.
- **`np.trapz` se renombró a `np.trapezoid`** en numpy 2.0. Usar
  `getattr(np, "trapezoid", None) or np.trapz` para que ande en las dos versiones.
