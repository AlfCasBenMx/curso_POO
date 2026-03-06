# 🧠 Cheatsheet de Prompts — Sesión 3: Pipeline mensual con Copilot 365

> Guía rápida de prompts para usar en **copilot.microsoft.com**.
> Adjunta tus archivos Excel y usa estos prompts como base. Ajústalos a tu caso.

---

## 📥 Exploración de archivos

### Pedir resumen de estructura
```
Tengo estos [N] archivos Excel. Para cada uno dame:
- Nombre del archivo
- Número de filas y columnas
- Lista completa de columnas
- Las primeras 2 filas de ejemplo
```

### Verificar que Copilot leyó bien
```
Dame un resumen para verificar:
- Tabla: Archivo | Filas | Columnas | Suma de monto
- ¿Hay archivos con filas vacías?
- ¿Hay archivos con menos columnas de lo esperado?
```

### Crear mapa de equivalencias
```
Haz un MAPA DE EQUIVALENCIAS de columnas.
Tabla: Columna estándar | Archivo1 | Archivo2 | Archivo3 | ...
Hazlo para TODAS las columnas que se puedan mapear.
```

---

## 🔀 Homologación con verificación

### Script con prints de verificación
```
Genera un script Python que homologue los [N] archivos usando el mapa.
Para CADA archivo imprimir: filas antes/después, columnas antes/después,
primeras 3 filas del resultado. Tabla resumen al final.
Si alguna columna no existe, pon NaN y agrégalo a un log de excepciones.
```

### Revisar antes de ejecutar
```
EXPLÍCAME paso a paso qué hace este script.
Para cada bloque: qué hace, qué podría salir mal, cómo lo verifico.
```

### Cuando algo no cuadra
```
El archivo '[nombre]' debería tener $[monto] en total,
pero después de la homologación dice $[otro monto]. ¿Qué pasó?
¿Se perdieron filas? ¿Hay NaN? Muéstrame las filas que no se consolidaron.
```

---

## 🔢 Conteo y cuadre

### Pruebas de cuadre
```
Imprime PRUEBAS DE CUADRE:
- Total filas consolidado vs suma de filas individuales
- Suma de 'monto' en consolidado vs suma por archivo_origen
- Cuántas filas tienen monto vacío/NaN
- Valores únicos en 'archivo_origen' (deben ser exactamente [N])
```

### Tabla de cuadre cruzado
```
Genera tabla de cuadre cruzado:
| Archivo | Filas original | Filas consolidado | ¿Cuadra? | Monto original | Monto consolidado | ¿Cuadra? |
Si algo tiene ✘, EXPLÍCAME por qué.
```

### Cuadre de clasificación
```
¿Cuántos registros quedaron en cada categoría (Ingreso/Gasto/Provisión/Sin clasificar)?
La suma de todas las categorías debe ser = total del consolidado. ¿Cuadra?
```

---

## 👀 Antes / Después

### Comparar transformaciones
```
Muéstrame las primeras 5 filas ANTES de la transformación y DESPUÉS. Side by side.
```

```
Muéstrame los nombres de columnas ANTES y DESPUÉS del renombrado.
```

---

## 🚨 Excepciones y anomalías

### Detectar problemas
```
¿Hay filas con valores vacíos en [columna]? ¿Cuántas? Muéstrame 5 ejemplos.
```

```
¿Hay montos negativos? ¿Hay montos extremadamente altos (> $10M)? Muéstralos.
```

```
¿Hay filas que no se consolidaron? ¿Dónde están? ¿Por qué se descartaron?
```

---

## 🔁 Pipeline reutilizable

### Hacer el script reutilizable
```
Haz el script REUTILIZABLE:
1. Leer TODOS los .xlsx de una carpeta (sin hardcodear nombres)
2. Leer config desde un JSON (mapa de equivalencias + reglas)
3. Carpeta del mes como PARÁMETRO
4. Guardar consolidado con fecha en el nombre
5. Generar log de cuadre automático
El mes que viene solo pongo archivos nuevos en la carpeta y corro el script.
```

### Estructura de carpetas
```
Crea estructura de carpetas para un pipeline mensual:
pipeline_consolidacion/
├── config/ (mapa + reglas en JSON)
├── datos/ (subcarpeta por mes)
├── salida/ (consolidados por mes)
├── logs/ (logs de ejecución)
├── pipeline.py
└── comparar_meses.py
```

### Manejar errores sin parar
```
Agrega try/except que no pare la ejecución sino que guarde los errores en un log.
Si un archivo falla, que los demás sigan procesándose.
```

---

## 🔍 Detección de cambios entre periodos

### Comparar 2 meses
```
Compara el consolidado de [mes1] vs [mes2]:
- ¿Qué archivos son nuevos? ¿Cuáles faltan?
- Para cada archivo: filas y montos de ambos meses. 🚨 si cambio > ±20%.
- ¿Columnas nuevas o eliminadas en algún archivo?
- ¿Categorías nuevas en 'tipo' que no existían el mes pasado?
```

### Resumen ejecutivo de cambios
```
Genera un resumen ejecutivo:
- Total de alertas
- Las 3 alertas más críticas
- Recomendación: ¿Se puede confiar en el consolidado o hay que investigar?
```

### Simular cambios para probar
```
Crea versiones modificadas de los archivos con estos cambios:
1. [archivo1]: agregar 50 filas más
2. [archivo2]: agregar columna nueva
3. [archivo3]: NO incluir (simular que no llegó)
4. [archivo4]: reducir montos ~15%
Para probar que el script de comparación detecta TODO.
```

---

## 📊 Dashboard HTML

### Generar dashboard con datos reales
```
Con los resultados del consolidado, genera un HTML tipo dashboard:
- KPIs: archivos procesados, registros totales, monto consolidado
- Tabla de cuadre cruzado con ✔ y ✘
- Gráfico CSS de barras por archivo_origen
- Tabla de excepciones
Estilo corporativo, azul #0F62FE y amarillo #FFCD00.
```

---

## 🧠 Entender antes de ejecutar

### Pedir explicación
```
Explícame paso a paso qué hace este script. ¿Qué podría salir mal en cada paso?
```

```
¿Qué supuestos estás haciendo? ¿Qué pasa si uno de los archivos no tiene la columna X?
```

### Si hay error al ejecutar
```
Al ejecutar tu script me sale este error: [pegar error].
Corrígelo y dame el script completo corregido.
```

### Preguntar por robustez
```
Si corro este script el mes que viene con archivos nuevos, ¿qué podría fallar?
¿Cómo lo hago más robusto?
```
