import tkinter as tk
from tkinter import ttk, messagebox
from classes.notas import Nota

class NotaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar
        self.config(padx=20, pady=20)
        self.crear_widgets()

    def crear_widgets(self):
        marco = ttk.LabelFrame(self, text='Carga de Nota', padding=15)
        marco.pack(fill='both', expand=True)

        # Estudiante
        ttk.Label(marco, text='Estudiante:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.cmb_estudiante = ttk.Combobox(marco, state='readonly', width=40)
        self.cmb_estudiante.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_estudiante.bind('<<ComboboxSelected>>', self.actualizar_asignaturas_por_estudiante)

        # Asignatura (se actualizará dinámicamente)
        ttk.Label(marco, text='Asignatura:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.cmb_asignatura = ttk.Combobox(marco, state='readonly', width=40)
        self.cmb_asignatura.grid(row=1, column=1, padx=5, pady=5)

        # Nota
        ttk.Label(marco, text='Nota (0 a 10):').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.ent_nota = ttk.Entry(marco, width=10)
        self.ent_nota.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        self.btn_guardar = ttk.Button(marco, text='Guardar Nota', command=self.guardar)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, pady=15)

        self.actualizar_estudiantes()

    def actualizar_estudiantes(self):
        self.cmb_estudiante['values'] = [
            f'{e.apellido}, {e.nombre} ({e.dni})' for e in self.gestor_escolar.estudiantes
        ]

    def actualizar_asignaturas_por_estudiante(self, event=None):
        seleccion = self.cmb_estudiante.get()
        if not seleccion:
            return

        dni = seleccion.split('(')[-1].replace(')', '').strip()
        asignaturas = self.gestor_escolar.obtener_inscripciones(dni)

        self.cmb_asignatura['values'] = [f'{a.nombre} - {a.curso}' for a in asignaturas]
        self.cmb_asignatura.set('')  # Limpiar selección anterior

    def guardar(self):
        estudiante_str = self.cmb_estudiante.get()
        asignatura_str = self.cmb_asignatura.get()
        nota_texto = self.ent_nota.get()

        if not estudiante_str or not asignatura_str or not nota_texto:
            messagebox.showerror('Error', 'Por favor, complete todos los campos.')
            return

        try:
            nota_valor = float(nota_texto)
            if not 0 <= nota_valor <= 10:
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', 'La nota debe ser un número entre 0 y 10.')
            return

        dni = estudiante_str.split('(')[-1].replace(')', '').strip()
        estudiante = next((e for e in self.gestor_escolar.estudiantes if e.dni == dni), None)

        nombre_asignatura = asignatura_str.split(' - ')[0].strip()
        asignatura = next((a for a in self.gestor_escolar.asignaturas if a.nombre == nombre_asignatura), None)

        if estudiante and asignatura:
            nota = Nota(estudiante, asignatura, nota_valor)
            self.gestor_escolar.agregar_nota(nota)
            messagebox.showinfo('Éxito', 'Nota guardada correctamente.')
            self.ent_nota.delete(0, tk.END)
        else:
            messagebox.showerror('Error', 'Estudiante o asignatura no encontrados.')
