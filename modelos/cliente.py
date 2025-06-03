from dataBase import get_connection

def obtener_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

def agregar_cliente(nombre, direccion, telefono, correo):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, direccion, telefono, correo))
    conn.commit()