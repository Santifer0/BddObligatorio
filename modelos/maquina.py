
from dataBase import get_connection

def obtener_maquinas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT m.id, m.modelo, m.ubicacion_cliente, m.costo_alquiler_mensual, c.nombre AS cliente
        FROM maquinas m
        JOIN clientes c ON m.id_cliente = c.id
    """)
    return cursor.fetchall()

def agregar_maquina(modelo, id_cliente, ubicacion, costo):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO maquinas (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (modelo, id_cliente, ubicacion, costo))
    conn.commit()