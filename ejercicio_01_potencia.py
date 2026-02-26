"""
Ejercicio 1: Potencia Recursiva
Semana 3 - Algoritmos Recursivos

Implementa una función que calcule base^exponente de forma recursiva.
"""

def potencia(base, exponente):
    """
    Calcula base elevado a exponente de forma recursiva.
    
    Ejemplos:
        potencia(2, 3) = 8
        potencia(5, 0) = 1
        potencia(3, 4) = 81
    
    Caso base: exponente == 0 → retorna 1
    Caso recursivo: base × potencia(base, exponente - 1)
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * base^(exponente-1)
    return base * potencia(base, exponente - 1)


def potencia_optimizada(base, exponente):
    """
    BONUS: Versión optimizada usando la propiedad:
    - Si exponente es par: base^n = (base^(n/2))^2
    - Si exponente es impar: base^n = base × base^(n-1)
    
    Esto reduce la complejidad de O(n) a O(log n)
    """
    # Caso base
    if exponente == 0:
        return 1
    # Si el exponente es par: (base^(n/2))^2
    if exponente % 2 == 0:
        mitad = potencia_optimizada(base, exponente // 2)
        return mitad * mitad
    # Si el exponente es impar: base * base^(n-1)
    else:
        return base * potencia_optimizada(base, exponente - 1)


# ============ PRUEBAS ============
if __name__ == "__main__":
    print("=== Pruebas de potencia ===")
    
    casos = [
        (2, 0, 1),
        (2, 1, 2),
        (2, 3, 8),
        (2, 10, 1024),
        (3, 4, 81),
        (5, 3, 125),
    ]
    
    for base, exp, esperado in casos:
        resultado = potencia(base, exp)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} potencia({base}, {exp}) = {resultado} (esperado: {esperado})")
