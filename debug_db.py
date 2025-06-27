import dataBase
import mysql.connector

def debug_usuarios():
    try:
        conn = dataBase.connectAdmin()
        cursor = conn.cursor()
        
        print("🔍 Verificando usuarios en la base de datos...")
        cursor.execute("SELECT nombre, nombre_publico, contrasenia, permisos FROM Usuarios")
        usuarios = cursor.fetchall()
        
        print(f"📋 Encontrados {len(usuarios)} usuarios:")
        for i, (nombre, nombre_publico, contrasenia, permisos) in enumerate(usuarios, 1):
            print(f"{i}. Nombre: {nombre}")
            print(f"   Nombre público: {nombre_publico}")
            print(f"   Contraseña hash: {contrasenia[:20]}...")
            print(f"   Permisos admin: {permisos}")
            print()
        
        # Probar hash manual
        print("🔧 Probando hash de contraseña...")
        cursor.execute("SELECT SHA2('miContrasenia', 256) as hash_manual")
        hash_manual = cursor.fetchone()[0]
        print(f"Hash de 'miContrasenia': {hash_manual}")
        
        # Verificar si existe el usuario admin con esa contraseña
        cursor.execute("SELECT nombre, permisos FROM Usuarios WHERE nombre='admin' AND contrasenia=SHA2('miContrasenia', 256)")
        resultado = cursor.fetchone()
        if resultado:
            print(f"✅ Usuario admin encontrado con contraseña correcta: {resultado}")
        else:
            print("❌ Usuario admin NO encontrado con esa contraseña")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    debug_usuarios()
