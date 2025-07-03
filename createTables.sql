DROP DATABASE if exists Obligatorio;
CREATE DATABASE IF NOT EXISTS Obligatorio DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;
USE Obligatorio;
CREATE USER if not exists 'usuario'@'localhost' IDENTIFIED BY 'passusuario';
CREATE USER if not exists'administrador'@'localhost' IDENTIFIED BY 'passadministrador';
CREATE ROLE if not exists'usuario';
CREATE ROLE if not exists'administrador';
GRANT 'usuario' TO 'usuario'@'localhost';
GRANT 'administrador' TO 'administrador'@'localhost';
GRANT ALL PRIVILEGES ON Obligatorio.* TO 'administrador'@'localhost';

CREATE TABLE Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);
GRANT SELECT ON Obligatorio.Proveedores TO 'usuario'@'localhost';

CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    correo VARCHAR(100)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.Clientes TO 'usuario'@'localhost';

<<<<<<< HEAD
CREATE TABLE Maquinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    idCliente INT,
    ubicacionCliente VARCHAR(150),
    costo_alquiler DECIMAL(10,2),
    FOREIGN KEY (idCliente) REFERENCES Clientes(id)
);
GRANT SELECT ON Obligatorio.Maquinas TO 'usuario'@'localhost';
=======
>>>>>>> origin/main

CREATE TABLE Insumos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    idProveedor INT,
    FOREIGN KEY (idProveedor) REFERENCES Proveedores(id)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.insumos TO 'usuario'@'localhost';

<<<<<<< HEAD
=======
CREATE TABLE Maquinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    idCliente INT,
    direccionCliente VARCHAR(150),
    costo_alquiler DECIMAL(10,2),
    FOREIGN KEY (idCliente)   REFERENCES Clientes(id)
);



>>>>>>> origin/main
CREATE TABLE Registro_Consumo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_maquina INT,
    id_insumo  INT,
    fecha DATE,
    cantidad INT,
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(id),
    FOREIGN KEY (id_insumo)  REFERENCES Insumos(id)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.registro_consumo TO 'usuario'@'localhost';

CREATE TABLE Tecnicos (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(20)
);
GRANT SELECT ON Obligatorio.Tecnicos TO 'usuario'@'localhost';

CREATE TABLE Mantenimientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_maquina  INT,
    ci_tecnico  VARCHAR(20),
    tipo VARCHAR(50),
    fecha DATETIME,
    observaciones TEXT,
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(id),
    FOREIGN KEY (ci_tecnico) REFERENCES Tecnicos(ci)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.mantenimientos TO 'usuario'@'localhost' ;

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_publico VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    contrasenia   CHAR(64) NOT NULL,
    permisos BOOLEAN NOT NULL DEFAULT 0
);
INSERT INTO Usuarios (nombre_publico, nombre, contrasenia, permisos) VALUES
('Administrador', 'administrador', SHA2('passadministrador', 256), TRUE);
INSERT INTO Usuarios (nombre_publico, nombre, contrasenia, permisos) VALUES
('Usuario', 'usuario', SHA2('passusuario', 256), FALSE);


SHOW GRANTS FOR 'usuario'@'localhost';
SHOW GRANTS FOR 'administrador'@'localhost';