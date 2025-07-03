import dataBase

def obtener_Insumos ():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT i.id, i.nombre, i.precio, i.idProveedor
            FROM Insumos i
            JOIN Proveedores p ON i.idProveedor = p.id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_insumo(nombre, precio, id_proveedor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Insumos (nombre, precio, idProveedor) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, id_proveedor))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def eliminar_insumo(id_insumo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM insumos WHERE id = %s"
        cursor.execute(sql, (id_insumo,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modificar_insumo(id_insumo, nombre, precio, id_proveedor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "UPDATE Insumos SET nombre = %s, precio = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, id_proveedor, id_insumo))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

#no se si esta aca por una rason en especial, pero lo dejo por si acaso
def registrar_consumo(id_maquina, id_insumo, fecha, cantidad):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO registro_consumo (id_maquina, id_insumo, fecha, cantidad) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_maquina, id_insumo, fecha, cantidad))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def obtener_consumos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT rc.id, rc.id_maquina, m.modelo AS maquina, rc.id_insumo, i.nombre AS insumo, rc.fecha, rc.cantidad_usada
            FROM registro_consumo rc
            JOIN maquinas m ON rc.id_maquina = m.id
            JOIN insumos i ON rc.id_insumo = i.id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()