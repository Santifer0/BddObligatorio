import dataBase
from flask import session

def loggin(username, password):
    conexion = dataBase.connectAdmin()
    cursor = conexion.cursor(dictionary=True)
    try:
        # ya que nesesito compararlo en select porque la contraseña esta hashda
        sql = "SELECT permisos FROM usuarios WHERE nombre = %s AND contrasenia = SHA2(%s, 256)"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        # si el usuario existe y la contraseña es correcta result no sera vacio
        if result:
            if result['permisos'] == 1:
                session['logged_admin'] = True
                session['logged_user'] = False
                return "admin"
            else:
                session['logged_user'] = True
                session['logged_admin'] = False
            print("Inicio de sesión exitoso.")
            return "user"
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
    session.pop('logged_user', None)
    session.pop('logged_admin', None)
    print("Sesión cerrada exitosamente.")

def isLogged():
    if session.get('logged_user', False):
        return 1
    elif session.get('logged_admin', False):
        return 2
    else:
        return -1

def get_user_connection():
    """
    Devuelve la conexión adecuada según los permisos del usuario logueado.
    Si es admin, usa conexión de administrador; si es usuario normal, usa conexión de usuario.
    """
    if session.get('logged_admin', False):
        return dataBase.get_connection(True)  # Conexión de administrador
    elif session.get('logged_user', False):
        return dataBase.get_connection(False)  # Conexión de usuario normal
    else:
        # Si no hay sesión activa, usar conexión de usuario normal por defecto
        return dataBase.get_connection(False)

def is_admin():
    """
    Verifica si el usuario logueado tiene permisos de administrador.
    """
    return session.get('logged_admin', False)