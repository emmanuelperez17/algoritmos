"""
Ejercicio 4: Búsqueda Binaria Recursiva
Semana 3 - Algoritmos Recursivos
"""

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    """
    Busca un elemento en una lista ORDENADA usando búsqueda binaria.
    
    Algoritmo:
        1. Encontrar el elemento del medio
        2. Si es el objetivo, retornar su índice
        3. Si objetivo < medio, buscar en mitad izquierda
        4. Si objetivo > medio, buscar en mitad derecha
        5. Caso base: inicio > fin → no encontrado (-1)
    
    Args:
        lista: Lista ordenada de elementos
        objetivo: Elemento a buscar
        inicio: Índice inicial del rango de búsqueda
        fin: Índice final del rango de búsqueda
    
    Returns:
        Índice del elemento si se encuentra, -1 si no existe
    """
    # Inicializar fin en la primera llamada
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: rango inválido (elemento no encontrado)
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = (inicio + fin) // 2
    
    # Comparar y decidir en qué mitad buscar
    if lista[medio] == objetivo:
        return medio  # Encontrado
    elif objetivo < lista[medio]:
        # Buscar en la mitad izquierda
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        # Buscar en la mitad derecha
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


# ============ PRUEBAS ============
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Lista: {lista}\n")
    
    casos = [
        (7, 3),    # Existe, índice 3
        (1, 0),    # Primer elemento
        (19, 9),   # Último elemento
        (10, -1),  # No existe
        (0, -1),   # Menor que todos
        (20, -1),  # Mayor que todos
    ]
    
    for objetivo, esperado in casos:
        resultado = busqueda_binaria(lista, objetivo)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} buscar({objetivo}) = {resultado} (esperado: {esperado})")
