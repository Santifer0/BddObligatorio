#!/usr/bin/env python3
from dataBase import get_connection

def verificar_estructura_tablas():
    """Verificar la estructura real de las tablas en la base de datos"""
    try:
        conn = get_connection("admin")
        cursor = conn.cursor()
        
        print("=== Estructura de tabla 'usuarios' ===")
        cursor.execute("DESCRIBE usuarios")
        usuarios_estructura = cursor.fetchall()
        for campo in usuarios_estructura:
            print(f"- {campo}")
        
        print("\n=== Estructura de tabla 'maquinas' ===")
        cursor.execute("DESCRIBE maquinas")
        maquinas_estructura = cursor.fetchall()
        for campo in maquinas_estructura:
            print(f"- {campo}")
            
        print("\n=== Estructura de tabla 'tecnicos' ===")
        cursor.execute("DESCRIBE tecnicos")
        tecnicos_estructura = cursor.fetchall()
        for campo in tecnicos_estructura:
            print(f"- {campo}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verificar_estructura_tablas()
