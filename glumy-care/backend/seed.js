const pool = require('./db');

const seedProductos = async () => {
    // Nuevos productos adaptados a la visión Derma-Tech de GLUmy Care
    const productos = [
        {
            nombre: "GLUmy Clear Derma",
            descripcion: "Fórmula avanzada con Zinc y Niacinamida para controlar brotes severos.",
            precio: 29.99,
            imagen: "https://via.placeholder.com/300x300/00B4D8/FFFFFF?text=Clear+Derma",
            stock: 100,
            etiqueta: "Acné Activo"
        },
        {
            nombre: "GLUmy Neon Glow",
            descripcion: "Biotecnología con Vitamina C para desvanecer marcas y cicatrices.",
            precio: 34.99,
            imagen: "https://via.placeholder.com/300x300/00F5D4/1A1A24?text=Neon+Glow",
            stock: 80,
            etiqueta: "Recuperación"
        },
        {
            nombre: "GLUmy Zen Balance",
            descripcion: "Regulador hormonal con extractos botánicos y adaptógenos calmantes.",
            precio: 27.50,
            imagen: "https://via.placeholder.com/300x300/9D4EDD/FFFFFF?text=Zen+Balance",
            stock: 50,
            etiqueta: "Prevención"
        }
    ];

    try {
        console.log("Inyectando productos en la base de datos...");
        for (let prod of productos) {
            await pool.query(
                `INSERT INTO productos (nombre, descripcion, precio, imagen, stock, etiqueta) 
                 VALUES ($1, $2, $3, $4, $5, $6)`,
                [prod.nombre, prod.descripcion, prod.precio, prod.imagen, prod.stock, prod.etiqueta]
            );
        }
        console.log("✅ ¡Base de datos poblada! Los productos futuristas de GLUmy Care están listos.");
    } catch (err) {
        console.error("❌ Error al insertar productos:", err);
    } finally {
        pool.end();
    }
};

seedProductos();