# ════════════════════════════════════════════════════════════════════════
# PARCIAL 1: SISTEMA DE SEGURIDAD MULTINIVEL
# ════════════════════════════════════════════════════════════════════════
"""
ENUNCIADO:
----------
Una empresa implementa un sistema avanzado de control de acceso.

Cada usuario puede tener UNO o MÁS roles.
Cada rol tiene permisos.

Además:
- Existen permisos prohibidos globales.
- Existen permisos obligatorios para ciertas acciones.

El sistema debe:

1. Verificar si un usuario puede realizar una acción compleja
   (requiere múltiples permisos)

2. Detectar si un usuario tiene permisos prohibidos (ERROR CRÍTICO)

3. Encontrar intersección de permisos entre TODOS los roles de un usuario

4. Determinar si un usuario es "superusuario"
   (tiene TODOS los permisos del sistema)

5. Crear un rol limpio a partir de varios roles (eliminando peligrosos)

⚠️ TRAMPAS:
- Usuarios con múltiples roles
- Usuarios sin roles
- Permisos duplicados
- Comparaciones incorrectas de subconjuntos
"""

# ════════════════════════════════════════════════════════════════════════
# DATOS
# ════════════════════════════════════════════════════════════════════════

roles = {
    "admin": {"leer", "escribir", "eliminar", "configurar", "backup"},
    "dev": {"leer", "escribir", "deploy"},
    "ops": {"leer", "monitor", "backup"},
    "guest": {"leer"},
}

usuarios = {
    "Laura": {"admin", "ops"},
    "Diego": {"dev"},
    "Sofia": {"guest"},
    "Carlos": set(),  # ⚠️ TRAMPA: usuario sin roles
}

permisos_prohibidos = {"eliminar", "configurar"}

# ════════════════════════════════════════════════════════════════════════
# 1. VERIFICAR ACCESO COMPLEJO
# ════════════════════════════════════════════════════════════════════════

def puede_hacer(usuario, permisos_requeridos):
    """
    Un usuario puede hacer algo si la UNIÓN de sus roles
    contiene todos los permisos requeridos
    """
    roles_usuario = usuarios.get(usuario, set())

    permisos_totales = set()

    # acumulamos permisos de todos los roles
    for rol in roles_usuario:
        permisos_totales |= roles.get(rol, set())

    # verificamos subconjunto
    return permisos_requeridos <= permisos_totales


print("\n1. VERIFICACIÓN DE ACCESO")
print(puede_hacer("Laura", {"leer", "backup"}))  # True
print(puede_hacer("Diego", {"deploy"}))          # True
print(puede_hacer("Sofia", {"escribir"}))        # False
print(puede_hacer("Carlos", {"leer"}))           # False (TRAMPA)


# ════════════════════════════════════════════════════════════════════════
# 2. DETECTAR PERMISOS PROHIBIDOS
# ════════════════════════════════════════════════════════════════════════

def tiene_permisos_prohibidos(usuario):
    roles_usuario = usuarios.get(usuario, set())

    permisos_totales = set()

    for rol in roles_usuario:
        permisos_totales |= roles.get(rol, set())

    # intersección con prohibidos
    return permisos_totales & permisos_prohibidos


print("\n2. PERMISOS PROHIBIDOS")
for u in usuarios:
    conflicto = tiene_permisos_prohibidos(u)
    if conflicto:
        print(f"{u} → PROHIBIDOS: {conflicto}")


# ════════════════════════════════════════════════════════════════════════
# 3. INTERSECCIÓN DE ROLES (MUY IMPORTANTE)
# ════════════════════════════════════════════════════════════════════════

def permisos_comunes(usuario):
    """
    Intersección de TODOS los roles del usuario
    ⚠️ TRAMPA: si no se inicializa bien, falla
    """
    roles_usuario = usuarios.get(usuario)

    if not roles_usuario:
        return set()

    lista_roles = list(roles_usuario)

    comunes = roles[lista_roles[0]].copy()

    for rol in lista_roles[1:]:
        comunes &= roles[rol]

    return comunes


print("\n3. PERMISOS COMUNES ENTRE ROLES")
print("Laura:", permisos_comunes("Laura"))


# ════════════════════════════════════════════════════════════════════════
# 4. DETECTAR SUPERUSUARIO
# ════════════════════════════════════════════════════════════════════════

# todos los permisos del sistema
todos_permisos = set()
for p in roles.values():
    todos_permisos |= p

def es_superusuario(usuario):
    roles_usuario = usuarios.get(usuario, set())

    permisos_totales = set()
    for rol in roles_usuario:
        permisos_totales |= roles.get(rol, set())

    return permisos_totales == todos_permisos


print("\n4. SUPERUSUARIO")
for u in usuarios:
    print(u, es_superusuario(u))


# ════════════════════════════════════════════════════════════════════════
# 5. CREAR ROL LIMPIO
# ════════════════════════════════════════════════════════════════════════

def crear_rol_seguro(lista_roles):
    """
    Une roles pero elimina permisos peligrosos
    """
    nuevo = set()

    for rol in lista_roles:
        nuevo |= roles.get(rol, set())

    # eliminar peligrosos
    return nuevo - permisos_prohibidos


print("\n5. ROL LIMPIO")
print(crear_rol_seguro(["admin", "dev"]))