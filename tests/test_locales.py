import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos import locales

def test_agregar_local():
    locales.agregar_local(
        nombre='Local Test',
        direccion='Calle Ejemplo 456',
        telefono='22223333',
        correo='local@test.com'
    )
    print("Local agregado.")

def test_obtener_locales():
    resultado = locales.obtener_locales()
    print("Locales:", resultado)

def test_modificar_local():
    locales.modificar_local(
        id=1,
        nombre='Local Modificado',
        direccion='Calle Modificada 789',
        telefono='44445555',
        correo='local_modificado@test.com'
    )
    print("Local modificado.")

if __name__ == "__main__":
    test_agregar_local()
    test_obtener_locales()
    test_modificar_local()