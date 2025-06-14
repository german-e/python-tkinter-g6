class Gestor:
    def __init__(self):
        self.estudiantes = []    # Lista de instancias Estudiante
        self.asignaturas = []    # Lista de instancias Asignatura
        self.notas = []          # Lista de tu clase Nota

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def eliminar_estudiante(self, dni):
        """Elimina un estudiante por su nombre"""
        # Filtra la lista de estudiantes para eliminar al que coincide con el nombre
        self.estudiantes = [e for e in self.estudiantes if e.dni != dni]

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_notas_por_estudiante(self, nombre_estudiante):
        return [n for n in self.notas if n.estudiante.nombre == nombre_estudiante]