# ════════════════════════════════════════════════════════════════════════
# PARCIAL 2: MOTOR DE RECOMENDACIÓN
# ════════════════════════════════════════════════════════════════════════
"""
ENUNCIADO:
----------
Una plataforma tipo Netflix necesita un sistema de recomendación.

Cada usuario tiene:
- Películas vistas
- Categorías favoritas

El sistema debe:

1. Recomendar películas basadas en otros usuarios similares
2. Encontrar usuarios con gustos idénticos
3. Detectar usuarios extremos (sin intersección con nadie)
4. Calcular similitud (intersección / unión)
5. Generar super-recomendación combinada

⚠️ TRAMPAS:
- Usuarios sin películas
- División por cero
- Confundir unión con intersección
"""

# ════════════════════════════════════════════════════════════════════════
# DATOS
# ════════════════════════════════════════════════════════════════════════

usuarios = {
    "Ana": {"Matrix", "Avatar", "Titanic"},
    "Juan": {"Matrix", "Avatar"},
    "Pedro": {"Titanic"},
    "Luis": set(),  # TRAMPA
}

# ════════════════════════════════════════════════════════════════════════
# 1. RECOMENDACIÓN
# ════════════════════════════════════════════════════════════════════════

def recomendar(usuario):
    vistas = usuarios.get(usuario, set())
    recomendadas = set()

    for otro, peliculas in usuarios.items():
        if otro != usuario:
            if vistas & peliculas:  # tienen algo en común
                recomendadas |= peliculas

    return recomendadas - vistas


print("\n1. RECOMENDACIONES")
print("Ana:", recomendar("Ana"))


# ════════════════════════════════════════════════════════════════════════
# 2. USUARIOS IGUALES
# ════════════════════════════════════════════════════════════════════════

print("\n2. USUARIOS IGUALES")
for u1 in usuarios:
    for u2 in usuarios:
        if u1 != u2 and usuarios[u1] == usuarios[u2]:
            print(u1, "=", u2)


# ════════════════════════════════════════════════════════════════════════
# 3. USUARIOS AISLADOS
# ════════════════════════════════════════════════════════════════════════

print("\n3. USUARIOS AISLADOS")
for u1 in usuarios:
    aislado = True
    for u2 in usuarios:
        if u1 != u2 and usuarios[u1] & usuarios[u2]:
            aislado = False
    if aislado:
        print(u1)


# ════════════════════════════════════════════════════════════════════════
# 4. SIMILITUD (JACCARD)
# ════════════════════════════════════════════════════════════════════════

def similitud(u1, u2):
    a = usuarios[u1]
    b = usuarios[u2]

    if not (a | b):  # TRAMPA: evitar división por 0
        return 0

    return len(a & b) / len(a | b)


print("\n4. SIMILITUD")
print("Ana vs Juan:", similitud("Ana", "Juan"))


# ════════════════════════════════════════════════════════════════════════
# 5. SUPER RECOMENDACIÓN
# ════════════════════════════════════════════════════════════════════════

def super_recomendacion():
    todas = set()
    for pelis in usuarios.values():
        todas |= pelis
    return todas


print("\n5. SUPER RECOMENDACIÓN")
print(super_recomendacion())