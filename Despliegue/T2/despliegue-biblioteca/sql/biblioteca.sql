-- =====================================================================
--  Base de datos de ejemplo para el despliegue Apache + Tomcat + MariaDB
--  Ejecutar en phpMyAdmin (pestana SQL) o con:
--     C:\xampp\mysql\bin\mysql -u root < biblioteca.sql
-- =====================================================================

DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca;
SET NAMES utf8mb4;

-- Usuario propio para la aplicacion (nunca conectar la app como root)
CREATE USER IF NOT EXISTS 'biblio'@'localhost' IDENTIFIED BY 'biblio123';
CREATE USER IF NOT EXISTS 'biblio'@'127.0.0.1' IDENTIFIED BY 'biblio123';
GRANT SELECT, INSERT ON biblioteca.* TO 'biblio'@'localhost';
GRANT SELECT, INSERT ON biblioteca.* TO 'biblio'@'127.0.0.1';
FLUSH PRIVILEGES;

CREATE TABLE generos (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(40) NOT NULL UNIQUE,
    color  CHAR(7)     NOT NULL           -- color en hexadecimal para la interfaz
) ENGINE = InnoDB;

CREATE TABLE libros (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    titulo      VARCHAR(150) NOT NULL,
    autor       VARCHAR(100) NOT NULL,
    anio        SMALLINT     NOT NULL,
    paginas     SMALLINT     NOT NULL,
    valoracion  DECIMAL(2,1) NOT NULL,     -- de 0.0 a 5.0
    genero_id   INT          NOT NULL,
    CONSTRAINT fk_libro_genero FOREIGN KEY (genero_id) REFERENCES generos (id)
) ENGINE = InnoDB;

INSERT INTO generos (nombre, color) VALUES
    ('Ciencia ficción', '#7c5cff'),
    ('Fantasía',        '#22b07d'),
    ('Clásicos',        '#e0a526'),
    ('Divulgación',     '#2f8fe0'),
    ('Novela negra',    '#e0564f');

INSERT INTO libros (titulo, autor, anio, paginas, valoracion, genero_id) VALUES
    ('Dune',                                  'Frank Herbert',            1965, 688, 4.6, 1),
    ('Fundación',                             'Isaac Asimov',             1951, 255, 4.4, 1),
    ('Neuromante',                            'William Gibson',           1984, 271, 4.0, 1),
    ('La mano izquierda de la oscuridad',     'Ursula K. Le Guin',        1969, 304, 4.3, 1),
    ('El problema de los tres cuerpos',       'Liu Cixin',                2006, 400, 4.2, 1),
    ('El Hobbit',                             'J. R. R. Tolkien',         1937, 310, 4.7, 2),
    ('El señor de los anillos',               'J. R. R. Tolkien',         1954, 1216, 4.9, 2),
    ('Un mago de Terramar',                   'Ursula K. Le Guin',        1968, 183, 4.1, 2),
    ('El nombre del viento',                  'Patrick Rothfuss',         2007, 662, 4.5, 2),
    ('Don Quijote de la Mancha',              'Miguel de Cervantes',      1605, 1250, 4.8, 3),
    ('Cien años de soledad',                  'Gabriel García Márquez',   1967, 471, 4.7, 3),
    ('Orgullo y prejuicio',                   'Jane Austen',              1813, 432, 4.5, 3),
    ('Crimen y castigo',                      'Fiódor Dostoyevski',       1866, 671, 4.6, 3),
    ('Breve historia del tiempo',             'Stephen Hawking',          1988, 256, 4.4, 4),
    ('Cosmos',                                'Carl Sagan',               1980, 365, 4.7, 4),
    ('El gen egoísta',                        'Richard Dawkins',          1976, 360, 4.2, 4),
    ('Gödel, Escher, Bach',                   'Douglas Hofstadter',       1979, 777, 4.3, 4),
    ('El sueño eterno',                       'Raymond Chandler',         1939, 231, 4.1, 5),
    ('Asesinato en el Orient Express',        'Agatha Christie',          1934, 256, 4.4, 5),
    ('La verdad sobre el caso Harry Quebert', 'Joël Dicker',              2012, 672, 4.0, 5);

-- Consultas de comprobacion (las mismas que lanza la aplicacion Java)
SELECT COUNT(*) AS total_libros FROM libros;

SELECT g.nombre, COUNT(l.id) AS total, ROUND(AVG(l.valoracion), 2) AS media
FROM generos g LEFT JOIN libros l ON l.genero_id = g.id
GROUP BY g.id, g.nombre
ORDER BY total DESC;
