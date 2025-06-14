import tkinter as tk
from tkinter import ttk, messagebox

from classes.asignaturas import Asignatura

class AsignaturaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar
        self.crear_widgets()


    def crear_widgets(self):
        self.label = tk.Label(self, text="Formulario de Asignatura")
        self.label.config(font=("Arial", 16, "bold"))
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.asignatura_label = tk.Label(self, text="Asignatura:")
        self.asignatura_label.grid(row=1, column=0, padx=10, pady=10)
        self.asignatura_entry = tk.Entry(self)
        self.asignatura_entry.grid(row=1, column=1, padx=10, pady=10)

        #Agregar campo para curso
        self.curso_label = tk.Label(self, text="Curso:")
        self.curso_label.grid(row=2, column=0, padx=10, pady=10)
        self.curso_entry = tk.Entry(self)
        self.curso_entry.grid(row=2, column=1, padx=10, pady=10)


        


        #Boton para agregar asignatura
        self.agregar_button = tk.Button(self, text="Agregar Asignatura", command=self.agregar_asignatura)
        self.agregar_button.config(font=("Arial", 12, "bold"), bg="lightgreen", fg="black")
        self.agregar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


        self.lista_asignaturas = tk.Listbox(self)
        self.lista_asignaturas.config(width=50)
        self.lista_asignaturas.grid(row=1, column=2, rowspan=4, padx=10, pady=10)


    
    def agregar_asignatura(self):
        asignatura = self.asignatura_entry.get()
        curso = self.curso_entry.get()
        if asignatura and curso:            
            self.lista_asignaturas.insert(tk.END, f"{asignatura} - {curso}")

            asignatura = Asignatura(asignatura, curso)
            self.gestor_escolar.agregar_asignatura(asignatura)

            self.asignatura_entry.delete(0, tk.END)
            self.curso_entry.delete(0, tk.END)
            
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def mostrar_informacion(self):
        print(f"Información de la asignatura: {self.asignatura}")

    def actualizar_asignatura(self, nueva_asignatura):
        self.asignatura = nueva_asignatura
        print(f"Asignatura actualizada a: {self.asignatura}")