"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 3: NETFLIX - SISTEMA DE RECOMENDACIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Netflix quiere mejorar su sistema de recomendaciones usando conjuntos.
Cada película tiene un conjunto de géneros/etiquetas.
El sistema debe:

1. Encontrar películas similares (comparten géneros)
2. Recomendar películas según los géneros favoritos del usuario
3. Encontrar géneros únicos en el catálogo
4. Agrupar películas por género
5. Calcular un "puntaje de similitud" entre películas

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"romance", "drama", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}

# Géneros favoritos del usuario
favoritos_usuario = {"ciencia ficción", "acción", "thriller"}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   NETFLIX - SISTEMA DE RECOMENDACIONES")
print("=" * 60)

print("\nCatálogo:")
for pelicula, generos in catalogo.items():
    print(f"  {pelicula}: {generos}")

# 1. Películas similares (comparten al menos 2 géneros)
print("\n" + "=" * 60)
print("1. PELÍCULAS SIMILARES (comparten 2+ géneros)")
print("=" * 60)

peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]
        if len(comunes) >= 2:
            print(f"  {p1} <-> {p2}")
            print(f"    Géneros comunes: {comunes}")

# 2. Recomendaciones según gustos del usuario
print("\n" + "=" * 60)
print(f"2. RECOMENDACIONES (gustos: {favoritos_usuario})")
print("=" * 60)

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = generos & favoritos_usuario
    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos_usuario)
        recomendaciones.append((pelicula, puntaje, coincidencias))

# Ordenar por puntaje (mayor primero)
recomendaciones.sort(key=lambda x: x[1], reverse=True)

for pelicula, puntaje, coincidencias in recomendaciones:
    barra = "█" * int(puntaje * 10)
    print(f"  {pelicula:20} {barra} {puntaje:.0%} - {coincidencias}")

# 3. Todos los géneros del catálogo
print("\n" + "=" * 60)
print("3. GÉNEROS ÚNICOS EN EL CATÁLOGO")
print("=" * 60)

todos_generos = set()
for generos in catalogo.values():
    todos_generos = todos_generos | generos

print(f"  Total: {len(todos_generos)} géneros")
for g in sorted(todos_generos):
    print(f"  • {g}")

# 4. Agrupar películas por género
print("\n" + "=" * 60)
print("4. PELÍCULAS POR GÉNERO")
print("=" * 60)

for genero in sorted(todos_generos):
    peliculas_genero = set()
    for pelicula, generos in catalogo.items():
        if genero in generos:
            peliculas_genero.add(pelicula)
    print(f"  {genero}: {peliculas_genero}")

# 5. Puntaje de similitud entre dos películas
print("\n" + "=" * 60)
print("5. SIMILITUD (índice de Jaccard)")
print("=" * 60)

def similitud_jaccard(pelicula1, pelicula2):
    """
    Índice de Jaccard = |A ∩ B| / |A ∪ B|
    1.0 = idénticos, 0.0 = nada en común
    """
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    interseccion = len(g1 & g2)
    union = len(g1 | g2)
    return interseccion / union if union > 0 else 0

pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy Story", "Shrek"),
    ("The Godfather", "John Wick"),
]

for p1, p2 in pares:
    sim = similitud_jaccard(p1, p2)
    barra = "█" * int(sim * 20)
    print(f"  {p1:15} vs {p2:15} → {barra} {sim:.2f}")
