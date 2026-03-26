"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 4: SEGURIDAD - CONTROL DE ACCESO
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una empresa necesita un sistema de control de acceso basado en roles.
Cada rol tiene un conjunto de permisos. El sistema debe:

1. Verificar si un usuario puede realizar una acción
2. Encontrar permisos comunes entre roles
3. Encontrar permisos exclusivos de cada rol
4. Verificar si un rol es "superior" a otro (tiene todos sus permisos)
5. Crear un nuevo rol combinando permisos de otros

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}

usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SEGURIDAD - CONTROL DE ACCESO")
print("=" * 60)

print("\nRoles y permisos:")
for rol, permisos in roles.items():
    print(f"  {rol}: {sorted(permisos)}")

print("\nUsuarios:")
for usuario, rol in usuarios.items():
    print(f"  {usuario} → {rol}")

# 1. Verificar si un usuario puede realizar una acción
print("\n" + "=" * 60)
print("1. VERIFICAR ACCESO")
print("=" * 60)

def puede_hacer(usuario, acciones_requeridas):
    """Verifica si el usuario tiene todos los permisos necesarios"""
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos = roles.get(rol, set()) 
    return acciones_requeridas <= permisos  # subconjunto

verificaciones = [
    ("Juan", {"leer", "eliminar"}),
    ("María", {"leer", "escribir"}),
    ("María", {"eliminar"}),
    ("Pedro", {"leer"}),
    ("Pedro", {"escribir"}),
    ("Ana", {"leer", "ver_logs"}),
]

for usuario, acciones in verificaciones:
    resultado = "✓" if puede_hacer(usuario, acciones) else "✗"
    print(f"  {resultado} {usuario} → {acciones}")

# 2. Permisos comunes entre roles
print("\n" + "=" * 60)
print("2. PERMISOS COMUNES" \
"")
print("=" * 60)

pares_roles = [
    ("editor", "moderador"),
    ("moderador", "auditor"),
    ("editor", "auditor"),
]

for r1, r2 in pares_roles:
    comunes = roles[r1] & roles[r2]
    print(f"  {r1} ∩ {r2}: {sorted(comunes)}")

# 3. Permisos exclusivos de cada rol
print("\n" + "=" * 60)
print("3. PERMISOS EXCLUSIVOS")
print("=" * 60)

for nombre, permisos in roles.items(): 
    otros_permisos = set()
    for otro_nombre, otros in roles.items(): # a
        if otro_nombre != nombre:
            otros_permisos = otros_permisos | otros # va acumulando los permisos de otros roles en un solo set
    exclusivos = permisos - otros_permisos
    if exclusivos:
        print(f"  {nombre}: {sorted(exclusivos)}")
    else:
        print(f"  {nombre}: (ninguno exclusivo)")

# 4. ¿Un rol es "superior" a otro?
print("\n" + "=" * 60)
print("4. JERARQUÍA DE ROLES")
print("=" * 60)

for r1 in roles:
    for r2 in roles:    
        if r1 != r2 and roles[r2] < roles[r1]:
            print(f"  {r1} contiene todos los permisos de {r2}") #entre sets significa subconjunto estricto, es decir: ¿todos los permisos de r2 están en r1, Y además r1 tiene permisos extra?

# 5. Crear nuevo rol combinando otros
print("\n" + "=" * 60)
print("5. CREAR ROL COMBINADO")
print("=" * 60)

nuevo_rol = roles["editor"] | roles["auditor"]
print(f"  editor + auditor = {sorted(nuevo_rol)}")

# Verificar que no tenga permisos peligrosos
permisos_peligrosos = {"eliminar", "crear_usuarios", "configurar"}
conflictos = nuevo_rol & permisos_peligrosos
if conflictos:
    print(f"  Alerta: tiene permisos peligrosos: {conflictos}")
else:
    print(f"  Sin permisos peligrosos")

