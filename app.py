from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controladores.login_control import verificar_login
import dataBase

app = Flask(__name__)
CORS(app)  # Permitir requests del frontend

@app.route('/')
def home():
    return jsonify({"message": "API Backend funcionando correctamente"})

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        correo = data.get('correo')
        contraseña = data.get('contraseña')
        
        if not correo or not contraseña:
            return jsonify({"error": "Correo y contraseña son requeridos"}), 400
        
        resultado = verificar_login(correo, contraseña)
        
        if resultado:
            permisos = resultado[0]
            return jsonify({
                "success": True,
                "es_administrador": bool(permisos),
                "message": "Login exitoso"
            })
        else:
            return jsonify({
                "success": False,
                "message": "Credenciales incorrectas"
            }), 401
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test-db', methods=['GET'])
def test_database():
    try:
        conn = dataBase.connectUsuario()
        if conn.is_connected():
            conn.close()
            return jsonify({"message": "Conexión a base de datos exitosa"})
        else:
            return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
