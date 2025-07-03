#!/usr/bin/env python3
import requests

# Test simple de login
session = requests.Session()

def test_login():
    print("🔑 Probando login con admin...")
    response = session.post("http://localhost:5000/api/login", 
                           json={"nombre": "admin", "contrasenia": "admin"},
                           headers={"Content-Type": "application/json"})
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        print("✅ Login exitoso")
        return True
    else:
        print("❌ Login falló")
        return False

def test_session():
    print("\n🔍 Verificando sesión...")
    response = session.get("http://localhost:5000/api/check-session")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

def test_tecnicos():
    print("\n👨‍🔧 Probando endpoint de técnicos...")
    response = session.get("http://localhost:5000/api/tecnicos")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    if test_login():
        test_session()
        test_tecnicos()
