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
    print (conexion.is_connected())
    return conexion


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
    print (conexion.is_connected())
    return conexion

def ejecutarArchivoSQL(archivo_sql, conexion):
    try:
        with open(archivo_sql, 'r') as file:
            sql_script = file.read()
        cursor = conexion.cursor()
        for statement in sql_script.split(';'):
            if statement.strip(): 
                cursor.execute(statement)
                while cursor.nextset():
                    pass
        conexion.commit()
        print("Archivo SQL ejecutado exitosamente.")
    except Exception as e:
        print(f"Error al ejecutar el archivo SQL: {e}")
    finally:
        cursor.close()

def crearBase():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tupass"
        )
        ejecutarArchivoSQL("createTables.sql", conexion)

    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
    finally:
        if conexion.is_connected():
            conexion.close()

def get_connection(privilegiosAdmin):
    if privilegiosAdmin == True:
        return connectAdmin()
    else:
        return connectUsuario()
    
    