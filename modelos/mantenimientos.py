import dataBase
import modelos.login as login

def obtener_mantenimientos():
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(True)
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
    if login.isLogged() == -1:
        return ["No loggeado"]
    if tecnico_ocupado(ci_tecnico, fecha):
        return ["Tecnico ocupado en esa fecha"]
    conn = dataBase.get_connection(True)
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
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Mantenimientos WHERE id = %s"
        cursor.execute(sql, (id_mantenimiento,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_mantenimiento(id_mantenimiento, id_maquina, ci_tecnico, tipo, fecha, observaciones):
    if login.isLogged() == -1:
        return ["No loggeado"]
    if tecnico_ocupado(ci_tecnico, fecha):
        return ["Tecnico ocupado en esa fecha"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE Mantenimientos
            SET id_maquina = %s, ci_tecnico = %s, tipo = %s, fecha = %s, observaciones = %s
            WHERE id = %s
        """
        cursor.execute(sql, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id_mantenimiento))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def tecnico_ocupado(ci_tecnico, fecha):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT COUNT(*) FROM Mantenimientos
            WHERE ci_tecnico = %s AND fecha = %s
        """
        cursor.execute(sql, (ci_tecnico, fecha))
        count = cursor.fetchall()
        if count[0] != 0:
            return True
        else:
            return False
    finally:
        cursor.close()
        conn.close()