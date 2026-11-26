-- Ejecutar como administrador UNA VEZ. Sustituir la contraseña antes. POR DEFECTO HE PUESTO admin
CREATE USER IF NOT EXISTS 'aula_python'@'localhost' IDENTIFIED BY 'admin';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON tema4_aula.* TO 'aula_python'@'localhost';
-- Si ya existía el usuario, CREATE USER no cambia su contraseña.
