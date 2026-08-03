// ==========================================
// CONFIGURACIÓN DE AUTENTICACIÓN
// ==========================================
const API_URL = 'http://localhost:3000/api';

/**
 * Alterna entre la vista de Login y Registro en el Modal
 */
function toggleAuth(vista) {
    const formLogin = document.getElementById('form-login');
    const formRegistro = document.getElementById('form-registro');
    const title = document.getElementById('authModalTitle');

    if (vista === 'registro') {
        formLogin.classList.add('d-none');
        formRegistro.classList.remove('d-none');
        title.innerText = 'Crear Cuenta en GLUmy Care';
    } else {
        formRegistro.classList.add('d-none');
        formLogin.classList.remove('d-none');
        title.innerText = 'Bienvenido a GLUmy Care';
    }
}

/**
 * Procesa el formulario de Inicio de Sesión
 */
async function procesarLogin(event) {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    try {
        const respuesta = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await respuesta.json();

        if (respuesta.ok) {
            localStorage.setItem('glumyToken', data.token);
            localStorage.setItem('glumyUsuario', JSON.stringify(data.usuario));
            
            // Cerrar el modal
            const modalEl = document.getElementById('modalAuth');
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();

            Swal.fire({
                icon: 'success',
                title: `¡Hola, ${data.usuario.nombre}!`,
                text: 'Inicio de sesión exitoso.',
                background: 'var(--glass-bg)',
                color: 'var(--text-dark)',
                timer: 2000,
                showConfirmButton: false
            }).then(() => {
                if (data.usuario.rol === 'admin') {
                    window.location.href = "admin.html"; // Redirigir al panel de control
                } else {
                    window.location.reload(); // Recargar para actualizar la Navbar
                }
            });
        } else {
            Swal.fire('Error', data.error, 'error');
        }
    } catch (error) {
        Swal.fire('Error', 'No se pudo conectar con el servidor', 'error');
    }
}

/**
 * Procesa el formulario de Registro Nuevo
 */
async function procesarRegistro(event) {
    event.preventDefault();
    const nombre = document.getElementById('reg-nombre').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;

    try {
        const respuesta = await fetch(`${API_URL}/registro`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, email, password })
        });

        const data = await respuesta.json();

        if (respuesta.ok) {
            Swal.fire('¡Cuenta Creada!', 'Ahora puedes iniciar sesión con tus credenciales.', 'success');
            toggleAuth('login'); // Volver a la vista de login
        } else {
            Swal.fire('Error', data.error, 'error');
        }
    } catch (error) {
        Swal.fire('Error', 'No se pudo conectar con el servidor', 'error');
    }
}

/**
 * Verifica si hay una sesión activa y actualiza la Navbar
 */
function verificarSesion() {
    const usuario = JSON.parse(localStorage.getItem('glumyUsuario'));
    const authContainer = document.getElementById('auth-container');
    
    if (usuario && authContainer) {
        let adminLink = usuario.rol === 'admin' ? `<li><a class="dropdown-item text-accent" href="admin.html"><i class="bi bi-speedometer2"></i> Panel Admin</a></li>` : '';
        
        authContainer.innerHTML = `
            <div class="dropdown">
                <button class="btn btn-outline-accent rounded-pill px-3 py-2 btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown">
                    <i class="bi bi-person-circle"></i> ${usuario.nombre.split(' ')[0]}
                </button>
                <ul class="dropdown-menu dropdown-menu-end glass-card border-0" style="background: var(--glass-bg);">
                    ${adminLink}
                    <li><a class="dropdown-item text-danger" href="#" onclick="logout()"><i class="bi bi-box-arrow-right"></i> Cerrar Sesión</a></li>
                </ul>
            </div>
        `;
    }
}

function logout() {
    localStorage.removeItem('glumyToken');
    localStorage.removeItem('glumyUsuario');
    window.location.reload();
}

// Ejecutar verificación al cargar la página
document.addEventListener('DOMContentLoaded', verificarSesion);