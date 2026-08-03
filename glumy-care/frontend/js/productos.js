let productosDB = [];

const productosFallback = [
    { id: 1, nombre: "Clear Skin Gummies", precio: 29.99, desc: "Controla el acné desde adentro.", beneficios: "Reduce grasa", ingredientes: "Zinc, Vitamina A", img: "https://via.placeholder.com/300x300/F8BBD9/E91E63?text=Gomas+Acne", rating: 5, categoria: "acne" },
    { id: 2, nombre: "Glow Boost", precio: 24.99, desc: "Piel luminosa y radiante.", beneficios: "Hidratación profunda", ingredientes: "Colágeno, Vitamina C", img: "https://via.placeholder.com/300x300/FFF6FA/E91E63?text=Glow+Boost", rating: 4.8, categoria: "vitaminas" },
    { id: 3, nombre: "Detox Purity", precio: 27.50, desc: "Desintoxica y limpia poros.", beneficios: "Limpia impurezas", ingredientes: "Té verde, Biotina", img: "https://via.placeholder.com/300x300/FDEEF4/E91E63?text=Detox+Purity", rating: 4.9, categoria: "acne" }
];

async function cargarProductos() {
    try {
        const response = await fetch('/api/products');
        if (!response.ok) {
            throw new Error('No se pudo cargar la lista de productos');
        }
        productosDB = await response.json();
    } catch (error) {
        console.warn('Error al obtener productos desde el servidor, usando productos locales.', error);
        productosDB = productosFallback;
    }
    actualizarRenderizado();
}

function actualizarRenderizado() {
    const contenedorProductos = document.getElementById("productos-container");
    const buscador = document.getElementById("buscador");

    if (!contenedorProductos) return;

    renderizarProductos(productosDB);

    if (buscador) {
        buscador.addEventListener("input", (e) => {
            const query = e.target.value.toLowerCase();
            const filtrados = productosDB.filter(p => p.nombre.toLowerCase().includes(query));
            renderizarProductos(filtrados);
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {
    cargarProductos();
});

function renderizarProductos(productos) {
    const contenedor = document.getElementById("productos-container");
    if (!contenedor) return;
    contenedor.innerHTML = "";
    productos.forEach(prod => {
        contenedor.innerHTML += `
            <div class="col-lg-4 col-md-6 mb-4" data-aos="fade-up">
                <div class="card glass-card h-100 p-3">
                    <img src="${prod.img}" class="card-img-top rounded" alt="${prod.nombre}">
                    <div class="card-body text-center">
                        <h5 class="card-title">${prod.nombre}</h5>
                        <p class="text-muted small">${prod.desc || prod.descripcion}</p>
                        <h4 class="text-accent">$${prod.precio}</h4>
                        <div class="text-warning mb-3">
                            ${'★'.repeat(Math.floor(prod.rating || 0))}
                        </div>
                        <button class="btn btn-glowy w-100" onclick="agregarAlCarrito(${prod.id})">
                            <i class="bi bi-cart-plus"></i> Agregar al Carrito
                        </button>
                    </div>
                </div>
            </div>
        `;
    });
}