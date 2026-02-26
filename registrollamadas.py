"""✅ Lista simplemente enlazada

✅ Inserción en O(1) al inicio

✅ Promedio usando recursividad

✅ Filtrado recursivo creando nueva lista

✅ Eliminación recursiva modificando la original

❌ Sin usar listas de Python"""
class Nodo:
    def __init__(self, numero, duracion, tipo):
        self.numero = numero
        self.duracion = duracion
        self.tipo = tipo  # "entrante" o "saliente"
        self.siguiente = None
class Registro:
    def __init__(self):
        self.inicio = None

    # ═══════════════════════════════
    # PUNTO 2: Registrar llamada O(1)
    # ═══════════════════════════════
    def registrar(self, numero, duracion, tipo):
        nuevo = Nodo(numero, duracion, tipo)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    # ═══════════════════════════════
    # Mostrar (iterativo)
    # ═══════════════════════════════
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(f"{actual.numero} | {actual.tipo} | {actual.duracion}s")
            actual = actual.siguiente

    # ═══════════════════════════════
    # PUNTO 3: Duración promedio (RECURSIVO)
    # ═══════════════════════════════
    def duracion_promedio(self):
        total, cantidad = self._sumar_y_contar(self.inicio)
        if cantidad == 0:
            return 0
        return total / cantidad

    def _sumar_y_contar(self, nodo):
        if nodo is None:
            return (0, 0)

        suma_restante, cant_restante = self._sumar_y_contar(nodo.siguiente)

        return (nodo.duracion + suma_restante, 1 + cant_restante)

    # ═══════════════════════════════
    # PUNTO 4: Filtrar por tipo (RECURSIVO)
    # ═══════════════════════════════
    def filtrar_por_tipo(self, tipo):
        nueva_lista = Registro()
        nueva_lista.inicio = self._filtrar_rec(self.inicio, tipo)
        return nueva_lista

    def _filtrar_rec(self, nodo, tipo):
        if nodo is None:
            return None

        resto = self._filtrar_rec(nodo.siguiente, tipo)

        if nodo.tipo == tipo:
            nuevo = Nodo(nodo.numero, nodo.duracion, nodo.tipo)
            nuevo.siguiente = resto
            return nuevo

        return resto

    # ═══════════════════════════════
    # PUNTO 5: Eliminar llamadas cortas (RECURSIVO)
    # ═══════════════════════════════
    def eliminar_cortas(self, minimo):
        self.inicio = self._eliminar_rec(self.inicio, minimo)

    def _eliminar_rec(self, nodo, minimo):
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente, minimo)

        if nodo.duracion < minimo:
            return nodo.siguiente

        return nodo
if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL REGISTRO DE LLAMADAS")
    print("=" * 60)

    registro = Registro()

    registro.registrar("555-1111", 15, "saliente")
    registro.registrar("555-2222", 300, "entrante")
    registro.registrar("555-3333", 180, "saliente")
    registro.registrar("555-4444", 45, "entrante")
    registro.registrar("555-5555", 5, "saliente")

    print("\n📋 Registro inicial:")
    registro.mostrar()

    print("\n⏱️ Duración promedio:")
    print(registro.duracion_promedio(), "segundos")

    print("\n📞 Llamadas entrantes:")
    entrantes = registro.filtrar_por_tipo("entrante")
    entrantes.mostrar()

    print("\n🗑️ Eliminando llamadas < 30 segundos...")
    registro.eliminar_cortas(30)
    registro.mostrar()
