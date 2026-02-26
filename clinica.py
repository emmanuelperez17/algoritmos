# ═══════════════════════════════════════
# Clase NodoPaciente
# ═══════════════════════════════════════

class NodoPaciente:
    def __init__(self, nombre, documento, tipo):
        self.nombre = nombre
        self.documento = documento
        self.tipo = tipo  # "Normal" o "Emergencia"
        self.siguiente = None


# ═══════════════════════════════════════
# Clase ListaPacientes
# ═══════════════════════════════════════

class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    # ═══════════════════════════════
    # 1️⃣ Agregar paciente normal (AL FINAL) - RECURSIVO
    # ═══════════════════════════════
    def agregar_normal(self, nombre, documento):
        nuevo = NodoPaciente(nombre, documento, "Normal")
        self.cabeza = self._agregar_final_rec(self.cabeza, nuevo)

    def _agregar_final_rec(self, actual, nuevo):
        if actual is None:
            return nuevo

        actual.siguiente = self._agregar_final_rec(actual.siguiente, nuevo)
        return actual

    # ═══════════════════════════════
    # 2️⃣ Agregar paciente de emergencia (AL INICIO)
    # ═══════════════════════════════
    def agregar_emergencia(self, nombre, documento):
        nuevo = NodoPaciente(nombre, documento, "Emergencia")
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # ═══════════════════════════════
    # 3️⃣ Mostrar pacientes (RECURSIVO)
    # ═══════════════════════════════
    def mostrar(self):
        self._mostrar_rec(self.cabeza)

    def _mostrar_rec(self, actual):
        if actual is None:
            return
        print(f"- {actual.nombre} | CC: {actual.documento} | {actual.tipo}")
        self._mostrar_rec(actual.siguiente)

    # ═══════════════════════════════
    # 4️⃣ Atender paciente (eliminar primero)
    # ═══════════════════════════════
    def atender(self):
        if self.cabeza is None:
            print("No hay pacientes en espera.")
            return

        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente
        print(f"Paciente atendido: {atendido.nombre}")
if __name__ == "__main__":
    print("=" * 50)
    print("   SISTEMA DE PACIENTES - CLÍNICA")
    print("=" * 50)

    lista = ListaPacientes()

    # Llegan pacientes normales
    lista.agregar_normal("Ana Torres", "1010")
    lista.agregar_normal("Luis Pérez", "2020")
    lista.agregar_normal("María Gómez", "3030")

    # Llega una emergencia
    lista.agregar_emergencia("Carlos Ruiz", "9999")

    print("\n📋 Pacientes en espera:")
    lista.mostrar()

    print("\n👨‍⚕️ Atendiendo paciente...")
    lista.atender()

    print("\n📋 Pacientes restantes:")
    lista.mostrar()
