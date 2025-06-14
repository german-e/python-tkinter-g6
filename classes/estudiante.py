from classes.persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, fecha_nacimiento: str = None, tutor: str = ""):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)        
        self.tutor = tutor
        self.asignaturas = []
        

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido}"
    
    


    