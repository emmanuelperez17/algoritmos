# ═══════════════════════════════════════════════════════
#   TORNEO - ASIGNACIÓN DE EQUIPOS (con sets)
# ═══════════════════════════════════════════════════════

jugadores = {
    "Xander": {"CS2", "Valorant", "Apex", "Overwatch"},
    "Zara":   {"Valorant", "Apex", "Fortnite", "Warzone"},
    "Kai":    {"CS2", "Valorant", "Overwatch", "R6"},
    "Nyx":    {"Fortnite", "Warzone", "Apex"},
    "Rex":    {"Minecraft", "Terraria", "Stardew"},
    "Luna":   {"CS2", "R6", "Overwatch", "Valorant"},
}

# ─────────────────────────────────────────
# 1. ¿DOS JUGADORES PUEDEN SER COMPAÑEROS?
#    Condición: al menos 2 juegos en común
# ─────────────────────────────────────────
def pueden_ser_companeros(j1, j2):
    en_comun = jugadores[j1] & jugadores[j2]
    return len(en_comun) >= 2

verificaciones = [("Xander", "Kai"), ("Zara", "Nyx"), ("Rex", "Luna"), ("Xander", "Luna")]

for j1, j2 in verificaciones:
    en_comun = jugadores[j1] & jugadores[j2]
    simbolo  = "✓" if pueden_ser_companeros(j1, j2) else "✗"
    print(f"{simbolo} {j1} + {j2}: {len(en_comun)} juegos en común → {en_comun}")


# ─────────────────────────────────────────
# 2. TODOS LOS PARES VÁLIDOS
# ─────────────────────────────────────────
nombres      = list(jugadores.keys())
pares_validos = []

for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        j1, j2 = nombres[i], nombres[j]
        en_comun = jugadores[j1] & jugadores[j2]
        if len(en_comun) >= 2:
            pares_validos.append((j1, j2, en_comun))

print(f"\nTotal pares válidos: {len(pares_validos)}")
for j1, j2, en_comun in pares_validos:
    print(f"  {j1} + {j2}: {en_comun}")


# ─────────────────────────────────────────
# 3. BRECHA DE HABILIDAD
#    Diferencia simétrica = juegos que no comparten
# ─────────────────────────────────────────
pares_brecha = [("Xander", "Kai"), ("Zara", "Nyx"), ("Xander", "Rex")]

for j1, j2 in pares_brecha:
    brecha  = jugadores[j1] ^ jugadores[j2]   # diferencia simétrica
    solo_j1 = jugadores[j1] - jugadores[j2]   # solo los tiene j1
    solo_j2 = jugadores[j2] - jugadores[j1]   # solo los tiene j2
    print(f"\n{j1} vs {j2}:")
    print(f"  Brecha total ({len(brecha)} juegos): {brecha}")
    print(f"  Solo {j1}: {solo_j1}")
    print(f"  Solo {j2}: {solo_j2}")


# ─────────────────────────────────────────
# 4. JUGADOR MÁS VERSÁTIL
#    El que domina más juegos
# ─────────────────────────────────────────
ranking = sorted(jugadores.items(), key=lambda x: len(x[1]), reverse=True)

print("\nRanking de versatilidad:")
for jugador, juegos in ranking:
    barra = "█" * len(juegos)
    print(f"  {jugador:<8} {barra} ({len(juegos)})")

print(f"\nMás versátil: {ranking[0][0]} con {len(ranking[0][1])} juegos")


# ─────────────────────────────────────────
# 5. JUEGOS RAROS
#    Juegos que solo domina UNA persona
# ─────────────────────────────────────────
conteo = {}
for jugador, juegos in jugadores.items():
    for juego in juegos:
        conteo[juego] = conteo.get(juego, 0) + 1

print("\nJuegos raros (solo los domina una persona):")
for juego, cantidad in conteo.items():
    if cantidad == 1:
        duenio = [j for j, juegos in jugadores.items() if juego in juegos][0]
        print(f"  {juego:<12} → solo lo domina {duenio}")