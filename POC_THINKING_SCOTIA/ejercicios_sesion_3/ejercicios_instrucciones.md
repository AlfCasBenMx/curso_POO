# 📋 Instrucciones de Ejercicios — Sesión 3: Múltiples fuentes → Formato Global

> Todos los ejercicios se realizan con **Python + pandas** en **VS Code** con **GitHub Copilot** generando el código. No necesitas memorizar Python — Copilot programa por ti.

---

## 🎯 Contexto del ejercicio

Eres parte del equipo de **consolidación financiera** de una institución bancaria. Cada mes, recibes información de **12 fuentes diferentes**:

| # | Fuente | Formato | Área |
|---|--------|---------|------|
| 1 | Banca Comercial | XLSX | Línea de negocio |
| 2 | Banca Corporativa | XLSX | Línea de negocio |
| 3 | Seguros | XLSX | Línea de negocio |
| 4 | Inversiones | XLSX | Línea de negocio |
| 5 | Tarjetas | XLSX | Línea de negocio |
| 6 | Tesorería | XLSX | Área de soporte |
| 7 | Cumplimiento | XLSX | Área de soporte |
| 8 | Riesgos | XLSX | Área de soporte |
| 9 | Proveedor TI | XLSX | Proveedor externo |
| 10 | Proveedor Servicios | XLSX | Proveedor externo |
| 11 | Catálogo de Cuentas | CSV | Query SQL |
| 12 | Saldos Contables | CSV | Query SQL |

**Problema:** Cada fuente usa **nombres de columnas diferentes** y tiene formatos inconsistentes.

**Objetivo:** Automatizar la lectura, limpieza, homologación y consolidación de estas 12 fuentes en:
1. **3 Excels consolidados** (Ingresos, Gastos, Provisiones)
2. **1 Formato Global** con conceptos en filas × líneas de negocio en columnas

---

## Ejercicio 1 — Leer las 12 fuentes (20 min)

**Objetivo:** Leer todos los archivos de `datos_entrada/` y explorar su estructura.

### Instrucciones:

1. Abre VS Code y crea un archivo `paso1_leer.py`
2. Escribe este comentario al inicio y deja que Copilot genere el código:

```python
# Script para leer las 12 fuentes de datos financieros
# Lee todos los archivos .xlsx de la carpeta "datos_entrada/"
# Lee los archivos .csv de la misma carpeta
# Para cada archivo muestra: nombre, número de filas, columnas, lista de columnas
# Guarda un resumen en un DataFrame
```

3. Ejecuta el script: `python paso1_leer.py`
4. **Observa** las diferencias en nombres de columnas entre archivos

### Preguntas de validación:
- [ ] ¿Cuántos archivos .xlsx se leyeron? (Respuesta esperada: 10)
- [ ] ¿Cuántos archivos .csv se leyeron? (Respuesta esperada: 2)
- [ ] ¿Cuál archivo tiene más filas? (Respuesta esperada: banca_comercial.xlsx con 150)
- [ ] ¿Las columnas son idénticas en todos los archivos? (Respuesta: NO — cada uno usa nombres diferentes)

---

## Ejercicio 2 — Homologar columnas (15 min)

**Objetivo:** Crear un mapeo para unificar los nombres de columnas de las 12 fuentes.

### Instrucciones:

1. Crea un archivo `paso2_homologar.py`
2. Escribe este prompt como comentario:

```python
# Diccionario de mapeo de columnas por archivo fuente
# Cada archivo tiene columnas con nombres diferentes que deben mapearse a un estándar:
#   Columnas estándar: fecha, linea_negocio, concepto, subcuenta, monto, tipo, periodo, responsable
#
# Ejemplo de mapeo:
#   banca_comercial.xlsx: fecha_registro → fecha, concepto_operacion → concepto, monto_MXN → monto
#   banca_corporativa.xlsx: date → fecha, concept → concepto, amount_MXN → monto
#   seguros.xlsx: fecha → fecha, tipo_operacion → concepto, importe → monto
#   inversiones.xlsx: trade_date → fecha, description → concepto, amount → monto
#   etc.
#
# Aplica el mapeo a cada DataFrame y concatena todos en un solo DataFrame
```

3. Ejecuta y verifica que el DataFrame resultante tenga columnas uniformes

### Resultado esperado:
- Un DataFrame con ~876 filas (suma de todas las fuentes)
- Columnas: `fecha, linea_negocio, concepto, subcuenta, monto, tipo, periodo, responsable, archivo_origen`

---

## Ejercicio 3 — Clasificar y consolidar en 3 Excels (25 min)

**Objetivo:** Clasificar cada registro como Ingreso, Gasto o Provisión y generar 3 archivos de salida.

### Instrucciones:

1. Crea un archivo `paso3_consolidar.py`
2. Prompt sugerido:

```python
# Clasifica cada registro del DataFrame consolidado según reglas:
# 
# INGRESO: si concepto contiene "comisión", "spread", "prima", "rendimiento", 
#          "interés cobrado", "asesoría", "anualidad", "intereses tarjeta"
# GASTO:   si concepto contiene "nómina", "personal", "servicio", "licencia", 
#          "renta", "mantenimiento", "multa", "publicidad", "seguridad", "TI externo"
# PROVISIÓN: si concepto contiene "reserva", "pérdida", "provisión", "valuación"
#
# 1. Agrega columna "clasificacion" con: Ingreso, Gasto o Provisión
# 2. Registros no clasificados → "Sin clasificar" (guardar aparte)
# 3. Para cada clasificación, genera un Excel con 2 hojas:
#    - "Detalle": todas las filas
#    - "Resumen": pivot_table por linea_negocio y concepto (suma de monto)
# 4. Archivos de salida:
#    - consolidado_ingresos.xlsx
#    - consolidado_gastos.xlsx
#    - consolidado_provisiones.xlsx
#    - no_clasificados.xlsx (si hay registros sin clasificar)
```

3. Ejecuta y abre cada Excel para verificar

### Validación:
- La suma de filas de los 3 consolidados + no_clasificados == total de filas leídas
- El total de montos debe coincidir entre entrada y salida

---

## Ejercicio 4 — Generar el Formato Global (25 min)

**Objetivo:** Crear el Excel del Formato Global con conceptos × líneas de negocio.

### Instrucciones:

1. Crea un archivo `paso4_formato_global.py`
2. Prompt sugerido:

```python
# Genera el Formato Global a partir del DataFrame consolidado:
#
# Estructura del Excel:
# - Filas: cada concepto único (ordenado por clasificación: Ingresos → Gastos → Provisiones)
# - Columnas: cada línea de negocio + columna TOTAL
# - Valores: suma de montos
#
# Incluir:
# - Fila subtotal "TOTAL INGRESOS" después de todos los conceptos de ingreso
# - Fila subtotal "TOTAL GASTOS" después de todos los conceptos de gasto
# - Fila subtotal "TOTAL PROVISIONES" después de todas las provisiones
# - Fila final "RESULTADO NETO" = Total Ingresos - Total Gastos - Total Provisiones
# - Columna "TOTAL" con suma horizontal por concepto
#
# Formato del Excel:
# - Encabezados: fondo azul oscuro (#0F62FE), texto blanco, negrita
# - Filas de subtotal: fondo gris claro, negrita
# - Fila resultado neto: fondo amarillo (#FFCD00), negrita
# - Montos con formato $#,##0.00
# - Bordes en todas las celdas
# - Columnas auto-ajustadas
#
# Guardar como "formato_global.xlsx"
```

3. Ejecuta y abre el Formato Global en Excel
4. Verifica que los totales cuadren con los 3 consolidados

---

## Ejercicio 5 — Validaciones y log de excepciones (10 min)

**Objetivo:** Agregar validaciones automáticas y generar un log de excepciones.

### Instrucciones:

1. Crea un archivo `paso5_validaciones.py`
2. Prompt:

```python
# Agrega validaciones al proceso de consolidación:
#
# 1. Montos nulos: identifica registros con monto vacío o NaN
# 2. Montos negativos en ingresos: alerta si un ingreso tiene monto < 0
# 3. Cuadre de totales: suma de los 3 consolidados vs total de registros leídos
# 4. Cruce con saldos contables: compara totales por subcuenta con saldos_contables.csv
# 5. Conceptos vacíos: registros sin concepto definido
#
# Genera:
# - log_excepciones.xlsx con columnas: tipo_alerta, archivo_origen, fila, concepto, monto, detalle
# - Resumen en consola con conteos por tipo de alerta
```

3. Ejecuta y revisa el log

---

## Ejercicio 6 (Trabajo en célula) — Tu propio caso (25 min)

**Objetivo:** Adaptar el pipeline de consolidación a tu caso real de la Ficha de Problema.

### Instrucciones:

1. Identifica tus fuentes reales: ¿Cuántos archivos recibes? ¿De quién?
2. Define tu mapeo de columnas
3. Define tus reglas de clasificación
4. Define tu formato de salida (¿cómo se ve tu "Formato Global"?)
5. Modifica los scripts paso1 a paso5 para tu caso
6. Ejecuta end-to-end y valida

### Entregable:
- Un script `consolidar_mi_caso.py` que lea tus fuentes, consolide y genere tu formato de salida
- Un `log_excepciones.xlsx` con las alertas encontradas
- Una captura de los Excels de salida abiertos

---

## 🏆 Mini-POC: Script end-to-end

El entregable final de la Sesión 3 es un **script único** que:

1. ✅ Lee todas las fuentes de entrada (xlsx + csv)
2. ✅ Homologa nombres de columnas
3. ✅ Clasifica registros (Ingreso / Gasto / Provisión)
4. ✅ Genera 3 Excels consolidados con detalle y resumen
5. ✅ Genera el Formato Global por línea de negocio
6. ✅ Genera log de excepciones y validaciones
7. ✅ Imprime resumen en consola

Este script representa lo que antes tomaba **2-3 días manuales** y ahora toma **30 segundos**.
