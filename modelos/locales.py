from dataBase import get_connection

def obtener_locales():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Locales")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_local(nombre, direccion, telefono, correo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Locales (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, direccion, telefono, correo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_local(id, nombre, direccion, telefono, correo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "UPDATE Locales SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, direccion, telefono, correo, id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_local(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Locales WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()