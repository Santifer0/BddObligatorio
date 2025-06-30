from dataBase import get_connection

privilegiosAdmin = True

def agregar_usuario(nombre_publico, nombre,contrasenia, permisos):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO usuarios  (nombre_publico, nombre, contrasenia, permisos)
            VALUES (%s, %s, SHA2(%s, 256), %s)
        """
        cursor.execute(sql, (nombre_publico, nombre, contrasenia, permisos))
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
