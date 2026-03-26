"""
═══════════════════════════════════════════════════════════════════════════════
EJERCICIO 1: SISTEMA DE SEGUIMIENTO DE EPIDEMIA
Algoritmos y Programación 4 - Semana 7
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Un sistema de salud pública necesita rastrear el avance de una epidemia.
Cada zona de la ciudad tiene un conjunto de personas contagiadas.
El sistema debe:

1. Encontrar personas contagiadas en MÚLTIPLES zonas (posibles vectores)
2. Encontrar personas que aparecen en UNA SOLA zona (casos aislados)
3. Verificar si una zona está "contenida" (todos sus casos ya están
   en otra zona que se considera controlada)
4. Calcular la zona más crítica (más contagiados únicos que no están
   en ninguna otra zona)
5. Fusionar zonas: unir dos zonas en una sola y eliminarlas del sistema

Implementar usando la clase Conjunto con lista enlazada.
═══════════════════════════════════════════════════════════════════════════════
"""

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

    def esta_vacio(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamaño

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

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

    def es_igual(self, otro):
        if self.tamaño != otro.tamaño:
            return False
        return self.es_subconjunto(otro)

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

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self):
        return self.tamaño

    def __contains__(self, x):
        return self.pertenece(x)


# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

zonas = {
    "Norte": Conjunto(["Ana", "Luis", "Pedro", "María", "Carlos"]),
    "Sur":   Conjunto(["Luis", "Pedro", "Sofía", "Jorge", "Elena"]),
    "Este":  Conjunto(["María", "Carlos", "Fernanda", "Ricardo"]),
    "Oeste": Conjunto(["Ana", "Sofía", "Tomás", "Diana"]),
    "Centro":Conjunto(["Pedro", "Carlos", "Elena", "Diego", "Valeria"]),
}

zona_controlada = Conjunto(["Luis", "Pedro", "Sofía"])

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SISTEMA DE SEGUIMIENTO DE EPIDEMIA")
print("=" * 60)

print("\nZonas y contagiados:")
for zona, personas in zonas.items():
    print(f"  {zona} ({personas.cardinalidad()}): {personas}")


# 1. Personas contagiadas en múltiples zonas (posibles vectores)
print("\n" + "=" * 60)
print("1. POSIBLES VECTORES (en más de una zona)")
print("=" * 60)

# Para cada persona, contamos en cuántas zonas aparece
conteo_zonas = {}
for zona, personas in zonas.items():
    for persona in personas:
        conteo_zonas[persona] = conteo_zonas.get(persona, 0) + 1

vectores = Conjunto()
for persona, count in conteo_zonas.items():
    if count > 1:
        vectores.agregar(persona)

print(f"\n  Posibles vectores ({vectores.cardinalidad()}): {vectores}")
for persona in vectores:
    zonas_donde = [z for z, p in zonas.items() if p.pertenece(persona)]
    print(f"    → {persona}: aparece en {zonas_donde}")


# 2. Personas que aparecen en una sola zona (casos aislados)
print("\n" + "=" * 60)
print("2. CASOS AISLADOS (en una sola zona)")
print("=" * 60)

aislados = Conjunto()
for persona, count in conteo_zonas.items():
    if count == 1:
        aislados.agregar(persona)

print(f"\n  Casos aislados ({aislados.cardinalidad()}): {aislados}")


# 3. ¿Está una zona "contenida"? (todos sus casos ya están en zona_controlada)
print("\n" + "=" * 60)
print("3. ZONAS CONTENIDAS")
print("=" * 60)

# Una zona está contenida si es subconjunto de zona_controlada
for zona, personas in zonas.items():
    contenida = personas.es_subconjunto(zona_controlada)
    estado = "✓ CONTENIDA" if contenida else "✗ No contenida"
    print(f"  {zona}: {estado}")


# 4. Zona más crítica (más contagiados que NO están en ninguna otra zona)
print("\n" + "=" * 60)
print("4. ZONA MÁS CRÍTICA")
print("=" * 60)

# Los exclusivos de una zona son los que solo aparecen en ella (count == 1)
# y están en esa zona
zona_critica = None
max_exclusivos = -1

for zona, personas in zonas.items():
    exclusivos = Conjunto()
    for persona in personas:
        if conteo_zonas[persona] == 1:   # solo está en esta zona
            exclusivos.agregar(persona)
    print(f"  {zona}: {exclusivos.cardinalidad()} exclusivos → {exclusivos}")
    if exclusivos.cardinalidad() > max_exclusivos:
        max_exclusivos = exclusivos.cardinalidad()
        zona_critica = zona

print(f"\n  Zona más crítica: {zona_critica} ({max_exclusivos} casos exclusivos)")


# 5. Fusionar dos zonas: unirlas y eliminarlas del diccionario
print("\n" + "=" * 60)
print("5. FUSIONAR ZONAS")
print("=" * 60)

def fusionar_zonas(zonas_dict, z1, z2, nombre_nuevo):
    # Unir los dos conjuntos
    fusion = zonas_dict[z1].union(zonas_dict[z2])
    # Construir nuevo diccionario sin z1 ni z2, con el nuevo nombre
    nuevo_dict = {}
    for nombre, personas in zonas_dict.items():
        if nombre != z1 and nombre != z2:
            nuevo_dict[nombre] = personas
    nuevo_dict[nombre_nuevo] = fusion
    return nuevo_dict

zonas = fusionar_zonas(zonas, "Norte", "Sur", "NorteSur")
print("\nZonas después de fusionar Norte y Sur:")
for zona, personas in zonas.items():
    print(f"  {zona} ({personas.cardinalidad()}): {personas}")