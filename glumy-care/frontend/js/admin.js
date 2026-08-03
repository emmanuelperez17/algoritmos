const API_URL = 'http://localhost:3000/api';

// 1. ================= SEGURIDAD DE RUTA =================
function verificarAccesoAdmin() {
    const usuario = JSON.parse(localStorage.getItem('glumyUsuario'));
    const token = localStorage.getItem('glumyToken');

    // Si no hay usuario, no hay token, o no es admin, ¡AFUERA!
    if (!usuario || !token || usuario.rol !== 'admin') {
        Swal.fire({
            icon: 'error',
            title: 'Acceso Denegado',
            text: 'No tienes permisos de Administrador para ver esta página.',
            allowOutsideClick: false,
            showConfirmButton: false,
            timer: 2000
        }).then(() => {
            window.location.href = "index.html";
        });
        return false;
    }

    // Si es admin, mostramos su nombre en el Header
    document.getElementById('admin-name').innerHTML = `<i class="bi bi-person-check-fill text-accent"></i> ${usuario.nombre}`;
    return true;
}

// 2. ================= CARGAR PRODUCTOS =================
async function cargarProductosAdmin() {
    try {
        const respuesta = await fetch(`${API_URL}/productos`);
        const productos = await respuesta.json();
        
        const tbody = document.getElementById('tabla-admin-productos');
        tbody.innerHTML = ''; // Limpiar mensaje de "cargando"

        productos.forEach(prod => {
            tbody.innerHTML += `
                <tr>
                    <td class="fw-bold">#${prod.id}</td>
                    <td><img src="${prod.imagen}" alt="${prod.nombre}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;"></td>
                    <td>${prod.nombre}</td>
                    <td class="text-accent fw-bold">$${prod.precio}</td>
                    <td>
                        <span class="badge ${prod.stock > 10 ? 'bg-success' : 'bg-danger'}">${prod.stock}</span>
                    </td>
                    <td>
                        <button class="btn btn-sm btn-outline-primary me-1" title="Editar" onclick="editarProducto(${prod.id})"><i class="bi bi-pencil"></i></button>
                        <button class="btn btn-sm btn-outline-danger" title="Eliminar" onclick="eliminarProducto(${prod.id})"><i class="bi bi-trash"></i></button>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Error al cargar productos:", error);
        Swal.fire('Error', 'No se pudieron cargar los productos.', 'error');
    }
}

// 3. ================= CERRAR SESIÓN =================
function logout() {
    localStorage.removeItem('glumyToken');
    localStorage.removeItem('glumyUsuario');
    window.location.href = "index.html";
}

// ================= INICIALIZACIÓN =================
document.addEventListener('DOMContentLoaded', () => {
    // Primero verificamos que sea el Admin
    if (verificarAccesoAdmin()) {
        // Si todo está bien, cargamos los datos
        cargarProductosAdmin();
    }
});

// ==================================================
// FUNCIONES CRUD DE PRODUCTOS (Crear, Editar, Borrar)
// ==================================================

const modalProducto = new bootstrap.Modal(document.getElementById('modalProducto'));

// 1. Abrir modal vacío para Crear
function abrirModalProducto() {
    document.getElementById('form-producto').reset();
    document.getElementById('prod-id').value = '';
    document.getElementById('modalProductoTitle').innerText = 'Nuevo Producto Derma-Tech';
    modalProducto.show();
}

// 2. Guardar (Sirve tanto para Crear como para Editar)
async function guardarProducto(event) {
    event.preventDefault();
    
    const id = document.getElementById('prod-id').value;
    const productoData = {
        nombre: document.getElementById('prod-nombre').value,
        precio: document.getElementById('prod-precio').value,
        stock: document.getElementById('prod-stock').value,
        imagen: document.getElementById('prod-imagen').value,
        etiqueta: document.getElementById('prod-etiqueta').value,
        descripcion: document.getElementById('prod-descripcion').value
    };

    const url = id ? `${API_URL}/productos/${id}` : `${API_URL}/productos`;
    const method = id ? 'PUT' : 'POST';

    try {
        const respuesta = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(productoData)
        });

        if (respuesta.ok) {
            Swal.fire('¡Éxito!', 'El producto ha sido guardado.', 'success');
            modalProducto.hide();
            cargarProductosAdmin(); // Recargar la tabla
        }
    } catch (error) {
        Swal.fire('Error', 'No se pudo guardar el producto.', 'error');
    }
}

// 3. Eliminar Producto
async function eliminarProducto(id) {
    const confirmacion = await Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminar'
    });

    if (confirmacion.isConfirmed) {
        try {
            await fetch(`${API_URL}/productos/${id}`, { method: 'DELETE' });
            Swal.fire('Eliminado', 'El producto ha sido borrado.', 'success');
            cargarProductosAdmin(); // Recargar la tabla
        } catch (error) {
            Swal.fire('Error', 'No se pudo eliminar.', 'error');
        }
    }
}

// 4. Editar Producto (Llenar el modal)
async function editarProducto(id) {
    try {
        const respuesta = await fetch(`${API_URL}/productos`);
        const productos = await respuesta.json();
        const prod = productos.find(p => p.id === id);

        if (prod) {
            // Llenamos el formulario con los datos actuales
            document.getElementById('prod-id').value = prod.id;
            document.getElementById('prod-nombre').value = prod.nombre;
            document.getElementById('prod-precio').value = prod.precio;
            document.getElementById('prod-stock').value = prod.stock;
            document.getElementById('prod-imagen').value = prod.imagen;
            document.getElementById('prod-etiqueta').value = prod.etiqueta || '';
            document.getElementById('prod-descripcion').value = prod.descripcion || '';

            // Cambiamos el título y mostramos el modal
            document.getElementById('modalProductoTitle').innerText = 'Editar Producto Derma-Tech';
            modalProducto.show();
        }
    } catch (error) {
        Swal.fire('Error', 'No se pudo cargar la información.', 'error');
    }
}