import dataBase
import modelos.login as login


def obtener_maquinas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT m.id, m.modelo, m.ubicacion_cliente, m.costo_alquiler_mensual, c.nombre AS cliente
            FROM maquinas m
            JOIN clientes c ON m.id_cliente = c.id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_maquina(modelo, id_cliente, ubicacion, costo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO maquinas (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (modelo, id_cliente, ubicacion, costo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_maquina(id_maquina):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM maquinas WHERE id = %s"
        cursor.execute(sql, (id_maquina,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_maquina(id_maquina, modelo, id_cliente, ubicacion, costo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE maquinas
            SET modelo = %s, id_cliente = %s, ubicacion_cliente = %s, costo_alquiler_mensual = %s
            WHERE id = %s
        """
        cursor.execute(sql, (modelo, id_cliente, ubicacion, costo, id_maquina))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    
