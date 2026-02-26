# 🎬 Guión del Instructor — Sesión 1
## "Ideación y datos con Excel y Power BI"

> **Duración total:** 3 horas (180 min)  
> **Formato:** Presencial o virtual (Teams)  
> **Audiencia:** PMs y profesionales financieros (sin experiencia en programación)  
> **Herramientas:** Microsoft 365 Copilot (Excel, Power BI), OneDrive

---

## 📦 Materiales a preparar ANTES de la sesión

| # | Material | Acción requerida | Verificado |
|---|----------|-------------------|:---:|
| 1 | `gastos_departamentales.xlsx` (315 filas) | Subir a carpeta compartida en OneDrive/SharePoint. Ya tiene formato de Tabla. | ☐ |
| 2 | `ficha_problema.md` | Imprimir 1 por equipo O compartir como archivo editable | ☐ |
| 3 | `sesion1.html` abierto en navegador | Para mostrar agenda, prompts y tipología | ☐ |
| 4 | Excel con `gastos_departamentales.xlsx` abierto (ya tiene formato Tabla) | Verificar que Copilot aparece al abrir | ☐ |
| 5 | Power BI Desktop con `gastos_departamentales.xlsx` cargado | Tener un dashboard pre-construido como backup | ☐ |
| 7 | Timer visible (pantalla o teléfono) | Para respetar tiempos de cada actividad | ☐ |
| 8 | Slide de respaldo (PPT o imagen) con el pipeline | Excel → PBI → Word → PPT visual | ☐ |

### 🔒 Verificaciones técnicas (30 min antes)

- [ ] Tu licencia de Copilot 365 funciona — abre Excel, verifica ícono de Copilot
- [ ] Tu licencia de Power BI Pro/Premium con Copilot funciona
- [ ] Los archivos CSV están en OneDrive y Autoguardado está ON
- [ ] gastos_departamentales.xlsx abierto y se ve el formato de Tabla (ya viene pre-formateado)
- [ ] Power BI conecta correctamente al archivo
- [ ] Internet estable (hacer speed test)
- [ ] Compartir pantalla funciona (si virtual)
- [ ] Tener **resultados pre-calculados** en un Excel separado como Plan B

---

## ⏱️ Cronograma minuto a minuto

| Minuto | Bloque | Actividad |
|--------|--------|-----------|
| 0:00–0:05 | **Apertura** | Bienvenida y expectativas |
| 0:05–0:15 | **Bloque 1** | ¿Qué es un POC? |
| 0:15–0:30 | **Bloque 1** | Intro a Copilot 365 + demo rápida |
| 0:30–0:40 | **Bloque 1** | Alcances y limitaciones |
| 0:40–0:50 | **Bloque 1** | Tipología de POCs |
| 0:50–1:00 | **Bloque 1** | Formación inicial de células |
| 1:00–1:05 | **Transición** | Pausa + preparación de Excel |
| 1:05–1:45 | **Bloque 2A** | Lab Excel con Copilot (40 min) |
| 1:45–2:05 | **Bloque 2B** | Demo Power BI (20 min) |
| 2:05–2:10 | **Transición** | Pausa + distribución de Fichas |
| 2:10–2:25 | **Bloque 3** | Formación de equipos definitiva (15 min) |
| 2:25–2:55 | **Bloque 3** | Taller de descubrimiento (30 min) |
| 2:55–3:10 | **Bloque 3** | Pitch rápido por equipo (15 min) |
| 3:10–3:15 | **Mini-POC** | 🚀 Briefing Ejecutivo en vivo (5 min) |
| 3:15–3:20 | **Cierre** | Entregables + preview Sesión 2 |

---

# 🟡 APERTURA (0:00 – 0:05)

## Qué decir:

> _"Bienvenidos al programa POC Thinking con Microsoft 365 Copilot. En las próximas 3 sesiones vamos a pasar de una idea a un caso de negocio viable, usando las herramientas que ya conocen — Excel, Power BI, Word y PowerPoint — pero potenciadas con inteligencia artificial."_

> _"Hoy es la sesión más importante porque vamos a sentar las bases: vamos a entender qué es un POC, van a experimentar con Copilot en Excel y Power BI, y al final van a identificar un problema REAL de su día a día que vamos a convertir en su proyecto del curso."_

### Preguntas rompe-hielo (elegir 1-2):
- "¿Quién ha usado Copilot en Excel alguna vez?" (manos arriba)
- "¿Quién pasa más de 2 horas a la semana en tareas repetitivas en Excel?" (manos arriba)
- "¿Alguien ha hecho un POC o piloto en su área?"

### 📋 Expectativas rápidas:
> _"Este NO es un curso de programación. No van a escribir código. Todo lo que haremos será con lenguaje natural — escribir instrucciones como si le pidieran algo a un asistente inteligente."_

---

# 🎓 BLOQUE 1 — TEORÍA (0:05 – 1:00)

---

## 1.1 ¿Qué es un POC? (0:05 – 0:15) — 10 min

### Qué decir:

> _"Un POC — Proof of Concept — es un experimento acotado. NO es un producto terminado, NO es un sistema completo. Es la pregunta: '¿esto funciona?' respondida con evidencia real."_

### Puntos clave a cubrir:
1. **Definición simple:** Prueba rápida de valor antes de invertir recursos completos
2. **Por qué importa para PMs/financieros:**
   - Reduce riesgo → no comprometes presupuesto sin evidencia
   - Genera evidencia tangible → convences a tomadores de decisión
   - Alinea expectativas → negocio y tecnología hablan el mismo idioma
   - Iterar rápido → feedback real en días, no meses

### 💬 Ejemplo para conectar:

> _"Imaginen que quieren proponer automatizar la conciliación bancaria. Tienen dos opciones: (A) pedir un proyecto de 6 meses y $500K, o (B) hacer un POC en 2 semanas con datos de muestra que demuestre que el 80% del proceso se puede automatizar. ¿Cuál aprueba más fácil un CFO?"_

### ✅ Verificación: 
Preguntar: _"¿Alguien puede dar un ejemplo de algo que hayan querido probar pero les dijeron 'es muy caro' o 'es muy riesgoso'?"_ — Anotar 2-3 ejemplos en pizarrón/chat.

---

## 1.2 Intro a Copilot 365 (0:15 – 0:30) — 15 min

### Qué decir:

> _"Microsoft 365 Copilot es un asistente de IA integrado en las apps que ya usan. No es una app separada — está dentro de Excel, Word, PowerPoint y Teams. Funciona con 'prompts': instrucciones en lenguaje natural."_

### 📊 Diagrama — Mostrar en pantalla:

Abrir `sesion1.html` → sección "¿Qué es Microsoft 365 Copilot?" → mostrar el diagrama de arquitectura y los 5 recuadros.

```
                    ┌─────────────────────────────────┐
                    │                                 │
                    │    🧠  Microsoft 365 Copilot    │
                    │    ───────────────────────────   │
                    │    Motor de IA (GPT) integrado   │
                    │    en las apps que ya usas        │
                    │                                 │
                    └────────────┬────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │    Funciona con PROMPTS  │
                    │  (instrucciones en texto │
                    │    en lenguaje natural)  │
                    └────────────┬────────────┘
                                 │
          ┌──────────┬───────────┼───────────┬──────────┐
          │          │           │           │          │
          ▼          ▼           ▼           ▼          ▼
     ┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
     │ 📊      ││ 📈      ││ 📝      ││ 📽️      ││ 💬      │
     │ Excel   ││Power BI ││  Word   ││  PPT    ││ Teams   │
     │         ││         ││         ││         ││         │
     │Fórmulas ││Q&A  ✅  ││Redactar ││Slides   ││Resumir  │
     │Tablas   ││Smart ✅ ││Resumir  ││Diseñar  ││Action   │
     │Gráficos ││Narrative││Reportes ││Visuales ││Items    │
     │         ││         ││         ││         ││         │
     │🔑 M365  ││⚠️ Copilot││🔑 M365  ││🔑 M365  ││🔑 M365  │
     │ Copilot ││Premium/ ││ Copilot ││ Copilot ││ Copilot │
     │         ││Fabric   ││         ││         ││         │
     └─────────┘└─────────┘└─────────┘└─────────┘└─────────┘

     ✅ = Gratis (nativo, sin licencia adicional)
     🔑 = Requiere licencia Microsoft 365 Copilot
     ⚠️ = Copilot DENTRO de PBI requiere Premium/Fabric
         (Q&A y Smart Narrative son GRATIS — es lo que usamos en el curso)

     ┌──────────────────────────────────────────────────────┐
     │  📁 OneDrive / SharePoint                            │
     │  (Todos los archivos DEBEN estar aquí)               │
     └──────────────────────────────────────────────────────┘
```

> 💡 **Señalar cada app** mientras dices: _"Copilot NO es una app nueva. Es UNA inteligencia que vive DENTRO de cada app. Es como tener un asistente sentado al lado en Excel, otro en Word, otro en PPT..."_

### Demo relámpago (5 min dentro de este bloque):

**Abrir Excel con `gastos_departamentales.xlsx` (ya viene como Tabla — no necesitan Ctrl+T).**

1. Click en ícono de Copilot
2. Escribir: `"Describe esta tabla"`
3. Mostrar la respuesta — Copilot describe las columnas, el número de filas, los tipos de datos

> _"¿Ven? No escribí una fórmula. No usé menús. Le pedí en español que describiera los datos y me dio un resumen. Esto es Copilot."_

### 🛟 Plan B si Copilot no responde:
- Esperar 10 segundos y reintentar
- Si falla, cambiar a inglés: `"Describe this table"`
- Si sigue fallando, mostrar un screenshot pre-guardado del resultado esperado y decir: _"Copilot puede tardar. Aquí está el resultado que obtuve preparando la sesión. Veamos cómo se ve."_

### Transición:

> _"Ahora que vimos qué puede hacer, hablemos de qué NO puede hacer — porque esto es igual de importante."_

---

## 1.3 Alcances y limitaciones (0:30 – 0:40) — 10 min

### Qué decir:

> _"Copilot es poderoso pero NO es mágico. Conocer sus límites les va a ahorrar MUCHA frustración. Vamos a ver qué SÍ puede y qué NO puede."_

### Mostrar en pantalla:
`sesion1.html` → sección "Alcances y limitaciones" → grid verde/rojo

### Puntos críticos a enfatizar (con énfasis físico — señalar, pausar):

| # | Limitación | Cómo explicar | Demo/Ejemplo |
|---|-----------|---------------|--------------|
| 1 | **Ctrl+T obligatorio** | _"Si sus datos no están formateados como Tabla, Copilot los IGNORA. Es como hablarle a alguien con audífonos — no te oye."_ | Mostrar Excel: seleccionar datos SIN Ctrl+T → abrir Copilot → mostrar que dice "No puedo analizar" o no da resultados útiles |
| 2 | **OneDrive obligatorio** | _"Si abren el archivo desde el escritorio, Copilot no aparece. El archivo DEBE estar en OneDrive o SharePoint."_ | Si aplica, mostrar la diferencia |
| 3 | **No tiene memoria** | _"Cada prompt es independiente. Copilot no recuerda lo que le pidieron hace 5 minutos. Si necesitan contexto, inclúyanlo en el prompt."_ | — |
| 4 | **~5,000 filas** | _"Funciona bien hasta ~5K filas. Con datasets más grandes, puede dar resultados parciales o incompletos."_ | Nuestros datasets son 315 y 82 filas — perfectos |
| 5 | **No genera código** | _"No va a escribir macros ni VBA. No reemplaza a GitHub Copilot ni a un programador."_ | — |
| 6 | **Español < Inglés** | _"Los modelos de lenguaje son mejores en inglés. Si un prompt en español falla, pruébenlo en inglés."_ | — |

### 3 Reglas de oro (repetir con énfasis):
1. **Un prompt = una tarea.** _"No le pidan 5 cosas a la vez."_
2. **Siempre verifica.** _"Copilot puede inventar datos. SIEMPRE revisen."_
3. **Plan B en inglés.** _"Si falla en español, prueben en inglés."_

### ✅ Verificación:
Preguntar: _"¿Cuál de estas limitaciones creen que les va a afectar más en su trabajo diario?"_ — Anotar respuestas.

---

## 1.4 Tipología de POCs (0:40 – 0:50) — 10 min

### Qué decir:

> _"No todos los POCs son iguales. Clasificarlos nos ayuda a elegir la herramienta correcta y a medir éxito de forma diferente."_

### Mostrar en pantalla:
`sesion1.html` → tabla de tipología

### Recorrer cada tipo con ejemplo concreto:

| Tipo | Ejemplo que dar | Herramienta principal |
|------|----------------|----------------------|
| **Automatización financiera** | _"Imaginen que cada mes concilian 500 transacciones manualmente. Un POC de automatización probaría si Copilot puede marcar las diferencias automáticamente."_ | Excel + Copilot |
| **De Datos** | _"Tienen 3 años de datos de gastos y nadie los ha analizado. Un POC de datos valida si hay patrones útiles — como departamentos que siempre se pasan del presupuesto."_ | Excel + Power BI |
| **De Texto / IA** | _"Reciben 50 contratos al mes y necesitan extraer cláusulas clave. Un POC de texto prueba si Copilot puede resumirlos correctamente."_ | Word + Copilot |
| **De Experiencia** | _"Su CFO pide un dashboard mensual de KPIs. Un POC de experiencia valida si Copilot puede generar una presentación ejecutiva convincente."_ | PPT + Power BI |

### 💡 Consejo didáctico:
Después de presentar la tabla, preguntar: _"¿Qué tipo de POC creen que aplicaría a su trabajo? Levanten la mano por tipo"_ → hacer conteo rápido. Esto anticipa el Bloque 3.

---

## 1.5 Formación inicial de células (0:50 – 1:00) — 10 min

### Qué decir:

> _"Ahora vamos a formar las células de trabajo. En el Bloque 3 van a profundizar, pero por ahora necesito que se organicen para hacer el lab de Excel juntos."_

### Instrucciones paso a paso:

1. **Formar equipos de 4-6 personas** (dejar que se auto-organicen o asignar si son tímidos)
2. **Asignar roles preliminares:**
   - Product Owner (1-2): el que tiene el problema más claro
   - PM / Líder (1): el que mejor organiza
   - Analistas (2-3): los que van a hacer el trabajo en Excel
3. **Cada equipo elige un nombre** (opcional pero divertido — energiza el grupo)

### ⏱️ Timing:
- 0:50–0:53: Instrucciones
- 0:53–0:58: Formación de equipos
- 0:58–1:00: Verificar que todos tengan equipo

### 🛟 Si hay problemas:
- **Alguien solo:** asignarlo al equipo más pequeño
- **Equipos muy grandes (>6):** dividir en dos
- **Nadie quiere ser PO:** decir que el PO es el que más se queja de un proceso — eso suele motivar 😄

---

## 🔄 TRANSICIÓN (1:00 – 1:05) — 5 min

### Qué decir:

> _"Excelente. Ahora viene lo divertido — vamos a usar Copilot. Tómense 5 minutos para:"_
> 1. _"Ir al baño si necesitan"_
> 2. _"Abrir Excel"_
> 3. _"Abrir el archivo gastos_departamentales.xlsx DESDE OneDrive — ya tiene formato de Tabla, NO necesitan hacer Ctrl+T"_
> 5. _"Verificar que Autoguardado esté ON"_
> 6. _"Verificar que ven el ícono de Copilot"_

### ⚠️ Caminar entre los equipos (si presencial) o preguntar en chat (si virtual):
_"¿Quién ya tiene el archivo abierto como Tabla? ¿Quién ve el ícono de Copilot?"_

### 🚨 Problemas comunes en este momento:
| Problema | Solución |
|----------|----------|
| No encuentran el archivo | Compartir el link de OneDrive por chat |
| No ven el ícono de Copilot | Verificar que abrieron DESDE OneDrive, no desde una descarga local |
| Autoguardado está OFF | Click en el toggle superior izquierdo de Excel |
| No saben hacer Ctrl+T (si usan sus propios datos) | Mostrar en pantalla: seleccionar A1 → Ctrl+T → check "Mi tabla tiene encabezados" → Aceptar. Los .xlsx del curso ya vienen como Tabla. |
| El archivo se abre como solo lectura | Hacer una copia en su OneDrive personal |

---

# 🔬 BLOQUE 2A — LAB EXCEL CON COPILOT (1:05 – 1:45) — 40 min

---

### Formato: **Guiado** (instructor hace, alumnos replican)

### Qué decir al inicio:

> _"Este lab es guiado. Yo voy a mostrar cada prompt en pantalla, ustedes lo replican en su Excel. Si obtienen un resultado diferente al mío, está bien — Copilot puede variar. Lo importante es el proceso, no el resultado exacto."_

> _"Vamos a trabajar con el archivo gastos_departamentales.xlsx — tiene 315 filas de presupuestos vs gastos reales de 6 departamentos durante 2025. El archivo ya viene formateado como Tabla de Excel, así que Copilot lo reconoce directamente."_

---

## Ejercicio 1 — Resumen de datos (1:05 – 1:12) — 7 min

### Qué hacer:
1. Abrir panel de Copilot en Excel (cinta de opciones → ícono Copilot)
2. Escribir el prompt (mostrar en pantalla):

```
📊 "Resume esta tabla y muestra las estadísticas principales: promedio, total, máximo y mínimo de Presupuesto_MXN y Gasto_Real_MXN por Departamento"
```

3. Esperar respuesta (10-20 seg)
4. Copilot muestra el resultado en el panel o genera un archivo nuevo
5. Si genera archivo nuevo → abrir/descargar → mostrar al grupo
6. Analizar el resultado con el grupo

### Resultado esperado:
- Copilot muestra una tabla resumen con totales y promedios por departamento (puede ser en el panel lateral o en un archivo descargable)
- Debería identificar que hay 6 departamentos, 315 filas, datos de 2025

### 💬 Qué comentar:

> _"Fíjense que mencioné las columnas por nombre — Presupuesto_MXN y Gasto_Real_MXN. Esto es clave: entre más específico el prompt, mejor el resultado."_

### 🛟 Plan B:
- Si Copilot da un resumen genérico: _"Sé más específico: menciona columnas por nombre"_
- Si no responde: Prompt en inglés: `"Summarize this table showing average, total, max and min of Presupuesto_MXN and Gasto_Real_MXN grouped by Departamento"`
- **Backup total:** Mostrar resultado pre-calculado y pasar al siguiente ejercicio

---

## Ejercicio 2 — Tabla dinámica (1:12 – 1:19) — 7 min

### Qué hacer:
```
📊 "Crea una tabla dinámica que resuma el total de Gasto_Real_MXN por Departamento y por Mes"
```

### Resultado esperado:
- Copilot crea una tabla dinámica (PivotTable) en una hoja nueva
- Departamentos en filas, Meses en columnas, valores = suma de Gasto_Real_MXN

### 💬 Qué comentar:

> _"Esto normalmente toma 3-4 clics manuales y saber dónde están las opciones. Con un prompt lo hicieron en 10 segundos."_

> _"Tip: si la tabla dinámica no sale como esperaban, pueden pedir: 'Modifica la tabla dinámica para poner los Meses en filas en lugar de columnas'."_

### 🛟 Plan B:
- Si Copilot no crea tabla dinámica sino un resumen textual: agregar _"Quiero una PivotTable, no un resumen en texto"_
- **Backup:** Crear la tabla dinámica manualmente en 1 minuto mostrando el proceso clásico, y decir: _"Copilot a veces prefiere dar texto. Cuando eso pase, especifiquen el formato deseado."_

---

## Ejercicio 3 — Fórmulas con Copilot (1:19 – 1:25) — 6 min

### Qué hacer:
```
📊 "Agrega una columna llamada IVA_MXN que calcule el 16% de Gasto_Real_MXN"
```

### Resultado esperado:
- Copilot genera un **nuevo archivo** con la columna `IVA_MXN` ya agregada
- Descargar/abrir → verificar la fórmula: debería ser `=[@[Gasto_Real_MXN]]*0.16` o valores calculados
- La fórmula se aplica a todas las filas

### 💬 Qué comentar:

> _"Copilot generó un archivo nuevo con la columna ya calculada. Observen los valores — debería ser el 16% de cada Gasto_Real. Si quieren ver la fórmula, hagan click en una celda de la nueva columna."_

> _"Usa la sintaxis de Tabla estructurada — los corchetes con [@columna]. Esto es Excel nativo, no código. Copilot no inventa — usa fórmulas reales de Excel."_

### 🛟 Plan B:
- Si agrega la columna pero con valores, no fórmula: aceptable — el resultado es correcto
- Si no funciona: escribir manualmente `=[@[Gasto_Real_MXN]]*0.16` en la primera celda → Enter

---

## Ejercicio 4 — Reglas de negocio (1:25 – 1:33) — 8 min

### Qué hacer:
```
📊 "Agrega una columna Alerta_Variacion: si Variacion_Pct > 20 = '🔴 Excedido', si > 10 = '🟡 Atención', si no = '🟢 OK'"
```

### Resultado esperado:
- Copilot genera un **nuevo archivo** con la columna de alertas
- Descargar/abrir → verificar que tiene emojis o texto indicando el nivel de alerta
- Fórmula tipo `=IFS([@[Variacion_Pct]]>20, "🔴 Excedido", [@[Variacion_Pct]]>10, "🟡 Atención", TRUE, "🟢 OK")`

### 💬 Qué comentar:

> _"Abran el archivo que generó Copilot. ¿Ven la columna de alertas? Este es un caso de uso REAL para PMs y financieros: implementar semáforos de control sin código, sin macros, sin IT. Solo un prompt."_

> _"¿Ven cómo le di la lógica de negocio en lenguaje natural? 'Si mayor a 20 = Excedido'. Copilot la tradujo a una fórmula IFS."_

> _"Recuerden: su archivo original sigue intacto. Si quieren conservar estos cambios, guarden el nuevo archivo o copien la columna a su archivo original."_

### 🛟 Plan B:
- Si los emojis no aparecen: cambiar a texto simple ("Excedido", "Atención", "OK")
- Si no responde en español:
```
🔄 Plan B (inglés): "Add a column Alerta_Variacion: if Variacion_Pct > 20 = 'Exceeded', if > 10 = 'Warning', otherwise = 'OK'"
```
- **Backup:** Escribir la fórmula IFS manualmente y explicar qué hizo

---

## Ejercicio 5 — Detección de anomalías (1:33 – 1:39) — 6 min

### Qué hacer:
```
📊 "Identifica filas con Variacion_Pct mayor a 50% o menor a -30%. ¿Hay filas duplicadas con mismo Departamento, Categoria_Gasto y Mes?"
```

### Resultado esperado:
- Copilot muestra los resultados en el panel lateral o genera un **nuevo archivo** resaltando las filas
- Señala los outliers (hay ~5% intencionales: variaciones de 50%, 80%, -70%)
- Identifica 3 duplicados intencionales

### 💬 Qué comentar:

> _"Esto es detective de datos. En un dataset de 315 filas a simple vista no ves los outliers ni los duplicados. Copilot los encuentra en segundos."_

> _"Si les generó un archivo nuevo, ábranlo — ahí estarán las filas marcadas. Si les dio texto en el panel, anoten los números de fila. Ambos resultados son válidos."_

> _"Los duplicados y outliers los pusimos intencionalmente. En datos reales, esto es lo primero que hay que buscar antes de cualquier análisis."_

### 🛟 Plan B:
- Si solo encuentra outliers pero no duplicados (o viceversa): hacer dos prompts separados
- Si da resultados parciales: _"Lista las filas específicas con número de fila"_

---

## Ejercicio 6 — Gráfico (1:39 – 1:45) — 6 min

### Qué hacer:
```
📊 "Genera un gráfico de barras agrupadas comparando Presupuesto_MXN vs Gasto_Real_MXN por Departamento"
```

### Resultado esperado:
- Copilot genera un **nuevo archivo** con el gráfico incluido
- Descargar/abrir → mostrar el gráfico de barras agrupadas
- 6 departamentos en eje X, dos barras por departamento: presupuesto vs gasto real
- Se puede ver qué departamentos están sobre/bajo presupuesto

### 💬 Qué comentar:

> _"Abran el archivo. Ahí está el gráfico que Copilot generó. Este gráfico normalmente toma: seleccionar datos, insertar, elegir tipo de gráfico, configurar series... unos 2-3 minutos manuales. Con Copilot: 10 segundos y un archivo listo."_

> _"¿Qué departamento gasta más que su presupuesto? ¿Cuál está más controlado? Esto es lo que un CFO quiere ver."_

### 🛟 Plan B:
- Si Copilot genera un gráfico diferente: aceptar y ajustar con: _"Cambia a un gráfico de barras agrupadas"_
- Si no genera gráfico: hacerlo manualmente — Insertar → Gráfico → Barras agrupadas. Decir: _"A veces Copilot falla con gráficos. La alternativa manual toma 30 segundos."_

### 💡 Cierre del Lab Excel:

> _"En 40 minutos hicieron 6 análisis que manualmente tomarían 30-45 minutos cada uno. Eso es el poder de Copilot: no reemplaza su conocimiento financiero, pero acelera la ejecución."_

> _"Notaron que Copilot genera archivos nuevos con los resultados — su archivo original siempre queda intacto. Esto es una ventaja: pueden experimentar sin miedo a romper nada. Si les gusta el resultado, lo guardan. Si no, lo descartan y vuelven a intentar."_

> _"Ahora vamos a ver cómo estos MISMOS datos se ven en Power BI — del Excel detallado al dashboard ejecutivo."_

---

# 📈 BLOQUE 2B — POWER BI DESDE CERO + DAX CON COPILOT 365 (1:45 – 2:05) — 20 min

---

### Formato: **Demo guiada paso a paso** (los alumnos observan — explicar TODO, asumir que nunca han abierto Power BI)

### Qué decir al inicio:

> _"Ahora vamos a usar Power BI. Si nunca lo han abierto, no se preocupen — voy a mostrar TODO paso a paso. Power BI Desktop es gratuito y no necesitan licencia especial para usarlo en su computadora."_

> _"La idea clave: acabamos de hacer análisis DETALLADO en Excel. Ahora vamos a convertir eso en un DASHBOARD que un director o CFO pueda entender en 30 segundos."_

> _"Y vamos a hacer algo muy interesante: vamos a usar Copilot 365 chat para generar fórmulas DAX, y LUEGO vamos a crear TODOS los visuales usando Q&A — escribiendo preguntas en lenguaje natural. Sin arrastrar campos, sin menús. Escribes lo que quieres ver y Power BI lo genera."_

> _"Un tip importante: Q&A funciona MUCHO mejor en inglés. Así que las preguntas las vamos a escribir en inglés aunque los datos estén en español. Los nombres de las columnas van tal cual."_

---

## Paso 1 — Abrir Power BI Desktop (1:45 – 1:47) — 2 min

### Qué hacer:
1. Click en el menú de **Windows** (tecla Windows abajo a la izquierda)
2. Escribir **"Power BI Desktop"**
3. Click en la app para abrirla
4. Se abre una pantalla de bienvenida → **cerrar** la ventana emergente (X en la esquina)

### 💬 Qué comentar:

> _"Power BI Desktop es gratis — lo descargan de powerbi.microsoft.com/desktop. No confundir con Power BI Service que es la versión web y esa sí necesita licencia para publicar."_

### Lo que se ve en pantalla — explicar CADA zona:

> _"Vamos a orientarnos. Power BI tiene 3 zonas principales:"_
> - **Lienzo central (grande, blanco):** _"Aquí van nuestros gráficos y visuales. Ahorita está vacío."_
> - **Panel Visualizaciones (derecha arriba):** _"Estos íconos son los tipos de gráficos disponibles — barras, pastel, tabla, mapa, etc."_
> - **Panel Datos/Campos (derecha abajo):** _"Aquí aparecerán nuestras columnas cuando carguemos datos. Ahorita está vacío."_

### 🛟 Plan B:
- Si Power BI no está instalado: tener el `.pbix` pre-construido listo y mostrar el resultado final. Decir: _"En sus máquinas lo instalaremos después. Les muestro el resultado."_
- Si tarda en abrir: mientras carga, explicar la diferencia Desktop vs Service

---

## Paso 2 — Cargar el dataset (1:47 – 1:50) — 3 min

### Qué hacer:

> _"Ahora vamos a cargar el MISMO archivo que usamos en Excel — gastos_departamentales.xlsx."_

1. Click en pestaña **Inicio** (barra superior, primera pestaña)
2. Click en **"Obtener datos"** (botón grande a la izquierda)
3. En el menú que aparece, click en **"Libro de Excel"**
4. Navegar hasta el archivo `gastos_departamentales.xlsx` → **Abrir**
5. Aparece la ventana **"Navegador"** — marcar la tabla **GastosDepartamentales** (checkbox a la izquierda)
6. Se muestra una **vista previa** de los datos a la derecha

### 💬 Qué comentar en la vista previa:

> _"Miren — Power BI nos muestra cómo va a interpretar los datos. Verificamos:"_
> - _"¿Las columnas tienen los nombres correctos? Departamento, Presupuesto_MXN, Gasto_Real_MXN... ✅"_
> - _"¿Los números se ven como números, no como texto? ✅"_
> - _"¿Las fechas se ven como fechas? ✅"_

7. Click en **"Cargar"** (NO en "Transformar datos" — queremos los datos tal cual)
8. Esperar unos segundos → en el panel **Datos** (derecha abajo) aparece `GastosDepartamentales` con todas las columnas

### 🛟 Plan B:
- Si no encuentra el archivo: verificar que el filtro del explorador esté en "Archivos de Excel" o "Todos los archivos"
- Si las columnas aparecen mal: click en "Transformar datos" → verificar tipos de datos → Cerrar y aplicar

### ✅ Verificación:

> _"¿Ya les aparece la tabla en el panel de la derecha? Deben ver: Departamento, Centro_Costo, Categoria_Gasto, Mes, Presupuesto_MXN, Gasto_Real_MXN... Si no les aparece, avisen."_

---

## Paso 3 — Generar DAX con Copilot 365 chat (1:50 – 1:54) — 4 min

### Qué decir:

> _"Power BI usa un lenguaje llamado DAX para crear cálculos — es como las fórmulas de Excel pero más poderosas. En vez de aprender DAX desde cero, vamos a pedirle a Copilot 365 que nos las escriba."_

### Qué hacer:
1. Abrir otra pestaña del navegador → ir a **copilot.microsoft.com**
2. Click en el ícono de **adjuntar archivo** (clip) → seleccionar `gastos_departamentales.xlsx`
3. Escribir este prompt **en inglés** (funciona mejor):

```
🤖 "Analyze this Excel file. Generate DAX measures for Power BI.
The table in Power BI is named GastosDepartamentales. Generate these 5 DAX measures, each ready to copy and paste:
1. Total Gasto Real = SUM of Gasto_Real_MXN
2. Total Presupuesto = SUM of Presupuesto_MXN
3. Variacion Promedio = AVERAGE of Variacion_Pct
4. Registros Excedidos = COUNT of rows where Variacion_Pct > 20
5. Gasto Aprobado = SUM of Gasto_Real_MXN only where Estatus = 'Aprobado'"
```

4. Copilot genera las 5 medidas DAX

### 💬 Qué comentar:

> _"Fíjense en dos cosas: primero, le adjunté el archivo para que VEA las columnas reales — así el DAX usa los nombres exactos. Segundo, el prompt está en inglés porque Copilot genera DAX más preciso así. Los nombres de columnas van tal cual están en español."_

### Resultado esperado de Copilot:

```dax
Total Gasto Real = SUM(GastosDepartamentales[Gasto_Real_MXN])

Total Presupuesto = SUM(GastosDepartamentales[Presupuesto_MXN])

Variacion Promedio = AVERAGE(GastosDepartamentales[Variacion_Pct])

Registros Excedidos = COUNTROWS(
    FILTER(GastosDepartamentales, GastosDepartamentales[Variacion_Pct] > 20)
)

Gasto Aprobado = CALCULATE(
    SUM(GastosDepartamentales[Gasto_Real_MXN]),
    GastosDepartamentales[Estatus] = "Aprobado"
)
```

### 🛟 Plan B:
- Si Copilot no genera bien el DAX: tener las 5 medidas pre-escritas en un archivo de texto como backup
- Si el nombre de la tabla es diferente en PBI (por ejemplo `GastosDepartamentales1`): ajustar en el DAX antes de pegar

---

## Paso 4 — Pegar las medidas DAX en Power BI (1:54 – 1:57) — 3 min

### Qué decir:

> _"Ahora viene la parte más sencilla: copiar de Copilot y pegar en Power BI. Esto es como copiar una fórmula de Excel que alguien te compartió."_

### Qué hacer (repetir para cada medida):

1. En Copilot chat, **seleccionar y copiar** la primera medida: `Total Gasto Real = SUM(GastosDepartamentales[Gasto_Real_MXN])`
2. Ir a Power BI Desktop
3. Click en pestaña **"Modelado"** (barra superior)
4. Click en **"Nueva medida"**
5. En la **barra de fórmulas** que aparece arriba del lienzo (dice `Medida = `), **borrar todo**
6. **Pegar** (Ctrl+V) la medida DAX
7. Presionar **Enter** ✅
8. En el panel Datos (derecha), aparece la medida con un ícono de **calculadora** 🔢

### 💬 Qué comentar mientras pegas:

> _"Miren: Modelado → Nueva medida → pegar → Enter. Es todo. No necesitan saber DAX — Copilot lo escribió por ustedes."_

> _"El ícono de calculadora significa que es una MEDIDA — un cálculo dinámico. Si filtran los datos, el resultado cambia automáticamente."_

### Repetir para las 5 medidas (~30 segundos cada una)

### ✅ Verificación:

> _"En el panel de Datos deben ver 5 medidas con ícono de calculadora: Total Gasto Real, Total Presupuesto, Variacion Promedio, Registros Excedidos, Gasto Aprobado. ¿Las tienen todas?"_

### 🛟 Plan B si una medida da error:
- Copiar el mensaje de error
- Pegar en Copilot 365 chat: _"This DAX measure gives an error in Power BI: [paste error]. The DAX is: [paste DAX]. Can you fix it?"_
- Copilot corrige → copiar y pegar de nuevo

> _"¿Ven? Si algo falla, se lo devolvemos a Copilot y nos lo arregla. Por eso decimos que es un copiloto — trabaja CON ustedes."_

---

## Paso 5 — Crear el dashboard con Q&A — lenguaje natural (1:57 – 2:02) — 5 min

### Qué decir:

> _"Ahora viene lo más impresionante. En vez de arrastrar campos y buscar íconos de gráficos, vamos a escribir preguntas en lenguaje natural y Power BI genera los visuales. Esto se llama Q&A y existe desde 2019 — NO necesita Copilot."_

> _"Tip clave: Q&A funciona MUCHO mejor en inglés. Vamos a usar los nombres exactos de las columnas combinados con instrucciones en inglés."_

### Cómo funciona Q&A:
1. Click en un **espacio vacío** del lienzo
2. Panel **Visualizaciones** → click en ícono de **Q&A** (ícono con "??")
3. Aparece un cuadro de texto: _"Ask a question about your data"_
4. Escribir la pregunta → PBI genera el visual
5. Click en **"Turn this Q&A result into a standard visual"** (ícono de pin 📌) para fijarlo al dashboard
6. Click en espacio vacío → repetir para el siguiente visual

### Visual 1 — Tarjeta KPI:

Escribir en Q&A:
```
📈 "total Gasto_Real_MXN as a card"
```

> _"Así de simple — una línea de texto y Power BI genera una tarjeta KPI con el total. Esto que ven — un número grande limpio — es lo que un CFO quiere ver."_

Click en **📌 Turn into standard visual** → click en espacio vacío

### Visual 2 — Gráfico de barras (Presupuesto vs Gasto por Departamento):

Nuevo Q&A:
```
📈 "Presupuesto_MXN and Gasto_Real_MXN by Departamento as a clustered bar chart"
```

> _"Dos barras lado a lado: presupuesto vs gasto real. De un vistazo ven qué departamento se pasó. Y lo hicimos escribiendo una oración, no buscando en 15 menús."_

Click en **📌 Turn into standard visual** → click en espacio vacío

### Visual 3 — Gráfico de líneas (tendencia mensual):

Nuevo Q&A:
```
📈 "total Gasto_Real_MXN by Mes as a line chart"
```

> _"Tendencia mensual del gasto. Útil para detectar estacionalidad o picos inesperados."_

Click en **📌 Turn into standard visual** → click en espacio vacío

### Visual 4 — Tabla de detalle:

Nuevo Q&A:
```
📈 "show Departamento, Categoria_Gasto, sum of Gasto_Real_MXN, average of Variacion_Pct as a table"
```

> _"La tabla es para los que quieren ver los números exactos. El gráfico cuenta la historia, la tabla da la evidencia."_

Click en **📌 Turn into standard visual** → click en espacio vacío

### Visual 5 — Top departamentos con mayor desviación:

Nuevo Q&A:
```
📈 "top 3 Departamento by average Variacion_Pct as a bar chart"
```

> _"¿Cuáles son los 3 departamentos que más se desvían del presupuesto? Una pregunta, un visual."_

Click en **📌 Turn into standard visual** → click en espacio vacío

### Visual 6 — Filtro por Mes (Slicer):

> _"El slicer es el único visual que vamos a hacer 'manualmente' — es un filtro interactivo."_

1. Click en **espacio vacío** → panel Visualizaciones → ícono de **Segmentación** (parece un embudo con líneas)
2. Arrastrar **Mes** → al campo

> _"Hagan click en un mes..."_ [click en "Mar"] _"...y TODOS los visuales se filtran automáticamente. Esto en Excel no existe — en PBI es automático."_

### 🛟 Plan B:
- Si Q&A no entiende una pregunta: reformular usando los nombres EXACTOS de las columnas. Ejemplo: en vez de "expenses" usar "Gasto_Real_MXN"
- Si un visual no sale como esperaban: agregar "as a [tipo]" al final (bar chart, line chart, table, pie chart, card)
- **Backup total:** Abrir el `.pbix` pre-construido: _"Les muestro el dashboard terminado que preparé."_

---

## Paso 6 — Narrativa inteligente + Q&A interactivo (2:02 – 2:04) — 2 min

### Narrativa inteligente (Smart Narrative — NO necesita Copilot):

1. Click en espacio vacío → Visualizaciones → ícono de **Narración inteligente** (líneas de texto con ✨ sparkle)
2. Power BI genera automáticamente un párrafo tipo: _"El gasto total fue de $X MXN. El departamento con mayor gasto fue..."_

> _"Esto es análisis automático en texto. Imaginen poner esto en un correo para su director: 'Aquí está el resumen del mes' — y Power BI lo escribió por ustedes."_

### Q&A interactivo — preguntas de la audiencia:

> _"¿Qué más quieren preguntarle a los datos?"_

Abrir un nuevo Q&A y escribir lo que pida la audiencia. Ejemplos:

```
📈 "which Departamento has the highest Gasto_Real_MXN"
📈 "count of rows where Estatus is 'Rechazado'"
📈 "Gasto_Real_MXN by Categoria_Gasto as a pie chart"
📈 "average Variacion_Pct by Departamento where Variacion_Pct > 10"
```

> _"Q&A no es perfecto — a veces no entiende. Pero cuando funciona, es magia: escribes una pregunta y obtienes un visual en 2 segundos."_

---

## Paso 7 — Cierre: el pipeline completo (2:04 – 2:05) — 1 min

### 💬 Cierre del demo — Comparación + Pipeline:

> _"Recapitulemos lo que acabamos de hacer:"_
> 1. _"Analizamos datos DETALLADOS en Excel con Copilot"_
> 2. _"Le pedimos a Copilot 365 chat que nos genere fórmulas DAX — en inglés, porque funciona mejor"_
> 3. _"Las pegamos en Power BI"_
> 4. _"Creamos 5 visuales escribiendo preguntas en Q&A — en inglés — sin arrastrar un solo campo"_
> 5. _"Y Power BI nos escribió un resumen automático con Smart Narrative"_

> _"El pipeline completo es:"_
> **Excel** (limpia y analiza) → **Copilot 365 chat** (genera DAX en inglés) → **Power BI Q&A** (crea visuales en inglés) → **PPT** (presentación)

> _"TODO lo que hicimos en PBI fue AI-driven: Copilot escribió la lógica, Q&A creó los visuales, Smart Narrative escribió el resumen. En la Sesión 2 completaremos con Word y PowerPoint."_

### Mostrar la comparación:

| Aspecto | Excel + Copilot | Copilot 365 chat | Power BI Q&A |
|---------|----------------|------------------|--------------|
| **Mejor para** | Análisis detallado, fórmulas | Generar DAX, lógica, código | Crear visuales con lenguaje natural |
| **Interacción** | Prompt → columna/fórmula | Prompt → código DAX para copiar | Pregunta en inglés → visual automático |
| **Idioma** | Español funciona bien | Inglés genera mejor DAX | **Inglés funciona mucho mejor** |
| **Audiencia** | Analista, equipo operativo | El que construye el dashboard | Gerencia, dirección |
| **Licencia especial** | Copilot 365 | Copilot 365 (la misma) | Gratis (nativo desde 2019) |

---

## 🔄 TRANSICIÓN (2:05 – 2:10) — 5 min

### Qué decir:

> _"Bien, ya experimentaron con Copilot en Excel y vieron el poder de Power BI. Ahora viene la parte más importante de hoy: vamos a identificar problemas REALES de su trabajo que vamos a convertir en POCs."_

> _"Tómense 5 minutos de pausa. Cuando vuelvan, necesito que estén con su equipo y tengan la Ficha de Problema abierta."_

### Acción del instructor durante la pausa:
- Distribuir `ficha_problema.md` (impresa o digital)
- Si es virtual, pegar el link en el chat
- Preparar timer visible para las rondas del Bloque 3

---

# 🏗️ BLOQUE 3 — DESCUBRIMIENTO DE PROBLEMAS (2:10 – 3:10) — 60 min

---

## 3.1 Formación definitiva de equipos (2:10 – 2:25) — 15 min

### Qué decir:

> _"En el Bloque 1 formaron equipos preliminares. Ahora es el momento de confirmar o ajustar. Los equipos que se formen ahora serán los mismos para las 3 sesiones."_

### Instrucciones detalladas:

1. **(2:10–2:13)** — Recordar la estructura:
   - Product Owner (1-2): Define el problema y valida valor
   - PM / Líder (1): Coordina entregables
   - Analistas (2-3): Datos y prompts

2. **(2:13–2:18)** — Los equipos se confirman:
   - ¿Alguien quiere cambiar de equipo? (última oportunidad)
   - ¿Todos tienen 4-6 personas?
   - ¿Todos tienen PO y PM asignados?

3. **(2:18–2:22)** — Cada equipo:
   - Elige nombre definitivo
   - Abre la Ficha de Problema
   - Llena la sección 1 (Datos del equipo)

4. **(2:22–2:25)** — Verificación rápida:
   - Cada equipo dice su nombre y PO en voz alta
   - Instructor anota en pizarrón/chat

### 🛟 Si hay problemas:
- **Equipos desbalanceados:** redistribuir
- **Alguien sin licencia de Copilot:** asegurarse de que esté con alguien que sí la tenga
- **Todos quieren ser analistas, nadie PO:** _"El PO es el que sabe POR QUÉ el problema importa. El analista sabe CÓMO resolverlo. Ambos son esenciales."_

---

## 3.2 Taller de descubrimiento de problemas (2:25 – 2:55) — 30 min

### Qué decir al inicio:

> _"Ahora cada equipo va a descubrir su problema real. Vamos a hacer 3 rondas de 10 minutos cada una. Yo voy a poner el timer. Cuando suene, pasamos a la siguiente ronda."_

---

### 🔵 Ronda 1 — Lluvia de problemas (2:25 – 2:35) — 10 min

### Instrucción:

> _"Cada persona en el equipo tiene 2 minutos para compartir 1-2 problemas de su día a día. Usen estas 3 preguntas como guía:"_

1. _"¿Qué tarea me consume MÁS TIEMPO cada semana o mes?"_
2. _"¿Qué proceso REPITO manualmente que podría automatizarse?"_
3. _"¿Qué reporte o análisis me PIDEN FRECUENTEMENTE y es tedioso?"_

> _"Anótenlos todos — no descarten nada todavía. La cantidad importa más que la calidad en esta ronda."_

### Qué hace el instructor:
- Caminar entre equipos (presencial) o entrar a breakout rooms (virtual)
- Escuchar sin intervenir demasiado
- Si un equipo está callado, dar un ejemplo: _"¿Alguien hace conciliaciones? ¿Reportes mensuales? ¿Seguimiento de facturas vencidas?"_

### ⏱️ A los 8 minutos:
> _"Dos minutos más. Asegúrense de que TODOS hayan compartido al menos un problema."_

---

### 🟡 Ronda 2 — Priorización (2:35 – 2:45) — 10 min

### Instrucción:

> _"Ahora tienen una lista de problemas. Es hora de elegir UNO. Usen estos 4 criterios para evaluar cada problema:"_

| Criterio | Pregunta clave |
|----------|----------------|
| **Impacto** | ¿Cuántas horas/personas se benefician? |
| **Datos disponibles** | ¿Tenemos acceso a los datos necesarios? |
| **Viabilidad con Copilot** | ¿Se puede resolver con Excel + PBI + Word + PPT? |
| **Demostrable** | ¿Podemos mostrar resultados en 2 sesiones más? |

> _"Método de votación: cada persona pone una ⭐ (estrella) en su problema favorito. El más votado gana. Si hay empate, el PO decide."_

### Qué hace el instructor:
- Ayudar a equipos que están indecisos
- Validar que el problema elegido sea viable con Copilot
- ⚠️ **Filtrar problemas inviables:**
  - Si alguien propone algo que requiere código → _"Eso es más para un equipo de desarrollo. ¿Hay una parte de ese proceso que sí se pueda hacer en Excel?"_
  - Si el problema requiere datos confidenciales → _"Perfecto, generaremos datos simulados con la misma estructura"_
  - Si el problema es demasiado grande → _"¿Cuál es la PARTE MÁS PEQUEÑA que podemos demostrar?"_

### ⏱️ A los 8 minutos:
> _"Dos minutos. Ya deben tener UN problema elegido. Si no, el PO decide."_

---

### 🟢 Ronda 3 — Completar la Ficha (2:45 – 2:55) — 10 min

### Instrucción:

> _"Ya tienen el problema. Ahora necesito que llenen la Ficha de Problema — es el documento más importante de hoy, porque con él voy a generar datasets personalizados para cada equipo."_

> _"Secciones clave que necesito completas:"_
> 1. _"Sección 2 — El problema: qué, quién, frecuencia, tiempo invertido"_
> 2. _"Sección 3 — Los datos: qué columnas tienen, cuántas filas, si son confidenciales"_
> 3. _"Sección 4 — El resultado esperado: qué output quieren, para quién, en qué herramienta"_
> 4. _"Sección 5 — Tipología: marcar el tipo de POC que es"_

### ⚠️ PUNTO CRÍTICO — Sección 3 (Los datos):

> _"La sección 3 es la más importante para mí. NECESITO saber:"_
> - _"¿Qué columnas tiene su archivo? (ej: Fecha, Cliente, Monto, Cuenta)"_
> - _"¿Cuántas filas aproximadas?"_
> - _"¿Los datos son confidenciales?"_

> _"Entre más detalle me den sobre las columnas, MEJOR será el dataset que les genere. No me digan 'datos de facturación' — díganme las columnas exactas."_

### Qué hace el instructor:
- Ir equipo por equipo verificando que la Sección 3 tenga suficiente detalle
- Si un equipo no sabe las columnas exactas, ayudar: _"¿Cómo se ve tu Excel normalmente? ¿Qué hay en la columna A? ¿Y en la B?"_
- Si los datos son confidenciales: confirmar que se generarán datos simulados

### ⏱️ A los 8 minutos:
> _"Dos minutos. No necesita estar perfecto — necesita estar lo suficientemente detallado para que yo pueda generar sus datos."_

---

## 3.3 Pitch rápido por equipo (2:55 – 3:10) — 15 min

### Qué decir:

> _"Cada equipo tiene 2 MINUTOS para presentar. Solo 2 minutos — practiquen ser concisos. Esto es un pitch, no una presentación."_

### Formato del pitch (mostrar en pantalla):
1. **Nombre del equipo** (5 seg)
2. **El problema en UNA frase** (15 seg)
3. **¿Por qué importa?** — impacto en horas/dinero (30 seg)
4. **¿Qué herramienta principal?** — Excel, PBI, Word, PPT (15 seg)
5. **¿Qué esperan lograr?** — el output soñado (25 seg)

### Reglas:
- ⏱️ Timer estricto de 2 minutos
- Solo habla el PO o PM (no todo el equipo)
- Los demás equipos dan **1 sugerencia** después de cada pitch

### 💬 Frases del instructor después de cada pitch:

- ✅ Si el problema es claro: _"Excelente — eso es muy accionable. Me veo generando un dataset con esas columnas."_
- ⚠️ Si es vago: _"Me gusta la idea. ¿Puedes ser más específico sobre qué columnas tendría tu dataset ideal?"_
- 🔄 Si es inviable con Copilot: _"Ese es un gran problema, pero la parte de [X] se sale de Copilot. ¿Qué tal si nos enfocamos en la parte de [Y]?"_
- 💡 Si es ambicioso: _"Wow, eso es un proyecto grande. Para el POC, ¿cuál sería la MÍNIMA demostración que convencería a tu jefe?"_

### Cálculo de timing:
- 5 equipos × (2 min pitch + 1 min feedback) = 15 min ✅
- 6 equipos × (2 min + 30 seg feedback) = 15 min ✅
- Si hay más de 6 equipos: reducir a 1.5 min por pitch

---

# 🏁 CIERRE (3:10 – 3:20) — 10 min

---

## 🚀 Mini-POC en vivo: Briefing Ejecutivo en 5 Minutos (3:10 – 3:15) — 5 min

📁 **Archivo:** `gastos_departamentales.xlsx` (el mismo del Bloque 2A — ya lo tienen abierto)

### Qué decir:

> _"Antes de cerrar, vamos a hacer algo especial. Pero NO vamos a hacer fórmulas simples — eso ya saben hacerlo. Vamos a hacer algo que un analista senior tarda 2-3 HORAS en preparar: un briefing ejecutivo completo para el CFO. Clasificación de tendencias, scoring de riesgo, resumen con recomendaciones, y un dashboard que use esas nuevas dimensiones. En 5 minutos."_

### Formato: **Demo rápida del instructor** (los alumnos observan)

### 💡 Punto clave — decir esto ANTES de empezar:

> _"Un IF o un SUMIFS lo hacen en 30 segundos, ya lo sé. Lo que NO pueden hacer rápido es: clasificar tendencias cruzando filas por departamento, calcular un score de riesgo acumulado que cuente meses excedidos, y escribir un resumen ejecutivo profesional. AHÍ es donde la IA aporta valor real."_

---

### Paso 1 — Enriquecer datos con tendencias y riesgo (Excel Copilot) — 1 min

Abrir `gastos_departamentales.xlsx` en Excel → Copilot:

```
📊 "Agrega dos columnas: 1) Tendencia — clasifica cada departamento como 'Creciente', 'Estable' o 'Decreciente' según el patrón de Gasto_Real_MXN en los últimos meses. 2) Riesgo_Acumulado — calcula para cada departamento el total acumulado de meses donde Variacion_Pct superó 10%, y clasifica: 4+ meses = 'Crítico', 2-3 = 'Medio', 0-1 = 'Bajo'."
```

- Copilot genera un **nuevo archivo** con las 2 columnas añadidas → abrirlo
- Mostrar las columnas al grupo: _"¿Ven? Ahora cada fila tiene una clasificación de tendencia y un nivel de riesgo basado en cuántos meses se han excedido. Este archivo enriquecido es el que vamos a usar en los siguientes pasos."_

> _"Tendencia requiere que Copilot analice fila por fila por departamento, comparando meses. Riesgo_Acumulado necesita contar cuántos meses cada departamento superó el 10% de variación y luego clasificar. Eso es un COUNTIFS anidado dentro de un IF — fácil equivocarse y lento de armar. Copilot lo hizo en segundos."_

### 🛟 Plan B:
- Inglés: `"Add two columns: 1) Tendencia — classify each department as 'Creciente', 'Estable' or 'Decreciente' based on Gasto_Real_MXN pattern. 2) Riesgo_Acumulado — for each department count months where Variacion_Pct > 10%, classify: 4+ = 'Crítico', 2-3 = 'Medio', 0-1 = 'Bajo'."`
- Backup: tener el archivo con las columnas ya calculadas como respaldo

---

### Paso 2 — Resumen ejecutivo para el CFO (Copilot 365 Chat) — 1.5 min

1. Abrir otra pestaña → **copilot.microsoft.com**
2. Adjuntar el **archivo nuevo del Paso 1** (el que tiene Tendencia y Riesgo_Acumulado)
3. Escribir:

```
🤖 "Act as a financial controller. Analyze this budget execution data — pay special attention to the Tendencia and Riesgo_Acumulado columns. Write a 5-bullet executive summary for the CFO highlighting: top risks, departments requiring immediate attention, and 3 recommended actions. Be specific with numbers."
```

4. Copilot genera un resumen ejecutivo profesional aprovechando las columnas que ya clasificamos

> _"Miren: el resumen ya menciona cuáles departamentos tienen riesgo crítico y cuáles están en tendencia creciente. ¿Por qué? Porque le dimos datos ENRIQUECIDOS, no solo números crudos. Eso es el pipeline: cada paso alimenta al siguiente."_

### 🛟 Plan B:
- Si Copilot 365 chat tarda: tener el resumen pre-generado en un archivo de texto
- Si no reconoce el archivo: copiar 20 filas de muestra (incluyendo Tendencia y Riesgo_Acumulado) directo en el prompt

---

### Paso 3 — Dashboard de riesgo con datos enriquecidos (Power BI Q&A) — 1 min

Cargar el **archivo nuevo del Paso 1** en Power BI → Q&A:

**Visual 1 — Gasto por tendencia:**
```
📈 "sum of Gasto_Real_MXN by Departamento by Tendencia as a clustered bar chart"
```

1. Click en **📌 Turn into standard visual**

**Visual 2 — Gasto por nivel de riesgo:**
```
📈 "sum of Gasto_Real_MXN by Departamento by Riesgo_Acumulado as a stacked bar chart"
```

2. Click en **📌 Turn into standard visual**

> _"¿Ven? El primer gráfico muestra cuánto gasta cada departamento agrupado por su TENDENCIA — esa columna no existía hace 2 minutos, Copilot la creó. El segundo muestra cómo se distribuye el gasto por nivel de riesgo. Sin el Paso 1, estos gráficos serían imposibles. ESO es el pipeline."_

### 🛟 Plan B:
- Si Q&A no reconoce las columnas: arrastrar manualmente Departamento + Tendencia al visual, y Departamento + Riesgo_Acumulado al segundo
- Backup: mostrar el `.pbix` pre-construido

---

### Paso 4 — Narrativa automática (Smart Narrative) — 30 seg

1. Click en espacio vacío → Visualizaciones → **Narración inteligente**
2. Power BI genera automáticamente un párrafo analítico

> _"Y el último paso: Power BI escribe el análisis por ustedes. Combinen esto con el resumen del CFO que Copilot chat nos dio y tienen un briefing ejecutivo completo."_

---

### 💬 Cierre impactante:

> _"¿Qué acabamos de hacer? Y más importante: ¿por qué esto NO se puede hacer con un IF en Excel?"_

| Paso | Herramienta | Qué hizo la IA (imposible rápido a mano) | Manual | Con IA |
|------|-------------|-------------------------------------------|:---:|:---:|
| 1 | Excel Copilot | Clasificó tendencias y calculó riesgo acumulado → nuevo archivo enriquecido | ~30 min | ~30 seg |
| 2 | Copilot 365 Chat | Escribió resumen ejecutivo con riesgos y recomendaciones | ~45 min | ~30 seg |
| 3 | PBI Q&A | Creó dashboard usando Tendencia y Riesgo_Acumulado del Paso 1 | ~15 min | ~20 seg |
| 4 | Smart Narrative | Generó narrativa analítica del dashboard | ~20 min | ~5 seg |
| **TOTAL** | | | **~2 horas** | **~5 min** |

> _"Lo que acabamos de hacer — enriquecer datos con tendencias y riesgo acumulado, generar un resumen ejecutivo con esos datos, y crear un dashboard que usa columnas que NO existían — es un PIPELINE. Cada paso alimentó al siguiente. Eso tarda 2-3 HORAS manualmente. Eso NO lo reemplaza un IF. ESO es un POC."_

> _"Y lo más importante: ustedes van a hacer algo así con SUS datos en la Sesión 2."_

---

## Cierre y entregables (3:15 – 3:20) — 5 min

### Qué decir:

> _"Excelente sesión. Recapitulemos lo que lograron hoy:"_

1. ✅ _"Aprendieron qué es un POC y los tipos que existen"_
2. ✅ _"Usaron Copilot en Excel — resúmenes, tablas dinámicas, fórmulas, gráficos, detección de anomalías"_
3. ✅ _"Vieron cómo los mismos datos se transforman en un dashboard en Power BI"_
4. ✅ _"Identificaron un problema REAL y crearon su Ficha de Problema"_
5. ✅ _"Y acabamos de hacer un mini-POC completo en 5 minutos — de Excel a dashboard con narrativa"_

### Entregables (recordar):
> _"Antes de irse, necesito:"_
> 1. _"Su archivo de Excel con los ejercicios de Copilot (al menos 4 prompts)"_
> 2. _"Su Ficha de Problema completa — es IMPRESCINDIBLE. Sin ella no puedo generar sus datos."_

### Preview Sesión 2:

> _"¿Qué va a pasar ahora? Con sus Fichas de Problema, yo voy a generar datasets personalizados que se parecen a sus datos reales. En la Sesión 2:"_
> - _"Van a trabajar con SUS datos (simulados pero con la misma estructura)"_
> - _"Van a crear un documento de estructura del POC en Word con Copilot"_
> - _"Van a empezar el wireframe de su presentación en PowerPoint"_
> - _"El pipeline completo: Excel → Power BI → Word → PPT"_

### Tarea entre sesiones (opcional pero recomendada):

> _"Si quieren adelantar:"_
> 1. _"Practiquen 5 prompts más en Excel con cualquier dato que tengan"_
> 2. _"Refinen mentalmente su problema: ¿qué output convencería a su jefe?"_
> 3. _"Si tienen datos reales (no confidenciales), tráiganlos en Excel para la Sesión 2"_

### Despedida:

> _"Gracias por su energía hoy. Nos vemos en la Sesión 2 con sus datos personalizados. ¡A construir POCs!"_

---

## 📊 Checklist post-sesión (para el instructor)

| # | Tarea | Completado |
|---|-------|:---:|
| 1 | Recopilar TODAS las Fichas de Problema | ☐ |
| 2 | Verificar que cada ficha tenga Sección 3 completa (columnas, filas, confidencialidad) | ☐ |
| 3 | Generar datasets personalizados con `generate_datasets_sesion1.py` como base | ☐ |
| 4 | Subir datasets personalizados a OneDrive/SharePoint compartido | ☐ |
| 5 | Enviar confirmación a cada equipo con link a su dataset | ☐ |
| 6 | Preparar template de Word para Sesión 2 | ☐ |
| 7 | Anotar problemas técnicos encontrados (Copilot, licencias, etc.) | ☐ |
| 8 | Evaluar calidad de los problemas — ¿alguno necesita redirección? | ☐ |

---

## 🚨 Troubleshooting — Problemas comunes y soluciones

| Problema | Solución inmediata | Prevención |
|----------|-------------------|-----------|
| Copilot no aparece en Excel | Verificar: ¿archivo en OneDrive? ¿Autoguardado ON? ¿Tabla (Ctrl+T)? Cerrar y reabrir. | Verificar licencia 48hrs antes |
| Copilot responde en inglés | Es normal. Pedir: _"Responde en español"_ o aceptar la respuesta en inglés | Tener prompts en ambos idiomas |
| Copilot da resultados incorrectos | Refinar el prompt. Ser más específico. Mencionar columnas por nombre. | Practicar prompts antes |
| Copilot se tarda mucho (>30 seg) | Cancelar y reintentar. Si persiste, pasar al Plan B (resultado pre-calculado). | Tener backups para todo |
| Alguien no tiene licencia de Copilot | Emparejar con alguien que sí la tenga. El sin licencia observa y anota. | Verificar licencias 1 semana antes |
| El dataset no carga en Power BI | Verificar formato del archivo (.xlsx). Usar "Obtener datos" → "Libro de Excel". Si falla, intentar "Texto/CSV" como alternativa. | Probar la carga 1 hora antes |
| Un equipo no encuentra un problema | Darles las "Ideas semilla" de sesion1.html y pedir que adapten una a su contexto. | — |
| El pitch se extiende | Timer estricto. A los 2 minutos: _"Gracias, tiempo. Una sugerencia del grupo..."_ | Practicar antes |
| Power BI Copilot no funciona | Usar Q&A nativo. Si tampoco: mostrar screenshots preparados. | Tener `.pbix` pre-construido |
| Internet se cae | Tener todo en caché local como backup. Mostrar screenshots. | Descargar archivos localmente como respaldo |

---

## 📝 Notas del instructor

_Espacio para anotar observaciones durante la sesión:_

### Equipos formados:
| # | Nombre | PO | PM | # Integrantes | Problema (resumen) |
|---|--------|----|----|:---:|-----|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

### Problemas técnicos encontrados:
```
[Anotar aquí]
```

### Prompts que funcionaron especialmente bien:
```
[Anotar aquí]
```

### Prompts que fallaron (y alternativa usada):
```
[Anotar aquí]
```

### Notas para mejorar la próxima vez:
```
[Anotar aquí]
```
