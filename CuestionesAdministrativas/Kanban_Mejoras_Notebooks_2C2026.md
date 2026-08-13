---
kanban-plugin: board
cuatrimestre: 2C-2026
rama: juan
estado: implementado-pendiente-revision-de-juan
---

# Kanban — Mejoras a los notebooks (2C-2026)

> **Criterio transversal (aplicado a TODAS las tarjetas):** el enfoque del cuatrimestre es
> **organizacional**. Cada ejemplo, variable, dataset y explicación habla de la organización
> (empresa, área, proceso, costos, ventas, stock, gobierno), no de temas genéricos ni de ejemplos
> de juguete en inglés.

## 👀 Para que revise Juan

- [ ] **REVISIÓN FINAL** — 36 tarjetas implementadas. Groot abrió los notebooks en VS Code para el retoque final. Tachá de tu lista para verificar.

## ✅ Hecho

- [x] **T-37 · N00 · Control de flujo, ciclos, diccionarios y funciones, al español**<br>Segunda pasada de traducción, **manteniendo los mismos ejemplos**: `Control flow` → Control de flujo, `Loops` → Ciclos (`for`), `Dictionaries` → Diccionarios, `Pre-Built Functions` → Funciones predefinidas, `Crear Funciones` → Crear tus propias funciones. Los ejemplos se conservaron traducidos: `bermuda triangle` → triángulo de las Bermudas, `el dorado` → El Dorado, `atlantis` → **Atlántida**, `toothbrushes_packed` → cepillos_guardados, `l_countries_capitals` → paises_y_capitales (con Lesotho, Laos, Luxemburgo y Líbano intactos, y los saludos `¡Sabaidi!` / `¡Sveiki!`), `add_dramatic_pause` → agregar_pausa_dramatica y **la polémica de la piña en la pizza sobrevivió**. Se sumaron notas sobre la sangría, el `return` y los valores por defecto. **Verificado ejecutando las celdas encadenadas.**
- [x] **T-01 · N00 · Decimales, más detallado**<br>La sección ahora distingue **formatear vs. redondear** (y por qué importa cuando el número se sigue usando), explica **por qué `0.1 + 0.2` no da `0.3`** y cómo comparar decimales, suma una guía de **cuántos decimales corresponde** según qué se muestra, y cierra con **el punto y la coma en Argentina**, enganchando con la clase 01. **+6 celdas.**
- [x] **T-02 · N00 · Tuplas vs. diccionarios**<br>Bloque comparativo nuevo al final de diccionarios: tabla de cuándo usar cada uno, **el mismo dato guardado de las dos formas**, y el puente a pandas (columnas = claves, filas = tuplas). **+3 celdas.**
- [x] **T-03 · N00 · Listas y tuplas al español**<br>Volaron `whats_in_my_fridge`, `cool_tuple` con los ponies y unicornios, `drinks` y `sea_shells`. Ahora es el **stock de un depósito** (reponer, dar de baja, copiar el inventario de otra sucursal) y el **encabezado de un reporte** para las tuplas inmutables. Títulos traducidos y **7 "Understanding check" → "Para practicar"**.
- [x] **T-04 · N00 → N01 · La Parte 2 se mudó**<br>Las 51 celdas de pandas/DataFrames bajaron al notebook 01 como **"Parte G — Análisis de datos con pandas"**. Los objetivos del 00 se reescribieron: ya no promete pandas.
- [x] **T-05 · N00 · "📚 Más información" se quedó**<br>Junto con el easter egg del final. ✔️
- [x] **T-06 · N01 · Matriz de correlación volada**<br>Las 6 celdas viajaban dentro de la Parte 2: se eliminaron en la mudanza, no llegaron al 01.
- [x] **T-07 · N01 · Barra de Windows simplificada**<br>De dos celdas largas (el `SyntaxError` de unicode, las tres alternativas) a **una regla de tres líneas**: cambiá `\` por `/` y listo.
- [x] **T-08 · N01 · UTF-8 vs. latin-1 / cp1252, a fondo**<br>Qué es un encoding (con la analogía del código de artículos), tabla comparativa de ASCII/latin-1/cp1252/utf-8, **por qué `é` se convierte en `Ã©`** (los dos bytes leídos por separado), el caso del BOM de Excel, y **cómo recuperar** un texto ya roto. Con celdas que muestran los bytes reales. **+4 celdas.**
- [x] **T-09 · N03 · Fuera `math`, directo con NumPy**<br>Se eliminó el rodeo de mostrar que `math.sqrt` falla sobre un array. Arranca directo con NumPy y la idea de operar sobre la serie completa.
- [x] **T-10 · N03 · Logaritmos volados**<br>Fuera la sección "convierte cambios multiplicativos en aditivos" y la comparación de variaciones. (`np.log` sigue apareciendo como función de ejemplo, eso no se tocó.)
- [x] **T-11 · N03 · Estética**<br>10 títulos sueltos (`✅ Función lineal`, `✋ Preguntas disparadoras`) convertidos en **encabezados navegables**, para que aparezcan en el índice del notebook.
- [x] **T-12 · N03 · Ejercicios + integrador**<br>4 ejercicios de práctica (costos, demanda e ingreso, medio vs. marginal, leer un gráfico) y **el integrador "Textiles del Sur S.A."** con 7 consignas y nota de cómo se corrige. **+11 celdas.**
- [x] **T-13 · N04 · Estética**<br>Mismo criterio, cuidando de no convertir en título los bloques de conclusiones con ✅.
- [x] **T-14 · N04 · Estática comparativa a tierra**<br>Reescrita como **"la pregunta ¿y si...?"**: comparar dos fotos del equilibrio, sin derivadas parciales. Prioriza **la dirección** del efecto sobre la magnitud, y cierra con una tabla de 4 filas que resume la clase entera. Incluye un adelanto de que con derivadas esto se responde más rápido.
- [x] **T-15 · N04 · Caso de research económico**<br>**Incidencia impositiva: ¿quién paga realmente un impuesto?** El mismo impuesto de \$20 en dos mercados: con demanda sensible lo paga el consumidor en un **33%**, con demanda rígida en un **71%**. Cierra con las tres preguntas de research que se abren (estimar la elasticidad, cambios de comportamiento, pérdida de actividad). **+4 celdas, verificado numéricamente.**
- [x] **T-16 · N05 · Qué es un vector y qué es una matriz, con dibujos**<br>El notebook arrancaba en "Vectorización" **sin definir nunca qué es un vector**. Ahora abre con dos **diagramas SVG**: el vector como flecha y como fila de datos (ventas por día), y la matriz como grilla sucursales × meses con las anotaciones de fila/columna. **+5 celdas.**
- [x] **T-17 · TODAS · La rúbrica → REVERTIDA por decisión de Juan**<br>Se había agregado a los 12 notebooks, sacada de `Pautas_examen.pdf`. **Juan decidió sacarla de todos**: no va dentro del material de clase. Eliminada de los 9 que la tenían (él ya la había borrado a mano de la 00 y la 03). El contenido de la rúbrica sigue disponible en `CuestionesAdministrativas/Pautas/Pautas_examen.pdf`, que es su lugar.
- [x] **T-18 · TODAS · Bloques de código revisados**<br>Chequeo de sintaxis en las **12 notebooks**: 0 errores reales (el único hit es `!pip install`, que es sintaxis de notebook). Se arregló además `complemento-agente-groq.ipynb`, que era **inválido** (celdas markdown con `outputs`, celdas de código sin `execution_count`). Todos los notebooks del repo (28) validan contra `nbformat`.
- [x] **T-19 · TODAS · LaTeX arreglado**<br>9 celdas tenían **símbolos `$` de precios sin escapar** (`$30`, `$150.000`), que en Markdown abren modo matemático y rompen el párrafo entero. Escapados a `\$`, sin tocar las fórmulas reales.
- [x] **T-20 · REPO · Complementos por tema**<br>`notebooks/Complemento/` reorganizada en **Derivadas, Integrales, Sistemas_de_ecuaciones, Leontief, Inversiones, IA**, con un **README** que dice qué hay en cada una, de dónde salió y **por qué** salió.
- [x] **T-21 · N11 y N12 · Duopolio y monopolio afuera**<br>Salieron de **las dos** notebooks (32 menciones en la 11, 12 en la 12) al complemento `Derivadas/complemento-monopolio-y-duopolio.ipynb` (66 celdas): monopolio del agua, monopolio de Coca-Cola, duopolio Coca vs. Manaos y sus ejercicios.
- [x] **T-22 · N12 · Caso de gobierno**<br>**Repartir un presupuesto público** de \$500 M entre dos programas de empleo con rendimientos decrecientes. El óptimo (\$153,8 M / \$346,2 M) capacita 1.209 personas contra 685 si se vuelca todo al programa A. Cierra con **la regla del último peso**, verificada numéricamente (marginal A = marginal B = 1,2093), y la traducción a presupuesto de marketing o inversión entre sucursales. **+6 celdas.**
- [x] **T-23 · N11 y N12 · Optimización a tierra**<br>La 11 quedaba en 26 celdas al sacar el monopolio, así que se reconstruyó: **lote óptimo de pedido** (con el gráfico de las dos fuerzas y la lección de que el óptimo es plano) y **el precio que maximiza el beneficio** (\$52.667 contra los \$40.000 actuales, +\$28,9 M al año), con análisis de sensibilidad. Más **4 ejercicios organizacionales** incluido un integrador que cruza precio y logística. **De 26 a 40 celdas.**
- [x] **T-24 · TODAS · Prosa y orden narrativo**<br>Aplicado a medida que se tocó cada notebook: títulos navegables, secciones reordenadas y transiciones escritas entre bloques.
- [x] **T-25 · N05 · "Matrices especiales" al principio**<br>Estaba en la celda 56 de 65, casi al final. Ahora abre la sección de Matrices: **primero qué formas hay, después qué se hace con ellas.**
- [x] **T-26 · N07 · "¿Cuánto le puedo creer al resultado?" afuera**<br>Salieron las Partes C2 (número de condición) y D2 (mínimos cuadrados) — 11 celdas — al complemento. Quedó **un callout de tres líneas** con lo único que hace falta: verificá la solución, ¿tiene sentido?, ¿de dónde salieron los datos?
- [x] **T-27 · N07 · P2P simplificado**<br>Salieron el dimensionamiento del equipo y el business case (9 celdas). Queda el planteo, la matriz de flujos, la resolución y el control de consistencia.
- [x] **T-28 · N07 · De vuelta hacia lo simple**<br>Tenías razón: **49 → 59 → 75 celdas** en tres commits. Ahora **55**, cerca del original.
- [x] **T-29 · N09 · Solo ejercicios**<br>5 ejercicios nuevos (costo marginal, precio que maximiza el ingreso, leer la variación de una serie real, elasticidad con derivada, monotonía). **+11 celdas, sin tocar ni una celda existente.**
- [x] **T-30 · N13 + N14 · Integrales fusionadas**<br>Un solo notebook: **Parte 1 — indefinidas** (de lo marginal a lo total) y **Parte 2 — definidas** (cuánto se acumuló), con portada nueva que explica por qué son la misma herramienta. La ejercitación quedó al final. **299 celdas.** La 14 se archivó en `Backup/`.
- [x] **T-31 · N17 · La IA, el ROI y el LTV como historia**<br>**"La historia de un ROI que nadie podía calcular"**: en marzo se aprueba un proyecto de IA por el ahorro de 6 sueldos; en diciembre no se fue nadie y aparecieron costos nuevos. Las 4 trampas (el ahorro de tiempo no es ahorro de plata, los costos no terminan, el contrafactual no se observa, el horizonte es corto), la tabla de métricas (ROI, VAN, TIR, payback, LTV, CAC, TCO) y los números rehechos: **TIR 39,1% real contra 189,2% prometida** — rindió, pero un tercio de lo prometido. **+7 celdas, verificado.**
- [x] **T-32 · N17 · Más contexto financiero**<br>ROI vs. VAN (por qué el ROI no mira el tiempo), LTV y CAC con la **regla LTV/CAC ≥ 3**, y cómo la mejora de retención hace que el negocio recién ahí cierre (2,62 → 3,44). Con la advertencia de que atribuir la mejora al bot es la trampa del contrafactual.
- [x] **T-33 · N22 · El diagrama de los JOIN**<br>**No existía la foto en el repo** (busqué en los 28 notebooks y en `PPT's/`; lo que había en la 02 era una captura de "subir archivo"). Se dibujó como **SVG**: INNER, LEFT, RIGHT, FULL y CROSS, con tabla de cuándo se usa cada uno y **la advertencia del error caro**: un `INNER JOIN` que hace desaparecer ventas sin que nadie se entere.
- [x] **T-34 · N22 · Scripts SQL y esquemas**<br>Qué es un script y por qué una base se arma corriendo uno (reproducibilidad), y qué es un esquema: `PRIMARY KEY`, `REFERENCES` y `NOT NULL`, con **la diferencia grande contra Excel** — la base rechaza el dato malo en vez de guardarlo. Con un script ejecutable de punta a punta. **+5 celdas, probado.**
- [x] **T-35 · N22 · Vocabulario de una empresa de software**<br>Front-end y back-end (y dónde entra SQL: siempre en el back), **qué es un deploy** y los ambientes desarrollo/testing/producción con la regla de oro de no probar en producción, más API, repo, query, ETL, data warehouse, bug y rollback.
- [x] **T-36 · N01 · El segundo "01", resuelto**<br>No era de manejo de archivos: eran **vectores y matrices** con casos organizacionales. Sus **60 celdas** de casos resueltos (costos de fabricación, transporte de petróleo, panadería, producción industrial en 3 plantas) migraron a la **clase 05**, donde corresponden. El archivo quedó en `Backup/`.

## 🚫 Explícitamente NO tocar

- **N10 (`10_CasoElasticidades`)** — Juan la deja **como está**. ✔️ No se tocó.
- **N18 y N21** — Juan las va a **analizar él en detalle** antes de definir cambios. ✔️ No se tocaron.

## 🔍 Dudas — resueltas y pendientes

- [x] **D-01 · ¿Cuál es "la 01"?** → Eran dos y **no eran del mismo tema**. El de Colab (vectores y matrices) se mandó a la clase 05.
- [x] **D-02 · N03 · `math`** → Se voló; directo con NumPy.
- [x] **D-03 · Cambios sin commitear** → Eran de Juan e intencionales. **Se respetaron** (hay backup en el scratchpad de la sesión).
- [x] **D-04 · ¿Qué rúbrica?** → Salió de `Pautas_examen.pdf`. **Ver el pendiente de abajo.**
- [x] **D-05 · Carpeta de complementos** → Se reorganizó la existente en subcarpetas por tema.
- [x] **D-06 · Duopolio/monopolio** → Salió de las dos notebooks.
- [x] **D-07 · N07 · "¿cuánto le puedo creer?"** → Sin consultar (Juan pidió avanzar): **se sacó entera** al complemento y quedó un callout de 3 líneas. La sección equivalente de la **05 no se tocó**.

## ⚠️ Para que decida Juan

- [ ] **El PDF de pautas tiene un placeholder sin completar**<br>En `Pautas_examen.pdf`, criterio de la Parte 1: *"Interpretación (85%): lectura económica de resultados, conclusiones pertinentes, **[completar con cosas asociadas]**"*. Quedó a medio escribir en el documento oficial. La rúbrica de los notebooks se armó con lo que sí está definido.
- [ ] **El PDF dice "1er cuatrimestre 2026" y la fecha del parcial es el 5 de mayo**<br>Hay que actualizarlo al 2C-2026 (primer parcial: **29-sep**).
- [ ] **Solapamiento a revisar en el N01**<br>La Parte G que bajó del 00 trae indexación, filtrado y agrupación, temas que el 01 ya trabajaba con sus propios datos. **No se podó** para no perder material sin tu visto bueno: puede quedar repetido.

%% kanban:settings
```
{"kanban-plugin":"board","show-checkboxes":true,"lane-width":360}
```
%%
