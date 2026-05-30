from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import redis
import json

app = Flask(__name__)
CORS(app) 

# --- CONEXIÓN A LA BASE DE DATOS UPSTASH ---
db = None
if os.environ.get('KV_URL'):
    db = redis.from_url(os.environ.get('KV_URL'))

# 1. Catálogo de Juegos
catalogo_juegos = [{
    "id": 1,
    "nombre": "Ixora",
    "precio": 149.00,
    "descripcion": "Metroidvania ecológico basado en Tonalá.",
    "imagen": "imagenes/IxoraLogo.png"
}]

@app.route('/api/juegos', methods=['GET'])
def obtener_juegos():
    return jsonify(catalogo_juegos)

# 2. Login Simulado
@app.route('/api/login', methods=['POST'])
def login():
    datos = request.json
    if datos.get('usuario') == "pablo" and datos.get('password') == "ceti123":
        return jsonify({"status": "ok", "mensaje": "Bienvenido a Sonoma Studio"})
    else:
        return jsonify({"status": "error", "mensaje": "Credenciales incorrectas"}), 401

# 3. Guardar Encuesta
@app.route('/api/encuesta', methods=['POST'])
def guardar_encuesta():
    datos = request.json
    if db:
        db.lpush('encuestas_ixora', json.dumps(datos))
        return jsonify({"status": "ok", "mensaje": "¡Encuesta guardada con éxito!"})
    else:
        return jsonify({"status": "error", "mensaje": "Error conectando a la BD"}), 500

# 4. Ver Encuestas (Esta es la ruta que te daba el error 404)
@app.route('/api/ver_encuestas', methods=['GET'])
def ver_encuestas():
    if db:
        registros = db.lrange('encuestas_ixora', 0, -1)
        lista_registros = [json.loads(r) for r in registros]
        return jsonify(lista_registros)
    return jsonify({"mensaje": "Sin base de datos conectada"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
