"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO: CMS - MOTOR DE BÚSQUEDA Y RECOMENDACIÓN POR TAGS
Sets nativos de Python
Algoritmos y Programación 4 - Semana 7
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

articulos = {
    "Intro a Python":      {"python", "programación", "tutorial", "básico"},
    "Python para ML":      {"python", "machine-learning", "data-science"},
    "Redes Neuronales":    {"machine-learning", "deep-learning", "python"},
    "Docker para Devs":    {"docker", "devops", "tutorial"},
    "Kubernetes avanzado": {"docker", "kubernetes", "devops"},
    "React desde cero":    {"javascript", "react", "tutorial", "básico"},
    "SQL avanzado":        {"sql", "bases-de-datos", "data-science"},
    "Historia del Jazz":   {"música", "historia", "jazz"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   CMS - MOTOR DE BÚSQUEDA POR TAGS (sets nativos)")
print("=" * 60)

print("\nArtículos:")
for titulo, tags in articulos.items():
    print(f"  {titulo}: {tags}")


# 1. Búsqueda AND — artículos que tienen TODOS los tags buscados
# tags_buscados <= tags_articulo  (subconjunto)
print("\n" + "=" * 60)
print("1. BÚSQUEDA AND (todos los tags)")
print("=" * 60)

def buscar_and(tags_buscados, articulos_dict):
    resultados = []
    for titulo, tags in articulos_dict.items():
        if tags_buscados <= tags:
            resultados.append(titulo)
    return resultados

busquedas_and = [
    {"python", "tutorial"},
    {"docker", "devops"},
    {"machine-learning", "python"},
]
for b in busquedas_and:
    resultado = buscar_and(b, articulos)
    print(f"\n  AND {b}")
    print(f"  → {resultado if resultado else 'Sin resultados'}")


# 2. Búsqueda OR — artículos que tienen AL MENOS UNO de los tags
# len(tags_buscados & tags_articulo) > 0
print("\n" + "=" * 60)
print("2. BÚSQUEDA OR (al menos un tag)")
print("=" * 60)

def buscar_or(tags_buscados, articulos_dict):
    resultados = []
    for titulo, tags in articulos_dict.items():
        if len(tags_buscados & tags) > 0:
            resultados.append(titulo)
    return resultados

busquedas_or = [
    {"javascript", "python"},
    {"docker", "kubernetes"},
    {"música", "historia"},
]
for b in busquedas_or:
    resultado = buscar_or(b, articulos)
    print(f"\n  OR {b}")
    print(f"  → {resultado if resultado else 'Sin resultados'}")


# 3. Recomendar artículos similares (Jaccard >= 0.4)
# Jaccard = |A & B| / |A | B|
print("\n" + "=" * 60)
print("3. RECOMENDACIONES POR SIMILITUD (Jaccard ≥ 0.4)")
print("=" * 60)

def jaccard(tags1, tags2):
    interseccion = len(tags1 & tags2)
    union        = len(tags1 | tags2)
    return interseccion / union if union > 0 else 0

def recomendar(titulo, articulos_dict, umbral=0.4):
    tags_base  = articulos_dict[titulo]
    candidatos = []
    for otro_titulo, tags in articulos_dict.items():
        if otro_titulo == titulo:
            continue
        similitud = jaccard(tags_base, tags)
        if similitud >= umbral:
            candidatos.append((otro_titulo, similitud))

    def obtener_similitud(elemento):
        return elemento[1]

    candidatos.sort(key=obtener_similitud, reverse=True)
    return candidatos

articulos_consulta = ["Intro a Python", "Docker para Devs", "SQL avanzado"]
for art in articulos_consulta:
    recomendaciones = recomendar(art, articulos)
    print(f"\n  Leyendo: '{art}'")
    if recomendaciones:
        for titulo, sim in recomendaciones:
            barra = "█" * int(sim * 10)
            print(f"    {barra:<10} {sim:.0%}  →  {titulo}")
    else:
        print("    Sin recomendaciones")


# 4. Tags co-ocurrentes (aparecen juntos en el mismo artículo)
# Para cada par de tags, contar en cuántos artículos aparecen juntos
print("\n" + "=" * 60)
print("4. TAGS CO-OCURRENTES")
print("=" * 60)

coocurrencias = {}
for titulo, tags in articulos.items():
    lista_tags = list(tags)
    for i in range(len(lista_tags)):
        for j in range(i + 1, len(lista_tags)):
            par = tuple(sorted([lista_tags[i], lista_tags[j]]))
            coocurrencias[par] = coocurrencias.get(par, 0) + 1

# Mostrar solo los pares que co-ocurren más de una vez
print("\n  Pares de tags que aparecen juntos en 2+ artículos:")
hay_coocurrencias = False
for par, count in coocurrencias.items():
    if count >= 2:
        print(f"  {par[0]} + {par[1]}: {count} artículos")
        hay_coocurrencias = True
if not hay_coocurrencias:
    print("  Ningún par de tags co-ocurre en 2+ artículos")


# 5. Artículos huérfanos (sin tags en común con ningún otro)
# Un artículo es huérfano si su intersección con TODOS los demás es vacía
print("\n" + "=" * 60)
print("5. ARTÍCULOS HUÉRFANOS")
print("=" * 60)

huerfanos = []
for titulo, tags in articulos.items():
    es_huerfano = True
    for otro_titulo, otros_tags in articulos.items():
        if otro_titulo == titulo:
            continue
        if len(tags & otros_tags) > 0:
            es_huerfano = False
            break
    if es_huerfano:
        huerfanos.append(titulo)

if huerfanos:
    print(f"\n  Artículos sin ningún tag en común con otros:")
    for titulo in huerfanos:
        print(f"    · {titulo}  {articulos[titulo]}")
else:
    print("\n  No hay artículos huérfanos")

    