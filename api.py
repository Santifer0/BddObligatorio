from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from datetime import timedelta
from modelos.login import loggin
from modelos.insumo import obtener_Insumos, agregar_insumo, eliminar_insumo, modificar_insumo
from modelos.clientes import obtener_clientes, agregar_cliente, eliminar_cliente, modificar_cliente
from modelos.mantenimientos import agregar_mantenimiento, obtener_mantenimientos, eliminar_mantenimiento, modificar_mantenimiento
from modelos.proveedores import obtener_proveedores, agregar_proveedor, eliminar_proveedor, modificar_proveedor
from modelos.tecnico import obtener_tecnicos, agregar_tecnico, eliminar_tecnico, modificar_tecnico
from modelos.usuario import obtener_usuarios, agregar_usuario, eliminar_usuario, modificar_usuario
from modelos.maquina import obtener_maquinas, agregar_maquina, eliminar_maquina, modificar_maquina
from modelos.registros import consumo_insumos, total_cobrar_cliente, mantenimientos_por_tecnico, maquinas_por_cliente, alquiler_mensual_cliente


app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:5000"])
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"  # Menos restrictivo que None
app.config["SESSION_COOKIE_SECURE"] = False  # Para desarrollo local
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SECRET_KEY"] = "tu_clave_secreta"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)
Session(app)

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    usuario = data['nombre']
    contrasenia = data['contrasenia']
    resultado = loggin(usuario, contrasenia)
    if resultado == "admin":
        session['user'] = usuario
        session['role'] = "admin"
        session.permanent = True 
        print('LOGIN: role set to', session['role'])
        return jsonify({"status": "ok", "Permiso": True, "userName": usuario})
    elif resultado == "user":
        session['user'] = usuario
        session['role'] = "user"
        session.permanent = True
        print('LOGIN: role set to', session['role'])
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

@app.route('/api/proveedores/alta', methods=['POST', 'OPTIONS'])
def alta_proveedor():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en alta_proveedor:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado"}), 403
    
    data = request.json
    nombre = data['nombre']
    contacto = data['contacto']
    resultado = agregar_proveedor(nombre, contacto, permiso)
    if resultado.get("status") == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 201

@app.route('/api/proveedores/baja', methods=['DELETE', 'OPTIONS'])
def baja_proveedor():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en baja_proveedor:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado"}), 403
    
    data = request.json
    id_proveedor = data['id']
    resultado = eliminar_proveedor(id_proveedor, permiso)
    if resultado.get("status") == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 200

@app.route('/api/proveedores/modificacion', methods=['PUT', 'OPTIONS'])
def modificacion_proveedor():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en modificacion_proveedor:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado"}), 403
    
    data = request.json
    id_proveedor = data['id']
    nombre = data['nombre']
    contacto = data['contacto']
    resultado = modificar_proveedor(id_proveedor, nombre, contacto, permiso)
    if resultado.get("status") == "error":
        return jsonify(resultado), 400
    else:
        return jsonify(resultado), 200

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    try:
        data = obtener_clientes()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/clientes/alta', methods=['POST'])
def alta_cliente():
    data = request.json
    nombre = data['nombre']
    direccion = data['direccion']
    telefono = data['telefono']
    correo = data['correo']
    agregar_cliente(nombre, direccion, telefono, correo)
    return jsonify({"status": "ok"}), 201

@app.route('/api/clientes/baja', methods=['DELETE'])
def baja_cliente():
    data = request.json
    id_cliente = data['id']
    eliminar_cliente(id_cliente)
    return jsonify({"status": "ok"}), 200

@app.route('/api/clientes/modificacion', methods=['PUT'])
def modificacion_cliente():
    data = request.json
    id_cliente = data['id']
    nombre = data['nombre']
    direccion = data['direccion']
    telefono = data['telefono']
    correo = data['correo']
    modificar_cliente(id_cliente, nombre, direccion, telefono, correo)
    return jsonify({"status": "ok"}), 200

@app.route('/api/proveedores', methods=['GET', 'OPTIONS'])
def get_proveedores():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en get_proveedores:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado"}), 403
    
    try:
        data = obtener_proveedores()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/check-session', methods=['GET', 'OPTIONS'])
def check_session():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en check-session:', dict(session))
    role = session.get('role')
    user = session.get('user')
    
    if role and user:
        return jsonify({
            "status": "ok", 
            "logged_in": True,
            "role": role,
            "user": user,
            "Permiso": role == "admin"
        }), 200
    else:
        return jsonify({
            "status": "error", 
            "logged_in": False,
            "message": "No hay sesión activa"
        }), 401

@app.route('/api/insumos', methods=['GET', 'OPTIONS'])
def get_insumos():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = obtener_Insumos()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/mantenimientos', methods=['GET'])
def get_mantenimientos():
    print('SESSION en get_mantenimientos:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso not in ["admin", "user"]:
        return jsonify({"status": "error", "message": "Sesión requerida"}), 401
    
    try:
        data = obtener_mantenimientos(permiso)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/mantenimientos/alta', methods=['POST'])
def alta_mantenimiento():
    print('SESSION en alta_mantenimiento:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso not in ["admin", "user"]:
        return jsonify({"status": "error", "message": "Sesión requerida"}), 401
    
    data = request.json
    id_maquina = data['id_maquina']
    ci_tecnico = data['ci_tecnico']
    tipo = data['tipo']
    fecha = data['fecha']
    observaciones = data['observaciones']
    
    try:
        agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones, permiso)
        return jsonify({"status": "ok"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/api/mantenimientos/baja', methods=['DELETE'])
def baja_mantenimiento():
    print('SESSION en baja_mantenimiento:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso not in ["admin", "user"]:
        return jsonify({"status": "error", "message": "Sesión requerida"}), 401
    
    data = request.json
    id_mantenimiento = data['id']
    eliminar_mantenimiento(id_mantenimiento, permiso)
    return jsonify({"status": "ok"}), 200

@app.route('/api/mantenimientos/modificacion', methods=['PUT'])
def modificacion_mantenimiento():
    print('SESSION en modificacion_mantenimiento:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso not in ["admin", "user"]:
        return jsonify({"status": "error", "message": "Sesión requerida"}), 401
    
    data = request.json
    id_mantenimiento = data['id']
    id_maquina = data['id_maquina']
    ci_tecnico = data['ci_tecnico']
    tipo = data['tipo']
    fecha = data['fecha']
    observaciones = data['observaciones']
    
    try:
        modificar_mantenimiento(id_mantenimiento, id_maquina, ci_tecnico, tipo, fecha, observaciones, permiso)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/api/tecnicos', methods=['GET', 'OPTIONS'])
def get_tecnicos():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en get_tecnicos:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden acceder a técnicos"}), 403
    
    try:
        data = obtener_tecnicos(permiso)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/api/tecnicos/alta', methods=['POST', 'OPTIONS'])
def alta_tecnico():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en alta_tecnico:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden crear técnicos"}), 403
    
    data = request.json
    ci = data['ci']
    nombre = data['nombre']
    telefono = data['telefono']
    agregar_tecnico(ci, nombre, telefono, permiso)
    return jsonify({"status": "ok"}), 201

@app.route('/api/tecnicos/baja', methods=['DELETE', 'OPTIONS'])
def baja_tecnico():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en baja_tecnico:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden eliminar técnicos"}), 403
    
    data = request.json
    ci_tecnico = data['ci']
    eliminar_tecnico(ci_tecnico, permiso)
    return jsonify({"status": "ok"}), 200

@app.route('/api/tecnicos/modificacion', methods=['PUT', 'OPTIONS'])
def modificacion_tecnico():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en modificacion_tecnico:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden modificar técnicos"}), 403
    
    data = request.json
    ci_tecnico = data['ci']
    nombre = data['nombre']
    telefono = data['telefono']
    modificar_tecnico(ci_tecnico, nombre, telefono, permiso)
    return jsonify({"status": "ok"}), 200

# Endpoints para usuarios (solo admin)
@app.route('/api/usuarios', methods=['GET', 'OPTIONS'])
def get_usuarios():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en get_usuarios:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden acceder a usuarios"}), 403
    
    try:
        data = obtener_usuarios(permiso)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/usuarios/alta', methods=['POST', 'OPTIONS'])
def alta_usuario():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en alta_usuario:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden crear usuarios"}), 403
    
    data = request.json
    nombre_publico = data['nombre_publico']
    nombre = data['nombre']
    contrasenia = data['contrasenia']
    permisos = data['permisos']
    agregar_usuario(nombre_publico, nombre, contrasenia, permisos, permiso)
    return jsonify({"status": "ok"}), 201

@app.route('/api/usuarios/baja', methods=['DELETE', 'OPTIONS'])
def baja_usuario():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en baja_usuario:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden eliminar usuarios"}), 403
    
    data = request.json
    id_usuario = data['id']
    eliminar_usuario(id_usuario, permiso)
    return jsonify({"status": "ok"}), 200

@app.route('/api/usuarios/modificacion', methods=['PUT', 'OPTIONS'])
def modificacion_usuario():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en modificacion_usuario:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden modificar usuarios"}), 403
    
    data = request.json
    id_usuario = data['id']
    nombre_publico = data['nombre_publico']
    nombre = data['nombre']
    contrasenia = data.get('contrasenia', '')  # Opcional
    permisos = data['permisos']
    modificar_usuario(id_usuario, nombre_publico, nombre, contrasenia, permisos, permiso)
    return jsonify({"status": "ok"}), 200

# Endpoints para máquinas (solo admin)
@app.route('/api/maquinas', methods=['GET', 'OPTIONS'])
def get_maquinas():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en get_maquinas:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden acceder a máquinas"}), 403
    
    try:
        data = obtener_maquinas(permiso)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/maquinas/alta', methods=['POST', 'OPTIONS'])
def alta_maquina():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en alta_maquina:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden crear máquinas"}), 403
    
    data = request.json
    modelo = data['modelo']
    id_cliente = data['idCliente']
    ubicacion = data['ubicacionCliente']
    costo = data['costo_alquiler']
    agregar_maquina(modelo, id_cliente, ubicacion, costo, permiso)
    return jsonify({"status": "ok"}), 201

@app.route('/api/maquinas/baja', methods=['DELETE', 'OPTIONS'])
def baja_maquina():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en baja_maquina:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden eliminar máquinas"}), 403
    
    data = request.json
    id_maquina = data['id']
    eliminar_maquina(id_maquina, permiso)
    return jsonify({"status": "ok"}), 200

@app.route('/api/maquinas/modificacion', methods=['PUT', 'OPTIONS'])
def modificacion_maquina():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en modificacion_maquina:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Solo administradores pueden modificar máquinas"}), 403
    
    data = request.json
    id_maquina = data['id']
    modelo = data['modelo']
    id_cliente = data['id_cliente']
    ubicacion = data['ubicacion']
    costo = data['costo']
    modificar_maquina(id_maquina, modelo, id_cliente, ubicacion, costo, permiso)
    return jsonify({"status": "ok"}), 200


@app.route('/api/registro/alquiler', methods=['GET', 'OPTIONS'])
def registro_alquiler():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en registro_alquiler:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Se requiere permisos de administrador."}), 403

    data = alquiler_mensual_cliente()
    return jsonify(data), 200

@app.route('/api/registro/mantenimientos-tecnico', methods=['GET', 'OPTIONS'])
def registro_mantenimientos_tecnico():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en registro_mantenimientos_tecnico:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Se requiere permisos de administrador."}), 403

    data = mantenimientos_por_tecnico()
    return jsonify(data), 200

@app.route('/api/registro/maquinas-cliente', methods=['GET', 'OPTIONS'])
def registro_maquinas_cliente():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en registro_maquinas_cliente:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Se requiere permisos de administrador."}), 403

    data = maquinas_por_cliente()
    return jsonify(data), 200

@app.route('/api/registro/consumo', methods=['POST', 'OPTIONS'])
def registro_consumo():
    if request.method == 'OPTIONS':
        return '', 204

    data = request.json
    id_maquina = data['id_maquina']
    id_insumo = data['id_insumo']
    cantidad = data['cantidad']
    fecha = data['fecha']
    resultado = consumo_insumos(id_maquina, id_insumo, fecha, cantidad)
    if resultado["status"] == "ok":
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

@app.route('/api/registro/consumo/reporte', methods=['GET', 'OPTIONS'])
def reporte_total_cobrar_cliente():
    if request.method == 'OPTIONS':
        return '', 204
    
    print('SESSION en reporte_total_cobrar_cliente:', dict(session))
    permiso = session.get('role')
    print('PERMISO obtenido de sesión:', permiso)
    
    if permiso != "admin":
        return jsonify({"status": "error", "message": "Permiso denegado. Se requiere permisos de administrador."}), 403
    
    data = total_cobrar_cliente()
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)