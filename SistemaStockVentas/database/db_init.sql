-- Script para inicializar la base de datos
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL
);

INSERT INTO usuarios (nombre_usuario, contrasena, rol)
VALUES ('admin', 'admin', 'admin')
ON CONFLICT (nombre_usuario) DO NOTHING;

-- Más tablas pueden ser añadidas aquí
