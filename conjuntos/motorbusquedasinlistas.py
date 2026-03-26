# ═══════════════════════════════════════════════════════
#   CMS - MOTOR DE BÚSQUEDA POR TAGS (sets nativos)
# ═══════════════════════════════════════════════════════

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

# ─────────────────────────────────────────
# 1. BÚSQUEDA AND
#    Artículos que tienen TODOS los tags buscados
#    tags_buscados <= tags_articulo
# ─────────────────────────────────────────
def buscar_and(tags_buscados):
    resultados = set()
    for titulo, tags in articulos.items():
        if tags_buscados <= tags:          # subconjunto: todos los buscados están en el artículo
            resultados.add(titulo)
    return resultados

print("1. BÚSQUEDA AND")
busquedas_and = [
    {"python", "tutorial"},
    {"docker", "devops"},
    {"machine-learning", "python"},
]
for b in busquedas_and:
    print(f"  AND {b} → {buscar_and(b)}")


# ─────────────────────────────────────────
# 2. BÚSQUEDA OR
#    Artículos que tienen AL MENOS UN tag buscado
#    tags_buscados & tags != vacío
# ─────────────────────────────────────────
def buscar_or(tags_buscados):
    resultados = set()
    for titulo, tags in articulos.items():
        if tags_buscados & tags:           # intersección no vacía = tienen algo en común
            resultados.add(titulo)
    return resultados

print("\n2. BÚSQUEDA OR")
busquedas_or = [
    {"javascript", "python"},
    {"docker", "kubernetes"},
    {"música", "historia"},
]
for b in busquedas_or:
    print(f"  OR {b} → {buscar_or(b)}")


# ─────────────────────────────────────────
# 3. RECOMENDACIONES POR SIMILITUD (Jaccard)
#    Jaccard = |A & B| / |A | B|
#    Solo recomienda si similitud >= 0.4
# ─────────────────────────────────────────
def jaccard(tags1, tags2):
    interseccion = len(tags1 & tags2)
    union        = len(tags1 | tags2)
    return interseccion / union if union > 0 else 0

def recomendar(titulo, umbral=0.4):
    tags_base    = articulos[titulo]
    candidatos   = set()
    similitudes  = {}

    for otro_titulo, tags in articulos.items():
        if otro_titulo == titulo:
            continue
        sim = jaccard(tags_base, tags)
        if sim >= umbral:
            candidatos.add(otro_titulo)
            similitudes[otro_titulo] = sim

    return sorted(candidatos, key=lambda x: similitudes[x], reverse=True), similitudes

print("\n3. RECOMENDACIONES (Jaccard >= 0.4)")
for art in {"Intro a Python", "Docker para Devs", "SQL avanzado"}:
    candidatos, similitudes = recomendar(art)
    print(f"\n  Leyendo: '{art}'")
    if candidatos:
        for titulo in candidatos:
            barra = "█" * int(similitudes[titulo] * 10)
            print(f"    {barra:<10} {similitudes[titulo]:.0%} → {titulo}")
    else:
        print("    Sin recomendaciones")


# ─────────────────────────────────────────
# 4. TAGS CO-OCURRENTES
#    Pares de tags que aparecen juntos en 2+ artículos
# ─────────────────────────────────────────
coocurrencias = {}

for titulo, tags in articulos.items():
    lista_tags = list(tags)
    for i in range(len(lista_tags)):
        for j in range(i + 1, len(lista_tags)):
            par = tuple(sorted([lista_tags[i], lista_tags[j]]))
            coocurrencias[par] = coocurrencias.get(par, 0) + 1

print("\n4. TAGS CO-OCURRENTES (aparecen juntos en 2+ artículos)")
pares_frecuentes = {par for par, count in coocurrencias.items() if count >= 2}

if pares_frecuentes:
    for par in pares_frecuentes:
        print(f"  {par[0]} + {par[1]}: {coocurrencias[par]} artículos")
else:
    print("  Ningún par co-ocurre en 2+ artículos")


# ─────────────────────────────────────────
# 5. ARTÍCULOS HUÉRFANOS
#    Sin ningún tag en común con ningún otro artículo
# ─────────────────────────────────────────
huerfanos = set()

for titulo, tags in articulos.items():
    otros_tags = set()
    for otro_titulo, tags_otro in articulos.items():
        if otro_titulo != titulo:
            otros_tags |= tags_otro          # acumula todos los tags ajenos

    if tags.isdisjoint(otros_tags):          # si no comparte nada con nadie
        huerfanos.add(titulo)

print("\n5. ARTÍCULOS HUÉRFANOS")
if huerfanos:
    for titulo in huerfanos:
        print(f"  · {titulo}: {articulos[titulo]}")
else:
    print("  No hay artículos huérfanos")