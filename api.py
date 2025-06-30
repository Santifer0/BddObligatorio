from flask import Flask, request, jsonify
from flask_cors import CORS
from modelos.login import loggin

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    usuario = data['nombre']
    contrasenia = data['contrasenia']
    resultado = loggin(usuario, contrasenia)
    if resultado:
        # Aquí puedes devolver permisos, nombre, etc.
        return jsonify({"status": "ok", "Permiso": True, "userName": usuario})
    else:
        return jsonify({"status": "error"}), 401