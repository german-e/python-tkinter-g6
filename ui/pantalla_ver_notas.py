import tkinter as tk
from tkinter import ttk

class VerNotasForm(tk.Frame):
    def __init__(self, master, gestor_datos):
        super().__init__(master)
        self.gestor_datos = gestor_datos

        # Label y ComboBox para elegir estudiante
        tk.Label(self, text="Seleccionar Estudiante:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.cmb_estudiante = ttk.Combobox(self, state="readonly")
        self.cmb_estudiante.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_estudiante.bind("<<ComboboxSelected>>", self.mostrar_notas)

        # Treeview para mostrar las notas
        self.tree = ttk.Treeview(self, columns=("asignatura", "nota"), show="headings", height=8)
        self.tree.heading("asignatura", text="Asignatura")
        self.tree.heading("nota", text="Nota")
        self.tree.column("asignatura", width=150)
        self.tree.column("nota", width=80)
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.actualizar_estudiantes()

    def actualizar_estudiantes(self):
        """Carga los estudiantes desde el gestor de datos al ComboBox"""
        self.cmb_estudiante["values"] = [e.nombre for e in self.gestor_datos.estudiantes]

    def mostrar_notas(self, event=None):
        """Muestra las notas del estudiante seleccionado"""
        estudiante_nombre = self.cmb_estudiante.get()
        notas = self.gestor_datos.obtener_notas_por_estudiante(estudiante_nombre)

        # Limpiar el treeview antes de cargar nuevas notas
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar las notas
        for nota in notas:
            self.tree.insert("", tk.END, values=(nota.asignatura.nombre, nota.nota))
