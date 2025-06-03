USE obligatorio;
DROP TABLE IF EXISTS mantenimientos;
DROP TABLE IF EXISTS registro_consumo;
DROP TABLE IF EXISTS maquinas;
DROP TABLE IF EXISTS insumos;
DROP TABLE IF EXISTS proveedores;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS tecnicos;
DROP TABLE IF EXISTS login;
-- Tabla de login
CREATE TABLE login (
    correo VARCHAR(100) PRIMARY KEY,
    contraseña VARCHAR(100) NOT NULL,
    es_administrador BOOLEAN DEFAULT FALSE
);

-- Tabla de proveedores
CREATE TABLE proveedores (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla de insumos
CREATE TABLE insumos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    descripcion TEXT NOT NULL,
    tipo VARCHAR(50),
    precio_unitario DECIMAL(10,2) NOT NULL,
    id_proveedor INT UNSIGNED,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
);

-- Tabla de clientes
CREATE TABLE clientes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

-- Tabla de maquinas
CREATE TABLE maquinas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    id_cliente INT UNSIGNED,
    ubicacion_cliente TEXT,
    costo_alquiler_mensual DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

-- Tabla de registro de consumo de insumos
CREATE TABLE registro_consumo (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_maquina INT UNSIGNED,
    id_insumo INT UNSIGNED,
    fecha DATE NOT NULL,
    cantidad_usada DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (id_insumo) REFERENCES insumos(id)
);

-- Tabla de técnicos
CREATE TABLE tecnicos (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla de mantenimientos
CREATE TABLE mantenimientos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_maquina INT UNSIGNED,
    ci_tecnico VARCHAR(20),
    tipo VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    observaciones TEXT,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (ci_tecnico) REFERENCES tecnicos(ci)
);