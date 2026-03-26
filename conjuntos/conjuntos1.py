"""
A=[5,7,9,9,2,3,1,5,7,5,8,6,3,2]
A=list(set(A))

print(A)"""

"""amigos_juan={"Maria", "Pedro", "Ana", "Carlos", "Laura"}
amigos_maria={"Pedro", "Laura", "Sofia", "Diego", "Ana", "Juan"}

comunes= amigos_maria.intersection(amigos_juan)

ordenados= sorted(comunes)

cont=len(amigos_juan.union(amigos_maria))

print("Amigos en comun: ", comunes)
print("Amigos en común:",ordenados)
print("Cantidad:", cont)
print(f"Amigos que no son en comun: {amigos_juan^ amigos_maria}")"""

print("\n" + "=" * 60)
print("6. Búsqueda eficiente")
print("=" * 60)

# Lista vs Set para búsqueda
import time

# Crear datos
datos_lista = list(range(100000))
datos_set = set(range(100000))

# Buscar elemento
elemento = 99999

# Búsqueda en lista
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_lista
tiempo_lista = time.time() - inicio

# Búsqueda en set
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_set
tiempo_set = time.time() - inicio

print(f"Tiempo búsqueda en lista: {tiempo_lista:.4f}s")
print(f"Tiempo búsqueda en set: {tiempo_set:.4f}s")
