from classes.asignaturas import Asignatura
from classes.estudiante import Estudiante


class Nota:
    def __init__(self, estudiante:Estudiante, asignatura:Asignatura, nota:int):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.nota = nota

    

    def to_dict(self):
        return {
            "estudiante": self.estudiante.mostrar_informacion(),
            "asignatura": self.asignatura.nombre,
            "nota": self.nota
        }
    