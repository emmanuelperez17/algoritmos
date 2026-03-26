"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 1: SPOTIFY - PLAYLISTS COMPARTIDAS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Spotify quiere implementar una función de "Playlists Compartidas".
Dados dos usuarios con sus canciones favoritas, el sistema debe:

1. Encontrar canciones que ambos disfrutan (para playlist compartida)
2. Sugerir canciones que uno tiene y el otro no
3. Mostrar el catálogo combinado de ambos
4. Verificar si un usuario escucha un subconjunto de lo que escucha otro

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

canciones_juan = {
    "Blinding Lights", "Bohemian Rhapsody", "Shape of You",
    "Despacito", "Hotel California", "Billie Jean",
    "Rolling in the Deep", "Smells Like Teen Spirit"
}

canciones_maria = {
    "Shape of You", "Despacito", "Bad Guy",
    "Blinding Lights", "Watermelon Sugar", "Levitating",
    "Rolling in the Deep", "drivers license"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print(f"\nCanciones de Juan ({len(canciones_juan)}):")
for c in sorted(canciones_juan):
    print(f"  ♪ {c}")

print(f"\nCanciones de María ({len(canciones_maria)}):")
for c in sorted(canciones_maria):
    print(f"  ♪ {c}")

# 1. Playlist compartida (intersección)
compartidas = canciones_juan & canciones_maria
print(f"\n1. Playlist compartida ({len(compartidas)} canciones):")
for c in sorted(compartidas):
    print(f"  ♪ {c}")

# 2. Sugerencias (diferencia)
sugerencias_para_juan = canciones_maria - canciones_juan
sugerencias_para_maria = canciones_juan - canciones_maria

print(f"\n2. Sugerencias para Juan ({len(sugerencias_para_juan)}):")
for c in sorted(sugerencias_para_juan):
    print(f"  → {c}")

print(f"\n   Sugerencias para María ({len(sugerencias_para_maria)}):")
for c in sorted(sugerencias_para_maria):
    print(f"  → {c}")

# 3. Catálogo combinado (unión)
catalogo = canciones_juan | canciones_maria
print(f"\n3. Catálogo combinado ({len(catalogo)} canciones únicas):")
for c in sorted(catalogo):
    print(f"  ♪ {c}")

# 4. ¿Un usuario escucha subconjunto del otro?
print(f"\n4. ¿Juan escucha subconjunto de María? {canciones_juan <= canciones_maria}")
print(f"   ¿María escucha subconjunto de Juan? {canciones_maria <= canciones_juan}")

# Bonus: Canciones exclusivas (diferencia simétrica)
exclusivas = canciones_juan ^ canciones_maria
print(f"\n5. Canciones que solo uno de los dos escucha ({len(exclusivas)}):")
for c in sorted(exclusivas):
    print(f"  ♪ {c}")
