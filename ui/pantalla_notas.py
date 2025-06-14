import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from classes.notas import Nota

class NotaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar

        self.crear_widgets()

    def crear_widgets(self):

        tk.Label(self, text="Estudiante:").grid(row=0, column=0, sticky="e")
        self.cmb_estudiante = ttk.Combobox(self, values=[e.nombre for e in self.gestor_escolar.estudiantes])
        self.cmb_estudiante.grid(row=0, column=1)

        tk.Label(self, text="Asignatura:").grid(row=1, column=0, sticky="e")
        self.cmb_asignatura = ttk.Combobox(self, values=[a.nombre for a in self.gestor_escolar.asignaturas])
        self.cmb_asignatura.grid(row=1, column=1)

        tk.Label(self, text="Nota:").grid(row=2, column=0, sticky="e")
        self.ent_nota = tk.Entry(self)
        self.ent_nota.grid(row=2, column=1)

        self.btn_guardar = tk.Button(self, text="Guardar Nota", command=self.guardar)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)

    def actualizar_listas(self):
        self.cmb_estudiante["values"] = [e.nombre for e in self.gestor_datos.estudiantes]
        self.cmb_asignatura["values"] = [a.nombre for a in self.gestor_datos.asignaturas]

    def guardar(self):
        estudiante_nombre = self.cmb_estudiante.get()
        asignatura_nombre = self.cmb_asignatura.get()
        nota_valor = float(self.ent_nota.get())
        if not estudiante_nombre or not asignatura_nombre or not nota_valor:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        estudiante = next((e for e in self.gestor_escolar.estudiantes if e.nombre == estudiante_nombre), None)
        asignatura = next((a for a in self.gestor_escolar.asignaturas if a.nombre == asignatura_nombre), None)
        nota = Nota(estudiante, asignatura, nota_valor)
        self.gestor_escolar.agregar_nota(nota)


        messagebox.showinfo("Éxito", "Nota guardada correctamente.")