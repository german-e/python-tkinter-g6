from classes.persona import Persona


class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento=None, ):
        super().__init__(nombre, apellido, dni)
        self.__asignaturas = []

    def __str__(self):
        return f"{super().__str__()}"
    
    def asignar_asignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.__asignaturas.append(asignatura)

    def obtener_asignaturas(self):
        return self.__asignaturas

    