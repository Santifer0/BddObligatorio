USE obligatorio;

INSERT INTO login (correo, contraseña, es_administrador) VALUES
('admin@cafesmarloy.com', 'admin123', TRUE),
('usuario@cafesmarloy.com', 'usuario123', FALSE);

INSERT INTO proveedores (nombre, contacto) VALUES
('Proveedor Café SA', 'contacto@cafesa.com'),
('Insumos Gourmet', 'ventas@gourmet.com');

INSERT INTO insumos (descripcion, tipo, precio_unitario, id_proveedor) VALUES
('Café molido', 'Café', 120.00, 1),
('Leche en polvo', 'Lácteo', 90.00, 2),
('Canela', 'Especias', 50.00, 2);

INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES
('Oficinas Sur S.A.', 'Av. Independencia 123', '098123456', 'cliente1@empresa.com'),
('Universidad Central', 'Calle Ciencia 45', '099876543', 'admin@uc.edu');

INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES
('1234567', 'Mario', 'Pérez', '091111111'),
('7654321', 'Laura', 'Gómez', '092222222');