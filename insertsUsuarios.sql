USE Obligatorio;

-- Insertar usuarios de prueba
INSERT INTO Usuarios (nombre_publico, nombre, contrasenia, permisos) VALUES
('Administrador Principal', 'admin', SHA2('miContrasenia', 256), true),
('Usuario Técnico', 'tecnico1', SHA2('miContraseniaSegura', 256), false);

-- Verificar que se insertaron correctamente
SELECT * FROM Usuarios;
