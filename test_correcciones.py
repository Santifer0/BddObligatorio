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
        return True
    else:
        print(f"❌ Error en login: {response.status_code} - {response.text}")
        return False

def test_crear_usuario():
    """Test crear usuario con permisos convertidos a entero"""
    print("\n👤 Probando crear usuario...")
    
    nuevo_usuario = {
        "nombre_publico": "Usuario Test",
        "nombre": "usertest",
        "contrasenia": "test123",
        "permisos": "user"  # Esto se convertirá a 0 automáticamente
    }
    response = session.post(f"{BASE_URL}/api/usuarios/alta", json=nuevo_usuario)
    if response.status_code == 201:
        print("✅ Crear usuario: OK")
    else:
        print(f"❌ Error creando usuario: {response.status_code}")
        if response.status_code != 500:  # Si no es error 500, mostrar el texto
            print(f"   Respuesta: {response.text}")

def test_crear_maquina():
    """Test crear máquina con nombres de columnas correctos"""
    print("\n🏭 Probando crear máquina...")
    
    nueva_maquina = {
        "modelo": "Nueva Máquina Test",
        "id_cliente": 1,  # Asumiendo que existe cliente con ID 1
        "ubicacion": "Ubicación Test",
        "costo": 2500.50
    }
    response = session.post(f"{BASE_URL}/api/maquinas/alta", json=nueva_maquina)
    if response.status_code == 201:
        print("✅ Crear máquina: OK")
    else:
        print(f"❌ Error creando máquina: {response.status_code}")
        if response.status_code != 500:  # Si no es error 500, mostrar el texto
            print(f"   Respuesta: {response.text}")

def test_obtener_maquinas():
    """Test obtener máquinas"""
    print("\n🏭 Probando obtener máquinas...")
    
    response = session.get(f"{BASE_URL}/api/maquinas")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Obtener máquinas: OK - {len(data)} máquinas encontradas")
        if data:
            print(f"   Primera máquina: {data[0]}")
    else:
        print(f"❌ Error obteniendo máquinas: {response.status_code}")
        if response.status_code != 500:
            print(f"   Respuesta: {response.text}")

def test_obtener_mantenimientos():
    """Test obtener mantenimientos"""
    print("\n🔧 Probando obtener mantenimientos...")
    
    response = session.get(f"{BASE_URL}/api/mantenimientos")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Obtener mantenimientos: OK - {len(data)} mantenimientos encontrados")
        if data:
            print(f"   Primer mantenimiento: {data[0]}")
    else:
        print(f"❌ Error obteniendo mantenimientos: {response.status_code}")
        if response.status_code != 500:
            print(f"   Respuesta: {response.text}")

def main():
    print("🔧 Probando correcciones de alta usuarios y máquinas...")
    
    if test_login_admin():
        test_obtener_maquinas()
        test_crear_maquina()
        test_crear_usuario()
        test_obtener_mantenimientos()
    
    print("\n✨ Pruebas de corrección completadas!")

if __name__ == "__main__":
    main()
