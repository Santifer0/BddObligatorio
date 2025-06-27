import dataBase
global loggedUser
loggedUser = False
global loggedAdmin
loggedAdmin = False

def loggin(username, password):
    global loggedUser
    global loggedAdmin

    conexion = dataBase.connectAdmin()
    cursor = conexion.cursor(dictionary=True)
    # try:
    #     sqlPass = "SELECT contrasenia FROM usuarios WHERE nombre = %s"
    #     cursor.execute(sqlPass, (username,))
    #     result = cursor.fetchone()

    #     if result and result['contrasenia'] == password: 
    #         sqlPerm = "SELECT permisos FROM usuarios WHERE nombre = %s"
    #         cursor.execute(sqlPerm, (username,))
    #         result = cursor.fetchone()
    #         if result and result['permisos'] == 1:
    #             loggedAdmin = True
    #         else:
    #             loggedUser = True
    #         print("Inicio de sesión exitoso.")
    #         return True
    #     else:
    #         print("Usuario o contraseña incorrectos.")
    #         return False
    try:
        # ya que nesesito compararlo en select porque la contraseña esta hashda
        sql = "SELECT permisos FROM usuarios WHERE nombre = %s AND contrasenia = SHA2(%s, 256)"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        # si el usuario existe y la contraseña es correcta result no sera vacio
        if result:
            if result['permisos'] == 1:
                loggedAdmin = True
            else:
                loggedUser = True
            print("Inicio de sesión exitoso.")
            return True
        else:#si el usuario no existe o la contraseña es incorrecta
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

def isLogged():
    global loggedUser
    global loggedAdmin
    if loggedUser:
        return 1
    elif loggedAdmin:
        return 2
    else:
        return -1