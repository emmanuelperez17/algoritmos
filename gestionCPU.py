"""✅ Lista simplemente enlazada

✅ Inserción O(1)

✅ Métodos recursivos obligatorios

✅ Eliminación recursiva correcta

✅ Reordenamiento SIN crear nueva lista

✅ Sin usar listas de Python

✅ Sin intercambiar datos (solo nodos)"""
class NodoProceso:
    def __init__(self, pid, nombre, prioridad, memoria):
        self.pid = pid
        self.nombre = nombre
        self.prioridad = prioridad
        self.memoria = memoria
        self.siguiente = None
class ListaProcesos:
    def __init__(self):
        self.inicio = None

    # ═══════════════════════════════
    # PUNTO 2: Agregar O(1)
    # ═══════════════════════════════
    def agregar(self, pid, nombre, prioridad, memoria):
        nuevo = NodoProceso(pid, nombre, prioridad, memoria)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    # Mostrar
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(f"PID:{actual.pid} | {actual.nombre} | P:{actual.prioridad} | {actual.memoria}MB")
            actual = actual.siguiente
    def memoria_por_prioridad(self, prioridad):
        return self._memoria_rec(self.inicio, prioridad)

    def _memoria_rec(self, nodo, prioridad):
        if nodo is None:
            return 0

        suma_restante = self._memoria_rec(nodo.siguiente, prioridad)

        if nodo.prioridad == prioridad:
            return nodo.memoria + suma_restante

        return suma_restante
    def eliminar_memoria_mayor(self, limite):
        self.inicio = self._eliminar_rec(self.inicio, limite)

    def _eliminar_rec(self, nodo, limite):
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente, limite)

        if nodo.memoria > limite:
            return nodo.siguiente

        return nodo
    def reordenar_por_prioridad(self):
        if self.inicio is None:
            return

        # Inicializar cabezas y colas para prioridades 1–5
        heads = {i: None for i in range(1, 6)}
        tails = {i: None for i in range(1, 6)}

        actual = self.inicio

        # Separar nodos según prioridad
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = None

            p = actual.prioridad

            if heads[p] is None:
                heads[p] = tails[p] = actual
            else:
                tails[p].siguiente = actual
                tails[p] = actual

            actual = siguiente

        # Reconstruir lista desde prioridad 5 → 1
        nueva_cabeza = None
        ultimo = None

        for p in range(5, 0, -1):
            if heads[p]:
                if nueva_cabeza is None:
                    nueva_cabeza = heads[p]
                    ultimo = tails[p]
                else:
                    ultimo.siguiente = heads[p]
                    ultimo = tails[p]

        self.inicio = nueva_cabeza
    def esta_ordenada(self):
        return self._ordenada_rec(self.inicio)

    def _ordenada_rec(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return True

        if nodo.prioridad < nodo.siguiente.prioridad:
            return False

        return self._ordenada_rec(nodo.siguiente)
if __name__ == "__main__":
    print("=" * 60)
    print("        SISTEMA DE PROCESOS - PRUEBAS")
    print("=" * 60)

    lista = ListaProcesos()

    lista.agregar(1, "Chrome", 3, 500)
    lista.agregar(2, "VSCode", 5, 300)
    lista.agregar(3, "Spotify", 2, 200)
    lista.agregar(4, "Docker", 4, 800)
    lista.agregar(5, "Slack", 3, 150)

    print("\n📋 Lista original:")
    lista.mostrar()

    print("\n💾 Memoria prioridad 3:")
    print(lista.memoria_por_prioridad(3), "MB")

    print("\n🗑 Eliminando procesos > 600MB...")
    lista.eliminar_memoria_mayor(600)
    lista.mostrar()

    print("\n🔀 Reordenando por prioridad...")
    lista.reordenar_por_prioridad()
    lista.mostrar()

    print("\n✔ ¿Está ordenada?")
    print(lista.esta_ordenada())
