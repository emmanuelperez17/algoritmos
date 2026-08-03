const pool = require('./db');
const bcrypt = require('bcryptjs');

const crearAdmin = async () => {
    try {
        // Tus datos de acceso como Admin
        const email = 'admin@glumycare.com';
        const passwordNormal = 'AdminSeguro2026'; // Esta es tu contraseña (luego puedes cambiarla)
        
        // Magia de encriptación
        const salt = await bcrypt.genSalt(10);
        const passwordEncriptada = await bcrypt.hash(passwordNormal, salt);

        // Guardar en la base de datos con el rol 'admin'
        await pool.query(
            `INSERT INTO usuarios (nombre, email, password, rol) 
             VALUES ($1, $2, $3, $4)
             ON CONFLICT (email) DO NOTHING`,
            ['Súper Admin', email, passwordEncriptada, 'admin']
        );
        console.log("✅ ¡Tu cuenta de Administrador supremo ha sido creada con éxito!");
        console.log(`✉️ Correo: ${email}`);
        console.log(`🔑 Contraseña encriptada en la BD, usa: ${passwordNormal} para entrar luego.`);
    } catch (err) {
        console.error("❌ Error al crear admin:", err);
    } finally {
        pool.end();
    }
};

crearAdmin();