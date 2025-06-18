

from classes.asignaturas import Asignatura
from classes.estudiante import Estudiante
from classes.notas import Nota


class Gestor:
    def __init__(self):
        self.estudiantes = []          # Lista de objetos Estudiante
        self.asignaturas = []          # Lista de objetos Asignatura
        self.notas = []                # Lista de objetos Nota
        self.inscripciones = {}        # dict: dni (str) -> list[Asignatura]
        self.valores_iniciales()

    def valores_iniciales(self):

        # Cargar datos iniciales de estudiantes
        self.agregar_estudiante(Estudiante('Juan', 'Pérez', '12345678', '01-01-2000', 'Ana Pérez'))
        self.agregar_estudiante(Estudiante('María', 'Gómez', '87654321', '02-02-2001', 'Luis Gómez'))

        

    # === Estudiantes ===
    def agregar_estudiante(self, estudiante):
        if not any(e.dni == estudiante.dni for e in self.estudiantes):
            self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, dni):
        self.estudiantes = [e for e in self.estudiantes if e.dni != dni]
        self.inscripciones.pop(dni, None)  # También quitar inscripciones

    # === Asignaturas ===
    def agregar_asignatura(self, asignatura):
        if not any(a.nombre == asignatura.nombre and a.curso == asignatura.curso for a in self.asignaturas):
            self.asignaturas.append(asignatura)

    # === Notas ===
    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_notas_por_estudiante(self, estudiante_dni):
        return [n for n in self.notas if n.estudiante.dni == estudiante_dni]
    
    def obtener_notas_por_asignatura(self, asignatura_nombre):
        return [n for n in self.notas if n.asignatura.nombre == asignatura_nombre]

    # === Inscripciones ===
    def inscribir_estudiante(self, dni, lista_asignaturas):
        self.inscripciones[dni] = lista_asignaturas

    def obtener_inscripciones(self, dni):
        return self.inscripciones.get(dni, [])

    def estudiante_esta_inscripto(self, dni, asignatura):
        '''Verifica si un estudiante está inscripto en una asignatura'''
        asignaturas = self.inscripciones.get(dni, [])
        return any(a.nombre == asignatura.nombre and a.curso == asignatura.curso for a in asignaturas)

    def obtener_asignaturas_disponibles_para(self, dni):
        '''Devuelve las asignaturas en las que aún no está inscripto'''
        inscriptas = self.inscripciones.get(dni, [])
        return [a for a in self.asignaturas if a not in inscriptas]
