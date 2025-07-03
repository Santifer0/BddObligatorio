from dataBase import get_connection

def obtener_empresas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Empresa")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_empresa(nombre, telefono, correo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Empresa (nombre, telefono, correo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, telefono, correo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_empresa(id, nombre, telefono, correo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "UPDATE Empresa SET nombre = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, telefono, correo, id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_empresa(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Empresa WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()