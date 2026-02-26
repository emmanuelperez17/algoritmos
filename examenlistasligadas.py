"""Insertar al final.

Eliminar todos los nodos que contengan un valor X (RECURSIVO).

Invertir la lista completamente (RECURSIVO).

Determinar si la lista es palíndromo (RECURSIVO).

Contar los elementos mayores que un valor dado (RECURSIVO)"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Lista:
    def __init__(self):
        self.cabeza = None

    # ═══════════════════════════════
    # 1️⃣ Insertar al final
    # ═══════════════════════════════
    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    # ═══════════════════════════════
    # Mostrar
    # ═══════════════════════════════
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # ═══════════════════════════════
    # 2️⃣ Eliminar valor X (RECURSIVO)
    # ═══════════════════════════════
    def eliminar_x(self, x):
        self.cabeza = self._eliminar_x_rec(self.cabeza, x)

    def _eliminar_x_rec(self, nodo, x):
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_x_rec(nodo.siguiente, x)

        if nodo.dato == x:
            return nodo.siguiente

        return nodo

    # ═══════════════════════════════
    # 3️⃣ Invertir lista (RECURSIVO)
    # ═══════════════════════════════
    def invertir(self):
        self.cabeza = self._invertir_rec(self.cabeza)

    def _invertir_rec(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return nodo

        nueva_cabeza = self._invertir_rec(nodo.siguiente)

        nodo.siguiente.siguiente = nodo
        nodo.siguiente = None

        return nueva_cabeza

    # ═══════════════════════════════
    # 4️⃣ Contar mayores que X (RECURSIVO)
    # ═══════════════════════════════
    def contar_mayores(self, x):
        return self._contar_mayores_rec(self.cabeza, x)

    def _contar_mayores_rec(self, nodo, x):
        if nodo is None:
            return 0

        if nodo.dato > x:
            return 1 + self._contar_mayores_rec(nodo.siguiente, x)

        return self._contar_mayores_rec(nodo.siguiente, x)

    # ═══════════════════════════════
    # 5️⃣ Verificar palíndromo (RECURSIVO)
    # ═══════════════════════════════
    def es_palindromo(self):
        self.aux = self.cabeza
        return self._palindromo_rec(self.cabeza)

    def _palindromo_rec(self, nodo):
        if nodo is None:
            return True

        if not self._palindromo_rec(nodo.siguiente):
            return False

        es_igual = (self.aux.dato == nodo.dato)
        self.aux = self.aux.siguiente

        return es_igual
if __name__ == "__main__":
    print("=" * 60)
    print("💀 EXAMEN - LISTA LIGADA + RECURSIVIDAD")
    print("=" * 60)

    lista = Lista()

    datos = [1, 2, 3, 2, 1]
    for d in datos:
        lista.insertar(d)

    print("\nLista original:")
    lista.mostrar()

    print("\n¿Es palíndromo?")
    print(lista.es_palindromo())

    print("\nMayores que 1:")
    print(lista.contar_mayores(1))

    print("\nEliminando 2 (recursivo):")
    lista.eliminar_x(2)
    lista.mostrar()

    print("\nInvirtiendo lista (recursivo):")
    lista.invertir()
    lista.mostrar()
