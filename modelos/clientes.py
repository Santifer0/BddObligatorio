import dataBase
from .login import get_user_connection

def obtener_clientes():
    conn = get_user_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Empresa")
        return {"status": "ok", "data": cursor.fetchall()}
    except Exception as e:
        return {"status": "error", "message": f"Error al obtener clientes: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

def agregar_cliente(nombre, telefono, correo):
    conn = get_user_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO Empresa (nombre, telefono, correo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, telefono, correo))
        conn.commit()
        return {"status": "ok", "message": "Cliente agregado correctamente"}
    except Exception as e:
        return {"status": "error", "message": f"Error al agregar cliente: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id_cliente):
    conn = get_user_connection()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Empresa WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
        if cursor.rowcount == 0:
            return {"status": "error", "message": "No existe el cliente"}
        return {"status": "ok", "message": "Cliente eliminado correctamente"}
    except Exception as e:
        return {"status": "error", "message": f"Error al eliminar cliente: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

def modificar_cliente(id_cliente, nombre, telefono, correo):
    conn = get_user_connection()
    cursor = conn.cursor()
    try:
        sql = "UPDATE Empresa SET nombre = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, telefono, correo, id_cliente))
        conn.commit()
        if cursor.rowcount == 0:
            return {"status": "error", "message": "No existe el cliente"}
        return {"status": "ok", "message": "Cliente modificado correctamente"}
    except Exception as e:
        return {"status": "error", "message": f"Error al modificar cliente: {str(e)}"}
    finally:
        cursor.close()
        conn.close()