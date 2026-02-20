def funcion(a, b):
    if b==0:
        return 1
    return a * funcion(a, b-1)

print(funcion(5, 3))  # Esto imprimirá 125, ya que 5^3 = 125

def funcion_(a, b):
    if b==0:
        return 1
    if b%2==0:  # Si b es par
        mitad = funcion_(a, b//2)
        return mitad * mitad
    else:  # Si b es impar
        return a * funcion_(a, b-1)
    
print(funcion_(5, 3))  # Esto también imprimirá 125, ya que 5^3 = 125

# palindromos 
def es_palindromo_invertible(texto):
    limpio = texto.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    invertido = limpio[::-1]  # Invertir el texto
    return limpio == invertido  # Comparar el texto limpio con su versión invertida

print(es_palindromo_invertible("Anita lava la tina"))  # Esto imprimirá True, ya que es un palíndromo
print(es_palindromo_invertible("Hola mundo"))  # Esto imprimirá False, ya que no es un palíndromo

def es_palindromo(palabra):
    palabra = palabra.lower()
    inicio = 0
    fin = len(palabra) - 1
    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

print(es_palindromo("reconocer"))  # Esto imprimirá True, ya que es un palíndromo
print(es_palindromo("Hola mundo"))  # Esto imprimirá False, ya que no es un palíndromo

#palindrome recursivo
def es_palindromo_recursivo(palabra):
    palabra = palabra.lower() 
    if len(palabra) <= 1: # Si la palabra tiene 0 o 1 caracteres, es un palíndromo
        return True # Si el primer y último carácter no son iguales, no es un palíndromo
    if palabra[0] != palabra[-1]: # Comparar el primer y último carácter
        return False # Si el primer y último carácter son iguales, continuar verificando el resto de la palabra
    return es_palindromo_recursivo(palabra[1:-1]) # Llamar a la función recursivamente con la palabra sin el primer y último carácter

print(es_palindromo_recursivo("reconocer"))  # Esto imprimirá True, ya que es un palíndromo
print(es_palindromo_recursivo("Hola mundo"))  # Esto imprimirá False, ya que no es un palíndromo

def es_palindromo_recursivo_invertible(palabra, inicio, fin):
    if inicio >= fin:
        return True
    if palabra[inicio] != palabra[fin]:
        return False
    return es_palindromo_recursivo_invertible(palabra, inicio + 1, fin - 1)

palabra = "reconocer"
print(es_palindromo_recursivo_invertible(palabra, 0, len(palabra) - 1))  # Esto imprimirá True, ya que es un palíndromo
palabra = "Hola mundo"
print(es_palindromo_recursivo_invertible(palabra, 0, len(palabra) - 1))  # Esto imprimirá False, ya que no es un palíndromo

# listas numeros
def sumar(lista):
    if len(lista) == 0: # Si la lista está vacía, el resultado de la suma es 0
        return 0 # Si la lista no está vacía, sumar el primer elemento con la suma del resto de la lista
    return sumar(lista[1:]) + lista[0] # Llamar a la función recursivamente con la lista sin el primer elemento y sumar el primer elemento al resultado

numeros = [5,3,1,2]
print(sumar(numeros))  # Esto imprimirá 11, ya que la suma de los números 5 ,3, 1 y 2 es 11

# ver el ultimo dijito de un numero y asi hasta llegar al ultimo
def ultimo_digito(numero):
    if numero < 10: # Si el número es menor que 10, el último dígito es el número mismo
        return numero # Si el número es mayor o igual a 10, obtener el último dígito utilizando el operador módulo
    return ultimo_digito(numero % 10)+ultimo_digito(numero // 10) # Llamar a la función recursivamente con el resultado del operador módulo y el número sin el último dígito

numero = 12345
print(ultimo_digito(numero))  # Esto imprimirá 15, ya que la suma de los dígitos 1, 2, 3, 4 y 5 es 15

# algoritmo de busqueda binaria
def busqueda_binaria(lista, objetivo, inicio, fin):
    if inicio > fin: # Si el índice de inicio es mayor que el índice de fin, el objetivo no se encuentra en la lista
        return -1 # Calcular el índice medio de la lista
    medio = (inicio + fin) // 2 # Si el elemento en el índice medio es igual al objetivo, devolver el índice medio
    if lista[medio] == objetivo:
        return medio # Si el elemento en el índice medio es mayor que el objetivo, buscar en la mitad izquierda de la lista
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1) # Si el elemento en el índice medio es menor que el objetivo, buscar en la mitad derecha de la lista
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
resultado = busqueda_binaria(numeros, objetivo, 0, len(numeros) - 1)
if resultado != -1:
    print(f"El número {objetivo} se encuentra en el índice {resultado}.")  # Esto imprimirá "El número 7 se encuentra en el índice 6."

# permutaciones
def permutaciones(lista):
    if len(lista) <= 1: # Si la lista está vacía, la única permutación es la lista vacía
        return [lista] # Si la lista no está vacía, generar permutaciones para cada elemento de la lista
    resultado = [] # Crear una lista para almacenar las permutaciones resultantes
    for i in range(len(lista)): # Iterar sobre cada índice de la lista
        elemento = lista[i] # Obtener el elemento en el índice actual
        resto = lista[:i] + lista[i+1:] # Crear una nueva lista que contiene todos los elementos excepto el elemento actual
        for perm in permutaciones(resto): # Generar permutaciones para la lista restante
            resultado.append([elemento] + perm) # Agregar el elemento actual al inicio de cada permutación generada y agregarla a la lista de resultados
    return resultado

print(permutaciones([1, 3, 7]))

def fibonacci(n):
    if n <= 1: # Si n es 0 o negativo, el resultado es 0
        return n # Si n es 1, el resultado es 1
    return fibonacci(n - 1) + fibonacci(n - 2) # Si n es mayor que 1, el resultado es la suma de los dos números anteriores en la secuencia de Fibonacci
    
def fibonacci_tail(n, actual=0, siguiente=1):
    if n == 0:
        return actual
    return fibonacci_tail(n - 1, siguiente, actual + siguiente)

print(fibonacci(10))  # Esto imprimirá 55, ya que el décimo número en la secuencia de Fibonacci es 55
print(fibonacci_tail(10))  # Esto también imprimirá 55, utilizando la versión

def suma_lista(lista, acumulador=0):
    if not lista: # Si la lista está vacía, el resultado de la suma es 0
        return acumulador # Si la lista no está vacía, sumar el primer elemento con la suma del resto de la lista
    return suma_lista(lista[1:], acumulador + lista[0]) # Llamar a la función recursivamente con la lista sin el primer elemento y sumar el primer elemento al acumulador

numeros = [5, 3, 1, 2]
print(suma_lista(numeros))  # Esto imprimirá 11, ya que la suma de los números 5, 3, 1 y 2 es 11

def potencia(base, exp, acumulador=1):
    if exp == 0: # Si el exponente es 0, cualquier número elevado a la potencia de 0 es 1
        return acumulador # Si el exponente es negativo, calcular la potencia utilizando el exponente positivo y luego tomar el recíproco
    elif exp < 0:
        return 1 / potencia(base, -exp) # Si el exponente es positivo, calcular la potencia multiplicando la base por sí misma exp veces
    else:
        return potencia(base, exp - 1, acumulador * base) # Llamar a la función recursivamente con el exponente reducido en 1 y el acumulador multiplicado por la base
    
print(potencia(5, 3))  # Esto imprimirá 125, ya que 5 elevado a la potencia de 3 es 125
print(potencia(5, -3))  # Esto imprimirá 0.008, ya que 5 elevado a la potencia de -3 es 1/125 = 0.008
