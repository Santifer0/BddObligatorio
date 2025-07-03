#!/usr/bin/env python3
from dataBase import get_connection

def verificar_contrasenia():
    """Verificar hash de contraseña en la base de datos"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor(dictionary=True)
        
        # Verificar hash actual
        cursor.execute("SELECT nombre, contrasenia FROM usuarios WHERE nombre = 'admin'")
        admin = cursor.fetchone()
        
        if admin:
            print(f"Usuario: {admin['nombre']}")
            print(f"Hash actual: {admin['contrasenia']}")
            
            # Probar diferentes contraseñas
            passwords_to_test = ["admin", "admin123", "123", "password"]
            for password in passwords_to_test:
                cursor.execute("SELECT SHA2(%s, 256) as hash", (password,))
                result = cursor.fetchone()
                test_hash = result['hash']
                print(f"SHA2('{password}', 256) = {test_hash}")
                if test_hash == admin['contrasenia']:
                    print(f"✅ ¡COINCIDENCIA! La contraseña es: '{password}'")
                    break
            else:
                print("❌ Ninguna contraseña de prueba coincide")
                
                # Actualizar la contraseña a 'admin'
                print("Actualizando contraseña a 'admin'...")
                cursor.execute("UPDATE usuarios SET contrasenia = SHA2('admin', 256) WHERE nombre = 'admin'")
                conn.commit()
                print("✅ Contraseña actualizada")
        else:
            print("❌ Usuario admin no encontrado")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verificar_contrasenia()
