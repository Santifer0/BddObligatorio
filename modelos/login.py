import dataBase
from flask import session

def loggin(username, password):
    conexion = dataBase.connectAdmin()
    cursor = conexion.cursor(dictionary=True)
    try:
        sql = "SELECT permisos FROM usuarios WHERE nombre = %s AND contrasenia = SHA2(%s, 256)"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        if result:
            if result['permisos'] == 1:
                session['logged_admin'] = True
                session['logged_user'] = False
                return "admin"
            else:
                session['logged_user'] = True
                session['logged_admin'] = False
                return "user"
        else:
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

def is_logged_in():
    return session.get('logged_user', False) or session.get('logged_admin', False)

def get_user_connection():
    if session.get('logged_admin', False):
        return dataBase.get_connection(True)
    elif session.get('logged_user', False):
        return dataBase.get_connection(False)
    else:
        return dataBase.get_connection(False)

def is_admin():
    return session.get('logged_admin', False)
