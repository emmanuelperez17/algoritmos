"""📚 Sistema de Gestión de Libros (Lista Simple + Recursividad)

Incluye:

✅ Lista simplemente enlazada

✅ Insertar ordenado por título

✅ Buscar libro

✅ Eliminar libro

✅ Método recursivo (contar libros)

✅ Método recursivo (mostrar inverso)"""

class NodoLibro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.siguiente = None
class Biblioteca:
    def __init__(self):
        self.cabeza = None

    # ═══════════════════════════════
    # 1️⃣ Insertar ordenado por título
    # ═══════════════════════════════
    def insertar(self, titulo, autor, anio):
        nuevo = NodoLibro(titulo, autor, anio)

        # Caso lista vacía o va al inicio
        if self.cabeza is None or titulo.lower() < self.cabeza.titulo.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.titulo.lower() < titulo.lower():
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    # ═══════════════════════════════
    # 2️⃣ Buscar libro
    # ═══════════════════════════════
    def buscar(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.titulo.lower() == titulo.lower():
                return actual
            actual = actual.siguiente
        return None

    # ═══════════════════════════════
    # 3️⃣ Eliminar libro
    # ═══════════════════════════════
    def eliminar(self, titulo):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        # Caso eliminar cabeza
        if self.cabeza.titulo.lower() == titulo.lower():
            self.cabeza = self.cabeza.siguiente
            print("Libro eliminado.")
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual:
            if actual.titulo.lower() == titulo.lower():
                anterior.siguiente = actual.siguiente
                print("Libro eliminado.")
                return
            anterior = actual
            actual = actual.siguiente

        print("Libro no encontrado.")

    # ═══════════════════════════════
    # 4️⃣ Contar libros (RECURSIVO)
    # ═══════════════════════════════
    def contar(self):
        return self._contar_rec(self.cabeza)

    def _contar_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_rec(nodo.siguiente)

    # ═══════════════════════════════
    # 5️⃣ Mostrar lista normal
    # ═══════════════════════════════
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"- {actual.titulo} | {actual.autor} | {actual.anio}")
            actual = actual.siguiente

    # ═══════════════════════════════
    # 6️⃣ Mostrar en orden inverso (RECURSIVO)
    # ═══════════════════════════════
    def mostrar_inverso(self):
        self._mostrar_inverso_rec(self.cabeza)

    def _mostrar_inverso_rec(self, nodo):
        if nodo is None:
            return
        self._mostrar_inverso_rec(nodo.siguiente)
        print(f"- {nodo.titulo} | {nodo.autor} | {nodo.anio}")

if __name__ == "__main__":
    print("=" * 50)
    print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 50)

    biblio = Biblioteca()

    biblio.insertar("Clean Code", "Robert C. Martin", 2008)
    biblio.insertar("Estructuras de Datos", "Mark Allen Weiss", 2014)
    biblio.insertar("Algoritmos", "Thomas H. Cormen", 2009)

    print("\n📚 Lista ordenada:")
    biblio.mostrar()

    print("\n🔎 Buscando 'Clean Code':")
    libro = biblio.buscar("Clean Code")
    if libro:
        print("Encontrado:", libro.titulo)

    print("\n🔢 Total libros:", biblio.contar())

    print("\n📖 Lista en orden inverso:")
    biblio.mostrar_inverso()

    print("\n🗑 Eliminando 'Clean Code'")
    biblio.eliminar("Clean Code")

    print("\n📚 Lista final:")
    biblio.mostrar()
