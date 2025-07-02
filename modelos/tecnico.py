from dataBase import get_connection
import modelos.login as login

def obtener_tecnicos():
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Tecnicos")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_tecnico(ci, nombre, apellido, telefono):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (ci, nombre, apellido, telefono))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_tecnico(ci):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Tecnicos WHERE ci = %s"
        cursor.execute(sql, (ci,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_tecnico(ci, telefono):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Tecnicos SET telefono = %s WHERE ci = %s"
        cursor.execute(sql, (telefono, ci))
        conn.commit()
    finally:
        cursor.close()
        conn.close()