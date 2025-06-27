import dataBase
import modelos.login as login

def obtener_clientes():
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Clientes")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_cliente(nombre, direccion, telefono, correo):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, direccion, telefono, correo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id_cliente):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_cliente(id_cliente, nombre, direccion, telefono, correo):
    if login.isLogged() == -1:
        return ["No loggeado"]
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Clientes SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, direccion, telefono, correo, id_cliente))
        conn.commit()
    finally:
        cursor.close()
        conn.close()