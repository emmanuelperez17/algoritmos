"""🧠 CONTEXTO

Una plataforma educativa gestiona estudiantes inscritos en tres áreas:

📘 Programación (P)
🗄 Bases de Datos (B)
🌐 Redes (R)

Cada área se representa como un conjunto enlazado.

🔴 PUNTO 1 (1.0) – ESTRUCTURA

Implemente:

Clase Nodo
Clase Conjunto con:
agregar()
pertenece()
mostrar()
🔴 PUNTO 2 (1.0) – INTERSECCIÓN + DIFERENCIA

👉 Obtener los estudiantes que:

Están en Programación y Bases de Datos
PERO NO están en Redes

💡 Pista:

(P ∩ B) - R

🔴 PUNTO 3 (1.0) – EXACTAMENTE DOS CONJUNTOS

👉 Obtener los estudiantes que están en exactamente dos áreas

⚠️ No duplicar elementos

🔴 PUNTO 4 (1.0) – FILTRO RECURSIVO

👉 Obtener estudiantes que:

Empiezan con consonante
Y tienen más de 5 letras

⚠️ Obligatorio recursivo

🔴 PUNTO 5 (1.0) – ELIMINACIÓN RECURSIVA

👉 Eliminar de Programación los estudiantes que:

Tienen menos de 5 letras
O contienen la letra "e"
🔴 PUNTO 6 (1.0) – SUBCONJUNTO

👉 Verificar si:

B ⊆ P

🔴 PUNTO 7 (1.0) – IGUALDAD

👉 Verificar si:

P == R

🔴 PUNTO 8 (1.0) – DIFERENCIA SIMÉTRICA

👉 Obtener estudiantes que están en:

Programación o Redes
PERO NO en ambos
🔴 PUNTO 9 (1.0) – CARDINALIDAD RECURSIVA

👉 Contar cuántos estudiantes hay en Redes
👉 SIN usar contador de clase

🔴 PUNTO 10 (1.0) – CASO COMBINADO (🔥 IMPORTANTE)

👉 Obtener estudiantes que:

Están en al menos dos áreas
Y su nombre contiene la letra "a"
🧠 BONUS (Opcional +1)

👉 Rotar el conjunto P (primer elemento al final)"""


# =========================================================
# EXAMEN COMPLETO - CONJUNTOS + NODOS + RECURSIVIDAD
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
        self.inicio = None

    def pertenece(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, dato):
        if not self.pertenece(dato):
            nuevo = Nodo(dato)
            if self.inicio is None:
                self.inicio = nuevo
            else:
                actual = self.inicio
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo

    def mostrar(self):
        actual = self.inicio

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
# 🔹 PUNTO 2: (P ∩ B) - R
# =========================================================

def interseccion(P, B):
    resultado = Conjunto()
    actual = P.inicio

    while actual:
        if B.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


def diferencia(A, R):
    resultado = Conjunto()
    actual = A.inicio

    while actual:
        if not R.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


def punto2(P, B, R):
    temp = interseccion(P, B)
    return diferencia(temp, R)


# =========================================================
# 🔹 PUNTO 3: EXACTAMENTE DOS
# =========================================================

def contar(dato, P, B, R):
    c = 0
    if P.pertenece(dato): c += 1
    if B.pertenece(dato): c += 1
    if R.pertenece(dato): c += 1
    return c


def union(P, B, R):
    resultado = Conjunto()

    actual = P.inicio
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente

    actual = B.inicio
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente

    actual = R.inicio
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


def punto3(P, B, R):
    resultado = Conjunto()
    todos = union(P, B, R)

    actual = todos.inicio
    while actual:
        if contar(actual.dato, P, B, R) == 2:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


# =========================================================
# 🔹 PUNTO 4: FILTRO RECURSIVO
# consonante + longitud > 5
# =========================================================

def es_vocal(letra):
    return letra.lower() in "aeiou"


def filtro_rec(nodo, resultado):
    if nodo is None:
        return

    if not es_vocal(nodo.dato[0]) and len(nodo.dato) > 5:
        resultado.agregar(nodo.dato)

    filtro_rec(nodo.siguiente, resultado)


def punto4(P):
    resultado = Conjunto()
    filtro_rec(P.inicio, resultado)
    return resultado


# =========================================================
# 🔹 PUNTO 5: ELIMINACIÓN RECURSIVA
# =========================================================

def eliminar_rec(nodo):
    if nodo is None:
        return None

    condicion = len(nodo.dato) < 5 or "e" in nodo.dato.lower()

    if condicion:
        return eliminar_rec(nodo.siguiente)

    nodo.siguiente = eliminar_rec(nodo.siguiente)
    return nodo


def punto5(P):
    P.inicio = eliminar_rec(P.inicio)


# =========================================================
# 🔹 PUNTO 6: SUBCONJUNTO
# =========================================================

def subconjunto_rec(nodo, P):
    if nodo is None:
        return True
    if not P.pertenece(nodo.dato):
        return False
    return subconjunto_rec(nodo.siguiente, P)


def punto6(B, P):
    return subconjunto_rec(B.inicio, P)


# =========================================================
# 🔹 PUNTO 7: IGUALDAD
# =========================================================

def iguales_rec(nodo, otro):
    if nodo is None:
        return True
    if not otro.pertenece(nodo.dato):
        return False
    return iguales_rec(nodo.siguiente, otro)


def punto7(P, R):
    return iguales_rec(P.inicio, R) and iguales_rec(R.inicio, P)


# =========================================================
# 🔹 PUNTO 8: DIFERENCIA SIMÉTRICA
# =========================================================

def diferencia_simetrica(P, R):
    resultado = Conjunto()

    actual = P.inicio
    while actual:
        if not R.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    actual = R.inicio
    while actual:
        if not P.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


# =========================================================
# 🔹 PUNTO 9: CARDINALIDAD RECURSIVA
# =========================================================

def cardinalidad_rec(nodo):
    if nodo is None:
        return 0
    return 1 + cardinalidad_rec(nodo.siguiente)


# =========================================================
# 🔹 PUNTO 10: AL MENOS DOS + LETRA "a"
# =========================================================

def punto10(P, B, R):
    resultado = Conjunto()
    todos = union(P, B, R)

    actual = todos.inicio
    while actual:
        if contar(actual.dato, P, B, R) >= 2 and "a" in actual.dato.lower():
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


# =========================================================
# 🔹 PRUEBA
# =========================================================

if __name__ == "__main__":
    P = Conjunto()
    B = Conjunto()
    R = Conjunto()

    for x in ["Ana", "Luis", "Carlos", "Andres"]:
        P.agregar(x)

    for x in ["Carlos", "Pedro", "Luis"]:
        B.agregar(x)

    for x in ["Luis", "Camila", "Pedro"]:
        R.agregar(x)

    print("PUNTO 2:")
    punto2(P, B, R).mostrar()

    print("\nPUNTO 3:")
    punto3(P, B, R).mostrar()

    print("\nPUNTO 4:")
    punto4(P).mostrar()

    print("\nPUNTO 5:")
    punto5(P)
    P.mostrar()

    print("\nPUNTO 6:")
    print(punto6(B, P))

    print("\nPUNTO 7:")
    print(punto7(P, R))

    print("\nPUNTO 8:")
    diferencia_simetrica(P, R).mostrar()

    print("\nPUNTO 9:")
    print(cardinalidad_rec(R.inicio))

    print("\nPUNTO 10:")
    punto10(P, B, R).mostrar()
