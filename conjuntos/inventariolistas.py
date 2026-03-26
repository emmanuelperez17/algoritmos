"""Ejercicio 2 — Inventario de tienda con múltiples sucursales
Difícil
Lista ligada
Una cadena de tiendas necesita comparar su inventario entre sucursales. Cada sucursal guarda sus productos en una lista ligada (Conjunto). El sistema debe detectar faltantes, duplicados y hacer auditorías.

Lo que debes implementar
diferencia_simetrica(otro): productos que solo tiene una de las dos sucursales
productos_exclusivos(sucursales): dado un dict de Conjuntos, retorna productos que SOLO están en una sucursal (en ninguna otra)
inventario_comun(lista_conjuntos): intersección de N conjuntos (más de 2)
cobertura_total(lista_conjuntos): unión de todos
auditoria(): imprime para cada producto en qué sucursales está
💡 Pista: Para intersección de N conjuntos: empieza con una copia del primero e itera el resto aplicando interseccion(). Para productos exclusivos: para cada sucursal, su diferencia con la unión de todas las demás."""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        
        # Inicializar con elementos si se proporcionan
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    # ═══════════════════════════════════════════════════════════════════════
    # OPERACIONES BÁSICAS
    # ═══════════════════════════════════════════════════════════════════════
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def cardinalidad(self):
        return self.tamaño
    
    def pertenece(self, x):
        """¿x ∈ Conjunto?"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        """Insertar x si no existe"""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def eliminar(self, x):
        """Quitar x del conjunto"""
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
    
    def vaciar(self):
        """Eliminar todos los elementos"""
        self.cabeza = None
        self.tamaño = 0
    
    # ═══════════════════════════════════════════════════════════════════════
    # OPERACIONES ENTRE CONJUNTOS
    # ═══════════════════════════════════════════════════════════════════════
    
    def union(self, otro):
        """A ∪ B"""
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
        """A ∩ B"""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia(self, otro):
        """A - B"""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia_simetrica(self, otro):
        """A △ B = (A - B) ∪ (B - A)"""
        return self.diferencia(otro).union(otro.diferencia(self))
    
    # ═══════════════════════════════════════════════════════════════════════
    # RELACIONES
    # ═══════════════════════════════════════════════════════════════════════
    
    def es_subconjunto(self, otro):
        """¿self ⊆ otro?"""
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True
    
    def es_igual(self, otro):
        """¿self = otro?"""
        if self.tamaño != otro.tamaño:
            return False
        return self.es_subconjunto(otro)
    
    # ═══════════════════════════════════════════════════════════════════════
    # UTILIDADES
    # ═══════════════════════════════════════════════════════════════════════
    
    def copiar(self):
        """Retorna copia del conjunto"""
        copia = Conjunto()
        actual = self.cabeza
        while actual:
            copia.agregar(actual.dato)
            actual = actual.siguiente
        return copia
    
    def a_lista(self):
        """Convierte a lista de Python"""
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    #Imprimir conjunto convirtiendolo a una lista y agregandole llaves a cada
    #elemento
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    
    def __len__(self):
        return self.tamaño
    
    def __contains__(self, x):
        return self.pertenece(x)
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente


# Funciones adicionales para el ejercicio
def inventario_comun(lista_conjuntos):
    if not lista_conjuntos: 
        return Conjunto()  # si no hay conjuntos → vacío
    
    resultado = lista_conjuntos[0].copiar()  
    # empezamos con una copia del primer conjunto
    
    for c in lista_conjuntos[1:]:
        resultado = resultado.interseccion(c)
        # vamos intersectando con los demás
    
    return resultado

def cobertura_total(lista_conjuntos):
    resultado = Conjunto()
    
    for c in lista_conjuntos:
        resultado = resultado.union(c)
        # vamos acumulando todos los elementos
    
    return resultado

def productos_exclusivos(sucursales):
    exclusivos = {}
    nombres = list(sucursales.keys())
    
    for nombre, conj in sucursales.items():
        otros = Conjunto()
        
        # unir todas las otras sucursales
        for otro_nombre, otro_conj in sucursales.items():
            if otro_nombre != nombre:
                otros = otros.union(otro_conj)
        
        # diferencia: lo que tiene esta sucursal y nadie más
        exclusivos[nombre] = conj.diferencia(otros)
    
    return exclusivos

# Test
sucursales = {
    "Norte": Conjunto(["leche", "pan", "huevos", "café"]),
    "Sur":   Conjunto(["pan", "café", "arroz", "sal"]),
    "Centro":Conjunto(["leche", "pan", "arroz", "aceite"]),
}
lista = list(sucursales.values())
print("Común a todas:", inventario_comun(lista))
print("Cobertura total:", cobertura_total(lista))
excl = productos_exclusivos(sucursales)
for s, conj in excl.items():
    print(f"Exclusivos de {s}: {conj}")