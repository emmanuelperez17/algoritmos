# -----------------------------
# Clase Cancion
# -----------------------------
class Cancion:
    def __init__(self, nombre, duracion_segundos):
        self.nombre = nombre
        self.duracion = duracion_segundos  # duración en segundos

    def tiempo_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"


# -----------------------------
# Clase Reproductor
# -----------------------------
class Reproductor:
    def __init__(self):
        self.lista = []       # Lista de canciones
        self.indice = 0       # Canción actual

    def esta_vacia(self):
        return not self.lista

    def agregar_cancion(self, nombre, duracion_segundos):
        cancion = Cancion(nombre, duracion_segundos)
        self.lista.append(cancion)
        print("Canción agregada correctamente.")

    def reproducir(self):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return

        actual = self.lista[self.indice]
        print(f" Reproduciendo: {actual.nombre} ({actual.tiempo_formato()} min)")

    def siguiente(self):
        if self.esta_vacia():
            print("No hay canciones.")
            return

        if self.indice < len(self.lista) - 1:
            self.indice += 1
        else:
            print("Ya estás en la última canción.")

        self.reproducir()

    def anterior(self):
        if self.esta_vacia():
            print("No hay canciones.")
            return

        if self.indice > 0:
            self.indice -= 1
        else:
            print("Ya estás en la primera canción.")

        self.reproducir()

    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía.")
            return

        print("\n--- Lista de canciones ---")
        for i, cancion in enumerate(self.lista):
            print(f"{i + 1}. {cancion.nombre} ({cancion.tiempo_formato()} min)")
        print("--------------------------")


# -----------------------------
# Programa principal (main)
# -----------------------------
reproductor = Reproductor()

while True:
    print("\n--- MENÚ REPRODUCTOR ---")
    print("1. Agregar canción")
    print("2. Reproducir canción actual")
    print("3. Siguiente canción")
    print("4. Canción anterior")
    print("5. Mostrar lista de canciones")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        duracion_segundos = input("Duración (segundos): ")
        try:
            duracion_segundos = int(duracion_segundos)
        except ValueError:
            print("Duración inválida. Debe ser un número entero de segundos.")
            continue
        reproductor.agregar_cancion(nombre, duracion_segundos)

    elif opcion == "2":
        reproductor.reproducir()

    elif opcion == "3":
        reproductor.siguiente()

    elif opcion == "4":
        reproductor.anterior()

    elif opcion == "5":
        reproductor.mostrar()

    elif opcion == "6":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida.")