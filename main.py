import dataBase
import os
import mysql.connector
import modelos.proveedores as proveedores
import modelos.login as login



dataBase.crearBase()

login.loggin("administrador", "passadministrador")
proveedores.agregar_proveedor("Proveedor1", "Contacto1")
proveedores.agregar_proveedor("Proveedor2", "Contacto2")
proveedores.eliminar_proveedor("Proveedor1")
print(login.isLogged())
print(proveedores.obtener_proveedores())

