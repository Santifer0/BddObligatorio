from dataBase import get_connection

def obtener_mantenimientos(permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT m.id, m.id_maquina, maq.modelo, m.ci_tecnico, t.nombre AS tecnico, m.tipo, m.fecha, m.observaciones
            FROM mantenimientos m
            JOIN maquinas maq ON m.id_maquina = maq.id
            JOIN tecnicos t ON m.ci_tecnico = t.ci
        """)
        return cursor.fetchall()
    finally:
            cursor.close()
            conn.close()

def agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO mantenimientos (id_maquina, ci_tecnico, tipo, fecha, observaciones)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_maquina, ci_tecnico, tipo, fecha, observaciones))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_mantenimiento(id_mantenimiento, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM mantenimientos WHERE id = %s"
        cursor.execute(sql, (id_mantenimiento,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE mantenimientos
            SET id_maquina = %s, ci_tecnico = %s, tipo = %s, fecha = %s, observaciones = %s
            WHERE id = %s
        """
        cursor.execute(sql, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()