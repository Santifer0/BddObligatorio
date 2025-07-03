
from dataBase import get_connection

def obtener_maquinas(permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT m.id, m.modelo, m.ubicacionCliente, m.costo_alquiler, c.nombre AS cliente
            FROM maquinas m
            JOIN clientes c ON m.idCliente = c.id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_maquina(modelo, id_cliente, ubicacion, costo, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO maquinas (modelo, idCliente, ubicacionCliente, costo_alquiler) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (modelo, id_cliente, ubicacion, costo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_maquina(id_maquina, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM maquinas WHERE id = %s"
        cursor.execute(sql, (id_maquina,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_maquina(id_maquina, modelo, id_cliente, ubicacion, costo, permiso):
    conn = get_connection(permiso)
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE maquinas
            SET modelo = %s, idCliente = %s, ubicacionCliente = %s, costo_alquiler = %s
            WHERE id = %s
        """
        cursor.execute(sql, (modelo, id_cliente, ubicacion, costo, id_maquina))
        conn.commit()
    finally:
        cursor.close()
        conn.close()