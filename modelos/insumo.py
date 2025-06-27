import dataBase
import modelos.login as login

def obtener_Insumos():
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Insumos")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_insumo(nombre, precio, id_proveedor):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Insumos (nombre, precio, idProveedor) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, id_proveedor))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_insumo(id_insumo):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Insumos WHERE id = %s"
        cursor.execute(sql, (id_insumo,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_insumo(id_insumo, nombre, precio, id_proveedor):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Insumos SET nombre = %s, precio = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, id_proveedor, id_insumo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def registrar_consumo(id_maquina, id_insumo, fecha, cantidad):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO registro_consumo (id_maquina, id_insumo, fecha, cantidad) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_maquina, id_insumo, fecha, cantidad))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def obtener_consumos():
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
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