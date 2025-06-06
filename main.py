import dataBase
import os
import mysql.connector



# Conexión como administrador para crear la base y las tablas
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    #sql_file_path = os.path.join(os.path.dirname(__file__), "createTables.sql")
    dataBase.ejecutarArchivoSQL("createTables.sql", conexion)

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
finally:
    if conexion.is_connected():
        conexion.close()


#dataBase.connectUsuario()

