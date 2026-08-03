const { Pool } = require('pg');

// Configuración de la conexión usando las variables que pusimos en Docker
const pool = new Pool({
    user: process.env.DB_USER || 'glumy_admin',
    host: process.env.DB_HOST || 'db',
    database: process.env.DB_NAME || 'glumy_care',
    password: process.env.DB_PASSWORD || 'glumy_password_123',
    port: 5432,
});

pool.on('connect', () => {
    console.log('🔗 Conectado a la base de datos PostgreSQL de GLUmy Care');
});

module.exports = pool;