# Notebooks — mapa del cuatrimestre 2C-2026

Esta tabla es **la brújula del repo**: dice qué archivo corresponde a cada clase del cronograma.
Si vas a tocar una clase, buscala acá primero.

Plan completo de migración: [`CuestionesAdministrativas/Plan_2C2026.md`](../CuestionesAdministrativas/Plan_2C2026.md)

Leyenda: ✅ listo · 🔄 hay que adaptarlo · ❌ falta crearlo

| # | Fecha | Tema | Docente | Notebook | Estado |
|---|-------|------|---------|----------|--------|
| 00 | 14-ago | Introducción a Colab, sintaxis y tipos de datos | Todos | `00_intro_python_y_datos.ipynb` | ✅ |
| 01 | 18-ago | Manejo de archivos y obtención de datos | **Juan** | `01_Manejo_de_archivos_y_obtencion_de_datos.ipynb` | ✅ |
| 02 | 21-ago | Visualización de datos | Rita | `02_Manipulación_de_datos_organizacionales_y_visualización.ipynb` | 🔄 |
| 03 | 25-ago | Funciones de oferta, demanda, costo, beneficio | Manu | `03_Modelización_de_funciones_económicas.ipynb` | ✅ |
| 04 | 28-ago | Puntos de equilibrio y ecuaciones | Manu | `04_Puntos_de_equilibrio_y_sistemas_de_ecuaciones.ipynb` | ✅ |
| 05 | 01-sep | Vectores y matrices | **Juan** | `05_Vectores_y_matrices.ipynb` | ✅ |
| 06 | 04-sep | Variables relevantes, filtrado y muestreo | Rita | — | ❌ |
| 07 | 08-sep | Sistemas de ecuaciones lineales | **Juan** | `07_Sistemas_de_ecuaciones_lineales.ipynb` | ✅ |
| 08 | 11-sep | Programación lineal | Rita | `07- Programación lineal en Python.ipynb` + `08- Modelización...` | 🔄 fusionar |
| 09 | 15-sep | La derivada y las métricas organizacionales | Manu | `09- Derivada y variaciones...ipynb` | ✅ |
| 10 | 18-sep | Marginales y elasticidades | Manu | `10_CasoElasticidades.ipynb` | ✅ |
| 11 | 22-sep | Optimización de funciones | Manu | `11- Optimización de funciones...ipynb` | ✅ |
| 12 | 25-sep | Casos de aplicación en organizaciones | Manu | `12- Optimización...` + `Complemento/12_1_Caso_Duopolio_` | ✅ (falta elegir uno) |
| — | **29-sep** | **PRIMER PARCIAL** | — | — | — |
| 13 | 02-oct | Herramientas de análisis financiero | Rita | `15-Aplicaciones para el análisis de inversiones.ipynb` | 🔄 rutas + cambia de docente |
| 14 | 06-oct | Aplicaciones financieras para inversiones | **Juan** | `17-Aplicaciones_..._inversiones_II.ipynb` | ✅ |
| 15 | 09-oct | Intro a procesos organizacionales y análisis de datos | Rita | — | ❌ |
| 16 | 13-oct | Funciones totales a partir de marginales | **Juan** | `13_Integrales_Indefinidas1.ipynb` (Parte 1) | ✅ |
| 17 | 16-oct | Integrales y valores acumulados (excedentes) | **Juan** | `13_Integrales_Indefinidas1.ipynb` (Parte 2) | ✅ fusionada con la 16 |
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

---

## Material de Sebastián

Sebastián compartió sus **48 mini-notebooks** (`C01` a `C48`) más un mapeo de qué tomar para cada
clase nuestra. Lo integrado hasta ahora:

| Nuestra clase | De Sebastián | Qué se tomó |
|---|---|---|
| 00 Intro | C01, C03, C04, C10 | Anatomía del notebook y **orden de ejecución**, formateo de números, resumir listas, el *groupby manual* con diccionario |
| 01 Archivos | C18 | Rutas en Windows, `sep`/`decimal`/`encoding` con la tabla de síntomas, inventario mínimo |
| 03 Funciones | C37, C38 | `math` vs `numpy`, la trampa del `nan`, el log en economía, costo fijo/variable/medio/marginal, **óptimo sin derivadas** |
| 04 Equilibrio | C39 | Exacto vs aproximado, verificar con `.subs()`, `lambdify`, elasticidad, estática comparativa |
| 05 Matrices | C13, C14, C32 | Vectorización, `dtype`, **`axis=0` vs `axis=1`**, `*` vs `@`, matrices especiales con significado económico |
| 07 Sistemas | C36 | Por qué no la inversa, **número de condición**, `lstsq` y el residuo, checklist de defensa |

**Pendiente** (clases de Rita): 02 Visualización (C21, C23, C24), 06 Filtrado y muestreo
(C15, C16, C19, C25-C29), 08 Programación lineal (C44-C48).

---

## Verificación

Todos los notebooks tocados se ejecutan de punta a punta con `nbclient` antes de commitear, en un
**sandbox**: se copia `DF/` a una carpeta temporal y el notebook corre ahí, así ninguna celda de
escritura puede tocar los datos del repositorio.

> ⚠️ **Por qué importa:** varios notebooks tienen celdas `to_csv` / `to_excel`. Si se ejecutan
> apuntando a `DF/`, **sobrescriben el dataset original**. Ya pasó una vez con `avocado.csv`.

Estado al 2026-08-12 — 16 notebooks verificados: 00, 01, 03, 04, 05, 07, 09, 10, 11, 12, 13, 14,
17, 18, 21, 22.

### Arreglos de fondo encontrados al verificar

| Notebook | Qué estaba roto |
|---|---|
| `09-` | `/content/YPF.xlsx` — el archivo no existía en esa ruta (se subió a `DF/`) |
| `10_` | Montaba Google Drive y leía de una carpeta personal; el `to_excel` de 18.249 filas colgaba |
| `12-` | Una celda tenía `f = dsajajsda` — un placeholder sin terminar que cortaba la ejecución |
| `17-` | Usaba `yfinance` sin instalarlo: en Colab se caía en la primera celda |
| `05-` | Dos rutas absolutas a la PC de un docente |
| `07_` | El texto decía "90 sillas y 20 mesas"; la solución real es 30 y 40 |
| `00_` | Había quedado un `ME QUEDE ACA` en el título de una sección |
| `16-` | Duplicado de `17-` sin el punto de Fisher → movido a `Backup/` |
