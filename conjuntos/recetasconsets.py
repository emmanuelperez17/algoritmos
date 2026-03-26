"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO: APP DE COCINA - SUGERENCIA DE RECETAS
Algoritmos y Programación 4 - Semana 7
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

mis_ingredientes = {
    "huevo", "leche", "harina", "mantequilla", "sal",
    "azúcar", "tomate", "cebolla", "ajo", "pollo"
}

recetas = {
    "Tortilla española": {"huevo", "papa", "cebolla", "aceite", "sal"},
    "Panqueques":        {"huevo", "leche", "harina", "mantequilla", "azúcar"},
    "Pollo al ajillo":   {"pollo", "ajo", "aceite", "sal", "limón"},
    "Salsa de tomate":   {"tomate", "cebolla", "ajo", "sal", "aceite"},
    "Arroz con leche":   {"leche", "arroz", "azúcar", "canela"},
    "Huevos revueltos":  {"huevo", "mantequilla", "sal"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   APP DE COCINA - SUGERENCIA DE RECETAS")
print("=" * 60)

print(f"\nMis ingredientes ({len(mis_ingredientes)}):")
print(f"  {mis_ingredientes}")

print("\nRecetas disponibles:")
for nombre, ingredientes in recetas.items():
    print(f"  {nombre}: {ingredientes}")


# 1. Recetas que puedo preparar con mis ingredientes exactamente
# ingredientes de la receta <= mis_ingredientes  (subconjunto)
print("\n" + "=" * 60)
print("1. RECETAS QUE PUEDO PREPARAR AHORA")
print("=" * 60)

puedo_preparar = []
for nombre, ingredientes in recetas.items():
    if ingredientes <= mis_ingredientes:
        puedo_preparar.append(nombre)

if puedo_preparar:
    for nombre in puedo_preparar:
        print(f"  ✓ {nombre}")
else:
    print("  Ninguna receta puede prepararse con exactamente tus ingredientes.")


# 2. Recetas donde solo me falta 1 ingrediente
# diferencia = ingredientes de la receta que NO tengo
print("\n" + "=" * 60)
print("2. RECETAS CON 1 INGREDIENTE FALTANTE")
print("=" * 60)

for nombre, ingredientes in recetas.items():
    faltantes = ingredientes - mis_ingredientes
    if len(faltantes) == 1:
        print(f"  {nombre} → te falta: {faltantes}")


# 3. Ordenar recetas por % de ingredientes que tengo
# porcentaje = len(receta & mis_ingredientes) / len(receta)
print("\n" + "=" * 60)
print("3. RECETAS ORDENADAS POR APROVECHAMIENTO")
print("=" * 60)

ranking = []
for nombre, ingredientes in recetas.items():
    tengo      = len(ingredientes & mis_ingredientes)
    total      = len(ingredientes)
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
# union de todos los ingredientes de todas las recetas
# luego mis_ingredientes - esa union
print("\n" + "=" * 60)
print("5. INGREDIENTES QUE NUNCA USO")
print("=" * 60)

todos_en_recetas = set()
for ingredientes in recetas.values():
    todos_en_recetas = todos_en_recetas | ingredientes

nunca_uso = mis_ingredientes - todos_en_recetas

if not nunca_uso:
    print("  ¡Todos tus ingredientes aparecen en al menos una receta!")
else:
    print(f"\n  Ingredientes que tienes pero no usas en ninguna receta:")
    for ing in nunca_uso:
        print(f"    · {ing}")