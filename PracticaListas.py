class Nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_al_final(self, documento, nombre):
        nodo = Nodo(documento, nombre)
        
        if self.cabeza == None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            self.cola = nodo    



// Ejemplo de uso de la clase Lista con apuntador al principio
class Nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_al_final(self, documento, nombre):
        nodo = Nodo(documento, nombre)
        
        if self.cabeza == None:
            self.cabeza = nodo
            
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo                    