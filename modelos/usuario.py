from dataBase import get_connection

def obtener_usuarios(permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nombre_publico, nombre, permisos FROM usuarios")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_usuario(nombre_publico, nombre, contrasenia, permisos, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        # Convertir permisos string a entero
        permisos_int = 1 if permisos in ["admin", 1, True] else 0
        
        sql = """
            INSERT INTO usuarios  (nombre_publico, nombre, contrasenia, permisos)
            VALUES (%s, %s, SHA2(%s, 256), %s)
        """
        cursor.execute(sql, (nombre_publico, nombre, contrasenia, permisos_int))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_usuario(id_usuario, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (id_usuario,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_usuario(id_usuario, nombre_publico, nombre, contrasenia, permisos, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        # Convertir permisos string a entero
        permisos_int = 1 if permisos in ["admin", 1, True] else 0
        
        if contrasenia:  # Si se proporciona nueva contraseña
            sql = """
                UPDATE usuarios
                SET nombre_publico = %s, nombre = %s, contrasenia = SHA2(%s, 256), permisos = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nombre_publico, nombre, contrasenia, permisos_int, id_usuario))
        else:  # No cambiar contraseña
            sql = """
                UPDATE usuarios
                SET nombre_publico = %s, nombre = %s, permisos = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nombre_publico, nombre, permisos_int, id_usuario))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_usuario(id, nombre_publico, nombre, contrasenia, permisos):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE usuarios
            SET nombre_publico = %s, nombre = %s, contrasenia = SHA2(%s, 256), permisos = %s
            WHERE id = %s
        """
        cursor.execute(sql, (nombre_publico, nombre, contrasenia, permisos, id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
