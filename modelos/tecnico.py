from dataBase import get_connection

def obtener_tecnicos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tecnicos")
    return cursor.fetchall()

def agregar_tecnico(ci, nombre, apellido, telefono):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (ci, nombre, apellido, telefono))
    conn.commit()