import modelos.login
import dataBase


def registrar_consumo(id_maquina, id_insumo, fecha, cantidad):
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO registro_consumo (id_maquina, id_insumo, fecha, cantidad) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_maquina, id_insumo, fecha, cantidad))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def obtener_consumos():
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT rc.id, rc.id_maquina, m.modelo AS maquina, rc.id_insumo, i.nombre AS insumo, rc.fecha, rc.cantidad
            FROM registro_consumo rc
            JOIN maquinas m ON rc.id_maquina = m.id
            JOIN insumos i ON rc.id_insumo = i.id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()