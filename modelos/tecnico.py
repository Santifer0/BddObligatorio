from dataBase import get_connection

def obtener_tecnicos(permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT t.ci, t.nombre, t.apellido, t.telefono
            FROM tecnicos t
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_tecnico(ci, nombre, telefono, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (ci, nombre, "", telefono))  # apellido vacío por consistencia
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_tecnico(ci, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM tecnicos WHERE ci = %s"
        cursor.execute(sql, (ci,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_tecnico(ci, nombre, telefono, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE tecnicos
            SET nombre = %s, telefono = %s
            WHERE ci = %s
        """
        cursor.execute(sql, (nombre, telefono, ci))
        conn.commit()
    finally:
        cursor.close()
        conn.close()