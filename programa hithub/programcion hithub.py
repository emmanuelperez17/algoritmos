""" SOLUCION- Ejercicio 6: Lista doblemente enlazada
semana 2 - clase 2 Listas Enlazadas 
"""
class NodoDoble:
    def __init__(self, dato):
        """Nodo para la lista doblemente enlazada."""
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    """Lista doblemente enlazada."""
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def esta_vacia(self):
        """Verifica si la lista esta vacia."""
        return self.cabeza == None  
    def insertar_al_inicio(self, dato):
        """Inserta un nuevo nodo al inicio de la lista."""
        nodo = NodoDoble(dato)
        if self.esta_vacia():
            # Lista vacia: cabeza y cola apuntan al nuevo nodo
            self.cabeza = nodo
            self.cola = nodo
        else:
            # Conectar nuevo con la cabeza actual
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
    def insertar_al_final(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nodo = NodoDoble(dato)
        if self.esta_vacia():
            # Lista vacia: cabeza y cola apuntan al nuevo nodo
            self.cabeza = nodo
            self.cola = nodo
        else:
            # Conectar nuevo con la cola actual
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
    def eliminar_al_inicio(self):
        """Elimina el nodo al inicio de la lista."""
        if self.esta_vacia():
            print("La lista esta vacia, no se puede eliminar.")
            return
        dato = self.cabeza.dato    
        if self.cabeza == self.cola:
            # Solo un nodo en la lista
            self.cabeza = None
            self.cola = None
        else:
            # Mover cabeza al siguiente nodo
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        return dato
    def eliminar_al_final(self):
        """Elimina el nodo al final de la lista."""
        if self.esta_vacia():
            print("La lista esta vacia, no se puede eliminar.")
            return
        dato = self.cola.dato    
        if self.cabeza == self.cola:
            # Solo un nodo en la lista
            self.cabeza = None
            self.cola = None
        else:
            # Mover cola al nodo anterior
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        return dato
    def recorrer_adelante(self):
        """Recorre la lista desde la cabeza hasta la cola."""
        if self.esta_vacia():
            print("La lista esta vacia.")
            return

        print("inicio -> fin", end="")
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            print("<->".join(elementos))

    def recorrer_atras(self):
        """Recorre la lista desde la cola hasta la cabeza."""
        if self.esta_vacia():
            print("La lista esta vacia.")
            return

        print("fin -> inicio", end="")
        actual = self.cola
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        print("<->".join(elementos))

    def buscar(self, dato):
        """Busca un nodo con el dato especificado."""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def __len__(self):
        """Retorna la cantidad de elementos en la lista."""
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def __str__(self):
        """Representacion de la lista."""
        if self.esta_vacia():
            return "Lista vacia"

        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)