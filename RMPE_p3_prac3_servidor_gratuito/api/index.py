from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Base de datos simulada del catálogo
catalogo_juegos = [
    {
        "id": 1,
        "nombre": "Ixora",
        "precio": 149.00,
        "descripcion": "Metroidvania ecológico basado en Tonalá.",
        "imagen": "imagenes/IxoraLogo.png"
    }
]

# Ruta GET para el catálogo
@app.route('/api/juegos', methods=['GET'])
def obtener_juegos():
    return jsonify(catalogo_juegos)

# Ruta POST para el login simulado
@app.route('/api/login', methods=['POST'])
def login():
    datos = request.json
    usuario_bd = "pablo"
    password_bd = "ceti123"

    if datos.get('usuario') == usuario_bd and datos.get('password') == password_bd:
        return jsonify({"status": "ok", "mensaje": "Bienvenido a Sonoma Studio"})
    else:
        return jsonify({"status": "error", "mensaje": "Usuario o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)