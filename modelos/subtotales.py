import modelos.login
import dataBase

def totalAlquilerCliente(id_cliente):
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = "SELECT SUM(costo_alquiler) AS total FROM Maquinas WHERE idCliente = %s"
        cursor.execute(sql, (id_cliente,))
        result = cursor.fetchone()
        return result['total']
    finally:
        cursor.close()
        conn.close()

def totalInsumosCliente(id_cliente):
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor()
    try:
        sql = """
            SELECT SUM(rc.cantidad * i.precio) AS total
            FROM registro_consumo rc
            JOIN insumos i ON rc.id_insumo = i.id
            JOIN maquinas m ON rc.id_maquina = m.id
            WHERE m.idCliente = %s
        """
        cursor.execute(sql, (id_cliente,))
        result = cursor.fetchone()
        return result['total']
    finally:
        cursor.close()
        conn.close()

def totalCobro(id_cliente):
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    alquiler = totalAlquilerCliente(id_cliente)
    insumos = totalInsumosCliente(id_cliente)
    if alquiler is None:
        alquiler = 0
    if insumos is None:
        insumos = 0
    return alquiler + insumos

def masConsumidos():
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT i.nombre, SUM(rc.cantidad) AS total_consumido
            FROM registro_consumo rc
            JOIN insumos i ON rc.id_insumo = i.id
            GROUP BY i.nombre
            ORDER BY total_consumido DESC
            LIMIT 3
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def masCostosos():
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT i.nombre, SUM(rc.cantidad * i.precio) AS total_costo
            FROM registro_consumo rc
            JOIN insumos i ON rc.id_insumo = i.id
            GROUP BY i.nombre
            ORDER BY total_costo DESC
            LIMIT 3
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
def tecnicoMasMantenimientos():
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT t.nombre, t.apellido, COUNT(m.id) AS total_mantenimientos
            FROM Tecnicos t
            JOIN Mantenimientos m ON t.ci = m.ciTecnico
            GROUP BY t.ci
            ORDER BY total_mantenimientos DESC
            LIMIT 1
        """
        cursor.execute(sql)
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def clienteMasMaquinas():
    if modelos.login.isLogged() != 2:
        return ["Acceso denegado"]
    conn = dataBase.get_connection(True)
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT c.nombre, COUNT(m.id) AS total_maquinas
            FROM Clientes c
            JOIN Maquinas m ON c.id = m.idCliente
            GROUP BY c.id
            ORDER BY total_maquinas DESC
            LIMIT 1
        """
        cursor.execute(sql)
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()