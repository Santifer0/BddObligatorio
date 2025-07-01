from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from modelos.login import loggin
from modelos.insumo import obtener_Insumos, agregar_insumo, eliminar_insumo, modificar_insumo


app = Flask(__name__)  # <- Esta línea crea la app
CORS(app, supports_credentials=True, origins=["http://localhost:5173", "http://127.0.0.1:5173"])
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "tu_clave_secreta"
Session(app)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    usuario = data['nombre']
    contrasenia = data['contrasenia']
    resultado = loggin(usuario, contrasenia)
    if resultado  == "admin":
        session['user'] = usuario
        session['role'] = "admin"
        return jsonify({"status": "ok", "Permiso": True, "userName": usuario})
    elif resultado == "user":
        session['user'] = usuario
        session['role'] = "user"
        return jsonify({"status": "ok", "Permiso": False, "userName": usuario})
    else:
        return jsonify({"status": "error"}), 401

@app.route('/api/insumos/alta', methods=['POST'])
def alta():
    data = request.json
    nombre = data['nombre']
    precio = data['precio']
    id_proveedor = data['idProveedor']
    resultado = agregar_insumo(nombre, precio, id_proveedor)
    if resultado["status"] == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 201

@app.route('/api/insumos/baja', methods=['DELETE'])
def baja():
    data = request.json
    id_insumo = data['id']
    resultado = eliminar_insumo(id_insumo)
    if resultado["status"] == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 200

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"status": "ok", "message": "Sesión cerrada exitosamente"})

@app.route('/api/verify-login', methods=['POST'])
def verify_login():
    data = request.json
    usuario = data.get('nombre')
    contrasenia = data.get('contrasenia')
    
    if not usuario or not contrasenia:
        return jsonify({"status": "error", "message": "Faltan credenciales"}), 400
    
    resultado = loggin(usuario, contrasenia)
    if resultado == "admin":
        return jsonify({"status": "ok", "Permiso": True, "userName": usuario})
    elif resultado == "user":
        return jsonify({"status": "ok", "Permiso": False, "userName": usuario})
    else:
        return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

@app.route('/api/insumos/modificacion', methods=['PUT'])
def modificacion_insumo():
    data = request.json
    id_insumo = data['id']
    nombre = data['nombre']
    precio = data['precio']
    id_proveedor = data['idProveedor']
    resultado = modificar_insumo(id_insumo, nombre, precio, id_proveedor)
    if resultado["status"] == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
