document.addEventListener("DOMContentLoaded", () => {
    const formContacto = document.getElementById("formContacto");
    if (formContacto) {
        formContacto.addEventListener("submit", async (e) => {
            e.preventDefault();

            const nombre = document.getElementById("nombre").value.trim();
            const apellido = document.getElementById("apellido").value.trim();
            const email = document.getElementById("email").value.trim();
            const telefono = document.getElementById("telefono").value.trim();
            const mensaje = document.getElementById("mensaje").value.trim();

            if (!nombre || !email || !mensaje) {
                Swal.fire({ icon: 'error', title: 'Oops...', text: 'Rellena los campos obligatorios.', background: 'var(--bg-card)' });
                return;
            }

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ nombre, apellido, email, telefono, mensaje })
                });

                const result = await response.json();
                if (!response.ok) {
                    throw new Error(result.error || 'No se pudo enviar el mensaje.');
                }

                Swal.fire({ icon: 'success', title: 'Mensaje enviado', text: result.message, background: 'var(--bg-card)' });
                formContacto.reset();
            } catch (error) {
                Swal.fire({ icon: 'error', title: 'Error', text: error.message || 'Intenta de nuevo más tarde.', background: 'var(--bg-card)' });
            }
        });
    }
});