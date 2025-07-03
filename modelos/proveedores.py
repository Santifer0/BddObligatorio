from dataBase import get_connection

privilegiosAdmin = True

def obtener_proveedores():
    conn = get_connection("admin")  # Solo admin puede ver proveedores
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Proveedores")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def agregar_proveedor(nombre, contacto, Permiso):
    conn = get_connection(Permiso)
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO Proveedores (nombre, contacto)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (nombre, contacto))
        conn.commit()
        return {"status": "ok", "message": "Proveedor agregado exitosamente"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        conn.close()

def eliminar_proveedor(id_proveedor, Permiso):
    conn = get_connection(Permiso)
    cursor = conn.cursor()
    try:
        # Primero actualizar insumos que referencian este proveedor
        sql_update_insumos = "UPDATE Insumos SET idProveedor = NULL WHERE idProveedor = %s"
        cursor.execute(sql_update_insumos, (id_proveedor,))
        
        # Luego eliminar el proveedor
        sql = "DELETE FROM Proveedores WHERE id = %s"
        cursor.execute(sql, (id_proveedor,))
        conn.commit()
        return {"status": "ok", "message": "Proveedor eliminado exitosamente. Referencias actualizadas a NULL."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        conn.close()

def modificar_proveedor(id_proveedor, nombre, contacto, Permiso):
    conn = get_connection(Permiso)
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE Proveedores
            SET nombre = %s, contacto = %s
            WHERE id = %s
        """
        cursor.execute(sql, (nombre, contacto, id_proveedor))
        conn.commit()
        return {"status": "ok", "message": "Proveedor modificado exitosamente"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        conn.close()
