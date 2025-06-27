from dataBase import get_connection


def verificar_login(correo, contraseña):
    conn = None
    cursor = None
    try:
        conn = get_connection(True)  # Usar administrador para login
        cursor = conn.cursor()
        # Cambiado para usar la tabla Usuarios y campos correctos
        cursor.execute("SELECT permisos FROM Usuarios WHERE nombre=%s AND contrasenia=SHA2(%s, 256)", (correo, contraseña))
        resultado = cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error en verificar_login: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
