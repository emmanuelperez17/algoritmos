class estudiante:
    def __init__(self, nombre, docuento):
        self.nombre = nombre
        self.documento = docuento

estudiante1 = estudiante("Juan Perez", "12345678")
print("Nombre del estudiante:", estudiante1.nombre)
print("Documento del estudiante:", estudiante1.documento)