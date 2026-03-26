# =========================================================
# EXAMEN 1 - RECURSIVIDAD + CONJUNTOS (RESUELTO)
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
        print("{", ", ".join(elementos), "}")


# =========================================================
# 🔹 PUNTO 2: UNIÓN RECURSIVA
# =========================================================

def union_recursiva(nodo, resultado):
    if nodo is None:
        return
    resultado.agregar(nodo.dato)
    union_recursiva(nodo.siguiente, resultado)


def union(A, B):
    resultado = Conjunto()
    union_recursiva(A.cabeza, resultado)
    union_recursiva(B.cabeza, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 3: INTERSECCIÓN RECURSIVA
# =========================================================

def interseccion_recursiva(nodo, B, resultado):
    if nodo is None:
        return

    if B.pertenece(nodo.dato):
        resultado.agregar(nodo.dato)

    interseccion_recursiva(nodo.siguiente, B, resultado)


def interseccion(A, B):
    resultado = Conjunto()
    interseccion_recursiva(A.cabeza, B, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 4: EXACTAMENTE EN DOS CONJUNTOS
# =========================================================

def contar_en_conjuntos(x, A, B, C):
    count = 0
    if A.pertenece(x):
        count += 1
    if B.pertenece(x):
        count += 1
    if C.pertenece(x):
        count += 1
    return count


def exactamente_dos(A, B, C):
    resultado = Conjunto()

    # unión de todos
    todos = union(A, union(B, C))

    actual = todos.cabeza
    while actual:
        if contar_en_conjuntos(actual.dato, A, B, C) == 2:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


# =========================================================
# 🔹 PUNTO 5: FILTRO RECURSIVO
# =========================================================

def filtrar_recursivo(nodo, resultado):
    if nodo is None:
        return

    if len(nodo.dato) > 4:
        resultado.agregar(nodo.dato)

    filtrar_recursivo(nodo.siguiente, resultado)


def filtrar(A):
    resultado = Conjunto()
    filtrar_recursivo(A.cabeza, resultado)
    return resultado


# =========================================================
# 🔹 PRUEBAS
# =========================================================

if __name__ == "__main__":
    A = Conjunto()
    B = Conjunto()
    C = Conjunto()

    # Agregar datos
    for x in ["Ana", "Luis", "Pedro", "Sofía"]:
        A.agregar(x)

    for x in ["Sofía", "Carlos", "Luis"]:
        B.agregar(x)

    for x in ["Luis", "Pedro", "Camila"]:
        C.agregar(x)

    print("A:")
    A.mostrar()

    print("B:")
    B.mostrar()

    print("C:")
    C.mostrar()

    print("\nUNIÓN A ∪ B:")
    union(A, B).mostrar()

    print("\nINTERSECCIÓN A ∩ B:")
    interseccion(A, B).mostrar()

    print("\nELEMENTOS EN EXACTAMENTE DOS:")
    exactamente_dos(A, B, C).mostrar()

    print("\nFILTRADOS (>4 letras en A):")
    filtrar(A).mostrar()
