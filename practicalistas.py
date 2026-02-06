class nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class lista_estudiantes:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def agregar_estudiante(self, documento, nombre):
        nuevo = nodo(documento, nombre)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo