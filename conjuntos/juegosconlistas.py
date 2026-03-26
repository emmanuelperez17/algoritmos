"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO: TORNEO - ASIGNACIÓN DE EQUIPOS POR JUEGOS
Clase Conjunto con lista enlazada
Algoritmos y Programación 4 - Semana 7
═══════════════════════════════════════════════════════════════════════

════════
Un torneo asigna jugadores a equipos basándose en los juegos que dominan.
1. Dos jugadores pueden ser compañeros si dominan al menos 2 juegos en común
2. Encontrar todos los pares válidos de compañeros
3. Calcular la "brecha de habilidad" entre dos jugadores (diferencia simétrica)
4. Encontrar el jugador más versátil (domina más juegos)
5. Encontrar juegos que solo domina UNA persona (juegos raros)
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

    def diferencia_simetrica(self, otro):
        return self.diferencia(otro).union(otro.diferencia(self))

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

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

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

jugadores = {
    "Xander": Conjunto(["CS2", "Valorant", "Apex", "Overwatch"]),
    "Zara":   Conjunto(["Valorant", "Apex", "Fortnite", "Warzone"]),
    "Kai":    Conjunto(["CS2", "Valorant", "Overwatch", "R6"]),
    "Nyx":    Conjunto(["Fortnite", "Warzone", "Apex"]),
    "Rex":    Conjunto(["Minecraft", "Terraria", "Stardew"]),
    "Luna":   Conjunto(["CS2", "R6", "Overwatch", "Valorant"]),
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   TORNEO - ASIGNACIÓN DE EQUIPOS (lista enlazada)")
print("=" * 60)

print("\nJugadores y juegos:")
for jugador, juegos in jugadores.items():
    print(f"  {jugador}: {juegos}")


# 1. ¿Dos jugadores pueden ser compañeros?
# Intersección >= 2 juegos en común
print("\n" + "=" * 60)
print("1. VERIFICAR SI DOS JUGADORES SON COMPAÑEROS")
print("=" * 60)

def pueden_ser_companeros(j1, j2, jugadores_dict):
    en_comun = jugadores_dict[j1].interseccion(jugadores_dict[j2])
    return en_comun.cardinalidad() >= 2

verificaciones = [
    ("Xander", "Kai"),
    ("Zara",   "Nyx"),
    ("Rex",    "Luna"),
    ("Xander", "Luna"),
]
for j1, j2 in verificaciones:
    resultado = pueden_ser_companeros(j1, j2, jugadores)
    en_comun  = jugadores[j1].interseccion(jugadores[j2])
    simbolo   = "✓" if resultado else "✗"
    print(f"  {simbolo} {j1} + {j2}: {en_comun.cardinalidad()} juegos en común → {en_comun}")


# 2. Todos los pares válidos de compañeros
print("\n" + "=" * 60)
print("2. TODOS LOS PARES VÁLIDOS")
print("=" * 60)

nombres = list(jugadores.keys())
pares_validos = []

for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        j1, j2 = nombres[i], nombres[j]
        if pueden_ser_companeros(j1, j2, jugadores):
            en_comun = jugadores[j1].interseccion(jugadores[j2])
            pares_validos.append((j1, j2, en_comun))

print(f"\n  Total de pares válidos: {len(pares_validos)}")
for j1, j2, en_comun in pares_validos:
    print(f"  {j1} + {j2}: {en_comun}")


# 3. Brecha de habilidad (diferencia simétrica)
print("\n" + "=" * 60)
print("3. BRECHA DE HABILIDAD")
print("=" * 60)

def brecha_habilidad(j1, j2, jugadores_dict):
    return jugadores_dict[j1].diferencia_simetrica(jugadores_dict[j2])

pares_brecha = [
    ("Xander", "Kai"),
    ("Zara",   "Nyx"),
    ("Xander", "Rex"),
]
for j1, j2 in pares_brecha:
    brecha  = brecha_habilidad(j1, j2, jugadores)
    solo_j1 = jugadores[j1].diferencia(jugadores[j2])
    solo_j2 = jugadores[j2].diferencia(jugadores[j1])
    print(f"\n  {j1} vs {j2}:")
    print(f"    Brecha total ({brecha.cardinalidad()} juegos): {brecha}")
    print(f"    Solo {j1}: {solo_j1}")
    print(f"    Solo {j2}: {solo_j2}")


# 4. Jugador más versátil (domina más juegos)
print("\n" + "=" * 60)
print("4. JUGADOR MÁS VERSÁTIL")
print("=" * 60)

max_juegos   = -1
mas_versatil = None

for jugador, juegos in jugadores.items():
    if juegos.cardinalidad() > max_juegos:
        max_juegos   = juegos.cardinalidad()
        mas_versatil = jugador

print(f"\n  Jugador más versátil: {mas_versatil} ({max_juegos} juegos)")

print("\n  Ranking:")
ranking = list(jugadores.items())

def obtener_cantidad(elemento):
    return elemento[1].cardinalidad()

ranking.sort(key=obtener_cantidad, reverse=True)

for jugador, juegos in ranking:
    barra = "█" * juegos.cardinalidad()
    print(f"  {jugador:<8} {barra} ({juegos.cardinalidad()})")


# 5. Juegos raros (solo los domina una persona)
print("\n" + "=" * 60)
print("5. JUEGOS RAROS (solo los domina una persona)")
print("=" * 60)

conteo_juegos = {}
for jugador, juegos in jugadores.items():
    for juego in juegos:
        conteo_juegos[juego] = conteo_juegos.get(juego, 0) + 1

juegos_raros = {}
for juego, count in conteo_juegos.items():
    if count == 1:
        for jugador, juegos in jugadores.items():
            if juegos.pertenece(juego):
                juegos_raros[juego] = jugador

print(f"\n  Total de juegos raros: {len(juegos_raros)}")
for juego, jugador in juegos_raros.items():
    print(f"  {juego:<12} → solo lo domina {jugador}")

