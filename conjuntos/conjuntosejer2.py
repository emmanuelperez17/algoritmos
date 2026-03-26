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

#peliculas similares que comparten minimo 2 generos, devuelve tuplas ordenadas en lista


peliculas = list(catalogo.keys())   #lista de nombres de peliculas
peliculas_con_generos_en_comun=[]

for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]  
        generos_comunes = catalogo[p1].intersection(catalogo[p2])
        if len(generos_comunes) >= 2:
            peliculas_con_generos_en_comun.append((p1, p2, sorted(generos_comunes)))


peliculas_similares = peliculas_con_generos_en_comun
print(peliculas_similares)

#Que peliculas me recomiendas y con que porcentaje de similitud, si mis favoritas son accion, crimen y aventura, debe
#mostrar una lista, ordenada de mayor a menor porcentaje de similitud, con el nombre de la pelicula y el porcentaje de similitud.

mis_favoritas = {"acción", "crimen", "aventura"}
recomendaciones = []

for pelicula, generos in catalogo.items():
    generos_comunes = mis_favoritas.intersection(generos)
    if generos_comunes:
        porcentaje_similitud = (len(generos_comunes) / len(mis_favoritas)) * 100
        recomendaciones.append((pelicula, porcentaje_similitud))


def obtener_porcentaje(elemento):
    return elemento[1]

recomendaciones.sort(key=obtener_porcentaje, reverse=True)
print(recomendaciones)


# Como puedo mostrar todos los generos que hay en el catalogo, sin repetir, con union

generos_unicos = set()
for generos in catalogo.values():   #valor del diccionario, que es un conjunto de generos
    generos_unicos= generos_unicos.union(generos) #union de conjuntos, equivalente a generos_unicos = generos_unicos.union(generos)
print(generos_unicos)

# Debo mostrar que peliculas de cada genero hay
peliculas_por_genero = {}  #diccionario donde la clave es el genero y el valor es un conjunto de peliculas

for pelicula, generos in catalogo.items():
    for genero in generos:  
        if genero not in peliculas_por_genero:
            peliculas_por_genero[genero]=set()
        peliculas_por_genero[genero].add(pelicula) 
print(peliculas_por_genero)

# Metodo que reciba el nombre de dos peliculas y devuelva el indice de similitud Jaccard

def calcular_indice(p1, p2):
    g1= catalogo[p1]
    g2= catalogo[p2]

    interseccion= len(g1 & g2)
    union= len(g1 | g2)

    return interseccion / union



STOPWORDS= {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "a", "en", "con",
            "por", "para", "y", "o", "que", "es", "son", "se", "su", "sus", "como", "pero", "más",
            "este", "esta", "estos", "estas"}

#leer dos textos, calcular su indice de similitus ignorando los stopword, y si el indice es mayor a 0.6, se copiaron


STOPWORDS = {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "a", "en", "con",
             "por", "para", "y", "o", "que", "es", "son", "se", "su", "sus", "como", "pero", "más",
             "este", "esta", "estos", "estas"}


def limpiar_texto(texto):
    return set(texto.lower().split())- STOPWORDS

def detectar_copia(texto1, texto2):
    palabras1 = limpiar_texto(texto1)
    palabras2 = limpiar_texto(texto2)

    interseccion = palabras1.intersection(palabras2)
    union = palabras1.union(palabras2)

    if not union:
        return 0.0

    indice = len(interseccion) / len(union)

    if indice > 0.6:
        print(f"Se copiaron. Índice Jaccard: {indice:.2f}")
    else:
        print(f"No se copiaron. Índice Jaccard: {indice:.2f}")

    return indice

texto1 = "El gato negro corre rápido por el parque verde"
texto2 = "El gato negro corre veloz por el parque verde"

detectar_copia(texto1, texto2)
"""```

La función `limpiar_texto` hace dos cosas: convierte todo a minúsculas con `.lower()` para que "Gato" y "gato" sean la misma palabra, y luego separa el texto en palabras con `.split()`. De esas palabras filtra las que están en STOPWORDS usando un set comprehension — esas llaves `{}` con un `for` adentro son exactamente igual a una lista comprehension pero el resultado es un set, sin duplicados.

Después `detectar_copia` aplica Jaccard igual que con las películas, solo que ahora en lugar de comparar géneros compara palabras. Si el índice supera 0.6, se copiaron.

Para los textos del ejemplo la salida sería:
```
Se copiaron. Índice Jaccard: 0.78"""