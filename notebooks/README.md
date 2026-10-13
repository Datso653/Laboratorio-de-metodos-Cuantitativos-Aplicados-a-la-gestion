# Notebooks — mapa del cuatrimestre 2C-2026

Esta tabla es **la brújula del repo**: dice qué archivo corresponde a cada clase del cronograma.
Si vas a tocar una clase, buscala acá primero.

Cronograma oficial: [`CuestionesAdministrativas/Pautas/Cronograma detallado.xlsx - Sheet1.pdf`](../CuestionesAdministrativas/Pautas/Cronograma%20detallado.xlsx%20-%20Sheet1.pdf)

> 📌 **Los archivos están numerados según el cronograma**, no según el orden histórico del repo.
> El número del archivo, el título de adentro del notebook y el número de clase son **el mismo**.

Leyenda: ✅ listo · 🔄 hay que adaptarlo · ❌ falta crearlo

| # | Fecha | Tema | Docente | Notebook | Estado |
|---|-------|------|---------|----------|--------|
| 00 | 14-ago | Introducción a Colab, sintaxis y tipos de datos | Todos | `00_Introduccion_a_Python_y_datos.ipynb` | ✅ |
| 01 | 18-ago | Manejo de archivos y obtención de datos | **Juan** | `01_Manejo_de_archivos_y_obtencion_de_datos.ipynb` | ✅ |
| 02 | 21-ago | Visualización de datos | Rita | `02_Visualizacion_de_datos.ipynb` | 🔄 |
| 03 | 25-ago | Funciones de oferta, demanda, costo, beneficio | Manu | `03_Modelizacion_de_funciones_economicas.ipynb` | ✅ |
| 04 | 28-ago | Puntos de equilibrio y ecuaciones | Manu | `04_Puntos_de_equilibrio_y_sistemas_de_ecuaciones.ipynb` | ✅ |
| 05 | 01-sep | Vectores y matrices | **Juan** | `05_Vectores_y_matrices.ipynb` | ✅ |
| 06 | 04-sep | Variables relevantes, filtrado y muestreo | Rita | `06_Variables_relevantes_filtrado_y_muestreo.ipynb` | ✅ |
| 07 | 08-sep | Sistemas de ecuaciones lineales | **Juan** | `07_Sistemas_de_ecuaciones_lineales.ipynb` | ✅ |
| 08 | 11-sep | Programación lineal | Rita | `08_Programacion_lineal.ipynb` | ✅ el 08b pasó a [`Complemento/Optimizacion/`](Complemento/Optimizacion/) |
| 09 | 15-sep | La derivada y las métricas organizacionales | Manu | `09_Derivada_y_variaciones.ipynb` | ✅ |
| 10 | 18-sep | Marginales y elasticidades | Manu | `10_Marginales_y_elasticidades.ipynb` | ✅ |
| 11 | 22-sep | Optimización de funciones | Manu | `11_Optimizacion_de_funciones.ipynb` | ✅ |
| 12 | 25-sep | **Repaso integrador de cara al 1P** (virtual, 1h30) | Manu + **Juan** | `12_Repaso_integrador_1P.ipynb` | ✅ |
| — | **29-sep** | **PRIMER PARCIAL** | — | — | — |
| 13 | 02-oct | Herramientas de análisis financiero | Rita | `13_Herramientas_de_analisis_financiero.ipynb` | ✅ versión dada en clase; la larga quedó en `Backup/` |
| 14 | 06-oct | Aplicaciones financieras para inversiones: ROI, CAGR, payback, IR, ROA/ROE y FTE | **Juan** | `14_Aplicaciones_financieras_para_inversiones.ipynb` + PPT `Inversiones_Clase14.pdf` | ✅ rehecha 2C (no repite la 13); la del 1C quedó en `Backup/` |
| 15 | 09-oct | Intro a procesos organizacionales y análisis de datos | Rita | `15_Procesos_organizacionales_y_datos.ipynb` | 🔄 |
| 16 | 13-oct | Marginalidad y totalidad + aplicación económica (integrales) | **Juan** | `16_Integrales_y_aplicaciones_economicas.ipynb` + PPT `Integrales.pdf` | ✅ junta lo que antes eran las clases 16, 17 y 18; las versiones previas quedaron en `Backup/` |
| 17 | 16-oct | Simulación de datos y aplicaciones | Manu | — | ❌ |
| 18 | 20-oct | Aplicaciones económicas | Manu | — | ❌ |
| 19 | 23-oct | Métricas estadísticas | **Juan** | `21_Metricas_estadisticas.ipynb` | 🔄 renombrar a `19_` |
| 20 | 27-oct | SQL y manejo de tablas | **Juan** | `22_SQL_y_manejo_de_tablas.ipynb` | 🔄 renombrar a `20_` |
| 21 | 30-oct | Anonimización y ética | Rita | `23_Anonimizacion_de_datos.ipynb` | 🔄 ampliar y renombrar a `21_` |
| 22 | 03-nov | Repaso e integración | Todos | `Integradoras/` | 🔄 |
| — | **06-nov** | **PRESENTACIÓN DE TP** | — | — | — |
| — | 10-nov | Feriado (visita del Papa), sin clase | — | — | — |
| — | 13-nov | Clase de consultas previa al segundo parcial | — | — | — |
| — | **17-nov** | **SEGUNDO PARCIAL** | — | — | — |
| — | **24-nov** | **RECUPERATORIOS** | — | — | — |
| — | **01-dic** | **FINAL** | — | — | — |

---

## Lo que falta crear

| # | Fecha | Tema | Docente |
|---|-------|------|---------|
| 17 | 16-oct | Simulación de datos y aplicaciones | Manu |
| 18 | 20-oct | Aplicaciones económicas | Manu |

---

## Notas sobre la numeración

Los archivos **se renumeraron** para que coincidan con el cronograma 2C-2026. Antes había
desalineación entre el nombre del archivo, el título de adentro y la clase real. Los cambios:

| Antes | Ahora | Por qué |
|---|---|---|
| `07- Programación lineal en Python` | `08_Programacion_lineal` | Había **dos archivos con el 07**. La programación lineal es la clase 08 |
| `08- Modelización de problemas de optimización` | `Complemento/Optimizacion/complemento-clase08-...` | Era el segundo candidato a la clase 08. Pasó a complemento |
| `15-Aplicaciones para el análisis de inversiones` | `13_Herramientas_de_analisis_financiero` | La U4 se invirtió: finanzas va **antes** que integrales |
| `17-Aplicaciones_..._inversiones_II` | `14_Aplicaciones_financieras_para_inversiones` | Por dentro ya decía "Clase 14" |
| `18-Manejo_de_datos_estructurados` | `15_Procesos_organizacionales_y_datos` | Por dentro decía "Clase 17" |
| `13_Integrales_Indefinidas1` | `16_Integrales_en_el_analisis_economico` | Cubre las clases 16 **y** 17 (fusión de indefinidas + definidas) |
| `16_Integrales_en_el_analisis_economico` + `18_Aplicaciones_economicas_de_la_integracion` | `16_Integrales_y_aplicaciones_economicas` | El cronograma pasó integrales a **una sola clase** (13-oct). Los dos anteriores quedaron en `Backup/` |
| `19-Anonimizacion_de_datos` | `23_Anonimizacion_de_datos` | En el cronograma nuevo la anonimización es la clase 23 |
| `06-Manipulacion_de_datos_estructurados_y_Leontief` | `06_Variables_relevantes_filtrado_y_muestreo` | La clase 06 pasó a ser la de **muestreo**. El notebook anterior (MIP + ejercicios de pandas) quedó en `Backup/` |
| `05-Matrices y Leontief` | `05_Vectores_y_matrices` | Leontief salió del cronograma |

> ⚠️ **Si tenías un link de Colab guardado a alguno de estos archivos, se rompió.** Buscá el
> archivo nuevo en la tabla de arriba.

---

## Carpetas

| Carpeta | Qué tiene |
|---|---|
| `Complemento/` | Material de apoyo por tema. Ver su [README](Complemento/README.md) |
| `Backup/` | Versiones previas de notebooks reemplazados o fusionados |
