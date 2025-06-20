import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos import maquina

def test_login_admin():
    # Suponiendo que existe un usuario admin con estos datos
    assert maquina.loggin("admin", "adminpass") is True
    assert maquina.loggedAdmin is True

def test_agregar_maquina():
    # Cambia los datos según tu base de test
    maquina.loggin("admin", "adminpass")
    resultado = maquina.agregar_maquina("ModeloTest", 1, "UbicacionTest", 1000, "admin", "adminpass")
    assert resultado is True  # O ajustá según lo que retorne tu función

def test_obtener_maquinas():
    maquina.loggin("admin", "adminpass")
    maquinas = maquina.obtener_maquinas("admin", "adminpass")
    assert isinstance(maquinas, list)

def test_eliminar_maquina():
    maquina.loggin("admin", "adminpass")
    resultado = maquina.eliminar_maquina(1, "admin", "adminpass")
    assert resultado is True  # O ajustá según lo que retorne tu función