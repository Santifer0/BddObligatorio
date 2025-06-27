import dataBase
import modelos.login as login

def obtener_proveedores():
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    else:
        conn = dataBase.get_connection(True)
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Proveedores")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

def agregar_proveedor(nombre, contacto):
    
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    else:
        conn = dataBase.get_connection(True)
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
    print("el")
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    else:
        conn = dataBase.get_connection(True)
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM Proveedores WHERE id = %s"
            cursor.execute(sql, (id_proveedor,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

def eliminar_proveedor(nombre_proveedor):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    else:
        conn = dataBase.get_connection(True)
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM Proveedores WHERE nombre = %s"
            cursor.execute(sql, (nombre_proveedor,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

def modificar_proveedor(nombreViejo, contactoViejo,nombreNuevo, contactoNuevo):
    if login.isLogged() != 2:
        return ["Acceso denegado"]
    else:
        conn = dataBase.get_connection(True)
        cursor = conn.cursor()
        try:
            sql = """
                UPDATE Proveedores
                SET nombre = %s, contacto = %s
                WHERE nombre = %s and contacto = %s
            """
            cursor.execute(sql, (nombreNuevo, contactoNuevo, nombreViejo, contactoViejo))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
