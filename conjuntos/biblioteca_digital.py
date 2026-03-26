suscripciones = {
    "basica":    {"leer_libros", "buscar"},
    "premium":   {"leer_libros", "buscar", "descargar", "sin_anuncios"},
    "estudiante":{"leer_libros", "buscar", "descargar", "acceso_academico"},
    "docente":   {"leer_libros", "buscar", "descargar", "acceso_academico",
                  "subir_material", "ver_estadisticas"},
}

usuarios = {
    "Laura":   "premium",
    "Andrés":  "basica",
    "Sofía":   "estudiante",
    "Marcos":  "docente",
    "Valeria": "basica",
}

# Escribe una función tiene_acceso(usuario, acciones) que verifique si el usuario puede realizar todas las acciones requeridas.
def tiene_acceso(usuario, acciones_requeridas):
    rol= usuarios.get(usuario)
    if not rol:
        return False
    permisos= suscripciones.get(rol, set())
    return acciones_requeridas<= permisos 

# ¿Qué permisos comparten estudiante y docente? ¿Y basica y premium?
permisos_estudiante= suscripciones["estudiante"]
permisos_docente= suscripciones["docente"]
permisos_compartidos_estudiante_docente= permisos_estudiante.intersection(permisos_docente)
permisos_basica= suscripciones["basica"]
permisos_premium= suscripciones["premium"]
permisos_compartidos_basica_premium= permisos_basica.intersection(permisos_premium)

print(suscripciones["estudiante"].intersection(suscripciones["docente"]) )
print(suscripciones["basica"].intersection(suscripciones["premium"]) )

# ¿Qué permisos son exclusivos de docente (que ningún otro plan tiene)?

permisos_exclusivos_docente= suscripciones["docente"]
otros= set()  # va a acumular los permisos de otros roles
for rol, permiso in suscripciones.items():
    if rol != "docente":
        otros |= permiso # va acumulando todos los permisos de otros roles en un solo set
permisos_exclusivos_docente -= otros # permisos exclusivos de docente son los que tiene docente pero no otros roles
print(permisos_exclusivos_docente)

#¿Qué suscripciones son "superiores" a basica? (tienen todos sus permisos y más)
basica_permisos= suscripciones["basica"]
superiores_a_basica= []
for rol, permisos in suscripciones.items():
    if basica_permisos <= permisos and permisos != basica_permisos:
        superiores_a_basica.append(rol)
print(superiores_a_basica)



#La biblioteca quiere crear un plan "coordinador" combinando docente + un permiso nuevo "gestionar_usuarios". Muestra sus permisos y verifica que tenga {"subir_material", "ver_estadisticas"} como subconjunto.

coordinador_permisos= suscripciones["docente"].union({"gestionar_usuarios"})
print(coordinador_permisos)
print({"subir_material", "ver_estadisticas"}.issubset(coordinador_permisos))
