"""
Gantt Editor Backend - Orchestrator System
Classifies user intent and requests confirmation before applying Gantt changes.
Supports streaming responses for real-time chat.
"""

import os
import json
import uuid
import httpx
import urllib3
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# Disable SSL warnings (for corporate proxy)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

app = Flask(__name__)
CORS(app)

# OpenAI client with SSL disabled for corporate proxy
http_client = httpx.Client(verify=False)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=http_client
)

# Store pending changes waiting for confirmation
pending_changes = {}

# Store conversation history (last 10 exchanges)
conversation_history = []
MAX_HISTORY = 10  # Número de conversaciones a recordar

# ============ PROMPTS ============

CLASSIFIER_PROMPT = """Eres un clasificador de intenciones para un editor de Gantt.
Tu ÚNICA tarea es determinar qué tipo de acción quiere el usuario:

1. CHANGE - Modificar TAREAS del Gantt (agregar, eliminar, mover, CAMBIAR COLOR DE BARRAS, extender, cambiar owner/revisor de una tarea específica)
2. STYLE - Cambiar el ESTILO VISUAL del diagrama (fondo, tema, colores de TEXTOS/COLUMNAS, colores de labels/títulos)
3. STRUCTURE - Cambiar la ESTRUCTURA del diagrama (agregar/quitar columnas, cambiar encabezados)
4. LOGO - Agregar, mover, eliminar o modificar LOGOS/IMÁGENES en el diagrama
5. INFO - Obtener información, recomendaciones, explicaciones o consejos

⚠️ REGLAS IMPORTANTES PARA COLORES:

🎨 COLORES DE BARRAS = CHANGE:
- "Cambia el color de la barra de Testing a rojo" → CHANGE
- "Pon las barras de Planning en amarillo" → CHANGE
- "Color de la categoría Testing" → CHANGE (es la barra de esa categoría)
- "Todas las tareas en azul" → CHANGE (cambiar color de todas las barras)
- "Cambia el color de Desarrollo a verde" → CHANGE (es la barra)
- "Las tareas de Testing en rojo" → CHANGE (barras bajo Testing)

📝 COLORES DE TEXTO = STYLE:
- "El texto de las tareas en amarillo" → STYLE
- "Títulos de tareas en azul" → STYLE (texto de la columna label)
- "Nombres de actividades en rojo" → STYLE (columna de nombres)
- "Fondo negro" → STYLE
- "Columna de owners en blanco" → STYLE

EJEMPLOS ADICIONALES:
- "Cambia el color de Testing" → CHANGE (barra de Testing)
- "La barra de QA en verde" → CHANGE
- "Las barras de las categorías en amarillo" → CHANGE
- "Agrega una tarea QA" → CHANGE
- "Asigna a Juan como revisor" → CHANGE
- "Tema oscuro" → STYLE
- "Agrega columna de revisor" → STRUCTURE
- "Pon el logo de EY" → LOGO
- "¿Qué me recomiendas?" → INFO

Responde SOLO con una palabra: CHANGE, STYLE, STRUCTURE, LOGO o INFO"""

EXECUTOR_PROMPT = """Eres un asistente que modifica diagramas de Gantt.
Recibirás el estado actual del Gantt en JSON y una instrucción del usuario.

DEBES modificar el Gantt cuando el usuario quiera:
- Agregar, eliminar, mover o extender tareas
- Cambiar el color de una BARRA específica (tarea o categoría)
- Cambiar el color de TODAS las barras de una categoría (tareas bajo esa categoría)
- Cambiar el color de TODAS las barras de tareas
- Cambiar owner/revisor de una tarea específica
- Cambiar cualquier propiedad de las tareas

⚠️ IMPORTANTE PARA COLORES DE BARRAS:
- Cuando el usuario dice "cambiar el color de Testing a rojo" → Cambiar el campo "color" de la categoría/tarea
- Cuando dice "color de las barras de Testing" → Cambiar el campo "color" de TODAS las tareas bajo esa categoría
- Cuando dice "todas las tareas en azul" → Cambiar el campo "color" de TODAS las tareas (kind: "task")
- Cuando dice "todas las categorías en amarillo" → Cambiar el campo "color" de todas las categorías (kind: "category")
- El campo "color" de cada tarea/categoría controla el color de SU BARRA en el diagrama

NO modifiques el Gantt si:
- El usuario pregunta sobre el fondo o interfaz del diagrama (eso es STYLE)
- Es una pregunta general o solicitud de información

Formato del Gantt:
{
  "kind": "category" | "task",
  "label": "Nombre de la tarea",
  "owner": "Responsable",
  "start": número de semana (1-12),
  "duration": duración en semanas,
  "color": "#HEXCOLOR"  ← ESTE CAMPO CONTROLA EL COLOR DE LA BARRA
}

EJEMPLOS DE CAMBIOS DE COLOR:
- "Cambia la barra de Testing a rojo" → Buscar item con label que contenga "Testing" y cambiar su color a "#FF0000"
- "Pon las tareas de Desarrollo en verde" → Cambiar color de todas las tareas bajo la categoría "Desarrollo" a "#00FF00"
- "Todas las categorías en amarillo" → Cambiar color de todos los items con kind="category" a "#FFD700"

RESPONDE SIEMPRE EN JSON CON ESTE FORMATO EXACTO:
{
  "action": "modify" | "none",
  "description": "Descripción clara en español de lo que se va a cambiar",
  "gantt": [array completo del Gantt actualizado]
}

Si action es "none", gantt debe ser null y description explica por qué no se hizo el cambio."""

INFO_PROMPT = """Eres un asistente experto en gestión de proyectos y diagramas de Gantt.
El usuario te hace preguntas o pide recomendaciones sobre su proyecto.

Tu rol es:
- Dar información útil sobre gestión de proyectos
- Ofrecer recomendaciones para mejorar el cronograma
- Responder preguntas sobre el proyecto actual
- Ayudar al usuario a formular mejor su solicitud si no es clara

IMPORTANTE - Si el usuario dice algo ambiguo o que no entiendes (como "fondo negro", "azul", etc.):
1. NO digas que "no puedes modificar el Gantt" - eso es confuso
2. EN CAMBIO, pregunta amablemente qué quiere hacer exactamente
3. Ofrece ejemplos concretos de lo que SÍ puedes ayudar

Ejemplos de respuestas útiles:
- "¿Quieres cambiar el color de alguna tarea específica? Por ejemplo: 'Cambia el color de la tarea Testing a rojo'"
- "¿Te refieres a cambiar el color de una categoría o tarea? Dime cuál y qué color prefieres."

Lo que SÍ puedo hacer con el Gantt:
✅ Agregar nuevas tareas o categorías
✅ Eliminar tareas existentes
✅ Cambiar colores de tareas específicas
✅ Modificar duración, fechas o responsables
✅ Extender o acortar tareas

Responde de forma concisa, amigable y útil en español. 
Siempre ofrece ayudar al usuario a lograr lo que necesita."""

STYLE_PROMPT = """Eres un asistente que ayuda a cambiar el estilo visual de un diagrama de Gantt.
El usuario quiere cambiar aspectos visuales como el fondo, tema, colores de columnas o elementos específicos.

PROPIEDADES DE ESTILO DISPONIBLES:

🎨 COLORES GENERALES:
- backgroundColor: color de fondo del diagrama (ej: "#000000" para negro)
- textColor: color general del texto (ej: "#ffffff" para blanco)
- headerColor: color del texto del encabezado de semanas
- gridColor: color de las líneas de la cuadrícula

📊 COLUMNAS ESPECÍFICAS (MUY IMPORTANTE):
- labelColor: color del texto de los TÍTULOS/NOMBRES DE TAREAS (primera columna, la que dice "Diseño", "Development", etc.)
- ownerColor: color del texto de la columna de responsables/owners
- categoryColor: color del texto de las categorías (filas que son categorías)

🎯 ELEMENTOS:
- barTextColor: color del texto dentro de las barras del Gantt

⚠️ INTERPRETACIONES IMPORTANTES:
- "color de las tareas", "color de los títulos", "nombres de actividades", "labels", "primera columna" → labelColor
- "owners", "responsables", "asignados", "segunda columna" → ownerColor
- "categorías", "encabezados de grupo" → categoryColor

EJEMPLOS DE SOLICITUDES:
- "Pon la columna de owners en blanco" → ownerColor: "#ffffff"
- "Texto de las tareas en amarillo" → labelColor: "#ffff00"
- "Títulos en azul" → labelColor: "#0066ff"
- "Nombres de las actividades en rojo" → labelColor: "#ff0000"
- "Color de las categorías en rojo" → categoryColor: "#ff0000"
- "Fondo negro y letras blancas" → backgroundColor: "#000000", textColor: "#ffffff"
- "Owners en verde" → ownerColor: "#00ff00"
- "Primera columna en morado" → labelColor: "#8b5cf6"

RESPONDE SIEMPRE EN JSON CON ESTE FORMATO:
{
  "action": "style",
  "description": "Descripción del cambio de estilo en español",
  "styles": {
    "propiedad": "#hexcolor"
  }
}

Solo incluye las propiedades que el usuario quiere cambiar.
Si pide "fondo negro" o "tema oscuro", ajusta también textColor, headerColor, labelColor y ownerColor a colores claros.
IMPORTANTE: Cuando el usuario mencione "tareas", "títulos", "nombres", "labels", "actividades" → usa labelColor."""

STRUCTURE_PROMPT = """Eres un asistente que ayuda a modificar la ESTRUCTURA del diagrama de Gantt.
El usuario quiere agregar, quitar o modificar columnas del diagrama.

COLUMNAS DISPONIBLES ACTUALMENTE:
- label: Nombre de la tarea (siempre visible, no se puede quitar)
- owner: Responsable de la tarea
- reviewer: Revisor de la tarea (puede agregarse)

ACCIONES POSIBLES:
- addColumn: agregar una nueva columna
- removeColumn: quitar una columna existente

RESPONDE SIEMPRE EN JSON CON ESTE FORMATO:
{
  "action": "structure",
  "description": "Descripción del cambio estructural en español",
  "structure": {
    "operation": "addColumn" | "removeColumn",
    "column": "nombre_de_columna",
    "displayName": "Nombre a mostrar en el encabezado"
  }
}

EJEMPLOS:
- "Agrega columna de revisor" → { "operation": "addColumn", "column": "reviewer", "displayName": "Revisor" }
- "Pon una nueva columna llamada revisor" → { "operation": "addColumn", "column": "reviewer", "displayName": "Revisor" }
- "Quita la columna de owner" → { "operation": "removeColumn", "column": "owner" }
- "Agrega columna de prioridad" → { "operation": "addColumn", "column": "priority", "displayName": "Prioridad" }

IMPORTANTE: La columna "label" nunca se puede quitar."""

LOGO_PROMPT = """Eres un asistente que ayuda a agregar, mover o eliminar LOGOS e IMÁGENES en un diagrama de Gantt.

El usuario puede querer:
- Agregar un logo/imagen proporcionando una URL
- Mover un logo existente a otra posición
- Cambiar el tamaño de un logo
- Eliminar un logo

POSICIONES DISPONIBLES:
- "top-left": Arriba a la izquierda
- "top-center": Arriba en el centro
- "top-right": Arriba a la derecha
- "bottom-left": Abajo a la izquierda
- "bottom-center": Abajo en el centro
- "bottom-right": Abajo a la derecha

RESPONDE SIEMPRE EN JSON CON ESTE FORMATO:
{
  "action": "logo",
  "description": "Descripción del cambio en español",
  "logo": {
    "operation": "add" | "move" | "resize" | "remove",
    "url": "URL de la imagen (solo para add)",
    "position": "top-left" | "top-center" | "top-right" | "bottom-left" | "bottom-center" | "bottom-right",
    "size": número en píxeles (altura, default 50),
    "id": "identificador del logo (para move/resize/remove)"
  }
}

EJEMPLOS:
- "Agrega el logo de EY" (sin URL) → Pide al usuario que proporcione la URL
- "Agrega este logo: https://example.com/logo.png arriba a la derecha" → { "operation": "add", "url": "https://example.com/logo.png", "position": "top-right", "size": 50 }
- "Pon una imagen en la esquina superior izquierda" → Pide la URL
- "Mueve el logo abajo" → { "operation": "move", "position": "bottom-center", "id": "logo-1" }
- "Hazlo más grande" → { "operation": "resize", "size": 80, "id": "logo-1" }
- "Quita el logo" → { "operation": "remove", "id": "logo-1" }

IMPORTANTE: 
- Si el usuario NO proporciona una URL, responde pidiendo que la proporcione.
- Si el usuario menciona "arriba", "superior" usa posiciones top-*
- Si menciona "abajo", "inferior" usa posiciones bottom-*
- Si menciona "izquierda" usa *-left, "derecha" usa *-right, "centro" usa *-center
- El tamaño por defecto es 50px"""


# ============ HELPER FUNCTIONS ============

def add_to_history(role, content):
    """Add a message to conversation history, keeping only the last MAX_HISTORY exchanges"""
    global conversation_history
    conversation_history.append({"role": role, "content": content})
    # Keep only last MAX_HISTORY * 2 messages (pairs of user/assistant)
    if len(conversation_history) > MAX_HISTORY * 2:
        conversation_history = conversation_history[-(MAX_HISTORY * 2):]

def get_history_for_context():
    """Get conversation history formatted for API calls"""
    return conversation_history.copy()


# ============ ROUTES ============

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main endpoint - classifies intent and returns appropriate response.
    For CHANGE: returns confirmation request with pending change_id
    For INFO: returns direct response
    """
    try:
        data = request.json
        user_message = data.get('message', '')
        current_gantt = data.get('currentGantt', [])

        if not user_message:
            return jsonify({'success': False, 'error': 'No message provided'})

        # Add user message to history
        add_to_history("user", user_message)

        # Step 1: Classify intent (with history context for better understanding)
        history_context = get_history_for_context()
        classify_messages = [
            {"role": "system", "content": CLASSIFIER_PROMPT}
        ]
        # Add recent history for context
        classify_messages.extend(history_context[-6:])  # Last 3 exchanges
        classify_messages.append({"role": "user", "content": f"Clasifica esta solicitud: {user_message}"})
        
        classify_response = client.chat.completions.create(
            model="gpt-4o",
            messages=classify_messages,
            temperature=0
        )
        
        intent = classify_response.choices[0].message.content.strip().upper()
        print(f"[CLASSIFIER] Intent: {intent} for message: '{user_message}'")

        if intent == "CHANGE":
            # Step 2a: Generate the change (with history)
            executor_messages = [
                {"role": "system", "content": EXECUTOR_PROMPT}
            ]
            executor_messages.extend(history_context[-6:])
            executor_messages.append({"role": "user", "content": f"Gantt actual:\n{json.dumps(current_gantt, indent=2)}\n\nInstrucción: {user_message}"})
            
            executor_response = client.chat.completions.create(
                model="gpt-4o",
                messages=executor_messages,
                temperature=0.3
            )
            
            response_text = executor_response.choices[0].message.content
            print(f"[EXECUTOR] Response: {response_text[:200]}...")
            
            # Parse JSON response
            try:
                # Clean response if needed
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0]
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0]
                
                result = json.loads(response_text.strip())
                
                if result.get('action') == 'modify' and result.get('gantt'):
                    # Store pending change
                    change_id = str(uuid.uuid4())
                    pending_changes[change_id] = {
                        'gantt': result['gantt'],
                        'description': result.get('description', 'Cambio en el Gantt'),
                        'original_message': user_message
                    }
                    
                    # Add response to history
                    add_to_history("assistant", f"Propongo: {result.get('description', 'Cambio en el Gantt')}")
                    
                    return jsonify({
                        'success': True,
                        'action_type': 'confirm',
                        'change_id': change_id,
                        'description': result.get('description', 'Se modificará el Gantt'),
                        'gantt': result['gantt']  # Preview only
                    })
                else:
                    # No modification needed
                    response_msg = result.get('description', 'No se detectó un cambio válido en el Gantt.')
                    add_to_history("assistant", response_msg)
                    return jsonify({
                        'success': True,
                        'action_type': 'info',
                        'response': response_msg
                    })
                    
            except json.JSONDecodeError as e:
                print(f"[ERROR] JSON parse error: {e}")
                error_msg = '⚠️ No pude procesar el cambio. Por favor, sé más específico sobre qué tarea quieres modificar.'
                add_to_history("assistant", error_msg)
                return jsonify({
                    'success': True,
                    'action_type': 'info',
                    'response': error_msg
                })

        elif intent == "STYLE":
            # Step 2b: Generate style change (with history)
            style_messages = [
                {"role": "system", "content": STYLE_PROMPT}
            ]
            style_messages.extend(history_context[-6:])
            style_messages.append({"role": "user", "content": f"El usuario quiere: {user_message}"})
            
            style_response = client.chat.completions.create(
                model="gpt-4o",
                messages=style_messages,
                temperature=0.3
            )
            
            response_text = style_response.choices[0].message.content
            print(f"[STYLE] Response: {response_text[:200]}...")
            
            try:
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0]
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0]
                
                result = json.loads(response_text.strip())
                
                if result.get('styles'):
                    change_id = str(uuid.uuid4())
                    pending_changes[change_id] = {
                        'type': 'style',
                        'styles': result['styles'],
                        'description': result.get('description', 'Cambio de estilo'),
                        'original_message': user_message
                    }
                    
                    # Add response to history
                    add_to_history("assistant", f"Propongo: {result.get('description', 'Cambio de estilo')}")
                    
                    return jsonify({
                        'success': True,
                        'action_type': 'confirm_style',
                        'change_id': change_id,
                        'description': result.get('description', 'Se cambiará el estilo del diagrama'),
                        'styles': result['styles']
                    })
                    
            except json.JSONDecodeError as e:
                print(f"[ERROR] Style JSON parse error: {e}")
            
            error_msg = '⚠️ No pude procesar el cambio de estilo. Intenta algo como "fondo negro" o "tema oscuro".'
            add_to_history("assistant", error_msg)
            return jsonify({
                'success': True,
                'action_type': 'info',
                'response': error_msg
            })

        elif intent == "STRUCTURE":
            # Step 2c: Generate structure change (with history)
            structure_messages = [
                {"role": "system", "content": STRUCTURE_PROMPT}
            ]
            structure_messages.extend(history_context[-6:])
            structure_messages.append({"role": "user", "content": f"El usuario quiere: {user_message}"})
            
            structure_response = client.chat.completions.create(
                model="gpt-4o",
                messages=structure_messages,
                temperature=0.3
            )
            
            response_text = structure_response.choices[0].message.content
            print(f"[STRUCTURE] Response: {response_text[:200]}...")
            
            try:
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0]
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0]
                
                result = json.loads(response_text.strip())
                
                if result.get('structure'):
                    change_id = str(uuid.uuid4())
                    pending_changes[change_id] = {
                        'type': 'structure',
                        'structure': result['structure'],
                        'description': result.get('description', 'Cambio estructural'),
                        'original_message': user_message
                    }
                    
                    # Add response to history
                    add_to_history("assistant", f"Propongo: {result.get('description', 'Cambio estructural')}")
                    
                    return jsonify({
                        'success': True,
                        'action_type': 'confirm_structure',
                        'change_id': change_id,
                        'description': result.get('description', 'Se modificará la estructura del diagrama'),
                        'structure': result['structure']
                    })
                    
            except json.JSONDecodeError as e:
                print(f"[ERROR] Structure JSON parse error: {e}")
            
            error_msg = '⚠️ No pude procesar el cambio estructural. Intenta algo como "agrega columna de revisor".'
            add_to_history("assistant", error_msg)
            return jsonify({
                'success': True,
                'action_type': 'info',
                'response': error_msg
            })

        elif intent == "LOGO":
            # Step 2d: Generate logo change (with history)
            logo_messages = [
                {"role": "system", "content": LOGO_PROMPT}
            ]
            logo_messages.extend(history_context[-6:])
            logo_messages.append({"role": "user", "content": f"El usuario quiere: {user_message}"})
            
            logo_response = client.chat.completions.create(
                model="gpt-4o",
                messages=logo_messages,
                temperature=0.3
            )
            
            response_text = logo_response.choices[0].message.content
            print(f"[LOGO] Response: {response_text[:200]}...")
            
            try:
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0]
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0]
                
                result = json.loads(response_text.strip())
                
                if result.get('logo'):
                    # Check if URL is needed but not provided
                    logo_data = result['logo']
                    if logo_data.get('operation') == 'add' and not logo_data.get('url'):
                        info_msg = '🖼️ Para agregar un logo, necesito la URL de la imagen. Por favor escribe algo como:\n\n"Agrega este logo: https://ejemplo.com/logo.png arriba a la derecha"'
                        add_to_history("assistant", info_msg)
                        return jsonify({
                            'success': True,
                            'action_type': 'info',
                            'response': info_msg
                        })
                    
                    change_id = str(uuid.uuid4())
                    pending_changes[change_id] = {
                        'type': 'logo',
                        'logo': logo_data,
                        'description': result.get('description', 'Cambio de logo'),
                        'original_message': user_message
                    }
                    
                    # Add response to history
                    add_to_history("assistant", f"Propongo: {result.get('description', 'Cambio de logo')}")
                    
                    return jsonify({
                        'success': True,
                        'action_type': 'confirm_logo',
                        'change_id': change_id,
                        'description': result.get('description', 'Se modificará un logo en el diagrama'),
                        'logo': logo_data
                    })
                    
            except json.JSONDecodeError as e:
                print(f"[ERROR] Logo JSON parse error: {e}")
            
            error_msg = '⚠️ No pude procesar la solicitud del logo. Intenta algo como "agrega este logo: [URL] arriba a la derecha".'
            add_to_history("assistant", error_msg)
            return jsonify({
                'success': True,
                'action_type': 'info',
                'response': error_msg
            })

        else:
            # Step 2e: INFO response (with full history for context)
            info_messages = [
                {"role": "system", "content": INFO_PROMPT}
            ]
            # Include more history for info responses (better context)
            info_messages.extend(history_context)
            info_messages.append({"role": "user", "content": f"Contexto del proyecto (Gantt actual):\n{json.dumps(current_gantt, indent=2)}\n\nPregunta del usuario: {user_message}"})
            
            info_response = client.chat.completions.create(
                model="gpt-4o",
                messages=info_messages,
                temperature=0.7
            )
            
            response_content = info_response.choices[0].message.content
            add_to_history("assistant", response_content)
            
            return jsonify({
                'success': True,
                'action_type': 'info',
                'response': response_content
            })

    except Exception as e:
        print(f"[ERROR] Chat error: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/confirm', methods=['POST'])
def confirm_change():
    """
    Confirm and apply a pending change.
    """
    try:
        data = request.json
        change_id = data.get('change_id')

        if not change_id or change_id not in pending_changes:
            return jsonify({
                'success': False,
                'error': 'Cambio no encontrado o ya expirado'
            })

        # Get and remove pending change
        change = pending_changes.pop(change_id)
        
        # Check if it's a style change, structure change, logo change or gantt change
        if change.get('type') == 'style':
            return jsonify({
                'success': True,
                'type': 'style',
                'styles': change['styles'],
                'message': 'Estilo aplicado exitosamente'
            })
        elif change.get('type') == 'structure':
            return jsonify({
                'success': True,
                'type': 'structure',
                'structure': change['structure'],
                'message': 'Estructura modificada exitosamente'
            })
        elif change.get('type') == 'logo':
            return jsonify({
                'success': True,
                'type': 'logo',
                'logo': change['logo'],
                'message': 'Logo modificado exitosamente'
            })
        else:
            return jsonify({
                'success': True,
                'type': 'gantt',
                'gantt': change['gantt'],
                'message': 'Cambio aplicado exitosamente'
            })

    except Exception as e:
        print(f"[ERROR] Confirm error: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/decline', methods=['POST'])
def decline_change():
    """
    Decline a change and ask for more context.
    """
    try:
        data = request.json
        change_id = data.get('change_id')

        if change_id and change_id in pending_changes:
            change = pending_changes.pop(change_id)
            original_message = change.get('original_message', '')
            
            response_msg = f'Entendido, no aplicaré el cambio. 🤔\n\nTu solicitud original fue: "{original_message}"\n\n¿Podrías darme más detalles sobre exactamente qué quieres modificar? Por ejemplo:\n- ¿Qué tarea específica?\n- ¿Qué propiedad cambiar (duración, color, fecha)?\n- ¿Cuál debería ser el nuevo valor?'
            add_to_history("assistant", response_msg)
            
            return jsonify({
                'success': True,
                'response': response_msg
            })
        
        response_msg = '🤔 Por favor, explícame con más detalle qué cambio necesitas hacer en el Gantt.'
        add_to_history("assistant", response_msg)
        return jsonify({
            'success': True,
            'response': response_msg
        })

    except Exception as e:
        print(f"[ERROR] Decline error: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear conversation history."""
    global conversation_history
    conversation_history = []
    return jsonify({
        'success': True,
        'message': 'Historial de conversación limpiado'
    })


@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    """
    Streaming endpoint for INFO responses.
    Uses Server-Sent Events (SSE) for real-time streaming.
    """
    try:
        data = request.json
        user_message = data.get('message', '')
        current_gantt = data.get('currentGantt', [])

        if not user_message:
            return jsonify({'success': False, 'error': 'No message provided'})

        # Add user message to history
        add_to_history("user", user_message)
        
        # Get history context
        history_context = get_history_for_context()

        # First, classify the intent (non-streaming)
        classify_messages = [
            {"role": "system", "content": CLASSIFIER_PROMPT}
        ]
        classify_messages.extend(history_context[-6:])
        classify_messages.append({"role": "user", "content": f"Clasifica esta solicitud: {user_message}"})
        
        classify_response = client.chat.completions.create(
            model="gpt-4o",
            messages=classify_messages,
            temperature=0
        )
        
        intent = classify_response.choices[0].message.content.strip().upper()
        print(f"[CLASSIFIER-STREAM] Intent: {intent}")

        # If not INFO, return JSON response to handle differently
        if intent != "INFO":
            return jsonify({
                'success': True,
                'action_type': 'redirect',
                'intent': intent,
                'message': 'Use /api/chat for this request type'
            })

        # For INFO: Stream the response
        def generate():
            info_messages = [
                {"role": "system", "content": INFO_PROMPT}
            ]
            info_messages.extend(history_context)
            info_messages.append({
                "role": "user", 
                "content": f"Contexto del proyecto (Gantt actual):\n{json.dumps(current_gantt, indent=2)}\n\nPregunta del usuario: {user_message}"
            })
            
            full_response = ""
            
            try:
                stream = client.chat.completions.create(
                    model="gpt-4o",
                    messages=info_messages,
                    temperature=0.7,
                    stream=True
                )
                
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        # Send as SSE event
                        yield f"data: {json.dumps({'content': content})}\n\n"
                
                # Add complete response to history
                add_to_history("assistant", full_response)
                
                # Send done event
                yield f"data: {json.dumps({'done': True})}\n\n"
                
            except Exception as e:
                print(f"[ERROR] Stream error: {e}")
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return Response(
            stream_with_context(generate()),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'X-Accel-Buffering': 'no',
                'Connection': 'keep-alive'
            }
        )

    except Exception as e:
        print(f"[ERROR] Chat stream error: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'pending_changes': len(pending_changes),
        'conversation_history_length': len(conversation_history)
    })


if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Gantt Editor Orchestrator Backend")
    print("=" * 50)
    print("Endpoints:")
    print("  POST /api/chat          - Classify intent & generate response")
    print("  POST /api/chat/stream   - Stream INFO responses (SSE)")
    print("  POST /api/confirm       - Apply pending change")
    print("  POST /api/decline       - Decline & ask for context")
    print("  POST /api/clear-history - Clear conversation memory")
    print("  GET  /api/health        - Health check")
    print(f"  Memory: Last {MAX_HISTORY} conversations")
    print("=" * 50)
    app.run(debug=True, port=8000)
