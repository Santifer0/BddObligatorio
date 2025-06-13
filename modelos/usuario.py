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
