import dataBase

loggedUser = False
loggedAdmin = False

def loggin(username, password):
    global loggedUser
    global loggedAdmin

    conexion = dataBase.connectAdmin()
    cursor = conexion.cursor(dictionary=True)
    try:
        sqlPass = "SELECT contrasenia FROM login WHERE nombre = %s"
        cursor.execute(sqlPass, (username,))
        result = cursor.fetchone()

        if result and result['contrasenia'] == password:
            sqlPerm = "SELECT permisos FROM login WHERE nombre = %s"
            cursor.execute(sqlPerm, (username,))
            result = cursor.fetchone()
            if result and result['permisos'] == 1:
                loggedAdmin = True
            else:
                loggedUser = True
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
    except Exception as e:
        print(f"Error en el inicio de sesión: {e}")
        return False
    finally:
        cursor.close()
        conexion.close()
def logout():
    global loggedUser
    global loggedAdmin
    loggedUser = False
    loggedAdmin = False
    print("Sesión cerrada exitosamente.")