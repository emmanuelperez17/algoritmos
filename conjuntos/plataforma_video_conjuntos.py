juegos_pc = {"Minecraft", "Valorant", "League of Legends", "GTA V", "Cyberpunk 2077", "Fortnite"}
juegos_consola = {"GTA V", "FIFA 24", "God of War", "Fortnite", "Minecraft", "Spider-Man"}

# Juegos disponibles en ambas plataformas
ambos= juegos_pc.intersection(juegos_consola)
print(ambos)

# ¿Qué juegos son exclusivos de PC? ¿Y exclusivos de consola?
exclusivos_pc= juegos_pc- juegos_consola
print(exclusivos_pc)

exclusivos_consola= juegos_consola-juegos_pc
print(exclusivos_consola)

# ¿Cuál es el catálogo completo de la tienda (sin repetidos)?
catalogo_completo= juegos_pc.union(juegos_consola)
print(catalogo_completo)

# ¿Qué juegos están en solo una de las dos plataformas?
solo_una_plataforma= exclusivos_pc | exclusivos_consola
print(solo_una_plataforma)

#¿Es juegos_pc subconjunto del catálogo completo? ¿Y juegos_consola?
if juegos_pc <= catalogo_completo:
    print("Si, los juegos pc son un subconjunto de catalogo completo")
else:
    print("No, juegos_pc no es un subconjunto de catalogo")

if juegos_consola <= catalogo_completo:
    print("Si, juegos consola es un subc de catalogo")
else:
    print("No, juegos consola no es un subconjunto de catalogo")