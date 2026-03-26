"""
═══════════════════════════════════════════════════════════════════════════════
SEMANA 7: CONJUNTOS CON LISTAS ENLAZADAS
Ejemplo 4: Implementación Completa
═══════════════════════════════════════════════════════════════════════════════

Clase Conjunto con todas las operaciones:
- Básicas: agregar, eliminar, pertenece, vacío, cardinalidad
- Entre conjuntos: unión, intersección, diferencia
- Relaciones: subconjunto, igualdad
- Extras: vaciar, copiar, a_lista
"""


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


# ═══════════════════════════════════════════════════════════════════════════════
# DEMO
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("CONJUNTO COMPLETO")
    print("=" * 50)
    
    # Crear con lista inicial
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 4, 5, 6])

    roles = {
        "admin": Conjunto(
            ["leer", "escribir", "eliminar", "crear_usuarios",
            "ver_logs", "configurar", "backup", "restaurar"]
        ),
        "editor": Conjunto(["leer", "escribir", "subir_archivos"]),
        "viewer": Conjunto(["leer"]),
        "moderador": Conjunto(["leer", "escribir", "eliminar", "ver_logs"]),
        "auditor": Conjunto(["leer", "ver_logs", "exportar_reportes"]),
    }

    usuarios = {
        "Juan": "admin",
        "María": "editor",
        "Pedro": "viewer",
        "Ana": "moderador",
        "Carlos": "auditor",
    }

    def validar_permisos(usuario, accion_requerida):
        rol = usuarios.get(usuario)
        if not rol:
            return False
        permisos = roles.get(rol, Conjunto())    
        return permisos.pertenece(accion_requerida)
    
    print(f"\nA = {A}")
    print(f"B = {B}")
    
    print(f"\n∪ A ∪ B = {A.union(B)}")
    print(f"∩ A ∩ B = {A.interseccion(B)}")
    print(f"- A - B = {A.diferencia(B)}")
    print(f"△ A △ B = {A.diferencia_simetrica(B)}")
    
    # Subconjuntos
    C = Conjunto([2, 3])
    print(f"\nC = {C}")
    print(f"¿C ⊆ A? {C.es_subconjunto(A)}")
    print(f"¿A ⊆ C? {A.es_subconjunto(C)}")
    
    # Operadores Python
    print(f"\n3 in A: {3 in A}")
    print(f"len(A): {len(A)}")
    
    # Iterar
    print("\nIterando sobre A:")
    for x in A:
        print(f"  {x}")
