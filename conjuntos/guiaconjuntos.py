# =============================================================================
#   GUÍA DE OPERACIONES DE CONJUNTOS
#   Cuándo usar cada operación · Cómo recorrer · Preguntas de examen
#   Algoritmos y Programación 4 — Semana 7
# =============================================================================


# =============================================================================
# SECCIÓN 0 — TABLA DE REFERENCIA RÁPIDA
# =============================================================================
# Antes de estudiar cada operación en detalle, usa esta tabla para orientarte
# rápido durante el examen.
#
#  Operación                | Sets nativos      | Clase Conjunto
#  -------------------------|-------------------|----------------------------
#  Unión A ∪ B              | A | B             | A.union(B)
#  Intersección A ∩ B       | A & B             | A.interseccion(B)
#  Diferencia A − B         | A - B             | A.diferencia(B)
#  Diferencia simétrica A△B | A ^ B             | A.diferencia_simetrica(B)
#  Subconjunto A ⊆ B        | A <= B            | A.es_subconjunto(B)
#  Subconjunto propio A ⊂ B | A < B             | no existe — implementar manual
#  Igualdad A = B           | A == B            | A.es_igual(B)
#  Pertenencia x ∈ A        | x in A            | A.pertenece(x)
#  Cardinalidad |A|         | len(A)            | A.cardinalidad()
#  ¿Vacío?                  | not A o len(A)==0 | A.esta_vacio()
#  Disjuntos A ∩ B = ∅      | A.isdisjoint(B)   | A.interseccion(B).esta_vacio()
#  |A ∪ B| sin calcular     |  —                | —
#  Fórmula cardinalidad     | |A∪B|=|A|+|B|−|A∩B| | |A∪B|=|A|+|B|−|A∩B|
# =============================================================================


# =============================================================================
# SECCIÓN 1 — INTERSECCIÓN (A ∩ B)
# =============================================================================
# ¿Qué hace?
#   Devuelve los elementos que están en A Y en B al mismo tiempo.
#   Si algo está en A pero no en B, o viceversa, no aparece en el resultado.
#
# ¿Cuándo usarla? — Palabras clave
#   Busca: "en común", "comparten", "ambos tienen", "coinciden", "juntos",
#          "playlist compartida", "amigos mutuos", "juegos que dominan los dos"
#
# ¿Se recorre el diccionario?
#   - Si la pregunta es sobre DOS elementos específicos → NO se recorre. Se aplica directo.
#   - Si la pregunta es sobre TODOS los pares o TODOS los elementos → SÍ se recorre con .items()

# Patrón básico — dos elementos específicos
# ¿Qué juegos tienen en común Xander y Kai?
from metodosconjuntolistas import Conjunto


en_comun = jugadores['Xander'].interseccion(jugadores['Kai'])
print(en_comun)  # no se recorre el diccionario

# Patrón con recorrido — todos los pares
# ¿Qué canciones comparten cada par de usuarios?
# Se recorre con .items() para tener nombre Y conjunto
for u1, canciones1 in usuarios.items():
    for u2, canciones2 in usuarios.items():
        if u1 != u2:
            comunes = canciones1.interseccion(canciones2)
            print(f'{u1} y {u2}: {comunes}')

# Patrón con recorrido — filtrar quién cumple condición
# Jugadores que tienen AL MENOS 2 juegos en común con Xander
# Se recorre .items() porque necesitamos nombre Y conjunto
for jugador, juegos in jugadores.items():
    if jugador == 'Xander':
        continue
    en_comun = jugadores['Xander'].interseccion(juegos)
    if en_comun.cardinalidad() >= 2:
        print(f'{jugador}: {en_comun}')

# ¿.items(), .keys() o .values()?
#   .items()  cuando necesitas TANTO el nombre como el conjunto.
#   .values() cuando solo necesitas el conjunto.
#   .keys()   casi nunca en conjuntos.

# --- Preguntas típicas de examen — Intersección ---
#
# P1: Dado un sistema de streaming, ¿cómo encuentras las películas que le
#     gustan a AMBOS usuarios Ana y Luis?
#     → peliculas['Ana'].interseccion(peliculas['Luis'])
#       No necesitas recorrer el diccionario porque ya sabes exactamente quiénes son.
#
# P2: En un torneo, ¿cómo verificas si dos jugadores pueden ser compañeros
#     (deben compartir al menos 2 juegos)?
#     → en_comun = jugadores[j1].interseccion(jugadores[j2])
#       return en_comun.cardinalidad() >= 2
#
# P3: ¿Cómo encuentras todos los pares de artículos de un blog que comparten
#     al menos 1 tag?
#     → Recorres con dos for anidados sobre .items(). El j siempre empieza
#       en i+1 para no repetir pares. Dentro verificas si la intersección no está vacía.
#
nombres = list(articulos.keys())

for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        a1 = nombres[i]
        a2 = nombres[j]

        tags1 = articulos[a1]
        tags2 = articulos[a2]

        comunes = tags1.interseccion(tags2)

        # Verificamos si hay al menos 1 tag en común
        if not comunes.esta_vacio():
            print(f"{a1} - {a2}: {comunes}")

# P4: En una red social, ¿cómo calculas los amigos en común entre dos usuarios?
#     → red['Ana'].interseccion(red['Carlos'])
#       Si además necesitas el conteo: .cardinalidad() sobre el resultado.

# Ejemplo completo — pares válidos de compañeros
nombres_vistos = Conjunto()
for j1, juegos1 in jugadores.items():
    nombres_vistos.agregar(j1)
    for j2, juegos2 in jugadores.items():
        if j2 == j1 or nombres_vistos.pertenece(j2):
            continue
        en_comun = juegos1.interseccion(juegos2)
        if en_comun.cardinalidad() >= 2:
            print(f'{j1} + {j2}: {en_comun}')


# =============================================================================
# SECCIÓN 2 — DIFERENCIA (A − B)
# =============================================================================
# ¿Qué hace?
#   Devuelve los elementos que están en A pero NO están en B.
#   Lo que tiene A de exclusivo respecto a B. El orden importa: A − B ≠ B − A.
#
# ¿Cuándo usarla? — Palabras clave
#   Busca: "le falta", "no tiene", "solo en A", "exclusivo de",
#          "sugerencias para", "permisos faltantes", "ingredientes que me faltan",
#          "canciones que tiene uno pero no el otro"

# Patrón básico — qué le falta a A para llegar a B
# ¿Qué ingredientes me faltan para hacer Panqueques?
faltantes = recetas['Panqueques'].diferencia(mis_ingredientes)
print(faltantes)  # lo que tiene la receta que yo no tengo

# Patrón con recorrido — filtrar recetas con exactamente 1 faltante
# Recetas donde solo me falta 1 ingrediente
# Se recorre .items() porque necesito nombre Y conjunto
for nombre, ingredientes in recetas.items():
    faltantes = ingredientes.diferencia(mis_ingredientes)
    if faltantes.cardinalidad() == 1:
        print(f'{nombre} → te falta: {faltantes}')

# Patrón con recorrido — sugerencias cruzadas
# Canciones que tiene María que Juan no tiene (sugerencias para Juan)
# No se recorre — se aplica directo con los dos usuarios específicos
sugerencias = canciones['Maria'].diferencia(canciones['Juan'])
print(f'Sugerencias para Juan: {sugerencias}')

# Si quieres sugerencias para TODOS los usuarios, ahí sí recorres
for usuario, mis_canciones in canciones.items():
    
    todas_las_otros = Conjunto()
    
    for otro, sus_canciones in canciones.items():
        if usuario == otro:
            continue
        
        todas_las_otros = todas_las_otros.union(sus_canciones)
    
    sugerencias = todas_las_otros.diferencia(mis_canciones)
    
    print(f"Sugerencias para {usuario}: {sugerencias}")         
          

# OJO con el orden:
#   A.diferencia(B) → lo que tiene A que no tiene B
#   B.diferencia(A) → lo contrario
# Confundir el orden es el error más común en examen.

# --- Preguntas típicas de examen — Diferencia ---
#
# P5: En el sistema de recetas, ¿cómo encuentras las recetas donde solo te
#     falta 1 ingrediente?
#     → Recorres recetas.items(). Para cada receta calculas
#       ingredientes.diferencia(mis_ingredientes). Si ese resultado tiene
#       cardinalidad 1, esa receta califica. El orden es clave.
#
# P6: En seguridad, ¿cómo encuentras los permisos que le faltan al rol
#     'editor' para igualar al 'moderador'?
#     → roles['moderador'].diferencia(roles['editor'])
#
# P7: ¿Cómo encuentras los ingredientes que tienes pero que nunca aparecen
#     en ninguna receta?
#     → Primero construyes la unión de todos los ingredientes de todas las recetas.
#       Luego: mis_ingredientes.diferencia(todos_en_recetas)

# Ejemplo completo — ingredientes que nunca uso
todos_en_recetas = Conjunto()
for ingredientes in recetas.values():  # solo values, no necesito el nombre
    todos_en_recetas = todos_en_recetas.union(ingredientes)
nunca_uso = mis_ingredientes.diferencia(todos_en_recetas)
print(f'Nunca usas: {nunca_uso}')


# =============================================================================
# SECCIÓN 3 — UNIÓN (A ∪ B)
# =============================================================================
# ¿Qué hace?
#   Devuelve todos los elementos de A más todos los de B, sin repetir.
#   Es la operación más inclusiva — todo lo que existe en alguno de los dos conjuntos.
#
# ¿Cuándo usarla? — Palabras clave
#   Busca: "todos los", "combinado", "catálogo completo", "cobertura total",
#          "fusionar", "reunir", "todos los ingredientes disponibles",
#          "total de juegos en el torneo"

# Patrón básico — combinar dos conjuntos
# Catálogo combinado de canciones de dos usuarios
catalogo = canciones['Juan'].union(canciones['Maria'])
print(f'Total canciones únicas: {catalogo.cardinalidad()}')

# Patrón acumulado — unión de TODOS los elementos del diccionario
# Todos los juegos que aparecen en el torneo (de cualquier jugador)
# Se recorre .values() porque solo necesitamos el conjunto, no el nombre
todos_los_juegos = Conjunto()
for juegos in jugadores.values():
    todos_los_juegos = todos_los_juegos.union(juegos)
print(f'Juegos en el torneo: {todos_los_juegos}')

# Patrón — fusionar dos zonas en una
# Fusionar zona Norte y Sur en NorteSur
# Se aplica directo, sin recorrer
fusion = zonas['Norte'].union(zonas['Sur'])
nuevo_dict = {}
for nombre, personas in zonas.items():
    if nombre != 'Norte' and nombre != 'Sur':
        nuevo_dict[nombre] = personas
nuevo_dict['NorteSur'] = fusion
zonas = nuevo_dict

# ¿.values() o .items()?
#   Si solo necesitas acumular todos los conjuntos (sin importar el nombre), usa .values().
#   Si además necesitas mostrar o comparar el nombre, usa .items().

# --- Preguntas típicas de examen — Unión ---
#
# P8: ¿Cómo calculas cuántos ingredientes únicos existen en total entre todas las recetas?
#     → Recorres recetas.values(). Acumulas con union en cada vuelta.
#       Al final llamas .cardinalidad() sobre el resultado.
#       Este es el patrón de 'unión acumulada'.

todos = Conjunto()

for ingredientes in recetas.values():
    todos = todos.union(ingredientes)

print("Ingredientes únicos:", todos)
print("Cantidad:", todos.cardinalidad())
#
# P9: ¿Cómo fusionas dos zonas de la epidemia en una sola?
#     → fusion = zonas['Norte'].union(zonas['Sur'])
#       Luego construyes un nuevo diccionario copiando todas las zonas excepto
#       las dos originales, y agregas la fusión con el nuevo nombre.
#
# P10: ¿Cómo encuentras todos los tags que existen en el CMS?
#      → Recorres articulos.values() acumulando con union.

# Ejemplo completo — todos los tags del CMS
todos_tags = Conjunto()
for tags in articulos.values():  # .values() suficiente
    todos_tags = todos_tags.union(tags)
print(f'Total de tags únicos: {todos_tags.cardinalidad()}')
print(todos_tags)


# =============================================================================
# SECCIÓN 4 — DIFERENCIA SIMÉTRICA (A △ B)
# =============================================================================
# ¿Qué hace?
#   Devuelve los elementos que están en A o en B, pero NO en ambos.
#   Es como la unión pero quitando lo que comparten.
#   Equivale a (A − B) ∪ (B − A).
#
# ¿Cuándo usarla? — Palabras clave
#   Busca: "solo uno de los dos tiene", "exclusivos de cada uno", "brecha",
#          "diferencia entre ambos", "canciones que no comparten",
#          "lo que los distingue", "qué los hace diferentes"

# Patrón básico
# Brecha de habilidad entre dos jugadores
# Lo que tiene uno que el otro no tiene (en cualquier dirección)
brecha = jugadores['Xander'].diferencia_simetrica(jugadores['Kai'])
print(f'Brecha: {brecha}')

# Para ver desglosado:
solo_xander = jugadores['Xander'].diferencia(jugadores['Kai'])
solo_kai = jugadores['Kai'].diferencia(jugadores['Xander'])
print(f'Solo Xander: {solo_xander}')
print(f'Solo Kai: {solo_kai}')

# Implementación manual en la clase Conjunto
def diferencia_simetrica(self, otro):
    # (A - B) union (B - A)
    return self.diferencia(otro).union(otro.diferencia(self))

# Sets nativos vs Clase Conjunto:
#   Con sets nativos: A ^ B
#   Con la clase:     A.diferencia_simetrica(B)
# La diferencia simétrica es conmutativa: A △ B = B △ A, el orden no importa.

# --- Preguntas típicas de examen — Diferencia simétrica ---
#
# P11: ¿Cómo muestras qué canciones tiene cada usuario pero no el otro
#      (en ambas direcciones)?
#      → canciones['Juan'].diferencia_simetrica(canciones['Maria'])
#        Si quieres desglosado, calculas por separado diferencia en cada dirección.
#
# P12: ¿Cómo encuentras los ingredientes que distinguen dos recetas entre sí?
#      → recetas['Panqueques'].diferencia_simetrica(recetas['Tortilla española'])
#        Si el resultado es vacío, las recetas usan exactamente los mismos ingredientes.
#
# P13: En el inventario de dos bodegas, ¿cómo encuentras los productos que NO
#      están en ambas bodegas?
#      → bodega_norte.diferencia_simetrica(bodega_sur)


# =============================================================================
# SECCIÓN 5 — SUBCONJUNTO (A ⊆ B)
# =============================================================================
# ¿Qué hace?
#   Verifica si TODOS los elementos de A están también en B.
#   Retorna True o False. No devuelve elementos, solo una respuesta sí/no.
#
# ¿Cuándo usarla? — Palabras clave
#   Busca: "puede realizar", "tiene todos los", "cumple todos los requisitos",
#          "está contenido en", "satisface", "verificar acceso",
#          "puede preparar", "rol superior"

# Patrón básico — verificación directa
# ¿Puedo preparar Panqueques con mis ingredientes?
# La receta debe ser subconjunto de mis ingredientes
puedo = recetas['Panqueques'].es_subconjunto(mis_ingredientes)
print(f'¿Puedo hacer Panqueques? {puedo}')

# Patrón con recorrido — filtrar quién cumple
# ¿Qué recetas puedo preparar? (recorrer todas)
for nombre, ingredientes in recetas.items():
    if ingredientes.es_subconjunto(mis_ingredientes):
        print(f'✓ Puedo hacer: {nombre}')

# ¿Qué médicos cubren TODAS las especialidades requeridas?
requeridas = Conjunto(['cardiologia', 'anestesiologia'])
for doctor, especialidades in medicos.items():
    if requeridas.es_subconjunto(especialidades):
        print(f'✓ {doctor} puede operar')

# Dirección del subconjunto — el error más común
# PREGUNTA: ¿puede el usuario hacer la acción?
# La acción requerida debe estar DENTRO de los permisos del usuario
accion_requerida = Conjunto(['leer', 'escribir'])
permisos_usuario = roles['editor']

# CORRECTO: la acción es subconjunto de los permisos
puede = accion_requerida.es_subconjunto(permisos_usuario)

# INCORRECTO: al revés no tiene sentido
# permisos_usuario.es_subconjunto(accion_requerida)  ← MALO

# Regla para recordar la dirección:
#   Pregúntate: ¿lo pequeño está dentro de lo grande?
#   Lo pequeño es el subconjunto (va primero).
#   Lo grande es el otro (va como argumento).

# --- Preguntas típicas de examen — Subconjunto ---
#
# P14: ¿Cómo verificas si una zona de la epidemia está 'contenida'
#      (todos sus casos ya están en la zona controlada)?
#      → zona.es_subconjunto(zona_controlada)

# Zonas con casos
zona_afectada = Conjunto(["caso1", "caso2", "caso3"])
zona_controlada = Conjunto(["caso1", "caso2", "caso3", "caso4", "caso5"])

def esta_contenida(zona, zona_controlada):
    return zona.es_subconjunto(zona_controlada)

# Prueba
if esta_contenida(zona_afectada, zona_controlada):
    print("La zona está contenida")
else:
    print("La zona NO está contenida")
#
# P15: En seguridad, ¿cómo verificas si el rol 'editor' hereda todos los
#      permisos del rol 'viewer'?
#      → roles['viewer'].es_subconjunto(roles['editor'])
#        viewer es el pequeño (subconjunto), editor es el grande.
roles = {
    "viewer": Conjunto(["leer"]),
    "editor": Conjunto(["leer", "escribir"]),
    "admin": Conjunto(["leer", "escribir", "eliminar"])
}

def hereda(rol_pequeno, rol_grande):
    return roles[rol_pequeno].es_subconjunto(roles[rol_grande])

# Pruebas
if hereda("viewer", "editor"):
    print("Editor hereda de Viewer")
else:
    print("Editor NO hereda de Viewer")

if hereda("editor", "viewer"):
    print("Viewer hereda de Editor")
else:
    print("Viewer NO hereda de Editor")
#
# P16: ¿Cómo encuentras los médicos que pueden realizar una cirugía que
#      requiere cardiología Y anestesiología?
#      → Creas un Conjunto con las especialidades requeridas.
#        Recorres medicos.items() y verificas requeridas.es_subconjunto(especialidades)

# Ejemplo completo — médicos aptos para una cirugía
requeridas = Conjunto(['cardiologia', 'anestesiologia'])
aptos = []
for doctor, datos in medicos.items():
    # requeridas debe ser subconjunto de sus especialidades
    if requeridas.es_subconjunto(datos['especialidades']):
        aptos.append(doctor)
print(f'Médicos aptos: {aptos}')


# =============================================================================
# SECCIÓN 6 — PERTENENCIA Y CONTEO
# =============================================================================
# ¿Cuándo usar pertenece() en lugar de las otras operaciones?
# Cuando la pregunta es sobre UN solo elemento específico, no sobre un conjunto completo.
#   La pertenencia verifica si x está en A.
#
#  Busca: "¿tiene el permiso X?", "¿está en la lista?",
#          "¿domina ese juego?", "¿contiene ese ingrediente?"

# Patrón de conteo — el más importante del examen
# El patrón conteo_dict.get(elemento, 0) + 1 aparece en casi todos los ejercicios.
# Sirve para contar cuántas veces aparece algo.

# Contar en cuántas recetas aparece cada ingrediente
conteo = {}
for nombre, ingredientes in recetas.items():  # .items() — necesito recorrer cada receta
    for ing in ingredientes:                  # itero el Conjunto con __iter__
        conteo[ing] = conteo.get(ing, 0) + 1  # si no existe pone 0, luego suma 1

# Resultado: {'sal': 4, 'huevo': 3, 'mantequilla': 2, ...}

# Patrón — buscar el máximo del conteo
# Ingrediente más versátil (aparece en más recetas)
max_count = -1
mas_versatil = None
for elemento, count in conteo.items():
    if count > max_count:
        max_count = count
        mas_versatil = elemento
print(f'Más versátil: {mas_versatil} ({max_count} veces)')

# Patrón — filtrar los que solo aparecen 1 vez (exclusivos / raros)
# Juegos raros — solo los domina una persona
conteo_juegos = {}
for jugador, juegos in jugadores.items():
    for juego in juegos:  # __iter__ recorre el Conjunto
        conteo_juegos[juego] = conteo_juegos.get(juego, 0) + 1

# Ahora filtrar los de count == 1
for juego, count in conteo_juegos.items():
    if count == 1:
        # Buscar quién lo tiene
        for jugador, juegos in jugadores.items():
            if juegos.pertenece(juego):  # pertenece para un elemento
                print(f'{juego} solo lo domina {jugador}')

# --- Preguntas típicas de examen — Pertenencia y conteo ---
#
# P17: ¿Cómo encuentras el tag más usado en el CMS?
#      → Recorres articulos.items() (o .values() si no necesitas el título).
#        Para cada artículo recorres sus tags con for tag in tags.
#        Acumulas en un diccionario conteo[tag] = conteo.get(tag,0)+1.
#        Luego buscas el máximo recorriendo conteo.items().

articulos = {
    "post1": Conjunto(["python", "ia", "datos"]),
    "post2": Conjunto(["python", "web"]),
    "post3": Conjunto(["ia", "ml"]),
}

conteo = {}

# Contar tags
for tags in articulos.values():
    for tag in tags:
        conteo[tag] = conteo.get(tag, 0) + 1

# Buscar el más usado
max_tag = None
max_count = 0

for tag, cantidad in conteo.items():
    if cantidad > max_count:
        max_tag = tag
        max_count = cantidad

print("Tag más usado:", max_tag, "→", max_count)
#
# P18: ¿Cómo detectas los juegos que solo domina una persona en el torneo?
#      → Construyes el conteo recorriendo jugadores.items() y los juegos de cada jugador.
#        Filtras count == 1. Luego para cada juego raro, recorres de nuevo
#        jugadores.items() usando juegos.pertenece(juego) para encontrar quién lo tiene.

articulos = {
    "post1": Conjunto(["python", "ia", "datos"]),
    "post2": Conjunto(["python", "web"]),
    "post3": Conjunto(["ia", "ml"]),
}

conteo = {}

# Contar tags
for tags in articulos.values():
    for tag in tags:
        conteo[tag] = conteo.get(tag, 0) + 1

# Buscar el más usado
max_tag = None
max_count = 0
# Buscar el más usado
for tag, cantidad in conteo.items():
    if cantidad > max_count:
        max_tag = tag
        max_count = cantidad

print("Tag más usado:", max_tag, "→", max_count)
#
# P19: ¿Cómo cuentas en cuántas zonas aparece cada persona de la epidemia?
#      → Recorres zonas.items(). Para cada zona, recorres sus personas con for persona in personas.
#        Acumulas conteo[persona] = conteo.get(persona,0)+1.
#        Después filtras count > 1 para vectores y count == 1 para aislados.

zonas = {
    "zona1": Conjunto(["Ana", "Carlos"]),
    "zona2": Conjunto(["Carlos", "Luis"]),
    "zona3": Conjunto(["Ana"]),
}

conteo = {}

# Contar personas
for zona, personas in zonas.items():
    for persona in personas:
        conteo[persona] = conteo.get(persona, 0) + 1

# Clasificar
repetidos = []
aislados = []

for persona, cantidad in conteo.items():
    if cantidad > 1:
        repetidos.append(persona)
    else:
        aislados.append(persona)

print("En varias zonas:", repetidos)
print("En una sola zona:", aislados)

# Ejemplo completo — vectores y aislados de la epidemia
conteo_zonas = {}
for zona, personas in zonas.items():  # .items() — recorro nombre y conjunto
    for persona in personas:          # __iter__ sobre el Conjunto
        conteo_zonas[persona] = conteo_zonas.get(persona, 0) + 1

# Vectores (en más de una zona)
vectores = Conjunto()
for persona, count in conteo_zonas.items():
    if count > 1:
        vectores.agregar(persona)

# Aislados (en exactamente una zona)
aislados = Conjunto()
for persona, count in conteo_zonas.items():
    if count == 1:
        aislados.agregar(persona)


# =============================================================================
# SECCIÓN 7 — ¿.items(), .keys() o .values()?
# =============================================================================
# Esta es la duda más frecuente. La respuesta depende de qué necesitas dentro del bucle.
#
#  ¿Qué necesito dentro del for? | ¿Cuál usar?  | Ejemplo
#  ------------------------------|--------------|-----------------------------------
#  Nombre + Conjunto             | .items()     | for n, c in d.items()
#  Solo el Conjunto (acumular)   | .values()    | for c in d.values()
#  Solo el Nombre                | .keys()      | for n in d.keys()
#  Nombre para comparar/filtrar  | .items()     | for n, c in d.items() if n != 'X'
#  Imprimir nombre + resultado   | .items()     | print(f'{n}: {c.union(otro)}')

# Usa .items() cuando...
# - Necesitas el nombre Y el conjunto al mismo tiempo
# - Necesitas imprimir o guardar el nombre junto con el resultado
# - Necesitas comparar por nombre (if nombre != 'Juan')
# - Es el caso más común — úsalo cuando tengas duda

# Necesito nombre Y conjunto → .items()
for jugador, juegos in jugadores.items():
    print(f'{jugador}: {juegos}')

for receta, ingredientes in recetas.items():
    faltantes = ingredientes.diferencia(mis_ingredientes)
    print(f'{receta}: faltan {faltantes}')

# Usa .values() cuando...
# - Solo necesitas los conjuntos, no los nombres
# - Estás acumulando (unión total, conteo total)
# - No vas a imprimir ni guardar el nombre

# Solo necesito el conjunto, no el nombre → .values()
# Acumular la unión de todos los tags de los artículos
todos_tags = Conjunto()
for tags in articulos.values():  # el título no importa
    todos_tags = todos_tags.union(tags)

# Contar total de elementos en todos los conjuntos
total = 0
for juegos in jugadores.values():
    total += juegos.cardinalidad()

# Usa .keys() cuando...
# - Solo necesitas los nombres para luego acceder al diccionario manualmente
# - Muy raro en estos ejercicios — casi siempre .items() es mejor

# .keys() — solo si necesito los nombres para acceder después
nombres = jugadores.keys()  # poco común
for n in nombres:
    print(jugadores[n])  # pero esto es igual que .items()


# =============================================================================
# SECCIÓN 8 — PATRONES COMBINADOS
# =============================================================================
# Los problemas de examen más difíciles combinan varias operaciones.
# Aquí están los patrones más frecuentes.

# --- Patrón 1 — Porcentaje de aprovechamiento (Jaccard simplificado) ---
# Pregunta típica: ordenar recetas / películas / artículos por qué tan bien
# encajan con mis gustos.

# % de ingredientes que tengo de cada receta
ranking = []
for nombre, ingredientes in recetas.items():
    tengo = ingredientes.interseccion(mis_ingredientes).cardinalidad()
    total = ingredientes.cardinalidad()
    porcentaje = tengo / total  # número entre 0 y 1
    ranking.append((nombre, porcentaje, tengo, total))

def obtener_porcentaje(elemento):
    return elemento[1]  # [1] es el porcentaje

ranking.sort(key=obtener_porcentaje, reverse=True)
for nombre, pct, tengo, total in ranking:
    print(f'✓ {nombre}: {pct:.0%} ({tengo}/{total})')


# --- Patrón 2 — Índice de Jaccard (similitud entre conjuntos) ---
# Pregunta típica: películas similares, artículos relacionados, usuarios con gustos parecidos.

# Similitud entre dos conjuntos: |A ∩ B| / |A ∪ B|
# Resultado entre 0.0 (nada en común) y 1.0 (idénticos)
def jaccard(c1, c2):
    inter = c1.interseccion(c2).cardinalidad()
    union = c1.union(c2).cardinalidad()
    return inter / union if union > 0 else 0

# Recomendar artículos similares al que estoy leyendo
tags_base = articulos['Intro a Python']
for titulo, tags in articulos.items():
    if titulo == 'Intro a Python':
        continue
    sim = jaccard(tags_base, tags)
    if sim >= 0.4:  # umbral de similitud
        print(f'✓ {sim:.0%} {titulo}')


# --- Patrón 3 — Buscar el máximo de un atributo calculado ---
# Pregunta típica: zona más crítica, jugador más versátil, ingrediente más usado.

# Zona más crítica: más personas exclusivas (no están en ninguna otra zona)
zona_critica = None
max_exclusivos = -1  # empieza en -1, no en 0 # porque puede haber zonas sin exclusivos, y queremos que esas queden por debajo de las que sí tienen exclusivos. 
for zona, personas in zonas.items():
    exclusivos = Conjunto()
    for persona in personas:
        if conteo_zonas[persona] == 1:  # solo aparece en esta zona
            exclusivos.agregar(persona)
    if exclusivos.cardinalidad() > max_exclusivos:
        max_exclusivos = exclusivos.cardinalidad()
        zona_critica = zona
print(f'Zona más crítica: {zona_critica} ({max_exclusivos} exclusivos)')


# --- Patrón 4 — Verificar condición sobre TODOS los elementos (subconjunto manual) ---
# Pregunta típica: zona contenida, rol jerárquico, receta que puedo preparar.

# ¿Está la zona 'Sur' contenida en zona_controlada?
# Una zona está contenida si TODOS sus casos están en zona_controlada
# Esto es exactamente lo que hace es_subconjunto()
for zona, personas in zonas.items():
    if personas.es_subconjunto(zona_controlada):
        print(f'✓ {zona}: CONTENIDA')
    else:
        print(f'✗ {zona}: no contenida')

# Si tuvieras que implementarlo sin es_subconjunto():
contenida = True
for persona in zonas['Sur']:  # __iter__
    if not zona_controlada.pertenece(persona):
        contenida = False
        break


# =============================================================================
# SECCIÓN 9 — BANCO DE PREGUNTAS DE EXAMEN
# =============================================================================

# --- Nivel básico ---
#
# P20: ¿Cómo sabes si un jugador domina un juego específico?
#      → jugadores['Xander'].pertenece('CS2')
#        Es una operación de pertenencia directa, sin recorrer nada.
#
# P21: ¿Cómo obtienes todos los juegos únicos del torneo?
#      → Unión acumulada recorriendo jugadores.values().
#        En cada vuelta: todos_juegos = todos_juegos.union(juegos)
#
# P22: ¿Cuántas canciones tienen en común Juan y María?
#      → canciones['Juan'].interseccion(canciones['Maria']).cardinalidad()
#
# P23: ¿Qué ingredientes le faltan a Ana para hacer Pollo al ajillo?
#      → recetas['Pollo al ajillo'].diferencia(ingredientes_ana)

# --- Nivel intermedio ---
#
# P24: ¿Cómo encuentras todos los artículos del CMS que tienen el tag 'tutorial'?
#      → Recorres articulos.items(). Para cada artículo usas tags.pertenece('tutorial').
#        Alternativa: verificas si Conjunto(['tutorial']).es_subconjunto(tags).

for titulo, tags in articulos.items():
    if tags.pertenece('tutorial'):
        print(f'✓ {titulo} tiene el tag tutorial')

tag_buscado = Conjunto(["tutorial"])

for titulo, tags in articulos.items():
    if tag_buscado.es_subconjunto(tags):
        print(f"✓ {titulo} tiene el tag 'tutorial'")

#
# P25: ¿Cómo detectas usuarios de la red social que no tienen ningún amigo en común
#      con otro usuario específico?
#      → Recorres red.items(). Para cada usuario calculas
#        red[usuario].interseccion(red['Carlos']). Si el resultado está vacío (.esta_vacio()),
#        no tienen amigos en común.
usuario_objetivo = "Carlos"

for usuario, amigos in red.items():
    if usuario == usuario_objetivo:
        continue
    
    comunes = amigos.interseccion(red[usuario_objetivo])
    
    if comunes.esta_vacio():
        print(f"{usuario} NO tiene amigos en común con {usuario_objetivo}")
#
# P26: ¿Cómo ordenas los jugadores de mayor a menor cantidad de juegos que dominan?
#      → Construyes una lista de tuplas (nombre, cardinalidad). Defines función
#        obtener_cantidad que retorna elemento[1]. Llamas .sort(key=obtener_cantidad, reverse=True).

lista = []

# Construir lista de tuplas
for nombre, juegos in jugadores.items():
    lista.append((nombre, juegos.cardinalidad()))

# Función clave
def obtener_cantidad(elem):
    return elem[1]

# Ordenar de mayor a menor
lista.sort(key=obtener_cantidad, reverse=True)

# Mostrar
for nombre, cantidad in lista:
    print(f"{nombre}: {cantidad} juegos")

#
# P27: ¿Cómo verificas si el rol 'moderador' tiene todos los permisos del rol 'editor' y más?
#      → roles['editor'].es_subconjunto(roles['moderador'])
#        Para 'y más' también verificas: not roles['editor'].es_igual(roles['moderador'])

if (roles["editor"].es_subconjunto(roles["moderador"]) and
    not roles["editor"].es_igual(roles["moderador"])):
    
    print("Moderador tiene todos los permisos de editor y más")
else:
    print("No cumple la condición")

# --- Nivel avanzado ---
#
# P28: ¿Cómo construyes el equipo mínimo de médicos para cubrir todas las especialidades?

def equipo_minimo(requeridas, medicos_dict):
    pendientes = requeridas.copiar()  # copia para no modificar el original
    equipo = []
    while not pendientes.esta_vacio():
        mejor_doctor = None
        mejor_cobertura = Conjunto()
        for doctor, datos in medicos_dict.items():
            if doctor in equipo:
                continue
            cobertura = datos['especialidades'].interseccion(pendientes)
            if cobertura.cardinalidad() > mejor_cobertura.cardinalidad():
                mejor_cobertura = cobertura
                mejor_doctor = doctor
        if mejor_doctor is None:
            break  # no hay solución
        equipo.append(mejor_doctor)
        pendientes = pendientes.diferencia(mejor_cobertura)
    return equipo

# P29: ¿Cómo encuentras pares de tags co-ocurrentes (aparecen juntos en 2+ artículos)?
#      → Para cada artículo generas todos los pares posibles de sus tags (dos for anidados
#        con j = i+1). Cada par lo ordenas con sorted() para que sea siempre el mismo.
#        Acumulas en un diccionario conteo. Al final filtras count >= 2.

articulos = {
    "post1": Conjunto(["python", "ia", "datos"]),
    "post2": Conjunto(["python", "web"]),
    "post3": Conjunto(["ia", "ml"]),
    "post4": Conjunto(["python", "ia"]),
}

conteo = {}

# Generar pares
for tags in articulos.values():
    lista_tags = tags.a_lista()  # convertir a lista para usar índices
    
    for i in range(len(lista_tags)):
        for j in range(i + 1, len(lista_tags)):
            
            t1 = lista_tags[i]
            t2 = lista_tags[j]
            
            # ordenar el par para evitar duplicados ("ia","python") = ("python","ia")
            par = tuple(sorted([t1, t2]))
            
            conteo[par] = conteo.get(par, 0) + 1

# Filtrar pares frecuentes
print("Pares co-ocurrentes (≥2):")
for par, cantidad in conteo.items():
    if cantidad >= 2:
        print(f"{par} → {cantidad} veces")
#
# P30: ¿Cómo detectas artículos 'huérfanos' (sin ningún tag en común con ningún otro artículo)?
#      → Para cada artículo, recorres todos los demás y calculas la intersección.
#        Si TODAS las intersecciones están vacías, es huérfano.
#        Usas una bandera es_huerfano = True que cambias a False en cuanto encuentres
#        una intersección no vacía, con break para salir del bucle interno.

print("\nArtículos huérfanos:")

for a1, tags1 in articulos.items():
    es_huerfano = True
    
    for a2, tags2 in articulos.items():
        if a1 == a2:
            continue
        
        comunes = tags1.interseccion(tags2)
        
        if not comunes.esta_vacio():
            es_huerfano = False
            break  # ya encontramos uno en común
    
    if es_huerfano:
        print(f"{a1} es huérfano")

# Ejemplo — artículos huérfanos
huerfanos = []
for titulo, tags in articulos.items():
    es_huerfano = True  # asume huérfano
    for otro_titulo, otros_tags in articulos.items():
        if otro_titulo == titulo:
            continue
        if not tags.interseccion(otros_tags).esta_vacio():
            es_huerfano = False
            break  # ya sé que no es huérfano
    if es_huerfano:
        huerfanos.append(titulo)
print(f'Huérfanos: {huerfanos}')


# =============================================================================
# CHEAT SHEET FINAL — DECIDE EN 3 PREGUNTAS
# =============================================================================

# Pregunta 1: ¿Qué quiero obtener?
#
#   Elementos en común entre A y B      → interseccion()
#   Lo que tiene A que B no tiene       → diferencia()  [orden importa]
#   Todo lo de A más todo lo de B       → union()
#   Lo exclusivo de cada uno            → diferencia_simetrica()
#   ¿A está completamente dentro de B?  → es_subconjunto()
#   ¿x está en A?                       → pertenece()
#   ¿Cuántos tiene A?                   → cardinalidad()

# Pregunta 2: ¿Necesito recorrer el diccionario?
#
#   Dos elementos específicos   → NO recorras, aplica directo
#   Todos los elementos         → SÍ, recorre con for
#   Filtrar los que cumplen algo → SÍ, recorre con for + if
#   Acumular (unión total, conteo) → SÍ, recorre con for

# Pregunta 3: ¿Qué método de recorrido?
#
#   Necesito nombre Y conjunto  → .items()  ← el más común
#   Solo necesito el conjunto   → .values()
#   Solo necesito el nombre     → .keys()   ← muy raro

# ¡Mucho éxito en el examen!
# Algoritmos y Programación 4 — Conjuntos con listas enlazadas