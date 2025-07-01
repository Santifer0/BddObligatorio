import dataBase

def obtener_Insumos():
    conn = dataBase.get_connection(False)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Insumos")
        return {"status": "ok", "data": cursor.fetchall()}
    except Exception as e:
        return {"status": "error", "message": f"Error al obtener insumos: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

def agregar_insumo(nombre, precio, id_proveedor):
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Insumos (nombre, precio, idProveedor) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, id_proveedor))
        conn.commit()
        return {"status": "ok", "message": "Insumo agregado correctamente"}
    except Exception as e:
        return {"status": "error", "message": f"Error al agregar insumo: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

def eliminar_insumo(id_insumo):
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Insumos WHERE id = %s"
        cursor.execute(sql, (id_insumo,))
        conn.commit()
        if cursor.rowcount == 0:
            return {"status": "error", "message": "No existe el insumo"}
        return {"status": "ok", "message": "Insumo eliminado correctamente"}
    finally:
        cursor.close()
        conn.close()

def modificar_insumo(id_insumo, nombre, precio, id_proveedor):
    conn = dataBase.get_connection(False)
    cursor = conn.cursor()
    try:
        sql = "UPDATE Insumos SET nombre = %s, precio = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, id_proveedor, id_insumo))
        conn.commit()
        if cursor.rowcount == 0:
            return {"status": "error", "message": "No existe el insumo"}
        return {"status": "ok", "message": "Insumo modificado correctamente"}
    except Exception as e:
        return {"status": "error", "message": f"Error al modificar insumo: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

