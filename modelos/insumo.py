from dataBase import get_connection

def registrar_consumo(id_maquina, id_insumo, fecha, cantidad):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO registro_consumo (id_maquina, id_insumo, fecha, cantidad_usada) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (id_maquina, id_insumo, fecha, cantidad))
    conn.commit()
