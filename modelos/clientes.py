from dataBase import get_connection

def obtener_clientes():
    conn = get_connection(False)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nombre, direccion, telefono, correo FROM Clientes")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_cliente(nombre, direccion, telefono, correo):
    conn = get_connection(False)
    cursor = conn.cursor()      
    try:
        sql = "INSERT INTO Clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, direccion, telefono, correo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id_cliente):
    conn = get_connection(False)
    cursor = conn.cursor()
    try:
        # Primero actualizar máquinas que referencian este cliente
        sql_update_maquinas = "UPDATE Maquinas SET idCliente = NULL WHERE idCliente = %s"
        cursor.execute(sql_update_maquinas, (id_cliente,))
        
        # Luego eliminar el cliente
        sql = "DELETE FROM Clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_cliente(id_cliente, nombre, direccion, telefono, correo):
    conn = get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Clientes SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, direccion, telefono, correo, id_cliente))
        conn.commit()
    finally:
        cursor.close()
        conn.close()