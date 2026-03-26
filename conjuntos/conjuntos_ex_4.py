# =========================================================
# EXAMEN 4 - RECURSIVIDAD + CONJUNTOS
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

        if actual is None:
            print("{ }")
            return

        print("{ ", end="")
        while actual:
            print(actual.dato, end="")
            if actual.siguiente:
                print(", ", end="")
            actual = actual.siguiente
        print(" }")


# =========================================================
# 🔹 PUNTO 1: DIFERENCIA SIMÉTRICA RECURSIVA
# (A - B) ∪ (B - A)
# =========================================================

def diferencia_rec(nodo, otro, resultado):
    if nodo is None:
        return

    if not otro.pertenece(nodo.dato):
        resultado.agregar(nodo.dato)

    diferencia_rec(nodo.siguiente, otro, resultado)


def diferencia_simetrica(A, B):
    resultado = Conjunto()

    diferencia_rec(A.cabeza, B, resultado)
    diferencia_rec(B.cabeza, A, resultado)

    return resultado


# =========================================================
# 🔹 PUNTO 2: USUARIOS EXCLUSIVOS (SOLO EN UNA RED)
# =========================================================

def exclusivos(A, B, C):
    resultado = Conjunto()

    def recorrer(nodo):
        if nodo is None:
            return

        count = 0
        if A.pertenece(nodo.dato): count += 1
        if B.pertenece(nodo.dato): count += 1
        if C.pertenece(nodo.dato): count += 1

        if count == 1:
            resultado.agregar(nodo.dato)

        recorrer(nodo.siguiente)

    recorrer(A.cabeza)
    recorrer(B.cabeza)
    recorrer(C.cabeza)

    return resultado


# =========================================================
# 🔹 PUNTO 3: USUARIOS EN TODOS MENOS UNA RED
# =========================================================

def todos_menos_uno(A, B, C):
    resultado = Conjunto()

    def recorrer(nodo):
        if nodo is None:
            return

        count = 0
        if A.pertenece(nodo.dato): count += 1
        if B.pertenece(nodo.dato): count += 1
        if C.pertenece(nodo.dato): count += 1

        if count == 2:
            resultado.agregar(nodo.dato)

        recorrer(nodo.siguiente)

    recorrer(A.cabeza)
    recorrer(B.cabeza)
    recorrer(C.cabeza)

    return resultado


# =========================================================
# 🔹 PUNTO 4: FILTRO RECURSIVO (CONTIENE LETRA)
# =========================================================

def filtrar_rec(nodo, letra, resultado):
    if nodo is None:
        return

    if letra.lower() in nodo.dato.lower():
        resultado.agregar(nodo.dato)

    filtrar_rec(nodo.siguiente, letra, resultado)


def filtrar(A, letra):
    resultado = Conjunto()
    filtrar_rec(A.cabeza, letra, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 5: VERIFICAR IGUALDAD
# =========================================================

def iguales_rec(nodo, otro):
    if nodo is None:
        return True

    if not otro.pertenece(nodo.dato):
        return False

    return iguales_rec(nodo.siguiente, otro)


def son_iguales(A, B):
    return iguales_rec(A.cabeza, B) and iguales_rec(B.cabeza, A)


# =========================================================
# 🔹 PRUEBAS
# =========================================================

if __name__ == "__main__":
    deportes = Conjunto()
    musica = Conjunto()
    noticias = Conjunto()

    # Datos de prueba
    for x in ["Ana", "Luis", "Carlos", "Pedro"]:
        deportes.agregar(x)

    for x in ["Carlos", "Pedro", "Sofía"]:
        musica.agregar(x)

    for x in ["Pedro", "Luis", "Camila"]:
        noticias.agregar(x)

    print("DEPORTES:")
    deportes.mostrar()

    print("MUSICA:")
    musica.mostrar()

    print("NOTICIAS:")
    noticias.mostrar()

    print("\nDIFERENCIA SIMÉTRICA (deportes vs musica):")
    diferencia_simetrica(deportes, musica).mostrar()

    print("\nUSUARIOS EXCLUSIVOS:")
    exclusivos(deportes, musica, noticias).mostrar()

    print("\nUSUARIOS EN TODOS MENOS UNA:")
    todos_menos_uno(deportes, musica, noticias).mostrar()

    print("\nFILTRAR (contienen 'a'):")
    filtrar(deportes, "a").mostrar()

    print("\n¿DEPORTES y MUSICA SON IGUALES?")
    print(son_iguales(deportes, musica))
