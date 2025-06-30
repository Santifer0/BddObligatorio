from flask import Flask, request, jsonify
from flask_cors import CORS
from modelos.login import loggin
from modelos.insumo import obtener_Insumos, agregar_insumo, eliminar_insumo, modificar_insumo


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

@app.route('/api/insumos/alta', methods=['POST'])
def alta():
    data = request.json
    nombre = data['nombre']
    precio = data['precio']
    id_proveedor = data['idProveedor']
    resultado = agregar_insumo(nombre, precio, id_proveedor)
    if isinstance(resultado, list) and resultado[0] == "No loggeado":
        return jsonify({"status": "error", "message": "No loggeado"}), 401
    return jsonify({"status": "ok", "message": "Insumo agregado correctamente"}), 201

@app.route('/api/insumos/baja', methods=['DELETE'])
def baja():
    data = request.json
    id_insumo = data['id']
    resultado = eliminar_insumo(id_insumo)
    if isinstance(resultado, list) and resultado[0] == "No loggeado":
        return jsonify({"status": "error", "message": "No loggeado"}), 401
    return jsonify({"status": "ok", "message": "Insumo eliminado correctamente"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
