# from ui.pantalla_inicio import PantallaInicio


# if __name__ == "__main__":
#     app = PantallaInicio()
#     app.mainloop() 
import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# -------------------------- CLASES --------------------------
import tkinter as tk
from tkinter import messagebox
import time

# -------------------- MODELOS SIMPLIFICADOS --------------------
class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, tutor=""):
        super().__init__(nombre, apellido, dni)
        self.tutor = tutor

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.asignaturas = []

class Asignatura:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

    def __str__(self):
        return self.nombre

class Nota:
    def __init__(self, estudiante, asignatura, valor):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.valor = valor

# -------------------- GESTOR ESCOLAR --------------------
class Gestor:
    def __init__(self):
        self.estudiantes = []
        self.asignaturas = []
        self.notas = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_notas_estudiante(self, nombre):
        return [n for n in self.notas if n.estudiante.nombre == nombre]

# -------------------- INTERFAZ TKINTER --------------------
class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Escolar")
        self.root.geometry("600x400")
        self.gestor = Gestor()

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        menu_estudiantes = tk.Menu(self.barra_menu, tearoff=0)
        menu_estudiantes.add_command(label="Agregar Estudiante", command=self.agregar_estudiante)
        self.barra_menu.add_cascade(label="Estudiantes", menu=menu_estudiantes)

        menu_tareas = tk.Menu(self.barra_menu, tearoff=0)
        menu_tareas.add_command(label="Lista de Tareas", command=self.mostrar_tareas)
        self.barra_menu.add_cascade(label="Tareas", menu=menu_tareas)

        self.reloj = tk.Label(self.root, font=("Arial", 16), bg="black", fg="white")
        self.reloj.pack(pady=10)
        self.actualizar_reloj()

        self.lista_tareas = tk.Listbox(self.root)
        self.lista_tareas.pack(pady=10)

        self.entrada_tarea = tk.Entry(self.root)
        self.entrada_tarea.pack()

        boton_agregar = tk.Button(self.root, text="Agregar tarea", command=self.agregar_tarea)
        boton_agregar.pack()

        boton_eliminar = tk.Button(self.root, text="Eliminar tarea", command=self.eliminar_tarea)
        boton_eliminar.pack()

    def actualizar_reloj(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.reloj.config(text=hora_actual)
        self.root.after(1000, self.actualizar_reloj)

    def agregar_estudiante(self):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Agregar Estudiante")

        tk.Label(nueva_ventana, text="Nombre:").pack()
        entrada_nombre = tk.Entry(nueva_ventana)
        entrada_nombre.pack()

        tk.Label(nueva_ventana, text="Apellido:").pack()
        entrada_apellido = tk.Entry(nueva_ventana)
        entrada_apellido.pack()

        tk.Label(nueva_ventana, text="DNI:").pack()
        entrada_dni = tk.Entry(nueva_ventana)
        entrada_dni.pack()

        def guardar():
            estudiante = Estudiante(entrada_nombre.get(), entrada_apellido.get(), entrada_dni.get())
            self.gestor.agregar_estudiante(estudiante)
            messagebox.showinfo("Éxito", "Estudiante agregado")
            nueva_ventana.destroy()

        tk.Button(nueva_ventana, text="Guardar", command=guardar).pack()

    def mostrar_tareas(self):
        messagebox.showinfo("Tareas", "Aquí puedes agregar y eliminar tareas usando el cuadro de entrada")

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()

