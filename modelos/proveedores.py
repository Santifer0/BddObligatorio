import dataBase
import modelos.login as login

def obtener_proveedores():
    if not login.is_logged_in():
        return {"status": "error", "message": "Acceso denegado"}
    else:
        conn = login.get_user_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Proveedores")
            return {"status": "ok", "data": cursor.fetchall()}
        finally:
            cursor.close()
            conn.close()

def agregar_proveedor(nombre, contacto):
    if not login.is_admin():
        return {"status": "error", "message": "Acceso denegado"}
    else:
        conn = login.get_user_connection()
        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO Proveedores (nombre, contacto)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (nombre, contacto))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            conn.close()

def eliminar_proveedor(id_proveedor):
    if not login.is_admin():
        return {"status": "error", "message": "Acceso denegado"}
    else:
        conn = login.get_user_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM Proveedores WHERE id = %s"
            cursor.execute(sql, (id_proveedor,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            conn.close()

def modificar_proveedor(id_proveedor, nombre, contacto):
    if not login.is_admin():
        return {"status": "error", "message": "Acceso denegado"}
    else:
        conn = login.get_user_connection()
        cursor = conn.cursor()
        try:
            sql = """
                UPDATE Proveedores
                SET nombre = %s, contacto = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nombre, contacto, id_proveedor))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            conn.close()
