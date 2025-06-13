import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos import mantenimientos

def test_agregar_mantenimiento():
    mantenimientos.agregar_mantenimiento(
        id_maquina=1,
        ci_tecnico='12345678',
        tipo='Preventivo',
        fecha='2025-06-13 10:00:00',
        observaciones='Test de inserción'
    )
    print("Mantenimiento agregado.")

def test_obtener_mantenimientos():
    resultado = mantenimientos.obtener_mantenimientos()
    print("Mantenimientos:", resultado)

def test_modificar_mantenimiento():
    mantenimientos.modificar_mantenimiento(
        id=1,
        id_maquina=1,
        ci_tecnico='12345678',
        tipo='Correctivo',
        fecha='2025-06-14 12:00:00',
        observaciones='Observación modificada'
    )
    print("Mantenimiento modificado.")

def test_eliminar_mantenimiento():
    mantenimientos.eliminar_mantenimiento(2)
    print("Mantenimiento eliminado.")

if __name__ == "__main__":
    test_agregar_mantenimiento()
    test_obtener_mantenimientos()
    test_modificar_mantenimiento()
    test_eliminar_mantenimiento()