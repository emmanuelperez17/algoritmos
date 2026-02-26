"""✅ Lista simplemente enlazada

✅ Manipulación real de punteros

✅ Separación en pares e impares

✅ Inversión SOLO de pares (recursiva)

✅ Conteo recursivo

✅ Reinserción alternada

✅ Casos límite bien manejados"""

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
    # Mostrar lista
    # ═══════════════════════════════
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # ═══════════════════════════════
    # 2️⃣ Separar en pares e impares
    # ═══════════════════════════════
    def separar(self):
        pares = Lista()
        impares = Lista()

        actual = self.cabeza
        while actual:
            if actual.dato % 2 == 0:
                pares.insertar(actual.dato)
            else:
                impares.insertar(actual.dato)
            actual = actual.siguiente

        return pares, impares

    # ═══════════════════════════════
    # 3️⃣ Invertir lista (RECURSIVO)
    # ═══════════════════════════════
    def invertir_recursivo(self):
        self.cabeza = self._invertir_rec(self.cabeza)

    def _invertir_rec(self, nodo):
        # Caso base
        if nodo is None or nodo.siguiente is None:
            return nodo

        nueva_cabeza = self._invertir_rec(nodo.siguiente)

        nodo.siguiente.siguiente = nodo
        nodo.siguiente = None

        return nueva_cabeza

    # ═══════════════════════════════
    # 4️⃣ Contar elementos (RECURSIVO)
    # ═══════════════════════════════
    def contar(self):
        return self._contar_rec(self.cabeza)

    def _contar_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_rec(nodo.siguiente)

    # ═══════════════════════════════
    # 5️⃣ Reintegration alternada
    # ═══════════════════════════════
    @staticmethod
    def alternar(lista1, lista2):
        resultado = Lista()

        n1 = lista1.cabeza
        n2 = lista2.cabeza

        while n1 or n2:
            if n1:
                resultado.insertar(n1.dato)
                n1 = n1.siguiente
            if n2:
                resultado.insertar(n2.dato)
                n2 = n2.siguiente

        return resultado
if __name__ == "__main__":
    print("=" * 60)
    print("        💀 EXAMEN NIVEL DIOS - LISTA SIMPLE")
    print("=" * 60)

    lista = Lista()

    datos = [7, 4, 9, 2, 8, 1, 6]
    for d in datos:
        lista.insertar(d)

    print("\n📌 Lista original:")
    lista.mostrar()

    # Separar
    pares, impares = lista.separar()

    print("\n🔹 Pares:")
    pares.mostrar()

    print("\n🔹 Impares:")
    impares.mostrar()

    # Invertir SOLO pares
    print("\n🔄 Invirtiendo pares (recursivo)...")
    pares.invertir_recursivo()
    pares.mostrar()

    # Reintegrar alternando
    print("\n🔀 Alternando pares invertidos e impares:")
    final = Lista.alternar(pares, impares)
    final.mostrar()

    print("\n📊 Total elementos finales (recursivo):", final.contar())
