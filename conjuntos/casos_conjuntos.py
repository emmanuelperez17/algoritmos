# ============================================
# 🔹 CASO 0: CREACIÓN DE CONJUNTOS
# ============================================

A = Conjunto(["Ana", "Luis", "Pedro", "Sofía", "María", "Carlos"])
B = Conjunto(["Sofía", "Carlos", "Julián", "María", "Andrés", "Camila"])
C = Conjunto(["Carlos", "María", "Camila", "Pedro"])
D = Conjunto(["Pedro", "Camila"])


# ============================================
# 🔹 CASO 1: OPERACIONES BÁSICAS
# ============================================

# Unión
union = A.union(B)

# Intersección
interseccion = A.interseccion(B)

# Diferencia
diferencia = A.diferencia(B)

# Diferencia simétrica
simetrica = A.diferencia_simetrica(B)


# ============================================
# 🔹 CASO 2: SUBCONJUNTOS
# ============================================

def es_subconjunto(c1, c2):
    actual = c1.cabeza
    while actual:
        if not c2.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True

# Ejemplo
print(es_subconjunto(C, A.union(B)))


# ============================================
# 🔹 CASO 3: EXACTAMENTE EN DOS CONJUNTOS
# ============================================

AB = A.interseccion(B)
AC = A.interseccion(C)
BC = B.interseccion(C)

dos = AB.union(AC).union(BC)

tres = A.interseccion(B).interseccion(C)

exactamente_dos = dos.diferencia(tres)


# ============================================
# 🔹 CASO 4: AL MENOS EN DOS CONJUNTOS
# ============================================

al_menos_dos = AB.union(AC).union(BC)


# ============================================
# 🔹 CASO 5: SOLO EN UN CONJUNTO
# ============================================

todos = A.union(B).union(C)

dos_o_mas = AB.union(AC).union(BC)

solo_uno = todos.diferencia(dos_o_mas)


# ============================================
# 🔹 CASO 6: APARECE EN N CONJUNTOS (CONTEO)
# ============================================

def contar_en_conjuntos(elemento, lista_conjuntos):
    contador = 0
    for conj in lista_conjuntos:
        if conj.pertenece(elemento):
            contador += 1
    return contador

# Ejemplo: en exactamente 2
resultado = Conjunto()
todos = A.union(B).union(C)

actual = todos.cabeza
while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C]) == 2:
        resultado.agregar(actual.dato)
    actual = actual.siguiente


# ============================================
# 🔹 CASO 7: APARECE EN NÚMERO IMPAR DE CONJUNTOS
# ============================================

impares = Conjunto()
actual = todos.cabeza

while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C]) % 2 == 1:
        impares.agregar(actual.dato)
    actual = actual.siguiente


# ============================================
# 🔹 CASO 8: TODOS MENOS UNO (n-1 conjuntos)
# ============================================

Z = Conjunto()
todos = A.union(B).union(C).union(D)

actual = todos.cabeza
while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C, D]) == 3:
        Z.agregar(actual.dato)
    actual = actual.siguiente


# ============================================
# 🔹 CASO 9: INTERSECCIÓN DE MUCHOS CONJUNTOS
# ============================================

interseccion_total = A.interseccion(B).interseccion(C)


# ============================================
# 🔹 CASO 10: DIFERENCIA COMPLEJA
# ============================================

# (A ∪ B) - (C ∩ D)
resultado = A.union(B).diferencia(C.interseccion(D))


# ============================================
# 🔹 CASO 11: VALIDAR IGUALDAD DE CONJUNTOS
# ============================================

def son_iguales(c1, c2):
    actual = c1.cabeza
    while actual:
        if not c2.pertenece(actual.dato):
            return False
        actual = actual.siguiente

    actual = c2.cabeza
    while actual:
        if not c1.pertenece(actual.dato):
            return False
        actual = actual.siguiente

    return True


# ============================================
# 🔹 CASO 12: CARDINALIDAD RECURSIVA
# ============================================

def contar_recursivo(nodo):
    if nodo is None:
        return 0
    return 1 + contar_recursivo(nodo.siguiente)


# ============================================
# 🔹 CASO 13: RECORRIDO RECURSIVO
# ============================================

def imprimir_recursivo(nodo):
    if nodo is None:
        return
    print(nodo.dato)
    imprimir_recursivo(nodo.siguiente)


# ============================================
# 🔹 CASO 14: INVERTIR CONJUNTO (RECURSIVO)
# ============================================

def invertir(nodo):
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    nuevo = invertir(nodo.siguiente)
    nodo.siguiente.siguiente = nodo
    nodo.siguiente = None
    return nuevo


# ============================================
# 🔹 CASO 15: FILTRAR ELEMENTOS (RECURSIVO)
# ============================================

def filtrar(nodo, resultado):
    if nodo is None:
        return
    if len(nodo.dato) > 4:
        resultado.agregar(nodo.dato)
    filtrar(nodo.siguiente, resultado)


# ============================================
# 🔹 CASO 16: GENERAR SUBCONJUNTOS (NIVEL ALTO)
# ============================================

def subconjuntos(lista):
    if len(lista) == 0:
        return [[]]
    
    primero = lista[0]
    resto = subconjuntos(lista[1:])
    
    nuevos = []
    for s in resto:
        nuevos.append([primero] + s)
    
    return resto + nuevos


# ============================================
# 🔹 CASO 17: CONVERTIR A LISTA Y USAR
# ============================================

lista_A = A.a_lista()


# ============================================
# 🔹 CASO 18: VALIDACIÓN COMPLEJA
# ============================================

# Verificar si TODOS los elementos cumplen condición

def todos_cumplen(nodo):
    if nodo is None:
        return True
    if len(nodo.dato) <= 4:
        return False
    return todos_cumplen(nodo.siguiente)
