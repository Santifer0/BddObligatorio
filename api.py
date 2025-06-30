from flask import Flask, request, jsonify
from flask_cors import CORS
from modelos.login import loggin

app = Flask(__name__)  # <- Esta línea crea la app
CORS(app)  # Permite peticiones desde el frontend

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    usuario = data['nombre']
    contrasenia = data['contrasenia']
    resultado = loggin(usuario, contrasenia)
    if resultado  == "admin":
        return jsonify({"status": "ok", "Permiso": True, "userName": usuario})
    elif resultado == "user":
        return jsonify({"status": "ok", "Permiso": False, "userName": usuario})
    else:
        return jsonify({"status": "error"}), 401

@app.route('/api/alta', methods=['POST'])
def alta():
    data = request.json
    # Aquí iría la lógica para alta de usuario o entidad
    # Por ejemplo, insertar datos en la base de datos
    try:
        # Simulación de inserción en la base de datos
        nombre = data['nombre']
        correo = data['correo']
        # Llamar a la función del modelo correspondiente
        # Por ejemplo: resultado = modelo.alta(nombre, correo)
        return jsonify({"status": "ok", "message": "Alta realizada con éxito"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
