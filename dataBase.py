import mysql.connector

def connectUsuario():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="passusuario",
            database="Obligatorio"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return conexion.is_connected()


def connectAdmin():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="administrador",
            password="passadministrador",
            database="Obligatorio"
    )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return conexion.is_connected()

def ejecutarArchivoSQL(archivo_sql, conexion):
    try:
        with open(archivo_sql, 'r') as file:
            sql_script = file.read()
        cursor = conexion.cursor()
        for statement in sql_script.split(';'):  # Dividir por ';' para ejecutar múltiples comandos
            if statement.strip():  # Ignorar líneas vacías
                cursor.execute(statement)
        conexion.commit()
        print("Archivo SQL ejecutado exitosamente.")
    except Exception as e:
        print(f"Error al ejecutar el archivo SQL: {e}")
    finally:
        cursor.close()