# ============================================
# 🔹 BASE: RECORRER EL CONJUNTO
# ============================================

# 💡 TODO parte de esto:
actual = A.cabeza
while actual:
    print(actual.dato)
    actual = actual.siguiente
# ============================================
# 🔹 CASO 1: BUSCAR POR INICIAL
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que empiezan por la letra 'A'"

def buscar_por_inicial(conjunto, letra):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato[0].lower() == letra.lower():
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 2: BUSCAR POR LETRA CONTENIDA
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que contienen la letra 'a'"

def contiene_letra(conjunto, letra):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if letra.lower() in actual.dato.lower():
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 3: BUSCAR POR TERMINACIÓN
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que terminan en 'a'"

def termina_en(conjunto, letra):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato[-1].lower() == letra.lower():
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 4: LONGITUD DEL NOMBRE
# ============================================

# 📝 ENUNCIADO:
# "Usuarios con nombres de más de 5 letras"

def longitud_mayor(conjunto, n):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if len(actual.dato) > n:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 5: LONGITUD EXACTA
# ============================================

# 📝 ENUNCIADO:
# "Usuarios con exactamente 5 letras"

def longitud_exacta(conjunto, n):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if len(actual.dato) == n:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 6: MAYORES QUE UN NÚMERO
# ============================================

# 📝 ENUNCIADO:
# "Elementos mayores que 10"

def mayores_que(conjunto, n):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato > n:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 7: MENORES QUE
# ============================================

def menores_que(conjunto, n):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato < n:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 8: PARES
# ============================================

# 📝 ENUNCIADO:
# "Números pares"

def pares(conjunto):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato % 2 == 0:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 9: IMPARES
# ============================================

def impares(conjunto):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato % 2 != 0:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 10: ORDEN ALFABÉTICO
# ============================================

# 📝 ENUNCIADO:
# "Mostrar usuarios en orden alfabético"

def ordenar_alfabetico(conjunto):
    lista = conjunto.a_lista()
    lista.sort()

    resultado = Conjunto()
    for elem in lista:
        resultado.agregar(elem)

    return resultado
# ============================================
# 🔹 CASO 11: ORDEN DESCENDENTE
# ============================================

def ordenar_desc(conjunto):
    lista = conjunto.a_lista()
    lista.sort(reverse=True)

    resultado = Conjunto()
    for elem in lista:
        resultado.agregar(elem)

    return resultado
# ============================================
# 🔹 CASO 12: INICIAL + LONGITUD
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que empiezan por 'A' y tienen más de 4 letras"

def inicial_y_longitud(conjunto):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        if actual.dato.startswith("A") and len(actual.dato) > 4:
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 13: CONTIENE LETRA Y TERMINA EN
# ============================================

# 📝 ENUNCIADO:
# "Usuarios que contienen 'a' y terminan en 'o'"

def filtro_combinado(conjunto):
    resultado = Conjunto()
    actual = conjunto.cabeza

    while actual:
        nombre = actual.dato.lower()
        if "a" in nombre and nombre.endswith("o"):
            resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado
# ============================================
# 🔹 CASO 14: BUSCAR POR INICIAL (RECURSIVO)
# ============================================

def buscar_recursivo(nodo, letra, resultado):
    if nodo is None:
        return
    
    if nodo.dato[0].lower() == letra.lower():
        resultado.agregar(nodo.dato)
    
    buscar_recursivo(nodo.siguiente, letra, resultado)
# ============================================
# 🔹 CASO 15: FILTRAR POR CONDICIÓN (RECURSIVO)
# ============================================

def filtrar_recursivo(nodo, resultado):
    if nodo is None:
        return
    
    if len(nodo.dato) > 4:
        resultado.agregar(nodo.dato)
    
    filtrar_recursivo(nodo.siguiente, resultado)
