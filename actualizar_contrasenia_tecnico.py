#!/usr/bin/env python3
from dataBase import get_connection

def actualizar_contrasenia_tecnico():
    """Actualizar contraseña del usuario tecnico1"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor()
        
        cursor.execute("UPDATE usuarios SET contrasenia = SHA2('tecnico', 256) WHERE nombre = 'tecnico1'")
        conn.commit()
        print("✅ Contraseña de tecnico1 actualizada a 'tecnico'")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    actualizar_contrasenia_tecnico()
