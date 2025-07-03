import dataBase
import modelos.login as login

def obtener_proveedores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Proveedores")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_proveedor(nombre, contacto):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO Proveedores (nombre, contacto)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (nombre, contacto))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_proveedor(id_proveedor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Proveedores WHERE id = %s"
        cursor.execute(sql, (id_proveedor,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_proveedor(id_proveedor, nombre, contacto):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE Proveedores
            SET nombre = %s, contacto = %s
            WHERE id = %s
        """
        cursor.execute(sql, (nombre, contacto, id_proveedor))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
