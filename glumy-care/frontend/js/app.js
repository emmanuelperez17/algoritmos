document.addEventListener("DOMContentLoaded", () => {
    // Loader
    setTimeout(() => {
        document.getElementById('loader').style.display = 'none';
    }, 1500);

    // Inicializar AOS (Animaciones)
    AOS.init({ duration: 1000, once: true });

    // Navbar Glass Effect al hacer scroll
    window.addEventListener("scroll", () => {
        const navbar = document.querySelector(".navbar");
        if (window.scrollY > 50) {
            navbar.classList.add("glass");
        } else {
            navbar.classList.remove("glass");
        }
    });

    // Dark Mode Toggle
    const themeToggle = document.getElementById("themeToggle");
    const body = document.body;
    
    // Check LocalStorage
    if(localStorage.getItem('theme') === 'dark') {
        body.setAttribute('data-theme', 'dark');
        themeToggle.innerHTML = '<i class="bi bi-sun"></i>';
    }

    themeToggle.addEventListener("click", () => {
        if (body.getAttribute('data-theme') === 'dark') {
            body.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
            themeToggle.innerHTML = '<i class="bi bi-moon"></i>';
        } else {
            body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeToggle.innerHTML = '<i class="bi bi-sun"></i>';
        }
    });

    // Actualizar badge del carrito
    actualizarBadgeCarrito();
});

function actualizarBadgeCarrito() {
    const carrito = JSON.parse(localStorage.getItem('carritoGlowy')) || [];
    const totalItems = carrito.reduce((acc, item) => acc + item.cantidad, 0);
    const badge = document.getElementById('cart-badge');
    if(badge) badge.innerText = totalItems;
}