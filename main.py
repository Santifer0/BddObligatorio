import dataBase
import os
import mysql.connector
import modelos.proveedores as proveedores
import modelos.login as login



dataBase.crearBase()

login.loggin("administrador", "passadministrador")
proveedores.agregar_proveedor("Proveedor1", "Contacto1")
proveedores.agregar_proveedor("Proveedor2", "Contacto2")
proveedores.modificar_proveedor("Proveedor2","Contacto2", "Proveedor2 Modificado", "Contacto2 Modificado")
proveedores.eliminar_proveedor("Proveedor1")
print(proveedores.obtener_proveedores())


