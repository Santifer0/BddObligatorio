import dataBase
import mysql.connector

def dar_permisos_usuario():
    try:
        conn = dataBase.connectAdmin()
        cursor = conn.cursor()
        
        print("🔧 Dando permisos al usuario normal...")
        
        # Dar permisos de SELECT en la tabla Usuarios
        cursor.execute("GRANT SELECT ON Obligatorio.Usuarios TO 'usuario'@'localhost'")
        print("✅ Permiso SELECT otorgado a usuario")
        
        # Aplicar cambios
        cursor.execute("FLUSH PRIVILEGES")
        print("✅ Permisos aplicados")
        
        conn.commit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    dar_permisos_usuario()
