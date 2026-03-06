# 🎬 Guión del Instructor — Sesión 3
## "Pipeline mensual: de 5 Excels a consolidado verificado + detección de cambios"

> **Duración total:** 3 horas (180 min)
> **Formato:** Presencial o virtual (Teams)
> **Audiencia:** PMs y profesionales financieros (sin experiencia en programación)
> **Herramientas:** Microsoft 365 Copilot (copilot.microsoft.com), Python (solo para ejecutar scripts generados por Copilot)

---

## 📦 Materiales a preparar ANTES de la sesión

| # | Material | Acción requerida | Verificado |
|---|----------|-------------------|:---:|
| 1 | 5 archivos Excel del ejercicio | Copiar de `datos_entrada/`: banca_comercial, banca_corporativa, seguros, tarjetas, tesoreria | ☐ |
| 2 | Carpeta compartida | Subir los 5 .xlsx a OneDrive/SharePoint o distribuir ZIP por Teams | ☐ |
| 3 | `sesion3.html` abierto en navegador | Para mostrar agenda, flujo, prompts y ejemplos | ☐ |
| 4 | Copilot 365 funcionando | Verificar en copilot.microsoft.com que puede recibir archivos adjuntos | ☐ |
| 5 | Python instalado (para ejecutar scripts) | `pip install pandas openpyxl` — solo para ejecutar, NO para programar | ☐ |
| 6 | Resultados pre-generados | Tener consolidado + logs listos como Plan B | ☐ |
| 7 | Timer visible | Para respetar tiempos de cada actividad | ☐ |

### 🔒 Verificaciones técnicas (30 min antes)

- [ ] copilot.microsoft.com abre y acepta archivos adjuntos
- [ ] Los 5 archivos Excel se pueden adjuntar sin error
- [ ] Python funciona: `python --version` muestra 3.9+
- [ ] pandas instalado: `python -c "import pandas; print(pandas.__version__)"`
- [ ] Internet estable (Copilot necesita conexión)
- [ ] Compartir pantalla funciona (si virtual)
- [ ] Tener **resultados pre-generados** como Plan B por si Copilot falla

---

## ⏱️ Cronograma minuto a minuto

| Minuto | Bloque | Actividad |
|--------|--------|-----------|
| 0:00–0:05 | **Apertura** | Bienvenida, recap Sesiones 1+2, objetivos de hoy |
| 0:05–0:20 | **Bloque 1** | El problema: 10 archivos, columnas distintas. ¿Cómo homologar? |
| 0:20–0:30 | **Bloque 1** | LA HABILIDAD CLAVE: pedir pruebas paso a paso a la IA |
| 0:30–0:40 | **Bloque 1** | Demo en vivo: "pido script → pido prueba → verifico → siguiente paso" |
| 0:40–0:45 | **Transición** | Pausa + abrir Copilot Chat + carpeta de Excels |
| 0:45–1:05 | **Bloque 2** | Lab 1: Subir archivos y explorar estructura (20 min) |
| 1:05–1:30 | **Bloque 2** | Lab 2: Pedir script de homologación + pruebas (25 min) |
| 1:30–1:50 | **Bloque 2** | Lab 3: Consolidar todo + verificar totales (20 min) |
| 1:50–2:00 | **Bloque 2** | Lab 4: Generar reporte HTML del resultado (10 min) |
| 2:00–2:05 | **Transición** | Pausa |
| 2:05–2:20 | **Bloque 3** | Pipeline mensual: convertir script en pipeline reutilizable |
| 2:20–2:40 | **Bloque 3** | Detección de cambios: comparar mes actual vs anterior |
| 2:40–2:50 | **Bloque 3** | Show & Tell: cada equipo muestra su pipeline + 1 cambio detectado |
| 2:50–3:00 | **Bloque 3** | Cierre: "ya tienen su pipeline" — próximos pasos |

---

# 🟡 APERTURA (0:00 – 0:05)

## Qué decir:

> _"Bienvenidos a la última sesión. En la Sesión 1 trabajamos con datos en Excel y Power BI. En la Sesión 2 generamos HTMLs profesionales. Hoy cerramos el ciclo con algo que van a usar CADA MES: un pipeline que consolida automáticamente los Excels que les llegan por correo."_

> _"La promesa de hoy: van a salir con un pipeline listo. La próxima vez que les lleguen esos 5+ correos con Excels, solo depositan los archivos en una carpeta, ejecutan un comando, y en 5 minutos tienen su consolidado verificado + un reporte de qué cambió respecto al mes pasado."_

### Preguntas rompe-hielo:
- "¿Quién recibe más de 3 Excels por mes que tiene que consolidar?" (manos arriba)
- "¿Cuánto tiempo les toma ese proceso? ¿Horas? ¿Todo un día?"
- "¿Alguna vez descubrieron un error DESPUÉS de entregar el consolidado?"

### Expectativas:
> _"Hoy NO necesitan programar. Copilot genera el código por ustedes. Lo que SÍ necesitan es VERIFICAR que lo que genera está bien. Esa es la habilidad clave de esta sesión."_

---

# 🎓 BLOQUE 1 — TEORÍA + HABILIDAD CLAVE (0:05 – 0:40)

## 1.1 El problema (0:05 – 0:20) — 15 min

### Qué mostrar:
- `sesion3.html` → sección del problema con la tabla de 5 archivos
- Las tarjetas de comparación (❌ manual vs ✅ con Copilot)

### Qué decir:
> _"Imaginen: cada mes les llegan 5 Excels. Banca Comercial llama a la fecha 'fecha_registro'. Corporativa la llama 'date'. Seguros la llama 'fecha'. ¡Mismo dato, 3 nombres! Y así con TODAS las columnas."_

> _"El proceso manual: abren cada archivo, buscan las columnas, renombran, copian, pegan... 6 horas después tienen algo que CREEN que está bien, pero no tienen forma de verificar."_

### Actividad (2 min):
> _"¿Cuántas fuentes diferentes consolidan en su trabajo? Escriban el número en el chat."_

## 1.2 La habilidad clave: pedir PRUEBAS (0:20 – 0:30)

### Qué decir:
> _"Hoy les voy a enseñar UNA habilidad que vale más que todas las fórmulas de Excel: PEDIRLE A LA IA QUE DEMUESTRE QUE HIZO BIEN SU TRABAJO."_

### Mostrar la comparación de sesion3.html:
- ❌ "Hazme un script" → ejecuto → confío ciegamente
- ✅ "Hazme un script Y muéstrame las pruebas" → verifico → avanzo

### Los 5 tipos de pruebas (tabla en sesion3.html):
1. Conteo de filas
2. Cuadre de montos
3. Antes/Después
4. Excepciones
5. Distribución

> _"Cada vez que le pidan algo a Copilot, agreguen al final: 'Y MUÉSTRAME CÓMO VERIFICO QUE ESTÁ BIEN'. Ese es el hábito que los va a separar del resto."_

## 1.3 Demo en vivo (0:30 – 0:40)

### Preparación:
- Copilot 365 abierto
- 3 de los 5 archivos adjuntados (banca_comercial, seguros, tarjetas)

### Demo paso a paso:
1. **Paso 1 — Explorar** (30 seg): Adjuntar 3 archivos → pedir resumen de estructura
2. **Paso 2 — Homologar** (30 seg): Pedir mapa de equivalencias → pedir script con prints de verificación
3. **Paso 3 — Verificar** (30 seg): Mostrar que el script imprime filas antes/después, tabla de cuadre

> _"¿Vieron? 3 pasos, 3 verificaciones. Nunca avancé sin confirmar. Eso es lo que separa a un usuario amateur de un profesional."_

---

# 🔬 BLOQUE 2 — LABS (0:45 – 2:00)

## Setup (0:40 – 0:45)

> _"Abran copilot.microsoft.com. Abran la carpeta donde descargaron los 5 Excels. Vamos a trabajar paso a paso, JUNTOS."_

## Lab 1: Explorar (0:45 – 1:05) — 20 min

Seguir los pasos de `ejercicios_instrucciones.md` - Lab 1.

### Errores comunes:
- Copilot no puede leer los 5 a la vez → adjuntar de a 2-3
- Copilot dice un número de filas diferente al real → verificar en Excel manualmente
- Copilot inventa datos → asegurar que se adjuntaron los archivos

### Validación grupal (2 min):
> _"¿Quién tiene los 5 archivos explorados? ¿Las filas coinciden con la tabla de la sesión? banca_comercial=150, corporativa=120, seguros=100, tarjetas=130, tesorería=90."_

## Lab 2: Homologación (1:05 – 1:30) — 25 min

Seguir Lab 2 de instrucciones.

### Momento clave — Revisar ANTES de ejecutar:
> _"ALTO. Antes de ejecutar, lean el script. No necesitan entender cada línea. Pero sí entiendan QUÉ hace. Pídanle a Copilot que se los explique."_

### Tip:
- Si el script tiene errores: pegar el error en Copilot y pedir corrección
- Si Python no está instalado: usar Google Colab (gratis, sin instalar)

## Lab 3: Consolidar (1:30 – 1:50) — 20 min

Seguir Lab 3 de instrucciones.

### El momento de la verdad:
> _"La tabla de cuadre cruzado. Todos los ✔ verdes? Perfecto. ¿Hay un ✘? NO AVANCEN. Investiguen por qué no cuadra. Siempre es mejor 5 minutos más de verificación que rehacer todo."_

## Lab 4: Dashboard HTML (1:50 – 2:00) — 10 min

Seguir Lab 4.

> _"Esto conecta con lo que aprendieron en Sesión 2. Mismo estilo, pero ahora con datos REALES de su consolidación."_

---

# 🏗️ BLOQUE 3 — PIPELINE MENSUAL (2:05 – 3:00)

## 3.1 Estructura del pipeline (2:05 – 2:20) — 15 min

### Qué decir:
> _"Todo lo que hicieron en los Labs fue para UN mes. Pero el mes que viene les llegan los mismos correos. La pregunta es: ¿van a repetir todo desde cero... o van a tener un pipeline listo?"_

### Demo:
- Mostrar la estructura de carpetas en sesion3.html
- Explicar: "Solo crean una carpeta nueva, ponen ahí los Excels, y corren pipeline.py"

### Trabajo individual (10 min):
Los participantes piden a Copilot que convierta su script en pipeline.py reutilizable.

## 3.2 Detección de cambios (2:20 – 2:40) — 20 min

### Qué decir:
> _"El pipeline ya funciona. Ahora la parte que ahorra HORAS: detectar qué cambió entre el mes pasado y el actual. ¿Un área mandó más datos? ¿Otra cambió el formato? ¿Alguien se atrasó y no mandó su archivo? El script lo detecta automáticamente."_

### Mostrar la tabla de escenarios en sesion3.html:
| Escenario | Sin detección | Con detección automática |
|-----------|---------------|--------------------------|
| +50 filas | No te enteras | 🚨 ALERTA: +33% filas |
| Columna nueva | Se ignora | 🚨 ALERTA: columna nueva |
| Archivo faltante | Consolidas incompleto | 🚨 ALERTA: falta archivo |
| Monto bajó 40% | Presentas cifras mal | 🚨 ALERTA: -40% monto |

### Trabajo (15 min):
Los participantes crean comparar_meses.py y lo prueban con datos simulados.

## 3.3 Show & Tell (2:40 – 2:50) — 10 min

Cada equipo presenta en 2 minutos:
1. ¿Su pipeline corre sin modificar código?
2. 1 alerta de cambio que detectó
3. ¿Cuadre al 100%?

## 3.4 Cierre (2:50 – 3:00) — 10 min

### Qué decir:
> _"Antes de hoy: recibían Excels → 6 horas de trabajo manual → sin garantía."_
> _"Después de hoy: reciben Excels → 5 minutos → consolidado verificado + reporte de cambios."_
> _"Ya tienen su pipeline listo. La próxima vez que lleguen esos correos, solo depositan archivos, ejecutan, y listo."_

### Mensaje final:
> _"La IA no reemplaza al profesional que verifica. La IA reemplaza al profesional que NO verifica. Ustedes ahora saben generar, verificar, automatizar y detectar cambios. Eso es una ventaja profesional enorme."_

### Entregables a solicitar:
1. pipeline.py funcional
2. comparar_meses.py funcional
3. Tabla de cuadre cruzado (evidencia)
4. Reporte de cambios entre meses
5. (Bonus) Dashboard HTML con datos reales

---

## 🛟 Plan B — Si algo falla

| Problema | Solución |
|----------|----------|
| Copilot no puede leer los 5 archivos a la vez | Adjuntar de a 2-3 por conversación |
| El script tiene errores de Python | Pegar el error en Copilot: "me sale este error: [error]. Corrígelo." |
| Las filas no cuadran | "¿Se descartaron filas? ¿Por qué? Muéstrame cuáles." |
| Copilot inventa datos | Adjuntar SIEMPRE los archivos. Si no se adjuntan, inventa. |
| No tengo Python | Opción A: Google Colab (gratis). Opción B: pedir a Copilot que haga todo internamente. |
| El monto no cuadra | Causas: filas filtradas, NaN descartados, tipos mixtos. Pedir diagnóstico a Copilot. |
| Mi archivo tiene >5,000 filas | Pedir que genere el script y ejecutarlo localmente. El script no tiene límite. |
| comparar_meses no detecta un cambio | Revisar los umbrales (±20% filas, ±15% montos). Ajustar si es necesario. |

---

## 📋 Resumen del flujo completo

```
Correos con Excels → Guardar en datos/[mes]/ → python pipeline.py [mes]
→ Consolidado verificado + Log de cuadre
→ python comparar_meses.py [mes_anterior] [mes_actual]
→ Reporte de cambios con alertas 🚨
→ Todo en 5 minutos ✔
```
