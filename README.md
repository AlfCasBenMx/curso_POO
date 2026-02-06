# POC Thinking con Python y ChatGPT

## 📚 Materiales del Curso

Este repositorio contiene los materiales del programa de formación "POC Thinking con Python y ChatGPT" para la colaboración entre EY Taxes + Data & AI.

## 📁 Estructura del Proyecto

```
curso_poc/
├── intro.html          # Syllabus/Brochure del curso
├── sesion1.html        # Guía del facilitador - Sesión 1
├── gantt-editor.html   # POC: Editor de Gantt con IA
├── app.py              # Backend Flask para el Gantt Editor
├── requirements.txt    # Dependencias de Python
├── .env                # Variables de entorno (API Key)
└── .gitignore          # Archivos ignorados por Git
```

## 🚀 Cómo correr el Gantt Editor

### 1. Instalar dependencias

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar la API Key

Asegúrate de que el archivo `.env` contiene tu API key de OpenAI:

```
OPENAI_API_KEY=tu-api-key-aquí
```

### 3. Ejecutar el servidor

```bash
python app.py
```

Verás este mensaje:
```
==================================================
🚀 Gantt Editor Backend
==================================================
Servidor corriendo en: http://localhost:5000
Abre gantt-editor.html en tu navegador
==================================================
```

### 4. Abrir el editor

Abre `gantt-editor.html` en tu navegador. El chat ahora se comunica con el backend Flask que hace de proxy seguro hacia la API de OpenAI.

## 📖 Contenido del Curso

### Sesiones (4 semanas, 12 sesiones)

| Semana | Sesiones | Temas |
|--------|----------|-------|
| 1 | 1-3 | Introducción, Python básico, Loops |
| 2 | 4-6 | Funciones, Pandas, APIs |
| 3 | 7-9 | ChatGPT integration, POC patterns |
| 4 | 10-12 | Proyectos finales y presentaciones |

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML/CSS puro con branding EY
- **Backend**: Flask (Python)
- **AI**: OpenAI GPT-4o-mini
- **Fonts**: Google Fonts (Inter)

## ⚠️ Seguridad

- El archivo `.env` está en `.gitignore` y NO se sube al repositorio
- La API key está protegida en el backend
- Usa variables de entorno en producción

## 👥 Equipo

**EY Taxes + Data & AI**

---

*Programa de formación 2025*
