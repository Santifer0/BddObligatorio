from dataBase import get_connection


def verificar_login(correo, contraseña):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT es_administrador FROM login WHERE correo=%s AND contraseña=%s", (correo, contraseña))
    return cursor.fetchone()
