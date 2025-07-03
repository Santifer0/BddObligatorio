from dataBase import get_connection

def alquiler_mensual_cliente():
    connection = get_connection(True)  # Usar admin porque accede a Maquinas
    cursor = connection.cursor()

    query = """
    SELECT c.nombre, SUM(m.costo_alquiler) AS total_alquiler
    FROM Maquinas m
    JOIN Clientes c ON m.idCliente = c.id
    GROUP BY c.nombre
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    return {"alquileres": resultados}

def consumo_insumos(id_maquina, id_insumo, fecha, cantidad):
    """Registra un nuevo consumo de insumo en la tabla Registro_Consumo"""
    connection = get_connection(False)
    cursor = connection.cursor()
    try:
        sql = """
            INSERT INTO Registro_Consumo (id_maquina, id_insumo, fecha, cantidad)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (id_maquina, id_insumo, fecha, cantidad))
        connection.commit()
        return {"status": "ok", "message": "Consumo registrado exitosamente"}
    except Exception as e:
        connection.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        connection.close()

def total_cobrar_cliente():
    connection = get_connection(True)  # Usar admin porque accede a Maquinas e Insumos
    cursor = connection.cursor()

    query = """
    SELECT c.nombre, 
           SUM(m.costo_alquiler) AS alquiler_total,
           COALESCE(SUM(rc.cantidad * i.precio), 0) AS insumos_total,
           (SUM(m.costo_alquiler) + COALESCE(SUM(rc.cantidad * i.precio), 0)) AS total_cobrar
    FROM Clientes c
    JOIN Maquinas m ON c.id = m.idCliente
    LEFT JOIN Registro_Consumo rc ON m.id = rc.id_maquina 
        AND YEAR(rc.fecha) = YEAR(CURDATE()) 
        AND MONTH(rc.fecha) = MONTH(CURDATE())
    LEFT JOIN Insumos i ON rc.id_insumo = i.id
    GROUP BY c.nombre, c.id
    ORDER BY total_cobrar DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    return {"totales": resultados}

def mantenimientos_por_tecnico():
    connection = get_connection(True)  # Usar admin porque accede a Tecnicos
    cursor = connection.cursor()

    query = """
    SELECT CONCAT(t.nombre, ' ', t.apellido) AS nombre_completo, 
           COUNT(ma.id) AS total_mantenimientos
    FROM Tecnicos t
    LEFT JOIN Mantenimientos ma ON t.ci = ma.ci_tecnico
    GROUP BY t.ci, t.nombre, t.apellido
    ORDER BY total_mantenimientos DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    return {"mantenimientos": resultados}

def maquinas_por_cliente():
    connection = get_connection(True)  # Usar admin porque accede a Maquinas
    cursor = connection.cursor()

    query = """
    SELECT c.nombre, COUNT(m.id) AS total_maquinas,
           GROUP_CONCAT(m.modelo SEPARATOR ', ') AS modelos
    FROM Clientes c
    LEFT JOIN Maquinas m ON c.id = m.idCliente
    GROUP BY c.nombre, c.id
    ORDER BY total_maquinas DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    return {"maquinas": resultados}