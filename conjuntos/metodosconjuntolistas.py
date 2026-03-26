# ═════════════════════════════
# NODO: unidad básica de la lista enlazada
# ═════════════════════════════
class Nodo:
    def __init__(self, dato):
        self.dato = dato              # valor almacenado en el nodo
        self.siguiente = None         # referencia al siguiente nodo


# ═════════════════════════════
# CLASE CONJUNTO (usando lista enlazada)
# ═════════════════════════════
class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None            # primer nodo de la lista
        self.tamaño = 0               # cantidad de elementos
        
        # Si se pasan elementos iniciales, se agregan uno a uno
        if elementos:
            for e in elementos:
                self.agregar(e)

    # ═════════════════════════════
    # OPERACIONES BÁSICAS
    # ═════════════════════════════
    
    def esta_vacio(self):
        # Retorna True si no hay elementos
        return self.cabeza is None
    
    def cardinalidad(self):
        # Retorna el número de elementos
        return self.tamaño
    
    def pertenece(self, x):
        # Verifica si x está en el conjunto (búsqueda lineal)
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        # Solo agrega si no existe (propiedad de conjunto)
        if self.pertenece(x):
            return False
        
        nuevo = Nodo(x)               # se crea nuevo nodo
        nuevo.siguiente = self.cabeza # apunta al anterior primero
        self.cabeza = nuevo           # ahora es la nueva cabeza
        self.tamaño += 1
        return True
    
    def eliminar(self, x):
        # Elimina un elemento del conjunto
        
        if self.esta_vacio():
            return False
        
        # Caso especial: eliminar la cabeza
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        # Buscar en el resto
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                # saltamos el nodo a eliminar
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        
        return False
    
    def vaciar(self):
        # Elimina todos los elementos
        self.cabeza = None
        self.tamaño = 0

    # ═════════════════════════════
    # OPERACIONES ENTRE CONJUNTOS
    # ═════════════════════════════
    
    def union(self, otro):
        # Une dos conjuntos sin repetir elementos
        resultado = Conjunto()
        
        # Agregar elementos del primero
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        # Agregar elementos del segundo
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def interseccion(self, otro):
        # Elementos comunes entre dos conjuntos
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia(self, otro):
        # Elementos que están en self pero no en otro
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia_simetrica(self, otro):
        # Elementos que están en uno u otro pero no en ambos
        return self.diferencia(otro).union(otro.diferencia(self))

    # ═════════════════════════════
    # RELACIONES ENTRE CONJUNTOS
    # ═════════════════════════════
    
    def es_subconjunto(self, otro):
        # Verifica si TODOS los elementos de self están en otro
        actual = self.cabeza
        
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        
        return True
    
    def es_igual(self, otro):
        # Son iguales si tienen el mismo tamaño y mismos elementos
        return self.tamaño == otro.tamaño and self.es_subconjunto(otro)

    # ═════════════════════════════
    # MÉTODOS AVANZADOS
    # ═════════════════════════════
    
    def minimo(self):
        # Retorna el menor elemento
        if self.esta_vacio():
            return None
        
        actual = self.cabeza
        min_val = actual.dato
        
        while actual:
            if actual.dato < min_val:
                min_val = actual.dato
            actual = actual.siguiente
        
        return min_val
    
    def maximo(self):
        # Retorna el mayor elemento
        if self.esta_vacio():
            return None
        
        actual = self.cabeza
        max_val = actual.dato
        
        while actual:
            if actual.dato > max_val:
                max_val = actual.dato
            actual = actual.siguiente
        
        return max_val
    
    def contar(self, x):
        # Cuenta cuántas veces aparece x (aunque no debería repetirse)
        contador = 0
        actual = self.cabeza
        
        while actual:
            if actual.dato == x:
                contador += 1
            actual = actual.siguiente
        
        return contador
    
    @classmethod
    def desde_lista(cls, lista):
        # Crea un conjunto desde una lista de Python
        nuevo = cls()
        for e in lista:
            nuevo.agregar(e)
        return nuevo
    
    def union_multiple(self, lista_conjuntos):
        # Unión de varios conjuntos
        resultado = self.copiar()
        for c in lista_conjuntos:
            resultado = resultado.union(c)
        return resultado
    
    def interseccion_multiple(self, lista_conjuntos):
        # Intersección de varios conjuntos
        resultado = self.copiar()
        for c in lista_conjuntos:
            resultado = resultado.interseccion(c)
        return resultado
    
    def son_disjuntos(self, otro):
        # True si NO comparten elementos
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True
    
    def producto_cartesiano(self, otro):
        # Devuelve pares (a,b)
        resultado = []
        actual1 = self.cabeza
        
        while actual1:
            actual2 = otro.cabeza
            while actual2:
                resultado.append((actual1.dato, actual2.dato))
                actual2 = actual2.siguiente
            actual1 = actual1.siguiente
        
        return resultado
    
    def filtrar(self, funcion):
        # Retorna elementos que cumplen una condición
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if funcion(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def mapear(self, funcion):
        # Aplica una función a cada elemento
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            resultado.agregar(funcion(actual.dato))
            actual = actual.siguiente
        
        return resultado
    
    def suma(self):
        # Suma todos los elementos
        total = 0
        actual = self.cabeza
        
        while actual:
            total += actual.dato
            actual = actual.siguiente
        
        return total
    
    def promedio(self):
        # Promedio de los elementos
        if self.esta_vacio():
            return 0
        return self.suma() / self.tamaño
    
    def invertir(self):
        # Invierte la lista enlazada
        anterior = None
        actual = self.cabeza
        
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        
        self.cabeza = anterior
    
    def todos(self, condicion):
        # True si TODOS cumplen condición
        actual = self.cabeza
        
        while actual:
            if not condicion(actual.dato):
                return False
            actual = actual.siguiente
        
        return True
    
    def alguno(self, condicion):
        # True si AL MENOS UNO cumple
        actual = self.cabeza
        
        while actual:
            if condicion(actual.dato):
                return True
            actual = actual.siguiente
        
        return False
    
    def buscar(self, x):
        # Retorna el nodo que contiene x
        actual = self.cabeza
        
        while actual:
            if actual.dato == x:
                return actual
            actual = actual.siguiente
        
        return None

    # ═════════════════════════════
    # UTILIDADES
    # ═════════════════════════════
    
    def copiar(self):
        # Retorna una copia del conjunto
        copia = Conjunto()
        actual = self.cabeza
        
        while actual:
            copia.agregar(actual.dato)
            actual = actual.siguiente
        
        return copia
    
    def a_lista(self):
        # Convierte a lista de Python
        lista = []
        actual = self.cabeza
        
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        
        return lista
    
    def __str__(self):
        # Representación tipo {1,2,3}
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    
    def __len__(self):
        # Permite usar len(conjunto)
        return self.tamaño
    
    def __contains__(self, x):
        # Permite usar: x in conjunto
        return self.pertenece(x)
    
    def __iter__(self):
        # Permite recorrer con for
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente