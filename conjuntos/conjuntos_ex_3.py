# =========================================================
# EXAMEN 3 - RECURSIVIDAD + CONJUNTOS (RESUELTO)
# =========================================================

# -------------------------------
# 🔹 CLASE NODO
# -------------------------------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# -------------------------------
# 🔹 CLASE CONJUNTO
# -------------------------------
class Conjunto:
    def __init__(self):
        self.cabeza = None

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if not self.pertenece(x):
            nuevo = Nodo(x)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("{" + ", ".join(map(str, elementos)) + "}")


# =========================================================
# 🔹 PUNTO 1: DIFERENCIA RECURSIVA (A - B)
# =========================================================

def diferencia_rec(nodo, B, resultado):
    if nodo is None:
        return

    if not B.pertenece(nodo.dato):
        resultado.agregar(nodo.dato)

    diferencia_rec(nodo.siguiente, B, resultado)


def diferencia(A, B):
    resultado = Conjunto()
    diferencia_rec(A.cabeza, B, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 2: ELEMENTOS EN AL MENOS DOS CONJUNTOS
# =========================================================

def contar_en_conjuntos(x, A, B, C):
    count = 0
    if A.pertenece(x): count += 1
    if B.pertenece(x): count += 1
    if C.pertenece(x): count += 1
    return count


def al_menos_dos(A, B, C):
    resultado = Conjunto()

    # unión manual
    def recorrer(nodo):
        if nodo is None:
            return
        
        if contar_en_conjuntos(nodo.dato, A, B, C) >= 2:
            resultado.agregar(nodo.dato)

        recorrer(nodo.siguiente)

    recorrer(A.cabeza)
    recorrer(B.cabeza)
    recorrer(C.cabeza)

    return resultado


# =========================================================
# 🔹 PUNTO 3: ELIMINAR POR CONDICIÓN (RECURSIVO)
# =========================================================

# Ejemplo: eliminar números menores a un valor

def eliminar_rec(nodo, condicion):
    if nodo is None:
        return None

    if condicion(nodo.dato):
        return eliminar_rec(nodo.siguiente, condicion)

    nodo.siguiente = eliminar_rec(nodo.siguiente, condicion)
    return nodo


def eliminar_por_condicion(conjunto, condicion):
    conjunto.cabeza = eliminar_rec(conjunto.cabeza, condicion)


# =========================================================
# 🔹 PUNTO 4: ORDENAR CONJUNTO
# =========================================================

def ordenar_conjunto(conjunto):
    lista = []

    # pasar a lista
    actual = conjunto.cabeza
    while actual:
        lista.append(actual.dato)
        actual = actual.siguiente

    lista.sort()

    nuevo = Conjunto()
    for x in lista:
        nuevo.agregar(x)

    return nuevo


# =========================================================
# 🔹 PUNTO 5: CARDINALIDAD RECURSIVA
# =========================================================

def cardinalidad_rec(nodo):
    if nodo is None:
        return 0
    return 1 + cardinalidad_rec(nodo.siguiente)


# =========================================================
# 🔹 PRUEBAS
# =========================================================

if __name__ == "__main__":
    A = Conjunto()
    B = Conjunto()
    C = Conjunto()

    # Ejemplo con números
    for x in [1, 2, 3, 4, 5]:
        A.agregar(x)

    for x in [3, 4, 5, 6]:
        B.agregar(x)

    for x in [5, 6, 7]:
        C.agregar(x)

    print("A:")
    A.mostrar()

    print("B:")
    B.mostrar()

    print("C:")
    C.mostrar()

    print("\nDIFERENCIA A - B:")
    diferencia(A, B).mostrar()

    print("\nELEMENTOS EN AL MENOS DOS:")
    al_menos_dos(A, B, C).mostrar()

    print("\nELIMINAR < 4 EN A:")
    eliminar_por_condicion(A, lambda x: x < 4)
    A.mostrar()

    print("\nORDENAR B:")
    ordenar_conjunto(B).mostrar()

    print("\nCARDINALIDAD DE C:")
    print(cardinalidad_rec(C.cabeza))
