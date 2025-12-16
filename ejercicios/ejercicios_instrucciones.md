Ejercicios prácticos (orientados a abrir cada Excel/CSV y usar columnas específicas)

Instrucciones generales:
- Abre el archivo `ejercicios/ejercicios.xlsx` si lo generaste con `generate_xlsx.py`, o abre los CSV directamente en Excel.
- Para cada ejercicio se indica el archivo (hoja) objetivo y las columnas relevantes.
- Todas las tareas son básicas: identificar columnas, usar SUM, COUNTIFS, IF, XLOOKUP o crear una tabla dinámica pequeña.

Ejercicio 1 — Hola (archivo: ninguno, simple script)
- Archivo: N/A (ejercicio de lectura rápida)
- Objetivo: abrir `ejercicio1_hola.py` o mirar el snippet en `soluciones.md`.
- Tarea: identificar qué imprime el script.

Ejercicio 2 — Sumar importes (archivo: `transacciones` hoja)
- Archivo/Hoja: `transacciones` (columnas: `fecha`, `concepto`, `importe`)
- Tarea: en Excel, coloca los importes en una columna y calcula el total con =SUM(C:C) o =SUM(C2:C4) si quieres un rango pequeño.

Ejercicio 3 — Contar operaciones grandes (archivo: `ventas` hoja)
- Archivo/Hoja: `ventas` (columnas: `id_cliente`, `fecha`, `importe`, `categoria`)
- Tarea: cuenta cuántas ventas tienen `importe >= 1000` usando =COUNTIFS(C:C,">=1000").

Ejercicio 4 — Aplicar IVA simple (archivo: `ventas` o `transacciones`)
- Archivo/Hoja: `ventas` o `transacciones` (usar columna `importe`)
- Tarea: crear una nueva columna llamada `importe_con_iva` con la fórmula =C2*1.16 y arrastrarla.

Ejercicio 5 — Sumar por categoría (archivo: `ventas`)
- Archivo/Hoja: `ventas` (columnas `categoria`, `importe`)
- Tarea: usar SUMIFS para obtener total por 'Servicios', por ejemplo: =SUMIFS(C:C,B:B,"Servicios").

Ejercicio 6 — Agrupar y sumar (archivo: `ventas`)
- Archivo/Hoja: `ventas`
- Tarea: crear una pequeña tabla dinámica que muestre la suma de `importe` por `categoria`. Alternativa: usar SUMIFS con una lista única de categorías.

Ejercicio 7 — Lookup entre hojas (archivo: `ventas` y `clientes`)
- Archivo/Hoja: `ventas` y `clientes` (clientes tiene `id` y `nombre`)
- Tarea: en la hoja `ventas` añade una columna `cliente_nombre` que traiga el nombre desde `clientes` con XLOOKUP o VLOOKUP: =XLOOKUP(A2, clientes!A:A, clientes!B:B)

Ejercicio 8 — Regla escalonada (archivo: `ventas`)
- Archivo/Hoja: `ventas` (columna `importe`)
- Tarea: crear una columna `impuesto` que aplique: si importe<=1000 → 5%, si <=5000 → 8%, si >5000 → 12%.
  - Fórmula sugerida: =IFS(C2<=1000, C2*0.05, C2<=5000, C2*0.08, C2>5000, C2*0.12)

Ejercicio 9 — Verificación entre Python y Excel (archivos: `ventas`, `tarifas`)
- Archivo/Hoja: `ventas` y `tarifas` (tarifas tiene `categoria` y `tasa`)
- Tarea: con XLOOKUP traes la tasa por categoría y calculas impuesto =C2 * tasa. Suma el impuesto y compáralo con el resultado que obtendrías ejecutando el ejemplo mínimo en Python (usa `generate_xlsx.py` si necesitas la hoja consolidada).

Ejercicio 10 — Usar un asistente IA para construir la fórmula (archivo: `ventas`)
- Archivo/Hoja: `ventas`
- Tarea: copia el prompt de `prompts_cheatsheet.md` "SUMIFS por categoría y rango de fechas" y ejecútalo en ChatGPT/Copilot. Comprueba la fórmula resultante en Excel usando los datos de la hoja.

Notas finales:
- Todos los ejercicios están diseñados para ser básicos y reproducibles sólo con Excel y sin conocimientos de programación avanzados.
- Si quieres, creo versiones de cada ejercicio en hojas separadas dentro de `ejercicios/ejercicios.xlsx` y agrego botones de descarga en `sesion3.html`.
