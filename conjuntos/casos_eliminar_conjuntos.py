# ============================================
# 🔹 CASO 1: ELIMINAR UN ELEMENTO ESPECÍFICO
# ============================================

# 📝 ENUNCIADO:
# "Eliminar el usuario 'Ana' del conjunto"

# 💡 IDEA:
# Usar método eliminar directamente

A.eliminar("Ana")
# ============================================
# 🔹 CASO 2: ELIMINAR SI EXISTE
# ============================================

# 📝 ENUNCIADO:
# "Eliminar un usuario solo si pertenece al conjunto"

if A.pertenece("Luis"):
    A.eliminar("Luis")
# ============================================
# 🔹 CASO 3: ELIMINAR TODOS LOS ELEMENTOS (VACIAR)
# ============================================

# 📝 ENUNCIADO:
# "Eliminar todos los usuarios"

A.vaciar()
# ============================================
# 🔹 CASO 4: ELIMINAR POR INICIAL
# ============================================

# 📝 ENUNCIADO:
# "Eliminar usuarios que empiezan por 'A'"

def eliminar_por_inicial(conjunto, letra):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if actual.dato[0].lower() == letra.lower():
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 5: ELIMINAR POR CONTENER LETRA
# ============================================

# 📝 ENUNCIADO:
# "Eliminar usuarios que contienen la letra 'a'"

def eliminar_contiene(conjunto, letra):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if letra.lower() in actual.dato.lower():
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 6: ELIMINAR POR LONGITUD
# ============================================

# 📝 ENUNCIADO:
# "Eliminar nombres con menos de 5 letras"

def eliminar_por_longitud(conjunto, n):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if len(actual.dato) < n:
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 7: ELIMINAR NÚMEROS PARES
# ============================================

# 📝 ENUNCIADO:
# "Eliminar todos los números pares"

def eliminar_pares(conjunto):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if actual.dato % 2 == 0:
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 8: ELIMINAR MAYORES A N
# ============================================

def eliminar_mayores(conjunto, n):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if actual.dato > n:
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 9: ELIMINAR ELEMENTOS DE OTRO CONJUNTO
# ============================================

# 📝 ENUNCIADO:
# "Eliminar de A todos los elementos que están en B"

def eliminar_conjunto(A, B):
    actual = B.cabeza

    while actual:
        A.eliminar(actual.dato)
        actual = actual.siguiente
# ============================================
# 🔹 CASO 10: ELIMINAR INTERSECCIÓN
# ============================================

# 📝 ENUNCIADO:
# "Eliminar elementos comunes entre A y B"

def eliminar_interseccion(A, B):
    inter = A.interseccion(B)
    eliminar_conjunto(A, inter)
# ============================================
# 🔹 CASO 11: ELIMINAR RECURSIVO POR CONDICIÓN
# ============================================

# 📝 ENUNCIADO:
# "Eliminar nombres con longitud menor a 5 (recursivo)"

def eliminar_recursivo(nodo, conjunto, n, anterior=None):
    if nodo is None:
        return

    if len(nodo.dato) < n:
        if anterior is None:
            conjunto.cabeza = nodo.siguiente
        else:
            anterior.siguiente = nodo.siguiente
        conjunto.tamaño -= 1
        eliminar_recursivo(nodo.siguiente, conjunto, n, anterior)
    else:
        eliminar_recursivo(nodo.siguiente, conjunto, n, nodo)
# ============================================
# 🔹 CASO 12: ELIMINAR DUPLICADOS (DEFENSIVO)
# ============================================

# 📝 ENUNCIADO:
# "Eliminar elementos repetidos (por si hay errores)"

def eliminar_duplicados(conjunto):
    vistos = Conjunto()
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if vistos.pertenece(actual.dato):
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            vistos.agregar(actual.dato)
            anterior = actual

        actual = actual.siguiente
# ============================================
# 🔹 CASO 13: ELIMINAR TODOS MENOS LOS QUE CUMPLEN
# ============================================

# 📝 ENUNCIADO:
# "Eliminar todos los usuarios que NO cumplen condición"

def filtrar_eliminando(conjunto):
    actual = conjunto.cabeza
    anterior = None

    while actual:
        if not (len(actual.dato) > 4):
            if anterior is None:
                conjunto.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            conjunto.tamaño -= 1
        else:
            anterior = actual

        actual = actual.siguiente
