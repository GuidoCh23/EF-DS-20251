CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP 
);

CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    fecha_creacion TIMESTAMP
);

INSERT INTO usuarios (nombre, email) VALUES 
('Juan Perez', 'juan@gmail.com'),
('Maria Garcia', 'maria@gmail.com');

INSERT INTO productos (nombre, precio, stock) VALUES 
('Producto A', 25.99, 120),
('Producto B', 15.50, 53);