import dataBase
import modelos.login as login


def obtener_maquinas():
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Maquinas")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def agregar_maquina(modelo, id_cliente, direccion_cliente, costo_alquiler):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Maquinas (modelo, idCliente, direccionCliente, costo_alquiler) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (modelo, id_cliente, direccion_cliente, costo_alquiler))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def eliminar_maquina(id_maquina):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Maquinas WHERE id = %s"
        cursor.execute(sql, (id_maquina,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def modificar_maquina(id_maquina, modelo, id_cliente, direccion_cliente, costo_alquiler):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Maquinas SET modelo = %s, idCliente = %s, direccionCliente = %s, costo_alquiler = %s WHERE id = %s"
        cursor.execute(sql, (modelo, id_cliente, direccion_cliente, costo_alquiler, id_maquina))
        conn.commit()
    finally:
        cursor.close()
        conn.close()