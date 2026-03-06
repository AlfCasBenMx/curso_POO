# 🧠 Cheatsheet de Prompts — Sesión 3: Python + pandas con GitHub Copilot

> Guía rápida de prompts para escribir como comentarios en Python.
> GitHub Copilot genera el código a partir de estos comentarios.

---

## 📥 Lectura de archivos

### Leer todos los xlsx de una carpeta
```python
# Lee todos los archivos .xlsx de la carpeta "datos_entrada/"
# Para cada archivo, guarda el DataFrame en un diccionario con el nombre del archivo como llave
# Muestra nombre, filas y columnas de cada archivo
```

### Leer CSVs con encoding correcto
```python
# Lee catalogo_cuentas.csv con encoding utf-8-sig
# Lee saldos_contables.csv con encoding utf-8-sig
# Muestra las primeras 5 filas de cada uno
```

### Agregar columna de origen
```python
# Para cada DataFrame, agrega una columna "archivo_origen" con el nombre del archivo
# Esto permite rastrear de dónde viene cada registro después de concatenar
```

---

## 🔀 Homologación de columnas

### Mapeo por archivo
```python
# Diccionario de mapeo de columnas por archivo:
# banca_comercial.xlsx: {"fecha_registro": "fecha", "concepto_operacion": "concepto", "monto_MXN": "monto", "tipo_movimiento": "tipo", "linea_negocio": "linea_negocio", "subcuenta_contable": "subcuenta"}
# banca_corporativa.xlsx: {"date": "fecha", "concept": "concepto", "amount_MXN": "monto", "type": "tipo", "business_line": "linea_negocio", "sub_account": "subcuenta"}
# seguros.xlsx: {"fecha": "fecha", "tipo_operacion": "concepto", "importe": "monto", "naturaleza": "tipo", "area": "linea_negocio", "cta_subcuenta": "subcuenta"}
# inversiones.xlsx: {"trade_date": "fecha", "description": "concepto", "amount": "monto", "category": "tipo", "desk": "linea_negocio", "gl_account": "subcuenta"}
# tarjetas.xlsx: {"fecha_movimiento": "fecha", "concepto": "concepto", "monto_pesos": "monto", "clasificacion": "tipo", "producto": "linea_negocio", "num_cuenta": "subcuenta"}
```

### Aplicar mapeo y concatenar
```python
# Aplica el diccionario de mapeo a cada DataFrame usando df.rename(columns=mapeo)
# Selecciona solo las columnas estándar: fecha, linea_negocio, concepto, subcuenta, monto, tipo, periodo, responsable, archivo_origen
# Concatena todos los DataFrames en uno solo con pd.concat()
```

---

## 🏷️ Clasificación

### Por concepto (regex)
```python
# Clasifica cada registro usando str.contains con regex:
# - Ingreso: concepto contiene "comisión|spread|prima|rendimiento|interés|asesoría|anualidad"
# - Gasto: concepto contiene "gasto|nómina|personal|servicio|licencia|renta|mantenimiento|multa|publicidad|seguridad"
# - Provisión: concepto contiene "reserva|pérdida|provisión|valuación"
# - Si no coincide con ninguna regla: "Sin clasificar"
```

### Con función personalizada
```python
# Crea una función clasificar(concepto, tipo) que devuelva "Ingreso", "Gasto", "Provisión" o "Sin clasificar"
# Aplica la función con df["clasificacion"] = df.apply(lambda row: clasificar(row["concepto"], row["tipo"]), axis=1)
```

---

## 📊 Consolidados (3 Excels)

### Filtrar y guardar con dos hojas
```python
# Para cada clasificación (Ingreso, Gasto, Provisión):
# 1. Filtra el DataFrame por clasificacion
# 2. Crea una hoja "Detalle" con todas las filas
# 3. Crea una hoja "Resumen" con pivot_table: index=["linea_negocio", "concepto"], values="monto", aggfunc="sum"
# 4. Guarda como consolidado_ingresos.xlsx, consolidado_gastos.xlsx, consolidado_provisiones.xlsx
```

### ExcelWriter con múltiples hojas
```python
# Usa pd.ExcelWriter con engine="openpyxl" para escribir múltiples hojas:
with pd.ExcelWriter("consolidado_ingresos.xlsx", engine="openpyxl") as writer:
    df_detalle.to_excel(writer, sheet_name="Detalle", index=False)
    df_resumen.to_excel(writer, sheet_name="Resumen")
```

---

## 📋 Formato Global (pivot)

### Pivot table con subtotales
```python
# Genera un pivot_table:
# - index="concepto" (cada concepto único)
# - columns="linea_negocio" (Banca Comercial, Banca Corporativa, Seguros, Inversiones, Tarjetas, Corporativo)
# - values="monto"
# - aggfunc="sum"
# - fill_value=0
# Agrega columna "TOTAL" con la suma horizontal
```

### Agregar filas de subtotal y resultado neto
```python
# Separa el pivot en 3 secciones: ingresos, gastos, provisiones
# Para cada sección, calcula una fila de subtotal (suma por columna)
# Concatena: ingresos + subtotal_ingresos + gastos + subtotal_gastos + provisiones + subtotal_provisiones
# Agrega fila final: "RESULTADO NETO" = subtotal_ingresos - subtotal_gastos - subtotal_provisiones
```

---

## ✅ Validaciones

### Cuadre de totales
```python
# Valida que:
# total_registros_entrada == total_ingresos + total_gastos + total_provisiones + total_sin_clasificar
# Imprime "✅ Cuadre OK" o "❌ Diferencia de X registros"
```

### Montos anómalos
```python
# Identifica:
# 1. Registros con monto nulo (NaN)
# 2. Ingresos con monto negativo
# 3. Gastos con monto negativo (podrían ser reversiones válidas)
# 4. Montos extremos (> 3 desviaciones estándar del promedio por concepto)
```

### Cruce con saldos contables
```python
# Para cada subcuenta, compara:
# - Suma de montos del consolidado
# - Saldo_final del archivo saldos_contables.csv
# Calcula la diferencia y marca como alerta si diferencia > 1%
```

---

## 📝 Formato Excel profesional

### Con openpyxl
```python
# Aplica formato al Excel de salida:
# 1. Encabezados: fondo azul (#0F62FE), texto blanco, negrita, centrado
# 2. Montos: formato de moneda "$#,##0.00"
# 3. Bordes delgados en todas las celdas
# 4. Filas de subtotal: fondo gris (#E0E0E0), negrita
# 5. Fila resultado neto: fondo amarillo (#FFCD00), negrita
# 6. Auto-ajustar ancho de columnas
```

### Con xlsxwriter (alternativa)
```python
# Usa xlsxwriter como engine de ExcelWriter para más control:
# writer = pd.ExcelWriter("formato_global.xlsx", engine="xlsxwriter")
# workbook = writer.book
# header_format = workbook.add_format({"bold": True, "bg_color": "#0F62FE", "font_color": "white"})
# money_format = workbook.add_format({"num_format": "$#,##0.00"})
```

---

## 🔧 Debugging con Copilot Chat

### Cuando hay un error
```
"Tengo este error al ejecutar mi script Python:
[pegar el traceback completo]
¿Qué está mal y cómo lo corrijo?"
```

### Cuando el resultado no es el esperado
```
"Mi pivot_table genera este resultado:
[pegar las primeras filas]
Pero esperaba que las líneas de negocio fueran columnas, no filas.
¿Cómo ajusto el código?"
```

### Para optimizar
```
"Este script tarda mucho porque lee archivos en un loop.
¿Puedes optimizarlo usando list comprehension y pd.concat?"
```

---

## ⚡ One-liners útiles

| Tarea | Código |
|-------|--------|
| Contar filas por archivo | `df.groupby("archivo_origen").size()` |
| Ver columnas únicas | `df.columns.tolist()` |
| Valores únicos de concepto | `df["concepto"].unique()` |
| Suma por línea de negocio | `df.groupby("linea_negocio")["monto"].sum()` |
| Filtrar nulos | `df[df["monto"].isna()]` |
| Quitar duplicados | `df.drop_duplicates()` |
| Exportar a CSV | `df.to_csv("salida.csv", index=False)` |
| Descripción estadística | `df["monto"].describe()` |
