class NodoPagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo  # en segundos
        self.siguiente = None

class Historial:
    def __init__(self):
        self.cabeza = None

    def visitar(self, url, titulo, tiempo):
        nuevo = NodoPagina(url, titulo, tiempo)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def tiempo_total(self):
        return self._tiempo_total_rec(self.cabeza)

    def _tiempo_total_rec(self, actual):
        if actual is None:
            return 0
        return actual.tiempo + self._tiempo_total_rec(actual.siguiente)
                    
    def buscar_por_dominio(self, texto):
        nueva = Historial()
        self._buscar_rec(self.cabeza, texto, nueva)
        return nueva

    def _buscar_rec(self, actual, texto, nueva):
        if actual is None:
            return

        if texto.lower() in actual.url.lower():
            nueva.visitar(actual.url, actual.titulo, actual.tiempo)

        self._buscar_rec(actual.siguiente, texto, nueva)    

    def eliminar_rapidas(self, minimo):
        self.cabeza = self._eliminar_rapidas_rec(self.cabeza, minimo)

    def _eliminar_rapidas_rec(self, actual, minimo):
        if actual is None:
            return None

        actual.siguiente = self._eliminar_rapidas_rec(actual.siguiente, minimo)

        if actual.tiempo < minimo:
            return actual.siguiente

        return actual

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"- {actual.titulo} | {actual.url} | {actual.tiempo}s")
            actual = actual.siguiente                

if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL HISTORIAL DE NAVEGACIÓN")
    print("=" * 60)
    
    # Crear historial
    historial = Historial()
    
    # Agregar páginas (la más reciente queda primero)
    historial.visitar("https://www.google.com/search", "Búsqueda Google", 15)
    historial.visitar("https://www.youtube.com/watch", "Video YouTube", 300)
    historial.visitar("https://www.github.com/repo", "GitHub Repo", 180)
    historial.visitar("https://www.youtube.com/home", "YouTube Home", 45)
    historial.visitar("https://www.google.com/maps", "Google Maps", 5)
    
    print("\\n📋 Historial inicial:")
    historial.mostrar()  # Implementa este método para visualizar
    
    # Prueba tiempo total
    print("\\n⏱️ Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")
    
    # Prueba buscar por dominio
    print("\\n🔍 Páginas de YouTube:")
    youtube = historial.buscar_por_dominio("youtube")
    youtube.mostrar()
    
    # Prueba eliminar rápidas
    print("\\n🗑️ Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")