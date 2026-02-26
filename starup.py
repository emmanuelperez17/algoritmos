class NodoTarea:
    def __init__(self, descripcion,prioridad):
        self.descripcion=descripcion
        self.prioridad=prioridad #1-5
        self.estado=False
        self.siguiente=None

class ListaTareas:
    def __init__(self):
        self.cabeza=None

    #agregar tarea
    def agregar(self,descripcion,prioridad):
        nuevo=NodoTarea(descripcion,prioridad)
        self.cabeza=self._agregar_rec(self.cabeza,nuevo)


    def _agregar_rec(self,actual,nuevo):
        #lista vacia
        if actual is None:
            return nuevo
        #mayor prioirdad
        if nuevo.prioridad>actual.prioridad:
            nuevo.siguiente=actual
            return nuevo
        
        #caso recrusivo
        actual.siguiente=self._agregar_rec(actual.siguiente,nuevo)
        return actual
    #contar pendientes
    def contar_pendientes(self,prioridad):
        return self._contar_pendientes_rec(self.cabeza,prioridad)
    
    def _contar_pendientes_rec(self,actual,prioridad):
        if actual is None:
            return 0
        if actual.prioridad==prioridad and not actual.estado:
            return 1+self._contar_pendientes_rec(actual.siguiente,prioridad)
        return self._contar_pendientes_rec(actual.siguiente,prioridad)
    #obtener urgentes
    def obtener_urgentes(self):
        urgentes=ListaTareas()
        self._obtener_urgentes_rec(self.cabeza,urgentes)
        return urgentes
    def _obtener_urgentes_rec(self,actual,urgentes):
        if actual is None:
            return 

        if actual.prioridad >=4 and not actual.estado:  
            urgentes.agregar(actual.prioridad,actual.descripcion)

        self._obtener_urgentes_rec(actual.siguiente,urgentes)      

    #limpiar limpiar completadas
    def limpiar_completadas(self):
        self.cabeza=self._limpiar_completadas_rec(self.cabeza)
    def _limpiar_completadas_rec(self,actual):
        if actual is None:
            return None
        actual.siguiente=self._limpiar_completadas_rec(actual.siguiente)
        if actual.estado:
            return actual.siguiente
        return actual
    
    def completar(self,descripcion):
        actual=self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                actual.estado=True
                return True
            actual=actual.siguiente 

    def mostrar(self):
        actual=self.cabeza
        while actual:
            estado="Completada" if actual.estado else "Pendiente"
            print(f"- {actual.descripcion} (Prioridad: {actual.prioridad}, Estado: {estado})") 
            actual=actual.siguiente             


if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA DE TAREAS")
    print("=" * 60)
    
    # Crear lista de tareas
    mis_tareas = ListaTareas()
    
    # Agregar tareas (deben quedar ordenadas por prioridad)
    mis_tareas.agregar("Comprar leche", 2)
    mis_tareas.agregar("Estudiar para parcial", 5)
    mis_tareas.agregar("Llamar al médico", 4)
    mis_tareas.agregar("Ver serie", 1)
    mis_tareas.agregar("Entregar proyecto", 5)
    mis_tareas.agregar("Hacer ejercicio", 3)
    
    print("\\n📋 Lista de tareas (ordenada por prioridad):")
    mis_tareas.mostrar()  # Implementa este método para visualizar
    print("   Esperado orden de prioridades: 5, 5, 4, 3, 2, 1")
    
    # Contar pendientes
    print("\\n🔢 Tareas urgentes (prioridad 5):", mis_tareas.contar_pendientes(5))
    print("   Esperado: 2")
    
    # Marcar algunas como completadas (implementa un método para esto)
    # mis_tareas.completar("Comprar leche")
    # mis_tareas.completar("Ver serie")
    # mis_tareas.completar("Estudiar para parcial")
    
    # Obtener urgentes
    print("\\n🚨 Tareas urgentes pendientes:")
    urgentes = mis_tareas.obtener_urgentes()
    urgentes.mostrar()
    
    # Limpiar completadas
    print("\\n🗑️ Eliminando tareas completadas...")
    mis_tareas.limpiar_completadas()
    mis_tareas.mostrar()    
        

        