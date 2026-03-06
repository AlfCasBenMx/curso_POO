# 📋 Instrucciones de Ejercicios — Sesión 3: Pipeline mensual de consolidación

> Todos los ejercicios se realizan **sin código manual**, usando **Copilot 365** (copilot.microsoft.com) para generar scripts de Python. No necesitas saber programar — Copilot genera el código por ti.

---

## 🎯 Contexto del ejercicio

Eres parte del equipo de **consolidación financiera** de una institución bancaria. Cada mes, recibes por correo **5 archivos Excel** de distintas áreas, cada uno con columnas nombradas diferente:

| # | Archivo | Filas | Col. fecha | Col. monto | Col. tipo |
|---|---------|-------|------------|------------|-----------|
| 1 | banca_comercial.xlsx | 150 | fecha_registro | monto_MXN | tipo_movimiento |
| 2 | banca_corporativa.xlsx | 120 | date | amount_MXN | type |
| 3 | seguros.xlsx | 100 | fecha | importe | naturaleza |
| 4 | tarjetas.xlsx | 130 | fecha_movimiento | monto_pesos | clasificacion |
| 5 | tesoreria.xlsx | 90 | value_date | amount_MXN | pnl_type |

**Problema:** Mismo dato, diferente nombre de columna. Cada mes repites el proceso manualmente.

**Objetivo:** Construir un **pipeline reutilizable** que:
1. Consolide los 5 archivos automáticamente
2. Verifique que todo cuadra (filas, montos)
3. Detecte cambios entre el mes actual y el anterior
4. Funcione sin tocar código — solo depositas archivos y ejecutas

---

## Lab 1 — Explorar las fuentes (20 min)

**Objetivo:** Entender qué tiene cada archivo ANTES de tocar nada.

### Paso 1 — Adjuntar y preguntar (5 min)
1. Abre [copilot.microsoft.com](https://copilot.microsoft.com)
2. Adjunta los 5 archivos (📎) y escribe:

```
Tengo estos 5 archivos Excel de distintas áreas de un banco.
Cada uno tiene columnas con nombres diferentes para lo mismo.
Para cada archivo, dame una tabla con:
1. Nombre del archivo
2. Número de filas
3. Número de columnas
4. Lista completa de nombres de columnas
5. Las primeras 2 filas de ejemplo
```

> **Plan B:** Si Copilot no puede leer todos a la vez, adjuntar de a 2-3 archivos por conversación.

### Paso 2 — Primera verificación (5 min)
```
Dame un RESUMEN para que yo pueda verificar:
- Tabla con: Archivo | Filas | Columnas | Suma del monto
- ¿Hay algún archivo con filas vacías o datos faltantes?
- ¿Hay algún archivo con menos columnas de las esperadas?
```

**🧪 VERIFICACIÓN:** Abran cada Excel manualmente → cuenten filas con la barra inferior de Excel → comparen con lo que dijo Copilot. Si no coincide, pregunten "El archivo X debería tener Y filas, tú dices Z. ¿Por qué?".

### Paso 3 — Mapa de equivalencias (10 min)
```
Basándote en los 5 archivos, haz un MAPA DE EQUIVALENCIAS.
Quiero una tabla con:
- Columna estándar (nombre final que deben tener)
- Para cada archivo: qué columna actual corresponde
Hazlo para TODAS las columnas que se puedan mapear.
```

**🧪 VERIFICACIÓN:** ¿El mapa tiene sentido? ¿`fecha_registro` realmente equivale a `date`? ¿`monto_pesos` está en la misma moneda que `amount_MXN`? Si algo no tiene sentido, corríjanlo AHORA.

---

## Lab 2 — Script de homologación + pruebas (25 min)

**Objetivo:** Que Copilot genere el código CON pruebas integradas.

### Paso 1 — Pedir el script CON verificación integrada (8 min)
```
Genera un script en Python que homologue los 5 archivos.
Usa el mapa de equivalencias que creaste. El script debe:
1. Leer cada archivo
2. Renombrar las columnas según el mapa
3. Agregar columna 'archivo_origen'
4. PARA CADA ARCHIVO imprimir:
   - Nombre del archivo
   - Filas ANTES y DESPUÉS (deben ser iguales)
   - Columnas ANTES y DESPUÉS (para verificar el renombrado)
   - Las primeras 3 filas DESPUÉS del renombrado
5. Al final: tabla resumen con Archivo | Filas | Monto Total

El script debe ser PASO A PASO con prints claros.
IMPORTANTE: si alguna columna no existe en un archivo, NO lo tires —
pon NaN y agrégalo a un log de excepciones.
```

### Paso 2 — Revisar el script ANTES de ejecutar (7 min)
No lo ejecuten todavía. Primero pidan que lo explique:
```
Antes de ejecutar, EXPLÍCAME paso a paso qué hace este script.
Para cada bloque de código, dime:
- Qué hace
- Qué podría salir mal
- Cómo lo verifico
Quiero entenderlo antes de correrlo.
```

### Paso 3 — Ejecutar y verificar las pruebas (10 min)
Copien el script, ejecútenlo, y revisen los prints:

**🧪 CHECKLIST DE VERIFICACIÓN:**
- [ ] Las filas ANTES = filas DESPUÉS para cada archivo (no se perdieron registros)
- [ ] Las columnas renombradas hacen sentido
- [ ] Las primeras 3 filas se ven correctas (los datos no se corrieron de columna)
- [ ] La tabla resumen tiene los 5 archivos con filas y montos
- [ ] Si hay excepciones, Copilot las reportó (no las ignoró en silencio)

Si algo no cuadra:
```
El archivo 'seguros.xlsx' debería tener $45,230,000 en total de importe,
pero después de la homologación dice $43,100,000. ¿Qué pasó?
¿Se perdieron filas? ¿Hay NaN? Muéstrame las filas que no se consolidaron.
```

---

## Lab 3 — Consolidar todo + cuadre final (20 min)

### Paso 1 — Consolidación con pruebas de cuadre (8 min)
```
Agrega al script un paso que:
1. Concatene los 5 DataFrames homologados en uno solo
2. Imprima PRUEBAS DE CUADRE:
   a) Total filas consolidado vs suma de filas individuales
   b) Suma de 'monto' en consolidado vs suma por archivo_origen
   c) ¿Cuántas filas tienen monto vacío/NaN?
   d) ¿Cuántas filas tienen fecha vacía?
   e) Valores únicos en 'archivo_origen' (deben ser exactamente 5)
   f) Valores únicos en 'tipo'
3. Guarde como 'consolidado_final.xlsx'
QUIERO VER TODAS LAS PRUEBAS EN CONSOLA ANTES DE GUARDAR.
```

### Paso 2 — Tabla de cuadre cruzado (7 min)
```
Genera una tabla de cuadre cruzado:
| Archivo | Filas original | Filas consolidado | ¿Cuadra? | Monto original | Monto consolidado | ¿Cuadra? |
Si algo tiene ✘, EXPLÍCAME por qué no cuadra.
```

**🧪 ESTE es el momento de la verdad.** Si todos los ✔ están verdes, pueden confiar en el consolidado. Si hay un ✘, NO AVANCEN.

### Paso 3 — Clasificar y generar Excel final (5 min)
```
Clasifica cada fila como 'Ingreso', 'Gasto' o 'Provisión' según 'tipo'.
Genera 3 archivos: ingresos.xlsx, gastos.xlsx, provisiones.xlsx.
PRUEBA: La suma de filas de los 3 + sin clasificar = total del consolidado.
```

---

## Lab 4 — Dashboard HTML del resultado (10 min)

### Paso 1 — Dashboard de consolidación (5 min)
```
Con los resultados del consolidado, genera un HTML tipo dashboard:
1. HEADER: 'Consolidación Financiera — [Fecha de hoy]'
2. KPIs en tarjetas: Total Archivos (5), Total Registros (590),
   Total Monto Consolidado, Registros sin clasificar
3. Tabla de cuadre cruzado con ✔ y ✘ visibles
4. Gráfico de barras CSS: monto por archivo_origen
5. Tabla de excepciones
Estilo EY corporativo, azul #0F62FE y amarillo #FFCD00. Un solo archivo HTML.
```

### Paso 2 — Conectar con presentación de Sesión 2 (5 min)
```
Agrega al slide de 'Métricas de éxito' de mi presentación HTML estos datos REALES:
- Archivos procesados: 5
- Registros consolidados: 590
- Tiempo manual estimado: 6 horas
- Tiempo con IA + verificación: 25 minutos
- Cuadre: 100% verificado
```

---

## Pipeline mensual — Armar la estructura (15 min)

**Objetivo:** Que el mes que viene, solo depositen archivos y ejecuten. Sin tocar código.

### Paso 1 — Crear estructura de carpetas (3 min)
```
Crea una estructura de carpetas para un pipeline mensual:
pipeline_consolidacion/
├── config/
│   ├── mapa_equivalencias.json
│   └── reglas_clasificacion.json
├── datos/
│   ├── 2025_01_enero/    ← archivos del mes pasado
│   └── 2025_02_febrero/  ← archivos del mes actual
├── salida/
│   ├── 2025_01_enero/
│   └── 2025_02_febrero/
├── logs/
├── pipeline.py            ← script maestro
└── comparar_meses.py      ← detección de cambios
Genera los comandos para crear esta estructura.
```

### Paso 2 — Convertir en pipeline.py reutilizable (7 min)
```
Toma el script del Lab y conviértelo en PIPELINE REUTILIZABLE:
1. NO hardcodear nombres — leer TODOS los .xlsx de la carpeta del mes
2. Leer mapa de equivalencias desde config/mapa_equivalencias.json
3. Leer reglas de clasificación desde config/reglas_clasificacion.json
4. La carpeta del mes se pasa como PARÁMETRO (ej: python pipeline.py 2025_02_febrero)
5. Guardar consolidado en salida/[mes]/consolidado_[fecha].xlsx
6. Guardar LOG completo en logs/log_[mes].txt
El script debe funcionar SIN que el usuario cambie UNA SOLA línea de código.
```

### Paso 3 — Probar con datos del Lab (5 min)
Copiar los 5 archivos a `datos/2025_02_febrero/` y ejecutar:
```
python pipeline.py 2025_02_febrero
```

**🧪 VERIFICACIÓN:**
- [ ] ¿Se creó el consolidado en salida/2025_02_febrero/?
- [ ] ¿Se creó el log en logs/log_2025_02.txt?
- [ ] ¿El log dice "CUADRE: SÍ"?
- [ ] ¿Los totales coinciden con los del Lab?
- [ ] ¿No tuve que modificar el script para que corriera?

---

## Detección de cambios entre periodos (20 min)

### Paso 1 — Script de comparación entre meses (8 min)
```
Genera comparar_meses.py que reciba 2 parámetros (mes anterior y actual):
python comparar_meses.py 2025_01_enero 2025_02_febrero

El script debe generar un REPORTE DE CAMBIOS:
1. ARCHIVOS: ¿Nuevos? ¿Faltantes?
2. ESTRUCTURA: ¿Columnas nuevas o eliminadas?
3. VOLUMEN: Filas por archivo, mes anterior vs actual (🚨 si cambio > ±20%)
4. MONTOS: Monto por archivo, comparación (🚨 si cambio > ±15%)
5. CLASIFICACIÓN: ¿Categorías nuevas o que desaparecieron?
6. RESUMEN EJECUTIVO: Total alertas, las 3 más críticas, ¿se puede confiar?
Guardar como logs/cambios_[mes1]_vs_[mes2].txt y versión HTML.
```

### Paso 2 — Simular cambios para probar (7 min)
```
Toma los 5 archivos originales → datos/2025_01_enero/.
Crea versiones "febrero" en datos/2025_02_febrero/ con cambios:
1. banca_comercial: +50 filas (200 total)
2. seguros: columna nueva 'canal_venta'
3. tesoreria: NO incluir (simula que no mandaron)
4. tarjetas: montos ~15% menores
5. banca_corporativa: sin cambios
```

### Paso 3 — Ejecutar y verificar alertas (5 min)
```
python comparar_meses.py 2025_01_enero 2025_02_febrero
```

**🧪 ¿El script detectó los 4 cambios simulados?**
- [ ] 🚨 banca_comercial: +33% filas (de 150 a 200)
- [ ] 🚨 seguros: columna nueva 'canal_venta'
- [ ] 🚨 tesorería: ARCHIVO FALTANTE
- [ ] 🚨 tarjetas: monto ~15% menor
- [ ] ✔ banca_corporativa: sin cambios significativos

Si detectó los 4: su pipeline está listo. Si no, pídanle a Copilot que corrija la lógica.

---

## Show & Tell (10 min)

Cada equipo presenta en **2 minutos**:
1. ¿Lograron que su pipeline corra sin modificar código?
2. **Muestren 1 alerta de cambio** que detectó su script
3. ¿El cuadre dio 100%? Si no, ¿qué encontraron?
4. ¿Qué pasaría si el mes que viene llegan 7 archivos en vez de 5?

---

## 🏆 Entregable final de la Sesión 3

1. **Mapa de equivalencias** — guardado en config/
2. **pipeline.py** — script reutilizable (depositar archivos y ejecutar)
3. **comparar_meses.py** — detección de cambios entre periodos con alertas
4. **Tabla de cuadre cruzado** — evidencia de que filas y montos cuadran
5. **Reporte de cambios** — comparación mes a mes con alertas 🚨
6. **consolidado_final.xlsx** — listo para usar
7. **(Bonus) Dashboard HTML** — con datos reales y tabla de cuadre

> 🎯 **Lo más valioso no es el consolidado de hoy — es tener el pipeline listo para el mes que viene.** La próxima vez que lleguen los correos, solo depositan archivos, ejecutan, y en 5 minutos tienen todo consolidado Y saben qué cambió.
