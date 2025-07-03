#!/usr/bin/env python3
import mysql.connector
from dataBase import get_connection

def verificar_usuarios():
    """Verificar si existen usuarios en la base de datos"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        
        print(f"Usuarios encontrados: {len(usuarios)}")
        for usuario in usuarios:
            print(f"- {usuario['nombre']} ({usuario['permisos']})")
        
        cursor.close()
        conn.close()
        
        return usuarios
        
    except Exception as e:
        print(f"Error verificando usuarios: {e}")
        return []

def crear_usuario_admin():
    """Crear usuario administrador de prueba"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor()
        
        # Verificar si ya existe
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = 'admin'")
        if cursor.fetchone()[0] > 0:
            print("Usuario admin ya existe")
            return
        
        sql = """
            INSERT INTO usuarios (nombre_publico, nombre, contrasenia, permisos)
            VALUES (%s, %s, SHA2(%s, 256), %s)
        """
        cursor.execute(sql, ("Administrador", "admin", "admin123", "admin"))
        conn.commit()
        
        print("Usuario admin creado exitosamente")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error creando usuario admin: {e}")

def crear_usuario_normal():
    """Crear usuario normal de prueba"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor()
        
        # Verificar si ya existe
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = 'user'")
        if cursor.fetchone()[0] > 0:
            print("Usuario user ya existe")
            return
        
        sql = """
            INSERT INTO usuarios (nombre_publico, nombre, contrasenia, permisos)
            VALUES (%s, %s, SHA2(%s, 256), %s)
        """
        cursor.execute(sql, ("Usuario Normal", "user", "user123", "user"))
        conn.commit()
        
        print("Usuario user creado exitosamente")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error creando usuario normal: {e}")

def main():
    print("🔍 Verificando usuarios existentes...")
    usuarios = verificar_usuarios()
    
    if not usuarios:
        print("No hay usuarios. Creando usuarios de prueba...")
        crear_usuario_admin()
        crear_usuario_normal()
        print("\n🔍 Verificando usuarios después de crear...")
        verificar_usuarios()
    else:
        print("✅ Usuarios encontrados en la base de datos")

if __name__ == "__main__":
    main()
