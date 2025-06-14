class Persona:
    def __init__(self, nombre: str, apellido: int, dni: str, fecha_nacimiento: str = None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        

    def __str__(self):
        return f"DNI: {self.dni} - {self.apellido}, {self.nombre}"

   