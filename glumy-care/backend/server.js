const express = require('express');
const cors = require('cors');
const pool = require('./db');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = process.env.PORT || 3000;

// Llave secreta para los Tokens (En producción esto va en un archivo .env)
const JWT_SECRET = 'GlumyDermaTech2026_UltraSecret';

// Middlewares
app.use(cors());
app.use(express.json());

// ==========================================
// RUTAS PÚBLICAS (Productos y Salud)
// ==========================================
app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', message: 'Servidor de GLUmy Care al 100% 🚀' });
});

app.get('/api/productos', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM productos ORDER BY id ASC');
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: 'Error al obtener los productos' });
    }
});

// Crear un nuevo producto
app.post('/api/productos', async (req, res) => {
    const { nombre, descripcion, precio, imagen, stock, etiqueta } = req.body;
    try {
        const nuevoProducto = await pool.query(
            'INSERT INTO productos (nombre, descripcion, precio, imagen, stock, etiqueta) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *',
            [nombre, descripcion, precio, imagen, stock, etiqueta]
        );
        res.json(nuevoProducto.rows[0]);
    } catch (err) {
        res.status(500).json({ error: 'Error al crear el producto' });
    }
});

// Actualizar un producto existente
app.put('/api/productos/:id', async (req, res) => {
    const { id } = req.params;
    const { nombre, descripcion, precio, imagen, stock, etiqueta } = req.body;
    try {
        await pool.query(
            'UPDATE productos SET nombre = $1, descripcion = $2, precio = $3, imagen = $4, stock = $5, etiqueta = $6 WHERE id = $7',
            [nombre, descripcion, precio, imagen, stock, etiqueta, id]
        );
        res.json({ message: 'Producto actualizado con éxito' });
    } catch (err) {
        res.status(500).json({ error: 'Error al actualizar el producto' });
    }
});

// Eliminar un producto
app.delete('/api/productos/:id', async (req, res) => {
    const { id } = req.params;
    try {
        await pool.query('DELETE FROM productos WHERE id = $1', [id]);
        res.json({ message: 'Producto eliminado' });
    } catch (err) {
        res.status(500).json({ error: 'Error al eliminar el producto' });
    }
});

// ==========================================
// RUTAS DE AUTENTICACIÓN (Login y Registro)
// ==========================================

// 1. Registro de Cliente Nuevo
app.post('/api/registro', async (req, res) => {
    const { nombre, email, password } = req.body;

    try {
        // Verificar si el correo ya existe
        const usuarioExistente = await pool.query('SELECT * FROM usuarios WHERE email = $1', [email]);
        if (usuarioExistente.rows.length > 0) {
            return res.status(400).json({ error: 'Este correo ya está registrado en GLUmy Care.' });
        }

        // Encriptar la contraseña
        const salt = await bcrypt.genSalt(10);
        const passwordEncriptada = await bcrypt.hash(password, salt);

        // Guardar en la base de datos (por defecto el rol es 'cliente')
        const nuevoUsuario = await pool.query(
            'INSERT INTO usuarios (nombre, email, password) VALUES ($1, $2, $3) RETURNING id, nombre, email, rol',
            [nombre, email, passwordEncriptada]
        );

        res.status(201).json({ message: 'Usuario creado exitosamente', usuario: nuevoUsuario.rows[0] });
    } catch (err) {
        console.error("Error en registro:", err);
        res.status(500).json({ error: 'Error en el servidor al registrar' });
    }
});

// 2. Inicio de Sesión (Login)
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        // Buscar al usuario por su correo
        const resultado = await pool.query('SELECT * FROM usuarios WHERE email = $1', [email]);
        if (resultado.rows.length === 0) {
            return res.status(401).json({ error: 'Correo o contraseña incorrectos.' });
        }

        const usuario = resultado.rows[0];

        // Comparar la contraseña ingresada con la encriptada en la BD
        const passwordValida = await bcrypt.compare(password, usuario.password);
        if (!passwordValida) {
            return res.status(401).json({ error: 'Correo o contraseña incorrectos.' });
        }

        // Crear el "Token" (pasaporte virtual) que dura 24 horas
        const token = jwt.sign(
            { id: usuario.id, rol: usuario.rol }, 
            JWT_SECRET, 
            { expiresIn: '24h' }
        );

        // Devolver el token y los datos útiles al frontend
        res.json({
            message: 'Bienvenido a GLUmy Care',
            token: token,
            usuario: {
                id: usuario.id,
                nombre: usuario.nombre,
                email: usuario.email,
                rol: usuario.rol
            }
        });
    } catch (err) {
        console.error("Error en login:", err);
        res.status(500).json({ error: 'Error en el servidor al iniciar sesión' });
    }
});

// ==========================================
// RUTAS DE COMPRAS (Pedidos)
// ==========================================

// Crear un nuevo pedido cuando el cliente paga
app.post('/api/pedidos', async (req, res) => {
    // Recibimos quién compra y cuánto gastó
    const { usuario_id, total } = req.body;

    try {
        // Guardamos el registro en PostgreSQL
        const nuevoPedido = await pool.query(
            'INSERT INTO pedidos (usuario_id, total, estado) VALUES ($1, $2, $3) RETURNING *',
            [usuario_id, total, 'Pendiente']
        );
        
        res.status(201).json({ 
            message: '¡Compra exitosa! Tu pedido está en proceso.', 
            pedido: nuevoPedido.rows[0] 
        });
    } catch (err) {
        console.error("Error al crear el pedido:", err);
        res.status(500).json({ error: 'Error al procesar la compra' });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});