from dataBase import get_connection

def obtener_mantenimientos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT m.id, m.id_maquina, maq.modelo, m.ci_tecnico, t.nombre AS tecnico, m.tipo, m.fecha, m.observaciones
            FROM Mantenimientos m
            JOIN Maquinas maq ON m.id_maquina = maq.id
            JOIN Tecnicos t ON m.ci_tecnico = t.ci
        """)
        return cursor.fetchall()
    finally:
            cursor.close()
            conn.close()

def agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO Mantenimientos (id_maquina, ci_tecnico, tipo, fecha, observaciones)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_maquina, ci_tecnico, tipo, fecha, observaciones))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_mantenimiento(id_mantenimiento):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Mantenimientos WHERE id = %s"
        cursor.execute(sql, (id_mantenimiento,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE Mantenimientos
            SET id_maquina = %s, ci_tecnico = %s, tipo = %s, fecha = %s, observaciones = %s
            WHERE id = %s
        """
        cursor.execute(sql, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()