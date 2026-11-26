
CREATE DATABASE IF NOT EXISTS tema4_aula CHARACTER SET utf8mb4;
USE tema4_aula;
CREATE TABLE IF NOT EXISTS categorias (
 id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS productos (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(100) NOT NULL,
 precio DECIMAL(10,2) NOT NULL,
 stock INT NOT NULL DEFAULT 0,
 categoria_id INT,
 FOREIGN KEY (categoria_id) REFERENCES categorias(id)
) ENGINE=InnoDB;
-- Vacía SOLO las tablas de práctica para recuperar el estado inicial.
DELETE FROM productos;
DELETE FROM categorias;
ALTER TABLE categorias AUTO_INCREMENT = 1;
ALTER TABLE productos AUTO_INCREMENT = 1;
INSERT INTO categorias (nombre) VALUES ('Papelería'), ('Hogar');
INSERT INTO productos (nombre,precio,stock,categoria_id) VALUES
('Lápiz',1.50,10,1),('Cuaderno',3.00,5,1),('Goma',0.80,20,1);
