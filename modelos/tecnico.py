from dataBase import get_connection

def obtener_tecnicos():
    conn = get_connection()
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

def agregar_tecnico(ci, nombre, apellido, telefono):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (ci, nombre, apellido, telefono))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_tecnico(ci):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM tecnicos WHERE ci = %s"
        cursor.execute(sql, (ci,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_tecnico(ci, telefono):
    # Modifica solo el teléfono del técnico normalmente no cambian de nombre o apellido
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE tecnicos
            SET telefono = %s
            WHERE ci = %s
        """
        cursor.execute(sql, (telefono, ci))
        conn.commit()
    finally:
        cursor.close()
        conn.close()