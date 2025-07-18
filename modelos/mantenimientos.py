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
        # Verificar si el técnico tiene mantenimientos recientes (menos de 30 minutos)
        sql_verificacion = """
            SELECT COUNT(*) as count
            FROM mantenimientos 
            WHERE ci_tecnico = %s 
            AND ABS(TIMESTAMPDIFF(MINUTE, fecha, %s)) < 30
        """
        cursor.execute(sql_verificacion, (ci_tecnico, fecha))
        resultado = cursor.fetchone()
        
        if resultado[0] > 0:
            raise Exception("No se puede registrar el mantenimiento. El técnico tiene otro mantenimiento registrado con menos de 30 minutos de diferencia.")
        
        # Si no hay conflictos, proceder con el insert
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
        # Verificar si el técnico tiene otros mantenimientos recientes (menos de 30 minutos)
        # Excluir el mantenimiento actual que se está modificando
        sql_verificacion = """
            SELECT COUNT(*) as count
            FROM mantenimientos 
            WHERE ci_tecnico = %s 
            AND id != %s
            AND ABS(TIMESTAMPDIFF(MINUTE, fecha, %s)) < 30
        """
        cursor.execute(sql_verificacion, (ci_tecnico, id, fecha))
        resultado = cursor.fetchone()
        
        if resultado[0] > 0:
            raise Exception("No se puede modificar el mantenimiento. El técnico tiene otro mantenimiento registrado con menos de 30 minutos de diferencia.")
        
        # Si no hay conflictos, proceder con el update
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