import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos import empresas

def test_agregar_empresa():
    empresas.agregar_empresa(
        nombre='Empresa Test',
        telefono='123456789',
        correo='empresa@test.com'
    )
    print("Empresa agregada.")

def test_obtener_empresas():
    resultado = empresas.obtener_empresas()
    print("Empresas:", resultado)

def test_modificar_empresa():
    empresas.modificar_empresa(
        id=1,
        nombre='Empresa Modificada',
        telefono='987654321',
        correo='empresa_modificada@test.com'
    )
    print("Empresa modificada.")


if __name__ == "__main__":
    test_agregar_empresa()
    test_obtener_empresas()
    test_modificar_empresa()