import dataBase
import mysql.connector

def insertar_usuarios():
    try:
        # Usar conexión de administrador para crear usuarios
        conn = dataBase.connectAdmin()
        cursor = conn.cursor()
        
        # Limpiar usuarios existentes (opcional)
        cursor.execute("DELETE FROM Usuarios")
        print("Usuarios existentes eliminados")
        
        # Insertar nuevos usuarios
        usuarios = [
            ('Administrador Principal', 'admin', 'miContrasenia', True),
            ('Usuario Técnico', 'tecnico1', 'miContraseniaSegura', False)
        ]
        
        for nombre_publico, nombre, contrasenia, permisos in usuarios:
            cursor.execute("""
                INSERT INTO Usuarios (nombre_publico, nombre, contrasenia, permisos) 
                VALUES (%s, %s, SHA2(%s, 256), %s)
            """, (nombre_publico, nombre, contrasenia, permisos))
            print(f"Usuario '{nombre}' insertado correctamente")
        
        conn.commit()
        print("✅ Todos los usuarios han sido insertados correctamente")
        
        # Verificar que se insertaron
        cursor.execute("SELECT nombre, nombre_publico, permisos FROM Usuarios")
        resultados = cursor.fetchall()
        print("\n📋 Usuarios en la base de datos:")
        for resultado in resultados:
            print(f"- {resultado[1]} (usuario: {resultado[0]}, admin: {resultado[2]})")
            
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL: {err}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    print("🔧 Configurando usuarios en la base de datos...")
    insertar_usuarios()
