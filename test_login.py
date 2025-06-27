import requests
import json

def probar_login():
    url = "http://localhost:5000/api/login"
    
    # Datos de prueba
    credenciales = {
        "correo": "admin",
        "contraseña": "miContrasenia"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("🔍 Probando login con admin...")
        response = requests.post(url, json=credenciales, headers=headers)
        
        print(f"Estado: {response.status_code}")
        print(f"Respuesta: {response.json()}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Login exitoso!")
                print(f"Es administrador: {data.get('es_administrador')}")
            else:
                print("❌ Login falló")
        else:
            print(f"❌ Error HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def probar_tecnico():
    url = "http://localhost:5000/api/login"
    
    credenciales = {
        "correo": "tecnico1",
        "contraseña": "miContraseniaSegura"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("\n🔍 Probando login con tecnico1...")
        response = requests.post(url, json=credenciales, headers=headers)
        
        print(f"Estado: {response.status_code}")
        print(f"Respuesta: {response.json()}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Login exitoso!")
                print(f"Es administrador: {data.get('es_administrador')}")
            else:
                print("❌ Login falló")
        else:
            print(f"❌ Error HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    probar_login()
    probar_tecnico()
