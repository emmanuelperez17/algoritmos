# ============================================
# 🔹 CASO 1: UNIÓN
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en AL MENOS una plataforma"

# 💡 IDEA:
# Unión → A ∪ B

resultado = A.union(B)
# ============================================
# 🔹 CASO 2: INTERSECCIÓN
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en AMBAS plataformas"

# 💡 IDEA:
# Intersección → A ∩ B

resultado = A.interseccion(B)
# ============================================
# 🔹 CASO 3: DIFERENCIA
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en web PERO NO en app"

# 💡 IDEA:
# A - B

resultado = A.diferencia(B)
# ============================================
# 🔹 CASO 4: DIFERENCIA SIMÉTRICA
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están SOLO en una plataforma"

# 💡 IDEA:
# (A - B) ∪ (B - A)

resultado = A.diferencia_simetrica(B)
# ============================================
# 🔹 CASO 5: SUBCONJUNTO
# ============================================

# 📝 ENUNCIADO:
# "Verificar si todos los usuarios premium están en la web"

# 💡 IDEA:
# C ⊆ A

resultado = es_subconjunto(C, A)
# ============================================
# 🔹 CASO 6: EXACTAMENTE EN DOS CONJUNTOS
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en EXACTAMENTE dos plataformas"

# 💡 IDEA:
# (A∩B ∪ A∩C ∪ B∩C) - (A∩B∩C)

AB = A.interseccion(B)
AC = A.interseccion(C)
BC = B.interseccion(C)

dos = AB.union(AC).union(BC)
tres = A.interseccion(B).interseccion(C)

resultado = dos.diferencia(tres)
# ============================================
# 🔹 CASO 7: AL MENOS EN DOS CONJUNTOS
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en al menos dos plataformas"

# 💡 IDEA:
# (A∩B ∪ A∩C ∪ B∩C)

resultado = AB.union(AC).union(BC)
# ============================================
# 🔹 CASO 8: SOLO EN UN CONJUNTO
# ============================================

# 📝 ENUNCIADO:
# "Usuarios exclusivos de una sola plataforma"

# 💡 IDEA:
# Total - los que están en más de uno

todos = A.union(B).union(C)
dos_o_mas = AB.union(AC).union(BC)

resultado = todos.diferencia(dos_o_mas)
# ============================================
# 🔹 CASO 9: APARECE EN N CONJUNTOS
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en EXACTAMENTE 2 plataformas"

# 💡 IDEA:
# Contar ocurrencias

def contar_en_conjuntos(elemento, conjuntos):
    count = 0
    for c in conjuntos:
        if c.pertenece(elemento):
            count += 1
    return count

resultado = Conjunto()
todos = A.union(B).union(C)

actual = todos.cabeza
while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C]) == 2:
        resultado.agregar(actual.dato)
    actual = actual.siguiente
# ============================================
# 🔹 CASO 10: IMPAR / PAR
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que aparecen en un número IMPAR de conjuntos"

# 💡 IDEA:
# count % 2

resultado = Conjunto()
actual = todos.cabeza

while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C]) % 2 == 1:
        resultado.agregar(actual.dato)
    actual = actual.siguiente
# ============================================
# 🔹 CASO 11: TODOS MENOS UNO
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en todos los sistemas MENOS uno"

# 💡 IDEA:
# count == total - 1

resultado = Conjunto()
todos = A.union(B).union(C).union(D)

actual = todos.cabeza
while actual:
    if contar_en_conjuntos(actual.dato, [A, B, C, D]) == 3:
        resultado.agregar(actual.dato)
    actual = actual.siguiente
# ============================================
# 🔹 CASO 12: INTERSECCIÓN TOTAL
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en TODOS los sistemas"

# 💡 IDEA:
# A ∩ B ∩ C

resultado = A.interseccion(B).interseccion(C)
# ============================================
# 🔹 CASO 13: OPERACIÓN COMPUESTA
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que están en web o app pero NO en premium"

# 💡 IDEA:
# (A ∪ B) - C

resultado = A.union(B).diferencia(C)
# ============================================
# 🔹 CASO 14: VALIDAR IGUALDAD
# ============================================

# 📝 ENUNCIADO:
# "Verificar si dos conjuntos tienen exactamente los mismos elementos"

# 💡 IDEA:
# doble verificación

resultado = son_iguales(A, B)
# ============================================
# 🔹 CASO 15: CARDINALIDAD RECURSIVA
# ============================================

# 📝 ENUNCIADO:
# "Calcular cantidad de elementos SIN usar tamaño"

# 💡 IDEA:
# Recorrer recursivamente

def contar_recursivo(nodo):
    if nodo is None:
        return 0
    return 1 + contar_recursivo(nodo.siguiente)
# ============================================
# 🔹 CASO 16: FILTRAR ELEMENTOS (RECURSIVO)
# ============================================

# 📝 ENUNCIADO:
# "Obtener usuarios cuyo nombre tenga más de 4 letras"

# 💡 IDEA:
# Recorrer y filtrar

def filtrar(nodo, resultado):
    if nodo is None:
        return
    if len(nodo.dato) > 4:
        resultado.agregar(nodo.dato)
    filtrar(nodo.siguiente, resultado)
# ============================================
# 🔹 CASO 17: INVERTIR CONJUNTO
# ============================================

# 📝 ENUNCIADO:
# "Invertir el orden de los elementos del conjunto"

# 💡 IDEA:
# Recursión sobre nodos

def invertir(nodo):
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    nuevo = invertir(nodo.siguiente)
    nodo.siguiente.siguiente = nodo
    nodo.siguiente = None
    return nuevo
# ============================================
# 🔹 CASO 18: SUBCONJUNTOS (MUY AVANZADO)
# ============================================

# 📝 ENUNCIADO:
# "Generar todos los subconjuntos posibles"

# 💡 IDEA:
# Incluir / no incluir

def subconjuntos(lista):
    if len(lista) == 0:
        return [[]]
    
    primero = lista[0]
    resto = subconjuntos(lista[1:])
    
    nuevos = []
    for s in resto:
        nuevos.append([primero] + s)
    
    return resto + nuevos
    