# Notebooks — mapa del cuatrimestre 2C-2026

Esta tabla es **la brújula del repo**: dice qué archivo corresponde a cada clase del cronograma.
Si vas a tocar una clase, buscala acá primero.

Plan completo de migración: [`CuestionesAdministrativas/Plan_2C2026.md`](../CuestionesAdministrativas/Plan_2C2026.md)

Leyenda: ✅ listo · 🔄 hay que adaptarlo · ❌ falta crearlo

| # | Fecha | Tema | Docente | Notebook | Estado |
|---|-------|------|---------|----------|--------|
| 00 | 14-ago | Introducción a Colab, sintaxis y tipos de datos | Todos | `00_intro_python_y_datos.ipynb` | 🔄 |
| 01 | 18-ago | Manejo de archivos y obtención de datos | **Juan** | `01_Manejo_de_archivos_y_obtencion_de_datos.ipynb` | ✅ |
| 02 | 21-ago | Visualización de datos | Rita | `02_Manipulación_de_datos_organizacionales_y_visualización.ipynb` | 🔄 |
| 03 | 25-ago | Funciones de oferta, demanda, costo, beneficio | Manu | `03_Modelización_de_funciones_económicas.ipynb` | ✅ |
| 04 | 28-ago | Puntos de equilibrio y ecuaciones | Manu | `04_Puntos_de_equilibrio_y_sistemas_de_ecuaciones.ipynb` | ✅ |
| 05 | 01-sep | Vectores y matrices | **Juan** | `05-Matrices y Leontief.ipynb` | 🔄 sacarle Leontief |
| 06 | 04-sep | Variables relevantes, filtrado y muestreo | Rita | — | ❌ |
| 07 | 08-sep | Sistemas de ecuaciones lineales | **Juan** | `07_Sistemas_de_ecuaciones_lineales.ipynb` | ✅ |
| 08 | 11-sep | Programación lineal | Rita | `07- Programación lineal en Python.ipynb` + `08- Modelización...` | 🔄 fusionar |
| 09 | 15-sep | La derivada y las métricas organizacionales | Manu | `09- Derivada y variaciones...ipynb` | 🔄 rutas |
| 10 | 18-sep | Marginales y elasticidades | Manu | `10_CasoElasticidades.ipynb` | 🔄 rutas |
| 11 | 22-sep | Optimización de funciones | Manu | `11- Optimización de funciones...ipynb` | ✅ |
| 12 | 25-sep | Casos de aplicación en organizaciones | Manu | `12- Optimización...` + `Complemento/12_1_Caso_Duopolio_` | 🔄 elegir uno |
| — | **29-sep** | **PRIMER PARCIAL** | — | — | — |
| 13 | 02-oct | Herramientas de análisis financiero | Rita | `15-Aplicaciones para el análisis de inversiones.ipynb` | 🔄 rutas + cambia de docente |
| 14 | 06-oct | Aplicaciones financieras para inversiones | **Juan** | `17-Aplicaciones_..._inversiones_II.ipynb` | 🔄 borrar el `16-` duplicado |
| 15 | 09-oct | Intro a procesos organizacionales y análisis de datos | Rita | — | ❌ |
| 16 | 13-oct | Funciones totales a partir de marginales | **Juan** | `13_Integrales_Indefinidas1.ipynb` | ✅ |
| 17 | 16-oct | Integrales y valores acumulados (excedentes) | **Juan** | `14_Integrales Definidas.ipynb` | 🔄 título interno |
| 18 | 20-oct | Aplicaciones económicas de la integración | **Juan** | `18_Aplicaciones_economicas_integrales.ipynb` | ✅ |
| 19 | 23-oct | Simulación de datos y aplicaciones | Manu | — | ❌ |
| 20 | 27-oct | Aplicaciones económicas (U5) | Manu | — | ❌ |
| 21 | 30-oct | Métricas estadísticas | **Juan** | `21_Metricas_estadisticas.ipynb` | ✅ |
| 22 | 03-nov | SQL y manejo de tablas | **Juan** | `22_SQL_y_manejo_de_tablas.ipynb` | ✅ |
| 23 | 06-nov | Anonimización y ética | Rita | `19-Anonimizacion_de_datos.ipynb` | 🔄 ampliar |
| 24 | 10-nov | Repaso e integración | Todos | `Integradoras/` | 🔄 |
| — | **13-nov** | **PRESENTACIÓN DE TP** | — | — | — |
| — | **17-nov** | **SEGUNDO PARCIAL** | — | — | — |

---

## Cómo escribir una clase nueva

Para que todas se sientan la misma materia, seguimos estas convenciones.

### 1. Las tres celdas de apertura

```markdown
**Laboratorio de Métodos Cuantitativos Aplicados a la Gestión**

---

# **Clase NN - Título de la clase**
```

```markdown
## Complemento

Este notebook se complementa con la presentación: **Nombre.pdf**

Te recomendamos leer el PDF para trabajar con este notebook y tener una mejor comprensión
de los conceptos teóricos.
```

```markdown
## ¿Qué vamos a hacer en esta clase?

| Parte | Tema | Herramienta |
|---|---|---|
| **A** | ... | ... |
```

### 2. Los datos se leen por URL, nunca por ruta local

```python
URL = "https://raw.githubusercontent.com/Datso653/Laboratorio-de-metodos-Cuantitativos-Aplicados-a-la-gestion/main/DF/"
df = pd.read_csv(URL + "ventas.csv")
```

Así el notebook corre igual en Colab, en la facultad y en la casa de cada uno, sin montar Drive
ni editar nada. **Nunca** `C:\Users\...` ni `/content/drive/...`.

Si el dataset no existe todavía, subilo a `DF/` en el mismo commit.

### 3. Estilo de las explicaciones

- **Tablas markdown** para comparar conceptos, operadores o variables.
- **Analogías concretas** antes de la fórmula. El alumno promedio se considera principiante.
- **Comentarios en cada línea de código** que no sea obvia.
- Avisos de trampas con `> ⚠️` y tips con `> 💡`.
- Emojis en los títulos de sección, con moderación.
- Colores de los gráficos: `#243b5e` (azul) y `#e07b39` (naranja).

### 4. Cierre obligatorio

- Una sección **📝 Ejercicios** con celdas `# Tu respuesta acá`.
- Una tabla final **🧭 Para llevarse** con los comandos de la clase.
- Los ejercicios difíciles se marcan con 🥇⚡🤓 (convención que ya usa la materia).

### 5. Antes de hacer el PR

- [ ] El notebook corre **de arriba a abajo** en Colab sin editar nada.
- [ ] El título interno coincide con el número de esta tabla.
- [ ] No hay rutas absolutas ni de Drive.
- [ ] Los datasets que usa están en `DF/`.
- [ ] Tiene ejercicios y tabla de cierre.

---

## Flujo de trabajo con git

El repo tiene una rama por docente: `juan`, `manu`, `rita`, y `main` como versión publicada.

```bash
git checkout juan                    # o manu / rita
git pull origin main                 # traer lo último antes de empezar
git checkout -b clase/2026-11-03-sql # una rama por clase
# ... trabajar ...
git add notebooks/22_SQL_y_manejo_de_tablas.ipynb
git commit -m "Clase 22: SQL y manejo de tablas"
git push origin clase/2026-11-03-sql
```

Después se abre un PR contra la rama del docente responsable de esa clase.

> ⚠️ **Los notebooks son archivos JSON**: si dos personas tocan el mismo, el conflicto de git es
> horrible de resolver. Por eso **una rama por clase** y avisar en el grupo antes de empezar a
> tocar un notebook que no sea tuyo.
