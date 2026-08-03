const pool = require('./db');

const crearTablas = async () => {
    try {
        // 1. Tabla de Usuarios
        await pool.query(`
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                rol VARCHAR(20) DEFAULT 'cliente'
            );
        `);
        console.log("✅ Tabla 'usuarios' lista.");

        // 2. Tabla de Productos (Ya la teníamos)
        await pool.query(`
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT,
                precio DECIMAL(10, 2) NOT NULL,
                imagen VARCHAR(255),
                stock INTEGER NOT NULL DEFAULT 50,
                etiqueta VARCHAR(50)
            );
        `);
        console.log("✅ Tabla 'productos' lista.");

        // 3. Tabla de Pedidos (Relacionada con el usuario)
        await pool.query(`
            CREATE TABLE IF NOT EXISTS pedidos (
                id SERIAL PRIMARY KEY,
                usuario_id INTEGER REFERENCES usuarios(id),
                total DECIMAL(10, 2) NOT NULL,
                estado VARCHAR(50) DEFAULT 'Pendiente',
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        `);
        console.log("✅ Tabla 'pedidos' lista.");

    } catch (err) {
        console.error("❌ Error al actualizar las tablas:", err);
    } finally {
        pool.end();
    }
};

crearTablas();