#!/usr/bin/env python3
import requests
import json

# Configuración
BASE_URL = "http://localhost:5000"
session = requests.Session()

def test_login_admin():
    """Test de login como administrador"""
    print("🔑 Probando login como admin...")
    response = session.post(f"{BASE_URL}/api/login", 
                           json={"nombre": "admin", "contrasenia": "admin"},
                           headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Login exitoso: {data}")
        return data.get("Permiso", False)
    else:
        print(f"❌ Error en login: {response.status_code} - {response.text}")
        return False

def test_tecnicos():
    """Test de endpoints de técnicos (requiere admin)"""
    print("\n👨‍🔧 Probando endpoints de técnicos...")
    
    # Obtener técnicos
    response = session.get(f"{BASE_URL}/api/tecnicos")
    if response.status_code == 200:
        print("✅ Obtener técnicos: OK")
        print(f"   Técnicos encontrados: {len(response.json())}")
    else:
        print(f"❌ Error obteniendo técnicos: {response.status_code} - {response.text}")
    
    # Crear técnico
    nuevo_tecnico = {
        "ci": "12345678",
        "nombre": "Juan Test",
        "telefono": "099123456"
    }
    response = session.post(f"{BASE_URL}/api/tecnicos/alta", json=nuevo_tecnico)
    if response.status_code == 201:
        print("✅ Crear técnico: OK")
    else:
        print(f"❌ Error creando técnico: {response.status_code} - {response.text}")

def test_usuarios():
    """Test de endpoints de usuarios (requiere admin)"""
    print("\n👤 Probando endpoints de usuarios...")
    
    # Obtener usuarios
    response = session.get(f"{BASE_URL}/api/usuarios")
    if response.status_code == 200:
        print("✅ Obtener usuarios: OK")
        print(f"   Usuarios encontrados: {len(response.json())}")
    else:
        print(f"❌ Error obteniendo usuarios: {response.status_code} - {response.text}")
    
    # Crear usuario
    nuevo_usuario = {
        "nombre_publico": "Test User",
        "nombre": "testuser",
        "contrasenia": "test123",
        "permisos": "user"
    }
    response = session.post(f"{BASE_URL}/api/usuarios/alta", json=nuevo_usuario)
    if response.status_code == 201:
        print("✅ Crear usuario: OK")
    else:
        print(f"❌ Error creando usuario: {response.status_code} - {response.text}")

def test_maquinas():
    """Test de endpoints de máquinas (requiere admin)"""
    print("\n🏭 Probando endpoints de máquinas...")
    
    # Obtener máquinas
    response = session.get(f"{BASE_URL}/api/maquinas")
    if response.status_code == 200:
        print("✅ Obtener máquinas: OK")
        print(f"   Máquinas encontradas: {len(response.json())}")
    else:
        print(f"❌ Error obteniendo máquinas: {response.status_code} - {response.text}")
    
    # Crear máquina (necesitamos un cliente existente)
    nueva_maquina = {
        "modelo": "Test Model X1",
        "id_cliente": 1,  # Asumiendo que existe cliente con ID 1
        "ubicacion": "Test Location",
        "costo": 1500.00
    }
    response = session.post(f"{BASE_URL}/api/maquinas/alta", json=nueva_maquina)
    if response.status_code == 201:
        print("✅ Crear máquina: OK")
    else:
        print(f"❌ Error creando máquina: {response.status_code} - {response.text}")

def test_mantenimientos():
    """Test de endpoints de mantenimientos (admin y user)"""
    print("\n🔧 Probando endpoints de mantenimientos...")
    
    # Obtener mantenimientos
    response = session.get(f"{BASE_URL}/api/mantenimientos")
    if response.status_code == 200:
        print("✅ Obtener mantenimientos: OK")
        print(f"   Mantenimientos encontrados: {len(response.json())}")
    else:
        print(f"❌ Error obteniendo mantenimientos: {response.status_code} - {response.text}")

def test_login_user():
    """Test de login como usuario regular"""
    print("\n🔑 Probando login como usuario regular...")
    response = session.post(f"{BASE_URL}/api/login", 
                           json={"nombre": "tecnico1", "contrasenia": "tecnico"},
                           headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Login como user exitoso: {data}")
        return data.get("Permiso", False)
    else:
        print(f"❌ Error en login como user: {response.status_code} - {response.text}")
        return False

def test_permisos_user():
    """Test que usuario regular no pueda acceder a endpoints de admin"""
    print("\n🚫 Probando restricciones de permisos para usuarios regulares...")
    
    endpoints_admin = [
        "/api/tecnicos",
        "/api/usuarios", 
        "/api/maquinas"
    ]
    
    for endpoint in endpoints_admin:
        response = session.get(f"{BASE_URL}{endpoint}")
        if response.status_code == 403:
            print(f"✅ Permiso denegado correctamente para {endpoint}")
        else:
            print(f"❌ ERROR: Usuario regular pudo acceder a {endpoint} (código: {response.status_code})")

def main():
    print("🚀 Iniciando pruebas de API completa...")
    
    # Test 1: Login como admin y probar endpoints que requieren admin
    is_admin = test_login_admin()
    if is_admin:
        test_tecnicos()
        test_usuarios()
        test_maquinas()
        test_mantenimientos()
    
    # Test 2: Login como user y verificar restricciones
    print("\n" + "="*50)
    is_user = test_login_user()
    if is_user is False:  # Solo users regulares
        test_permisos_user()
        test_mantenimientos()  # Users pueden acceder a mantenimientos
    
    print("\n✨ Pruebas completadas!")

if __name__ == "__main__":
    main()
