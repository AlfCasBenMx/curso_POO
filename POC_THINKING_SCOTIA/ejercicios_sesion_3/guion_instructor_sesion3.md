# 🎬 Guión del Instructor — Sesión 3
## "Automatización Python: Múltiples fuentes → Formato Global"

> **Duración total:** 3 horas (180 min)  
> **Formato:** Presencial o virtual (Teams)  
> **Audiencia:** PMs y profesionales financieros (sin experiencia previa en Python)  
> **Herramientas:** VS Code + GitHub Copilot + Python 3.9+ + pandas

---

## 📦 Materiales a preparar ANTES de la sesión

| # | Material | Acción requerida | Verificado |
|---|----------|-------------------|:---:|
| 1 | 12 archivos de entrada generados | Ejecutar `python generate_datasets_sesion3.py` en la carpeta ejercicios_sesion_3 | ☐ |
| 2 | Carpeta `datos_entrada/` compartida | Subir a OneDrive/SharePoint o distribuir ZIP por Teams | ☐ |
| 3 | `sesion3.html` abierto en navegador | Para mostrar agenda, flujo, prompts y ejemplos | ☐ |
| 4 | VS Code con GitHub Copilot funcionando | Verificar extensión activa, sesión de GitHub iniciada | ☐ |
| 5 | Python instalado con pandas y openpyxl | `pip install pandas openpyxl xlsxwriter` | ☐ |
| 6 | Script de solución `consolidar_solucion.py` | Tener listo como Plan B si algo falla en los labs | ☐ |
| 7 | Timer visible | Para respetar tiempos de cada actividad | ☐ |
| 8 | Excels de salida pre-generados | Tener los 3 consolidados + formato global listos como backup | ☐ |

### 🔒 Verificaciones técnicas (30 min antes)

- [ ] VS Code abre correctamente en tu máquina
- [ ] GitHub Copilot sugiere código al escribir un comentario
- [ ] `python --version` muestra 3.9 o superior
- [ ] `pip list` muestra pandas, openpyxl, xlsxwriter instalados
- [ ] Los 12 archivos de datos_entrada/ se leen sin error
- [ ] Internet estable (Copilot necesita conexión)
- [ ] Compartir pantalla funciona (si virtual)
- [ ] Tener **resultados pre-generados** como Plan B

---

## ⏱️ Cronograma minuto a minuto

| Minuto | Bloque | Actividad |
|--------|--------|-----------|
| 0:00–0:05 | **Apertura** | Bienvenida, recap Sesión 2, objetivos |
| 0:05–0:20 | **Bloque 1** | El problema de las múltiples fuentes |
| 0:20–0:35 | **Bloque 1** | Mapa de datos: 12 fuentes → 3 consolidados → 1 formato |
| 0:35–0:50 | **Bloque 1** | Intro a Python + pandas (5 conceptos clave) |
| 0:50–0:55 | **Transición** | Pausa + abrir VS Code |
| 0:55–1:15 | **Bloque 2** | Lab 1: Leer las 12 fuentes (20 min) |
| 1:15–1:40 | **Bloque 2** | Lab 2: Limpiar, homologar, consolidar (25 min) |
| 1:40–2:05 | **Bloque 2** | Lab 3: Formato Global (25 min) |
| 2:05–2:15 | **Bloque 2** | Lab 4: Validaciones y log (10 min) |
| 2:15–2:20 | **Transición** | Pausa + distribución de datasets personalizados |
| 2:20–2:45 | **Bloque 3** | Trabajo en célula (25 min) |
| 2:45–2:55 | **Bloque 3** | Revisión cruzada y demos (10 min) |
| 2:55–3:00 | **Cierre** | Retrospectiva del programa + entregables |

---

# 🟡 APERTURA (0:00 – 0:05)

## Qué decir:

> _"Bienvenidos a la última sesión del programa POC Thinking. En la Sesión 1 trabajamos con Excel y Power BI. En la Sesión 2 generamos HTMLs interactivos. Hoy vamos a dar el salto a Python — pero tranquilos, NO necesitan saber programar. GitHub Copilot va a programar por ustedes."_

> _"El problema de hoy es uno que seguro conocen: recibir información de 10, 12, 15 fuentes diferentes, cada una en su propio formato, y tener que consolidar todo en un solo entregable. Hoy vamos a automatizar eso."_

### Preguntas rompe-hielo:
- "¿Quién ha tenido que consolidar más de 5 archivos Excel en uno?" (manos arriba)
- "¿Cuánto tiempo les toma ese proceso? ¿Horas? ¿Días?"
- "¿Alguna vez un error de copiar-pegar les causó un problema serio?"

### Expectativas:
> _"Al terminar esta sesión, van a tener un script que hace en 30 segundos lo que hoy les toma 2-3 días. Y lo mejor: van a poder reproducirlo cada mes con solo ejecutar un comando."_

---

# 🎓 BLOQUE 1 — TEORÍA (0:05 – 0:50)

---

## 1.1 El problema de las múltiples fuentes (0:05 – 0:20) — 15 min

### Qué mostrar:
- Abrir `sesion3.html` en el navegador
- Mostrar la sección "El problema: Tengo 12 archivos y debo entregar 1 formato"
- Comparar proceso manual vs automatizado

### Qué decir:

> _"Imaginen esto: cada mes, les llegan 12 archivos de diferentes áreas. Banca Comercial manda un Excel con columnas que se llaman 'monto_MXN' y 'concepto_operacion'. Pero Banca Corporativa manda otro Excel donde las mismas columnas se llaman 'amount_MXN' y 'concept'. Y Seguros manda un tercero donde es 'importe' y 'tipo_operacion'."_

> _"Mismo dato, diferente nombre. ¿Les suena? Este es el problema #1 de la consolidación financiera."_

### Actividad interactiva (3 min):
> _"Levanten la mano — ¿cuántas fuentes de datos tienen que consolidar en su proceso actual?"_
> Anotar en el chat o pizarra las respuestas. Resaltar que el promedio suele ser 8-15.

---

## 1.2 Mapa de datos (0:20 – 0:35) — 15 min

### Qué mostrar:
- Sección del mapa de datos en sesion3.html
- Las 12 tarjetas de fuentes
- El diagrama de flujo: Fuentes → Python → 3 Consolidados → Formato Global

### Qué decir:

> _"Este es nuestro mapa. 12 fuentes entran: 10 son Excel, 2 son CSVs que vienen de queries a la base de datos SQL. El script de Python las lee todas, homologa los nombres, las clasifica en 3 categorías — Ingresos, Gastos y Provisiones — y genera los 3 Excels consolidados. Finalmente, genera el Formato Global que es el entregable final que va a la dirección."_

> _"El Formato Global tiene una estructura fija: conceptos en filas, líneas de negocio en columnas. Es lo que normalmente se llena celda por celda. Hoy lo vamos a generar automáticamente."_

---

## 1.3 Intro a Python + pandas (0:35 – 0:50) — 15 min

### 📌 IMPORTANTE — Postura del instructor:

> _"NO estamos aquí para aprender Python. Estamos aquí para entender lo suficiente como para DIRIGIR a GitHub Copilot. Piensen en ustedes como el director de orquesta — Copilot es el que toca los instrumentos."_

### Qué mostrar:
- Los 5 conceptos clave en sesion3.html (DataFrame, leer, filtrar, concatenar, pivot)
- Para cada uno, mostrar el código y explicar QUÉ hace (no CÓMO funciona)

### Guión para cada concepto:

**1. DataFrame:**
> _"Un DataFrame es una tabla. Idéntico a una hoja de Excel pero en memoria. Tiene filas y columnas."_

**2. Leer archivos:**
> _"Con una línea de código, Python lee un Excel completo. `pd.read_excel('archivo.xlsx')`. Eso es todo."_

**3. Filtrar:**
> _"Igual que poner un filtro en Excel. `df[df['tipo'] == 'Ingreso']` — me quedo solo con los ingresos."_

**4. Concatenar:**
> _"Es como copiar y pegar tablas una debajo de otra. `pd.concat([df1, df2, df3])`. Listo."_

**5. Pivot:**
> _"Tabla dinámica. Conceptos en filas, líneas de negocio en columnas, montos como valores."_

### Cierre de la teoría:
> _"Estos 5 conceptos son todo lo que necesitan. No memoricen el código — Copilot lo escribe por ustedes. Ustedes solo necesitan saber QUÉ pedirle."_

---

# 🔬 BLOQUE 2 — LABS (0:55 – 2:15)

---

## 2.1 Lab 1: Leer las 12 fuentes (0:55 – 1:15) — 20 min

### Setup (primeros 3 min):
1. Asegurar que todos tengan VS Code abierto
2. Verificar que la carpeta `datos_entrada/` está accesible
3. Crear un archivo nuevo: `paso1_leer.py`

### Demo en vivo (5 min):
Abrir VS Code, crear archivo, escribir este comentario:

```python
# Leer todos los archivos .xlsx de la carpeta datos_entrada/
# Mostrar nombre, número de filas y columnas de cada uno
```

Dejar que Copilot genere el código. Ejecutar. Mostrar la salida.

> _"Ven? Un comentario. Enter. Copilot escribe. Tab para aceptar. Ya está."_

### Trabajo individual (12 min):
Los participantes replican lo mismo en su máquina. Circular por las mesas (o monitorear chats).

### Errores comunes en este lab:
- Python no instalado → `pip` no reconocido → Instalar Python
- pandas no instalado → `pip install pandas openpyxl`
- Ruta incorrecta → Verificar que `datos_entrada/` esté en la misma carpeta que el script
- Copilot no sugiere → Verificar extensión activa, internet funcionando

### Validación grupal (2 min):
> _"¿Cuántos archivos leyeron? Deben ser 12. ¿Quién tiene 12? Perfecto. ¿Quién tuvo errores?"_

---

## 2.2 Lab 2: Homologar y consolidar (1:15 – 1:40) — 25 min

### Demo (5 min):
Mostrar el problema: abrir 2-3 archivos y señalar que las columnas se llaman diferente.

```python
# banca_comercial tiene: "monto_MXN"
# seguros tiene: "importe"
# inversiones tiene: "amount"
# ¡Son el mismo dato!
```

Escribir el prompt de mapeo y dejar que Copilot genere el diccionario.

### Trabajo individual (15 min):
Los participantes crean `paso2_homologar.py` y `paso3_consolidar.py`.

### Tips para el instructor:
- Si alguien se atora con el mapeo: darles el diccionario completo del cheatsheet
- Si Copilot genera un mapeo incompleto: pedirle "agrega el mapeo para los archivos que faltan"
- Recordar: "Si el prompt no funciona, hazlo más específico. Dile EXACTAMENTE qué columnas tiene cada archivo."

### Validación:
> _"¿Cuántas filas tiene su DataFrame consolidado? Debe ser la suma de todas las fuentes (~876 filas). ¿Las columnas son uniformes?"_

---

## 2.3 Lab 3: Formato Global (1:40 – 2:05) — 25 min

### Demo (5 min):
Mostrar el prompt del Formato Global. Copilot debe generar el pivot_table.

> _"Este es el momento estrella. Un pivot_table en Python hace lo mismo que pasar 3 días armando la tabla manualmente."_

### Trabajo individual (15 min):
Crear `paso4_formato_global.py`. El reto es que el formato del Excel sea profesional.

### Tips:
- Si el pivot sale vacío → Verificar que la columna de clasificación esté correcta
- Si faltan líneas de negocio → Verificar el mapeo de homologación
- Para formato → Usar el prompt del cheatsheet sobre formato Excel profesional

### Validación:
> _"Abran el formato_global.xlsx en Excel. ¿Tiene 6 líneas de negocio como columnas? ¿Tiene filas de subtotal? ¿La fila de Resultado Neto está al final?"_

---

## 2.4 Lab 4: Validaciones (2:05 – 2:15) — 10 min

### Demo rápida (3 min):
Mostrar cómo agregar una validación simple: contar nulos.

### Trabajo (7 min):
Los participantes crean `paso5_validaciones.py` con al menos 2 validaciones.

---

# 👥 BLOQUE 3 — TRABAJO EN CÉLULA (2:20 – 2:55)

---

## 3.1 Trabajo en célula (2:20 – 2:45) — 25 min

### Qué decir:
> _"Ahora es su turno. Cada célula toma su Ficha de Problema de la Sesión 1 y adapta este pipeline a su caso real. No necesitan 12 fuentes — empiecen con 2 o 3. Lo importante es que el flujo funcione: leer → homologar → clasificar → consolidar → formato de salida."_

### Circular entre equipos:
- Ayudar con mapeo de columnas (el 80% de los problemas)
- Si un equipo no tiene datos reales: usar los datos de ejemplo pero cambiar las reglas de clasificación
- Recordar: "Copilot es su programador. Escriban qué quieren como comentario."

---

## 3.2 Revisión cruzada (2:45 – 2:55) — 10 min

### Dinámica:
Cada célula le muestra su script y resultado a la célula de al lado. Usan el checklist de `sesion3.html`.

---

# 🏁 CIERRE (2:55 – 3:00)

### Qué decir:

> _"Felicidades. En 3 sesiones pasaron de no saber qué era un POC... a tener un script de Python que automatiza un proceso que les tomaba días. Piensen en lo que pueden hacer con esto."_

> _"Sesión 1: aprendieron a analizar datos con Copilot. Sesión 2: aprendieron a presentar resultados sin PowerPoint. Sesión 3: aprendieron a automatizar consolidación de múltiples fuentes."_

> _"Esto es POC Thinking: demostrar que una idea es viable con las herramientas que existen HOY."_

### Entregables finales:
1. Los 3 Excels consolidados
2. El Formato Global
3. El script de consolidación
4. El log de excepciones

### Próximos pasos sugeridos:
- Aplicar el script a datos reales del mes actual
- Agregar más fuentes incrementalmente
- Programar ejecución automática (Task Scheduler o cron)
- Versionar el script con Git

---

## 🆘 Plan B — Si algo falla

| Escenario | Plan B |
|-----------|--------|
| Python no se instala | Usar Google Colab (notebook en navegador, cero instalación) |
| GitHub Copilot no funciona | Usar Copilot Chat web (copilot.microsoft.com) para generar código, copiar a VS Code |
| Los archivos no se leen | Tener los Excels de salida pre-generados y hacer la demo desde ahí |
| Internet se cae | Tener el script de solución listo localmente, ejecutar sin Copilot |
| Un participante se atora | Darle el script de solución de un paso específico |

---

## 📊 Métricas de éxito de la sesión

| Indicador | Meta |
|-----------|------|
| Participantes que leyeron los 12 archivos | > 80% |
| Participantes que generaron al menos 1 consolidado | > 70% |
| Participantes que generaron el Formato Global | > 60% |
| Equipos que adaptaron su propio caso | > 50% |
| Satisfacción general (encuesta post) | > 4.0 / 5.0 |
