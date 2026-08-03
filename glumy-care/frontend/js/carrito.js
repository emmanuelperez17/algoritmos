/**
 * ============================================================================
 * Glowy Care - Lógica Avanzada del Carrito de Compras
 * Implementa: LocalStorage, cálculos dinámicos, formateo de moneda y validaciones.
 * ============================================================================
 */

// Configuración de negocio
const CONFIG = {
    tasaIva: 0.19,             // 19% de IVA
    costoEnvioBase: 12.50,     // Costo de envío estándar
    montoEnvioGratis: 50.00,   // Monto mínimo para envío gratis
    moneda: 'USD'
};

// Inicializar carrito desde LocalStorage
let carrito = JSON.parse(localStorage.getItem('carritoGlowy')) || [];

// Utilidad para formatear dinero profesionalmente
const formatearDinero = (monto) => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: CONFIG.moneda
    }).format(monto);
};

// ================= FUNCIONES PRINCIPALES =================

/**
 * Agrega un producto al carrito o incrementa su cantidad si ya existe.
 * @param {number} id - ID del producto
 * @param {number} cantidadAgregada - Cantidad a agregar (default 1)
 */
function agregarAlCarrito(id, cantidadAgregada = 1) {
    // Busca el producto en la base de datos simulada (productosDB en productos.js)
    const productoInfo = productosDB.find(p => p.id === id);
    
    if (!productoInfo) {
        console.error("Producto no encontrado en la base de datos.");
        return;
    }

    const productoEnCarrito = carrito.find(p => p.id === id);

    if (productoEnCarrito) {
        productoEnCarrito.cantidad += cantidadAgregada;
    } else {
        carrito.push({ ...productoInfo, cantidad: cantidadAgregada });
    }
    
    guardarYActualizar();
    
    // Notificación elegante con SweetAlert2
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: '¡Producto añadido!',
        text: `${productoInfo.nombre} está en tu carrito.`,
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
        background: 'var(--glass-bg)',
        color: 'var(--text-dark)',
        customClass: { popup: 'glass-card' }
    });
}

/**
 * Cambia la cantidad de un producto específico.
 * @param {number} id - ID del producto
 * @param {number} cambio - Número positivo o negativo para sumar/restar
 */
function cambiarCantidad(id, cambio) {
    const producto = carrito.find(p => p.id === id);
    if (!producto) return;

    producto.cantidad += cambio;

    // Validación para no tener cantidades negativas o cero
    if (producto.cantidad <= 0) {
        eliminarDelCarrito(id);
    } else {
        guardarYActualizar();
    }
}

/**
 * Elimina un producto por completo del carrito.
 * @param {number} id - ID del producto
 */
function eliminarDelCarrito(id) {
    Swal.fire({
        title: '¿Eliminar producto?',
        text: "Se quitará este ítem de tu carrito.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: 'var(--accent)',
        cancelButtonColor: '#aaa',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-card)',
        color: 'var(--text-dark)'
    }).then((result) => {
        if (result.isConfirmed) {
            carrito = carrito.filter(p => p.id !== id);
            guardarYActualizar();
        }
    });
}

/**
 * Vacía todo el carrito con confirmación previa.
 */
function vaciarCarrito() {
    if (carrito.length === 0) return;

    Swal.fire({
        title: '¿Vaciar carrito?',
        text: "Perderás todos los productos seleccionados.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#E91E63',
        cancelButtonColor: '#666',
        confirmButtonText: 'Sí, vaciar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-card)',
        color: 'var(--text-dark)'
    }).then((result) => {
        if (result.isConfirmed) {
            carrito = [];
            guardarYActualizar();
        }
    });
}

// ================= RENDERIZADO Y CÁLCULOS =================

/**
 * Dibuja los elementos en la tabla de la página del carrito.
 */
function renderizarCarrito() {
    const tbody = document.getElementById("tabla-carrito");
    if (!tbody) return; // Si no estamos en la página del carrito, no hace nada.
    
    tbody.innerHTML = "";
    
    if (carrito.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" class="text-center py-5">
                    <i class="bi bi-cart-x fs-1 text-muted mb-3 d-block"></i>
                    <h5 class="text-muted">Tu carrito está vacío</h5>
                    <a href="productos.html" class="btn btn-outline-glowy mt-3">Ir a la tienda</a>
                </td>
            </tr>`;
        actualizarResumen(0);
        return;
    }

    let subtotalGlobal = 0;

    carrito.forEach((prod) => {
        const subtotalProducto = prod.precio * prod.cantidad;
        subtotalGlobal += subtotalProducto;

        tbody.innerHTML += `
            <tr class="align-middle">
                <td>
                    <div class="position-relative d-inline-block">
                        <img src="${prod.img}" width="70" class="rounded shadow-sm" alt="${prod.nombre}">
                    </div>
                </td>
                <td class="fw-bold">${prod.nombre}</td>
                <td>
                    <div class="d-flex justify-content-center align-items-center">
                        <button class="btn btn-sm btn-outline-glowy rounded-circle me-2" onclick="cambiarCantidad(${prod.id}, -1)">
                            <i class="bi bi-dash"></i>
                        </button>
                        <span class="fw-bold fs-6 mx-2" style="min-width: 25px;">${prod.cantidad}</span>
                        <button class="btn btn-sm btn-outline-glowy rounded-circle ms-2" onclick="cambiarCantidad(${prod.id}, 1)">
                            <i class="bi bi-plus"></i>
                        </button>
                        <button class="btn btn-glowy w-100 rounded-pill mt-3" onclick="procesarCompra()">
                            Proceder al Pago Seguramente <i class="bi bi-lock-fill"></i>
                        </button>
                    </div>
                </td>
                <td class="text-accent fw-bold">${formatearDinero(subtotalProducto)}</td>
                <td>
                    <button class="btn btn-light btn-sm text-danger shadow-sm rounded-circle" onclick="eliminarDelCarrito(${prod.id})" title="Eliminar">
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        `;
    });

    actualizarResumen(subtotalGlobal);
}

/**
 * Calcula y actualiza el panel lateral de resumen (Subtotal, IVA, Envío, Total).
 * @param {number} subtotal - Subtotal de los productos.
 */
function actualizarResumen(subtotal) {
    const elSubtotal = document.getElementById("resumen-subtotal");
    const elIva = document.getElementById("resumen-iva");
    const elEnvio = document.getElementById("resumen-envio"); // Asume que agregas ID 'resumen-envio' al span del envío en HTML
    const elTotal = document.getElementById("resumen-total");

    if (!elSubtotal || !elTotal) return;

    // Cálculos
    const iva = subtotal * CONFIG.tasaIva;
    
    // Lógica dinámica de envío
    let envio = 0;
    if (subtotal > 0 && subtotal < CONFIG.montoEnvioGratis) {
        envio = CONFIG.costoEnvioBase;
    }
    
    const total = subtotal + iva + envio;

    // Actualización del DOM
    elSubtotal.innerText = formatearDinero(subtotal);
    elIva.innerText = formatearDinero(iva);
    elTotal.innerText = formatearDinero(total);

    if (elEnvio) {
        if (subtotal === 0) {
            elEnvio.innerHTML = formatearDinero(0);
        } else if (envio === 0) {
            elEnvio.innerHTML = `<span class="badge bg-success">¡Gratis!</span>`;
        } else {
            const faltante = CONFIG.montoEnvioGratis - subtotal;
            elEnvio.innerHTML = `${formatearDinero(envio)} <br> <small class="text-muted" style="font-size:10px;">Agrega ${formatearDinero(faltante)} para envío gratis</small>`;
        }
    }
}

// ================= UTILIDADES =================

/**
 * Guarda en LocalStorage y refresca la UI.
 */
function guardarYActualizar() {
    localStorage.setItem('carritoGlowy', JSON.stringify(carrito));
    actualizarBadgeCarrito();
    renderizarCarrito();
}

// ==========================================
// PROCESAMIENTO DE COMPRA REAL
// ==========================================

async function procesarCompra() {
    // 1. Verificamos que el carrito no esté vacío
    if (carrito.length === 0) {
        Swal.fire({
            icon: 'warning',
            title: 'Carrito Vacío',
            text: '¡Agrega algunos productos Derma-Tech antes de ir a pagar!',
            background: 'var(--glass-bg)',
            color: 'var(--text-dark)'
        });
        return;
    }

    // 2. Verificamos que el usuario haya iniciado sesión
    const usuarioStr = localStorage.getItem('glumyUsuario');
    if (!usuarioStr) {
        Swal.fire({
            icon: 'info',
            title: '¡Alto ahí!',
            text: 'Para realizar tu compra, por favor inicia sesión o regístrate primero.',
            background: 'var(--glass-bg)',
            color: 'var(--text-dark)',
            confirmButtonText: 'Ir a Inicio de Sesión'
        }).then(() => {
            // Si no está en el index, lo mandamos allá para que se loguee
            window.location.href = "index.html"; 
        });
        return;
    }

    const usuario = JSON.parse(usuarioStr);
    
    // Asegurarnos de que precio y cantidad sean números decimales y enteros
    const total = carrito.reduce((acc, item) => acc + (parseFloat(item.precio) * parseInt(item.cantidad)), 0);

    // 4. Enviamos la orden al Backend
    try {
        Swal.fire({
            title: 'Procesando pago...',
            text: 'Conectando con el servidor seguro',
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });

        const respuesta = await fetch('http://localhost:3000/api/pedidos', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                usuario_id: usuario.id,
                total: total
            })
        });

        const data = await respuesta.json();

        if (respuesta.ok) {
            Swal.fire({
                icon: 'success',
                title: '¡Compra Exitosa!',
                text: data.message,
                background: 'var(--glass-bg)',
                color: 'var(--text-dark)'
            });
            
            // 5. Vaciamos el carrito localmente
            carrito = [];
            guardarCarrito(); // Guarda el carrito vacío en localStorage
            renderizarCarrito(); // Actualiza la vista (asegúrate de que el nombre de tu función coincida)
        } else {
            Swal.fire('Error', data.error, 'error');
        }
    } catch (error) {
        console.error("Error al procesar:", error);
        Swal.fire('Error', 'Hubo un problema de conexión al procesar tu pago.', 'error');
    }
}

/**
 * Procesa el formulario de checkout una vez llenos los datos.
 */
function procesarPagoFinal(event) {
    // Evita que la página se recargue al enviar el formulario
    event.preventDefault();

    // Cierra el modal de Bootstrap
    const modalPagoEl = document.getElementById('modalPago');
    const modalPago = bootstrap.Modal.getInstance(modalPagoEl);
    modalPago.hide();

    const nombre = document.getElementById('checkoutNombre').value.trim();
    const email = document.getElementById('checkoutEmail').value.trim();
    const direccion = document.getElementById('checkoutDireccion').value.trim();
    const ciudad = document.getElementById('checkoutCiudad').value.trim();
    const codigoPostal = document.getElementById('checkoutPostal').value.trim();

    if (!nombre || !email || !direccion || !ciudad || !codigoPostal) {
        Swal.fire({ icon: 'error', title: 'Faltan datos', text: 'Completa los datos de envío antes de pagar.', background: 'var(--bg-card)' });
        return;
    }

    const subtotal = carrito.reduce((acc, prod) => acc + (prod.precio * prod.cantidad), 0);
    const iva = subtotal * CONFIG.tasaIva;
    const envio = (subtotal > 0 && subtotal < CONFIG.montoEnvioGratis) ? CONFIG.costoEnvioBase : 0;
    const total = subtotal + iva + envio;

    Swal.fire({
        title: 'Procesando tu pago...',
        html: 'Conectando con la pasarela bancaria encriptada de <b>Glowy Care</b>.',
        allowOutsideClick: false,
        didOpen: () => { 
            Swal.showLoading();
        },
        background: 'var(--glass-bg)',
        color: 'var(--text-dark)'
    });

    fetch('/api/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            cliente: { nombre, email, direccion, ciudad, codigoPostal },
            items: carrito,
            total
        })
    })
        .then(async response => {
            const result = await response.json();
            if (!response.ok) {
                throw new Error(result.error || 'No se pudo procesar la orden.');
            }
            carrito = [];
            localStorage.setItem('carritoGlowy', JSON.stringify(carrito));
            actualizarBadgeCarrito();
            renderizarCarrito();
            Swal.fire({
                icon: 'success',
                title: '¡Pago Exitoso!',
                text: result.message || 'Tu pedido ha sido confirmado. Gracias por comprar en GLUmy Care.',
                confirmButtonColor: 'var(--accent)',
                confirmButtonText: 'Volver al Inicio',
                background: 'var(--bg-card)',
                color: 'var(--text-dark)'
            }).then(() => {
                window.location.href = 'index.html';
            });
        })
        .catch(error => {
            Swal.fire({ icon: 'error', title: 'Error', text: error.message || 'Intenta nuevamente más tarde.', background: 'var(--bg-card)' });
        });
}

// Evento que se dispara al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    actualizarBadgeCarrito();
    renderizarCarrito();
});