<<<<<<< HEAD
USE Obligatorio;

-- Proveedores
INSERT INTO Proveedores (nombre, contacto) VALUES
('Nestlé Uruguay', 'contacto@nestle.uy'),
('Café del Sur', 'cafesur@correo.com');

-- Clientes
INSERT INTO Clientes (nombre, direccion, telefono, correo) VALUES
('Supermercado Doña María', '18 de Julio 1234', '24871122', 'dona@super.com'),
('Oficinas ITNet', 'Calle Ciencia 45', '26223344', 'contacto@itnet.com');

-- Maquinas
INSERT INTO Maquinas (modelo, idCliente, ubicacionCliente, costo_alquiler) VALUES
('Modelo A100', 1, '26 de marzo', 1500.00),
('Modelo C250', 2, 'av brasil', 1200.00),
('Modelo B150', 2, 'riccaldoni', 1300.00);

-- Tecnicos
INSERT INTO Tecnicos (ci, nombre, apellido, telefono) VALUES
('12345678', 'Martín', 'Pérez', '099123456'),
('98765432', 'Lucía', 'Gómez', '098765432');

=======
-- Proveedores
INSERT INTO Proveedores (nombre, contacto) VALUES
('Nestlé Uruguay', 'contacto@nestle.uy'),
('Café del Sur', 'cafesur@correo.com');

-- Empresa (Clientes)
INSERT INTO Empresa (nombre, telefono, correo) VALUES
('Supermercado Doña María', '24871122', 'dona@super.com'),
('Oficinas ITNet', '26223344', 'contacto@itnet.com');

-- Locales
INSERT INTO Locales (nombre, direccion, telefono, correo) VALUES
('Sucursal Centro', '18 de Julio 1234', '24001234', 'centro@super.com'),
('Sucursal Parque Rodó', 'Br. Artigas 456', '24119988', 'rodosuc@super.com');

-- Empresa_Local
INSERT INTO Empresa_Local (empresaId, localId) VALUES
(1, 1),
(1, 2),
(2, 2);

-- Maquinas
INSERT INTO Maquinas (modelo, idLocal, idEmpresa, ubicacionLocales, costo_alquiler) VALUES
('Modelo A100', 1, 1, 'Entrada principal', 1500.00),
('Modelo C250', 2, 1, 'Sala de espera', 1200.00),
('Modelo B150', 2, 2, 'Recepción 3er piso', 1300.00);

-- Tecnicos
INSERT INTO Tecnicos (ci, nombre, apellido, telefono) VALUES
('12345678', 'Martín', 'Pérez', '099123456'),
('98765432', 'Lucía', 'Gómez', '098765432');

>>>>>>> origin/main
-- Mantenimientos
INSERT INTO Mantenimientos (id_maquina, ci_tecnico, tipo, fecha, observaciones) VALUES
(1, '12345678', 'Preventivo', '2025-06-10 10:00:00', 'Cambio de filtros'),
(2, '98765432', 'Asistencia', '2025-06-12 14:30:00', 'Problema en el botón de selección');

-- Insumos
INSERT INTO Insumos (nombre, precio, idProveedor) VALUES
('Café Clásico', 1.25, 1),
('Leche en polvo', 0.95, 2),
('Chocolate', 1.75, 1),
('Canela', 0.60, 2);

-- Registro_Consumo
INSERT INTO Registro_Consumo (id_maquina, id_insumo, fecha, cantidad) VALUES
(1, 1, '2025-06-01', 20),
(1, 2, '2025-06-01', 10),
(2, 1, '2025-06-01', 15),
(3, 3, '2025-06-02', 5);

-- Usuarios
<<<<<<< HEAD
INSERT INTO Usuarios (nombre_publico, nombre, contrasenia, permisos) VALUES
('Administrador Principal', 'admin', SHA2('miContrasenia', 256), true),
('Usuario Técnico', 'tecnico1', SHA2('miContraseniaSegura', 256), false);
=======
INSERT INTO Usuarios (nombre_publico, nombre,contrasenia, permisos) VALUES
('Administrador Principal', 'admin', SHA2('miContrasenia', 256), true),
('Usuario Técnico', 'tecnico1', SHA2('miContraseniaSegura', 256),false);
>>>>>>> origin/main
