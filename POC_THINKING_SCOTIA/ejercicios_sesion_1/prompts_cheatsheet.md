# 🧠 Cheatsheet de Prompts — Microsoft 365 Copilot

> Guía rápida de prompts organizados por aplicación y caso de uso financiero/PM.

---

## 📊 Excel + Copilot

### Análisis de datos
```
"Resume esta tabla y muestra las estadísticas principales (promedio, total, máximo, mínimo)"
```
```
"¿Cuáles son las 10 filas con mayor monto? Ordénalas de mayor a menor"
```
```
"Identifica valores atípicos o transacciones con montos inusuales en esta tabla"
```
```
"Compara los totales del Q1 vs Q2 y muestra la variación porcentual"
```

### Fórmulas y cálculos
```
"Agrega una columna que calcule el IVA al 16% sobre la columna Monto"
```
```
"Crea una fórmula que clasifique el riesgo: si monto > 100,000 = Alto, si > 50,000 = Medio, si no = Bajo"
```
```
"Calcula el acumulado mensual (running total) de la columna Ventas"
```

### Tablas dinámicas y gráficos
```
"Crea una tabla dinámica que resuma el total por categoría y mes"
```
```
"Genera un gráfico de líneas que muestre la tendencia mensual de gastos"
```
```
"Crea un gráfico de barras comparando presupuesto vs real por departamento"
```

### Limpieza de datos
```
"Identifica filas duplicadas en esta tabla"
```
```
"Encuentra celdas vacías o con datos inconsistentes"
```
```
"Estandariza los nombres de la columna Proveedor (elimina espacios extra, unifica mayúsculas)"
```

---

## 📝 Word + Copilot

### Generación de documentos
```
"Redacta un business case ejecutivo con: problema, solución propuesta, beneficios esperados, cronograma estimado y presupuesto"
```
```
"Crea un documento de alcance (scope) para un proyecto de automatización de reportes financieros"
```
```
"Genera una minuta de reunión con: asistentes, temas tratados, acuerdos y próximos pasos"
```

### Resúmenes y análisis
```
"Resume este documento en un executive summary de máximo 1 página"
```
```
"Extrae los 5 puntos más importantes de este reporte"
```
```
"Identifica riesgos y dependencias mencionados en este plan de proyecto"
```

### Refinamiento de texto
```
"Reescribe este párrafo en un tono más ejecutivo y directo"
```
```
"Simplifica este texto técnico para que lo entienda un director financiero"
```
```
"Revisa la estructura de este documento y sugiere mejoras de organización"
```

### Plantillas y formatos
```
"Crea una plantilla de reporte mensual de finanzas con secciones para: resumen ejecutivo, ingresos, gastos, variaciones, proyecciones y recomendaciones"
```
```
"Genera un formato de propuesta de inversión con: justificación, análisis costo-beneficio, ROI esperado y riesgos"
```

---

## 📽️ PowerPoint + Copilot

### Crear presentaciones
```
"Crea una presentación de 8 slides sobre [tema] con diseño profesional"
```
```
"Transforma este documento de Word en una presentación ejecutiva"
```
```
"Genera un pitch deck para un comité directivo sobre un proyecto de automatización"
```

### Slides específicos
```
"Agrega un slide con un diagrama de flujo del proceso actual vs propuesto"
```
```
"Crea un slide de comparación antes/después con métricas clave"
```
```
"Agrega un slide de timeline con los hitos principales del proyecto"
```

### Refinamiento
```
"Mejora el diseño visual de esta presentación manteniendo el contenido"
```
```
"Agrega notas del presentador en cada slide con los puntos clave a mencionar"
```
```
"Resume esta presentación de 20 slides en una versión de 8 slides"
```

---

## 💬 Teams + Copilot

### Durante reuniones
```
"Resume lo discutido hasta ahora en esta reunión"
```
```
"¿Qué decisiones se han tomado?"
```
```
"Lista los action items mencionados con responsables"
```

### Post-reunión
```
"Genera un resumen completo de esta reunión"
```
```
"¿Cuáles fueron los temas principales y las conclusiones?"
```
```
"Crea una lista de seguimiento con fechas límite"
```

### En chats
```
"Resume las conversaciones de la última semana en este canal"
```
```
"¿Qué se decidió sobre [tema] en las últimas conversaciones?"
```
```
"Encuentra los archivos compartidos relacionados con [proyecto]"
```

---

## 🎯 Tips para mejores prompts

| Tip | Ejemplo malo | Ejemplo bueno |
|-----|-------------|---------------|
| **Sé específico** | "Analiza los datos" | "Analiza la tabla de gastos y muestra el top 5 por categoría" |
| **Da contexto** | "Haz un reporte" | "Genera un reporte mensual de gastos para el CFO con gráficos" |
| **Define formato** | "Resume esto" | "Resume en máximo 5 bullets de 1 línea cada uno" |
| **Itera** | (aceptar el primer resultado) | "Ahora hazlo más conciso y en tono ejecutivo" |
| **Usa roles** | "Escribe un email" | "Como PM, escribe un email de actualización de proyecto al sponsor" |

---

## 🔄 Patrón de prompt efectivo

```
[ROL] + [ACCIÓN] + [CONTEXTO] + [FORMATO] + [RESTRICCIONES]

Ejemplo:
"Como analista financiero, resume esta tabla de transacciones 
identificando los top 10 proveedores por monto total, 
en formato de tabla con columnas: Proveedor, Monto Total, % del Total,
sin incluir transacciones menores a $1,000"
```
