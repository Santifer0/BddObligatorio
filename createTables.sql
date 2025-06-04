DROP DATABASE if exists Obligatorio;
CREATE DATABASE IF NOT EXISTS Obligatorio;
USE Obligatorio;
CREATE USER if not exists 'usuario'@'localhost' IDENTIFIED BY 'passusuario';
CREATE USER if not exists'administrador'@'localhost' IDENTIFIED BY 'passadministrador';
CREATE ROLE if not exists'usuario';
CREATE ROLE if not exists'administrador';
GRANT 'usuario' TO 'usuario'@'localhost';
GRANT 'administrador' TO 'administrador'@'localhost';


CREATE TABLE Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

CREATE TABLE Empresa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.Empresa TO 'usuario'@'localhost';

CREATE TABLE Locales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    correo VARCHAR(100)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.locales TO 'usuario'@'localhost';

CREATE TABLE Insumos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    idProveedor INT,
    FOREIGN KEY (idProveedor) REFERENCES Proveedores(id)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.insumos TO 'usuario'@'localhost';

CREATE TABLE Maquinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    idLocal INT,
    idEmpresa INT,
    ubicacionLocales VARCHAR(150),
    costo_alquiler DECIMAL(10,2),
    FOREIGN KEY (idLocal)   REFERENCES Locales(id),
    FOREIGN KEY (idEmpresa) REFERENCES Empresa(id)
);


CREATE TABLE Empresa_Local (
    empresaId INT,
    localId   INT,
    PRIMARY KEY (empresaId, localId),
    FOREIGN KEY (empresaId) REFERENCES Empresa(id),
    FOREIGN KEY (localId)   REFERENCES Locales(id)
);
GRANT SELECT, INSERT, UPDATE, DELETE ON Obligatorio.empresa_local TO 'usuario'@'localhost';

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
    permisos VARCHAR(100)
);

CREATE TABLE Usuario_Contrasenia (
    nombreUsuario VARCHAR(50) PRIMARY KEY,
    contrasenia   VARCHAR(255) NOT NULL,
    FOREIGN KEY (nombreUsuario) REFERENCES Usuarios(nombre)
);


SHOW GRANTS FOR 'usuario'@'localhost';
SHOW GRANTS FOR 'administrador'@'localhost';