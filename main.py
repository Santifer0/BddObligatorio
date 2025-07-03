import dataBase
import os
import mysql.connector
import modelos.proveedores as proveedores
import modelos.login as login
import modelos.insumo as insumos
import modelos.clientes as clientes
import modelos.maquina as maquinas
import modelos.tecnico as tecnicos
import modelos.mantenimientos as mantenimientos
import modelos.consumo as consumo

dataBase.crearBase()


login.loggin("administrador", "passadministrador")

# test proveedores
proveedores.agregar_proveedor("Proveedor1", "Contacto1")
proveedores.agregar_proveedor("Proveedor2", "Contacto2")
resultado_proveedores = proveedores.obtener_proveedores()
primer_id = resultado_proveedores[0]['id']
segundo_id = resultado_proveedores[1]['id']
proveedores.eliminar_proveedor(segundo_id)
proveedores.modificar_proveedor(primer_id, "Proveedor1 Modificado", "Contacto1 Modificado")
print(proveedores.obtener_proveedores())
login.logout()



# Test insumos
dataBase.crearBase()
login.loggin("administrador", "passadministrador")
proveedores.agregar_proveedor("Proveedor1", "Contacto1")
proveedores.agregar_proveedor("Proveedor2", "Contacto2")
resultado_proveedores = proveedores.obtener_proveedores()
login.logout()
login.loggin("usuario", "passusuario")
id_proveedor = resultado_proveedores[0]['id']
insumos.agregar_insumo("insumo1", 150.0, id_proveedor)
insumos.agregar_insumo("insumo2", 80.0, id_proveedor)
insumos.modificar_insumo(1, "insumo1 modificado", 200, id_proveedor)
insumos.eliminar_insumo(2)  
print(insumos.obtener_Insumos())
login.logout()

# Test clientes
login.loggin("usuario", "passusuario")
clientes.agregar_cliente("nombre1", "direccion1", "telefono1", "email1")
clientes.agregar_cliente("nombre2", "direccion2", "telefono2", "email2")
clientes.modificar_cliente(1, "nombre1 modificado", "direccion1 modificada", "telefono1 modificado", "email1 modificado")
clientes.eliminar_cliente(2)
print(clientes.obtener_clientes())
login.logout()

# Test maquinas
dataBase.crearBase()
login.loggin("administrador", "passadministrador")
clientes.agregar_cliente("nombre1", "direccion1", "telefono1", "email1")
resultado_clientes = clientes.obtener_clientes()
id_cliente = resultado_clientes[0]['id']
maquinas.agregar_maquina("modelo1", id_cliente, "direccion1", 100)
maquinas.agregar_maquina("modelo2", id_cliente, "direccion2", 200)
maquinas.modificar_maquina(1, "modelo1 modificado", id_cliente, "direccion1 modificada", 150)
maquinas.eliminar_maquina(2)
print(maquinas.obtener_maquinas())
login.logout()

# Test tecnicos
login.loggin("administrador", "passadministrador")
tecnicos.agregar_tecnico("ci1", "nombre1", "apellido1", "telefono1")
tecnicos.agregar_tecnico("ci2", "nombre2", "apellido2", "telefono2")
tecnicos.modificar_tecnico("ci1", "nombre1 modificado", "apellido1 modificado", "telefono1 modificado")
tecnicos.eliminar_tecnico("ci2")
print(tecnicos.obtener_tecnicos())


# Test mantenimientos
dataBase.crearBase()
login.loggin("administrador", "passadministrador")
clientes.agregar_cliente("nombre1", "direccion1", "telefono1", "email1")
resultado_clientes = clientes.obtener_clientes()
id_cliente = resultado_clientes[0]['id']
maquinas.agregar_maquina("modelo1", id_cliente, "direccion1", 100)
maquinas.agregar_maquina("modelo2", id_cliente, "direccion2", 200)
resultado_maquinas = maquinas.obtener_maquinas()

tecnicos.agregar_tecnico("ci1", "nombre1", "apellido1", "telefono1")
resultado_tecnicos = tecnicos.obtener_tecnicos()

id_maquina = resultado_maquinas[0]['id']
ci_tecnico = resultado_tecnicos[0]['ci']
#"2025-06-27 10:30:00"
mantenimientos.agregar_mantenimiento(id_maquina, ci_tecnico, "tipo1", "2025-06-27", "observacion1")
mantenimientos.agregar_mantenimiento(id_maquina, ci_tecnico, "tipo2", "2025-06-28", "observacion2")
mantenimientos.modificar_mantenimiento(1, id_maquina, ci_tecnico, "tipo1 modificado", "2025-06-29", "observacion1 modificada")
mantenimientos.eliminar_mantenimiento(2)
print(mantenimientos.obtener_mantenimientos())
login.logout()

#Test consumo
print('entre')
login.loggin("administrador", "passadministrador")
maquinas.agregar_maquina("modelo1", id_cliente, "direccion1", 100)
resultado_maquinas = maquinas.obtener_maquinas()
id_maquina = resultado_maquinas[0]['id']

proveedores.agregar_proveedor("Proveedor1", "Contacto1")
resultado_proveedores = proveedores.obtener_proveedores()
id_proveedor = resultado_proveedores[0]['id']
insumos.agregar_insumo("insumo1", 150.0, id_proveedor)
resultado_insumos = insumos.obtener_Insumos()
id_insumo = resultado_insumos[0]['id']
consumo.registrar_consumo(id_maquina, id_insumo, "2025-06-27", 10)
consumo.registrar_consumo(id_maquina, id_insumo, "2025-06-28", 20)
print(consumo.obtener_consumos())
login.logout()