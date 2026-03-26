# ════════════════════════════════════════════════════════════════════════
# SIMULACRO PARCIAL - CONJUNTOS CON LISTAS ENLAZADAS
# Nivel: Alto (tipo examen real)
# ════════════════════════════════════════════════════════════════════════


# ═════════════════════════════
# CLASES BASE
# ═════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        
        if elementos:
            for e in elementos:
                self.agregar(e)

    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def cardinalidad(self):
        return self.tamaño

    def esta_vacio(self):
        return self.cabeza is None

    def eliminar(self, x):
        if self.esta_vacio():
            return False
        
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def union(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado

    def interseccion(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado

    def diferencia(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado

    def es_subconjunto(self, otro):
        actual = self.cabeza
        
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        
        return True

    def son_disjuntos(self, otro):
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True

    def copiar(self):
        copia = Conjunto()
        actual = self.cabeza
        
        while actual:
            copia.agregar(actual.dato)
            actual = actual.siguiente
        
        return copia

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═════════════════════════════
# CASO 1: SEGURIDAD AVANZADA
# ═════════════════════════════

roles = {
    "admin": Conjunto(["leer","escribir","eliminar","configurar"]),
    "editor": Conjunto(["leer","escribir"]),
    "viewer": Conjunto(["leer"]),
    "moderador": Conjunto(["leer","escribir","eliminar"]),
}

usuarios = {
    "Juan": "admin",
    "Ana": "editor",
    "Luis": "viewer",
    "Sofia": "moderador"
}


def puede_hacer(usuario, acciones):
    rol = usuarios.get(usuario)
    if not rol:
        return False
    return acciones.es_subconjunto(roles[rol])


print("\n===== VERIFICACIÓN =====")
acciones = Conjunto(["leer","eliminar"])
print("Juan:", puede_hacer("Juan", acciones))


# ═════════════════════════════
# CASO 2: PERMISOS COMUNES
# ═════════════════════════════

print("\n===== INTERSECCIÓN =====")
print("editor ∩ moderador:",
      roles["editor"].interseccion(roles["moderador"]))


# ═════════════════════════════
# CASO 3: SUGERIR AMIGOS
# ═════════════════════════════

red = {
    "Ana": Conjunto(["Carlos","Diana"]),
    "Carlos": Conjunto(["Ana","Diana"]),
    "Diana": Conjunto(["Ana","Carlos","Luis"]),
    "Luis": Conjunto(["Diana"])
}


def sugerencias(usuario):
    amigos = red[usuario]
    sugeridos = Conjunto()
    
    actual = amigos.cabeza
    while actual:
        amigo = actual.dato
        sugeridos = sugeridos.union(red[amigo])
        actual = actual.siguiente
    
    sugeridos = sugeridos.diferencia(amigos)
    sugeridos.eliminar(usuario)
    
    return sugeridos


print("\n===== SUGERENCIAS =====")
print("Ana:", sugerencias("Ana"))


# ═════════════════════════════
# CASO 4: MÁS CONECTADO
# ═════════════════════════════

def mas_conectado():
    mejor = None
    maximo = 0
    
    for u, amigos in red.items():
        if amigos.cardinalidad() > maximo:
            maximo = amigos.cardinalidad()
            mejor = u
    
    return mejor


print("\n===== MÁS CONECTADO =====")
print(mas_conectado())


# ═════════════════════════════
# EJERCICIOS (PARA TI)
# ═════════════════════════════

"""
1. Implementa:
   diferencia_multiple(self, lista_conjuntos)

2. Implementa:
   es_superconjunto(self, otro)

3. Implementa:
   eliminar_si(self, condicion)

4. Implementa:
   eliminar_mayores(self, valor)

5. Implementa:
   interseccion_manual(self, otro) (sin usar interseccion)

6. Implementa:
   usuarios_con_mismos_permisos(roles)

7. Implementa:
   verificar_3_disjuntos(A, B, C)

8. (DIFÍCIL)
   potencia(self) → conjunto de subconjuntos

9. (PROFE AMA)
   sugerir_rol(permisos_usuario)

10. (TRAMPA)
   contar cuántos elementos cumplen una condición SIN usar listas
"""