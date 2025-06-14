class Asignatura:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        

    def __str__(self):
        return f"{self.nombre}"
