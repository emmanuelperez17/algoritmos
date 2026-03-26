# =========================================================
# EXAMEN 2 - RECURSIVIDAD + CONJUNTOS (RESUELTO)
# =========================================================

# -------------------------------
# 🔹 CLASE NODO
# -------------------------------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# -------------------------------
# 🔹 CLASE CONJUNTO (ORDENADO)
# -------------------------------
class Conjunto:
    def __init__(self):
        self.cabeza = None

    # --------------------------------
    # 🔹 PERTENECE
    # --------------------------------
    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    # --------------------------------
    # 🔹 AGREGAR ORDENADO (RECURSIVO)
    # --------------------------------
    def agregar(self, x):
        self.cabeza = self._agregar_rec(self.cabeza, x)

    def _agregar_rec(self, nodo, x):
        if nodo is None:
            return Nodo(x)

        if nodo.dato == x:
            return nodo  # no duplicados

        if x < nodo.dato:
            nuevo = Nodo(x)
            nuevo.siguiente = nodo
            return nuevo

        nodo.siguiente = self._agregar_rec(nodo.siguiente, x)
        return nodo

    # --------------------------------
    # 🔹 MOSTRAR
    # --------------------------------
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("{", ", ".join(elementos), "}")


# =========================================================
# 🔹 PUNTO 2: SUBCONJUNTO (RECURSIVO)
# =========================================================

def es_subconjunto_rec(nodo, B):
    if nodo is None:
        return True

    if not B.pertenece(nodo.dato):
        return False

    return es_subconjunto_rec(nodo.siguiente, B)


def es_subconjunto(A, B):
    return es_subconjunto_rec(A.cabeza, B)


# =========================================================
# 🔹 PUNTO 3: INTERSECCIÓN DE MUCHOS CONJUNTOS
# =========================================================

def interseccion_rec(nodo, B, C, resultado):
    if nodo is None:
        return

    if B.pertenece(nodo.dato) and C.pertenece(nodo.dato):
        resultado.agregar(nodo.dato)

    interseccion_rec(nodo.siguiente, B, C, resultado)


def interseccion_total(A, B, C):
    resultado = Conjunto()
    interseccion_rec(A.cabeza, B, C, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 4: CONTAR APARICIONES
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


def contar_apariciones(A, B, C):
    resultado = {}

    # recorrer unión manual
    def recorrer(nodo):
        if nodo is None:
            return

        resultado[nodo.dato] = contar_en_conjuntos(nodo.dato, A, B, C)
        recorrer(nodo.siguiente)

    # usar A como base
    recorrer(A.cabeza)
    recorrer(B.cabeza)
    recorrer(C.cabeza)

    return resultado


# =========================================================
# 🔹 PUNTO 5: ELIMINAR GLOBAL (RECURSIVO)
# =========================================================

def eliminar_rec(nodo, x):
    if nodo is None:
        return None

    if nodo.dato == x:
        return eliminar_rec(nodo.siguiente, x)

    nodo.siguiente = eliminar_rec(nodo.siguiente, x)
    return nodo


def eliminar_global(conjunto, x):
    conjunto.cabeza = eliminar_rec(conjunto.cabeza, x)


# =========================================================
# 🔹 PRUEBAS
# =========================================================

if __name__ == "__main__":
    A = Conjunto()
    B = Conjunto()
    C = Conjunto()

    # Insertar datos (ordenados automáticamente)
    for x in ["Luis", "Ana", "Pedro", "Carlos"]:
        A.agregar(x)

    for x in ["Pedro", "Carlos", "Sofía"]:
        B.agregar(x)

    for x in ["Carlos", "Luis", "Camila"]:
        C.agregar(x)

    print("A:")
    A.mostrar()

    print("B:")
    B.mostrar()

    print("C:")
    C.mostrar()

    print("\n¿A es subconjunto de B?")
    print(es_subconjunto(A, B))

    print("\nINTERSECCIÓN TOTAL (A ∩ B ∩ C):")
    interseccion_total(A, B, C).mostrar()

    print("\nCONTAR APARICIONES:")
    print(contar_apariciones(A, B, C))

    print("\nELIMINAR 'Carlos' de todos:")
    eliminar_global(A, "Carlos")
    eliminar_global(B, "Carlos")
    eliminar_global(C, "Carlos")

    print("A:")
    A.mostrar()
    print("B:")
    B.mostrar()
    print("C:")
    C.mostrar()
