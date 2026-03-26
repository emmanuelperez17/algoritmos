"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO: APP DE COCINA - SUGERENCIA DE RECETAS
Algoritmos y Programación 4 - Semana 7
═══════════════════════════════════════════════════════════════════════════════
"""
"""Una app de cocina sugiere recetas según los ingredientes disponibles en casa.
1. Encontrar recetas que puedo preparar con mis ingredientes exactamente
2. Encontrar recetas donde solo me falta 1 ingrediente
3. Ordenar recetas por "cuánto puedo aprovechar" (% de ingredientes que tengo)
4. Encontrar el ingrediente más versátil (aparece en más recetas)
5. Encontrar ingredientes que tengo y nunca uso en ninguna receta"""
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

mis_ingredientes = Conjunto([
    "huevo", "leche", "harina", "mantequilla", "sal",
    "azúcar", "tomate", "cebolla", "ajo", "pollo"
])

recetas = {
    "Tortilla española": Conjunto(["huevo", "papa", "cebolla", "aceite", "sal"]),
    "Panqueques":        Conjunto(["huevo", "leche", "harina", "mantequilla", "azúcar"]),
    "Pollo al ajillo":   Conjunto(["pollo", "ajo", "aceite", "sal", "limón"]),
    "Salsa de tomate":   Conjunto(["tomate", "cebolla", "ajo", "sal", "aceite"]),
    "Arroz con leche":   Conjunto(["leche", "arroz", "azúcar", "canela"]),
    "Huevos revueltos":  Conjunto(["huevo", "mantequilla", "sal"]),
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   APP DE COCINA - SUGERENCIA DE RECETAS")
print("=" * 60)

print(f"\nMis ingredientes ({mis_ingredientes.cardinalidad()}):")
print(f"  {mis_ingredientes}")

print("\nRecetas disponibles:")
for nombre, ingredientes in recetas.items():
    print(f"  {nombre}: {ingredientes}")


# 1. Recetas que puedo preparar con mis ingredientes exactamente
print("\n" + "=" * 60)
print("1. RECETAS QUE PUEDO PREPARAR AHORA")
print("=" * 60)

puedo_preparar = []
for nombre, ingredientes in recetas.items():
    if ingredientes.es_subconjunto(mis_ingredientes):
        puedo_preparar.append(nombre)

if puedo_preparar:
    for nombre in puedo_preparar:
        print(f"  ✓ {nombre}")
else:
    print("  Ninguna receta puede prepararse con exactamente tus ingredientes.")


# 2. Recetas donde solo me falta 1 ingrediente
print("\n" + "=" * 60)
print("2. RECETAS CON 1 INGREDIENTE FALTANTE")
print("=" * 60)

for nombre, ingredientes in recetas.items():
    faltantes = ingredientes.diferencia(mis_ingredientes)
    if faltantes.cardinalidad() == 1:
        print(f"  {nombre} → te falta: {faltantes}")


# 3. Ordenar recetas por % de ingredientes que tengo
print("\n" + "=" * 60)
print("3. RECETAS ORDENADAS POR APROVECHAMIENTO")
print("=" * 60)

ranking = []
for nombre, ingredientes in recetas.items():
    tengo      = ingredientes.interseccion(mis_ingredientes).cardinalidad()
    total      = ingredientes.cardinalidad()
    porcentaje = tengo / total
    ranking.append((nombre, porcentaje, tengo, total))

def obtener_porcentaje(elemento):
    return elemento[1]

ranking.sort(key=obtener_porcentaje, reverse=True)

for nombre, pct, tengo, total in ranking:
    barra = "█" * int(pct * 10)
    print(f"  {nombre:<22} {barra:<10} {pct:.0%}  ({tengo}/{total} ingredientes)")


# 4. Ingrediente más versátil (aparece en más recetas)
print("\n" + "=" * 60)
print("4. INGREDIENTE MÁS VERSÁTIL")
print("=" * 60)

conteo = {}
for nombre, ingredientes in recetas.items():
    for ing in ingredientes:
        conteo[ing] = conteo.get(ing, 0) + 1

max_apariciones = -1
mas_versatil = None
for ing, cantidad in conteo.items():
    if cantidad > max_apariciones:
        max_apariciones = cantidad
        mas_versatil = ing

print(f"\n  Ingrediente más versátil: '{mas_versatil}' → aparece en {max_apariciones} recetas")

ranking_ings = list(conteo.items())

def obtener_cantidad(elemento):
    return elemento[1]

ranking_ings.sort(key=obtener_cantidad, reverse=True)

print("\n  Ranking de versatilidad:")
for ing, cantidad in ranking_ings:
    barra = "█" * cantidad
    print(f"    {ing:<15} {barra} ({cantidad})")


# 5. Ingredientes que tengo y nunca uso en ninguna receta
print("\n" + "=" * 60)
print("5. INGREDIENTES QUE NUNCA USO")
print("=" * 60)

todos_en_recetas = Conjunto()
for nombre, ingredientes in recetas.items():
    todos_en_recetas = todos_en_recetas.union(ingredientes)

nunca_uso = mis_ingredientes.diferencia(todos_en_recetas)

if nunca_uso.esta_vacio():
    print("  ¡Todos tus ingredientes aparecen en al menos una receta!")
else:
    print(f"\n  Ingredientes que tienes pero no usas en ninguna receta:")
    for ing in nunca_uso:
        print(f"    · {ing}")