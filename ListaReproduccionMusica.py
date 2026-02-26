"""1️⃣ Lista Doble – Sistema de Reproducción Musical
🎵 Contexto:

Implementar un reproductor donde el usuario puede:

Avanzar

Retroceder

Eliminar canciones

Insertar después de la actual

🔹 Complejidad:

Uso de anterior y siguiente

Eliminación en medio

Mantener referencias correctas

Posible método recursivo para contar o buscar

👉 Dificultad: Media-Alta"""

class NodoCancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # en segundos
        self.siguiente = None
        self.anterior = None
class Reproductor:
    def __init__(self):
        self.cabeza = None
        self.actual = None  # canción que está sonando

    # ═══════════════════════════════
    # 1️⃣ Agregar canción al final
    # ═══════════════════════════════
    def agregar(self, titulo, artista, duracion):
        nuevo = NodoCancion(titulo, artista, duracion)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = nuevo
            return

        temp = self.cabeza
        while temp.siguiente:
            temp = temp.siguiente

        temp.siguiente = nuevo
        nuevo.anterior = temp

    # ═══════════════════════════════
    # 2️⃣ Avanzar canción
    # ═══════════════════════════════
    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay siguiente canción.")

    # ═══════════════════════════════
    # 3️⃣ Retroceder canción
    # ═══════════════════════════════
    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("No hay canción anterior.")

    # ═══════════════════════════════
    # 4️⃣ Eliminar canción por título
    # ═══════════════════════════════
    def eliminar(self, titulo):
        temp = self.cabeza

        while temp:
            if temp.titulo == titulo:

                # Caso 1: es la cabeza
                if temp.anterior is None:
                    self.cabeza = temp.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None

                else:
                    temp.anterior.siguiente = temp.siguiente

                # Caso 2: no es el último
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior

                # Ajustar actual si se elimina
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior

                print(f"Canción '{titulo}' eliminada.")
                return

            temp = temp.siguiente

        print("Canción no encontrada.")

    # ═══════════════════════════════
    # 5️⃣ Contar canciones (RECURSIVO)
    # ═══════════════════════════════
    def contar(self):
        return self._contar_rec(self.cabeza)

    def _contar_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_rec(nodo.siguiente)

    # ═══════════════════════════════
    # Mostrar lista completa
    # ═══════════════════════════════
    def mostrar(self):
        temp = self.cabeza
        while temp:
            actual = " (SONANDO)" if temp == self.actual else ""
            print(f"- {temp.titulo} | {temp.artista} | {temp.duracion}s{actual}")
            temp = temp.siguiente
if __name__ == "__main__":
    print("=" * 50)
    print("   SISTEMA DE REPRODUCCIÓN MUSICAL")
    print("=" * 50)

    player = Reproductor()

    player.agregar("Shape of You", "Ed Sheeran", 240)
    player.agregar("Blinding Lights", "The Weeknd", 200)
    player.agregar("Levitating", "Dua Lipa", 210)

    print("\n🎵 Lista de canciones:")
    player.mostrar()

    print("\n⏭ Avanzando canción...")
    player.siguiente()
    player.mostrar()

    print("\n⏮ Retrocediendo canción...")
    player.anterior()
    player.mostrar()

    print("\n🗑 Eliminando 'Blinding Lights'...")
    player.eliminar("Blinding Lights")
    player.mostrar()

    print("\n🔢 Total canciones:", player.contar())
