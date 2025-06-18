import tkinter as tk
from tkinter import ttk, messagebox

from classes.asignaturas import Asignatura

class AsignaturaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar
        self.config(padx=20, pady=20)
        self.asignatura_en_edicion = None  # Referencia a la asignatura seleccionada
        self.crear_widgets()

    def crear_widgets(self):
        # Marco del formulario
        marco_formulario = ttk.LabelFrame(self, text='Registrar Asignatura', padding=15)
        marco_formulario.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        ttk.Label(marco_formulario, text='Asignatura:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.asignatura_entry = ttk.Entry(marco_formulario, width=30)
        self.asignatura_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(marco_formulario, text='Curso:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.curso_entry = ttk.Entry(marco_formulario, width=30)
        self.curso_entry.grid(row=1, column=1, padx=5, pady=5)

        self.agregar_button = ttk.Button(marco_formulario, text='Agregar Asignatura', command=self.agregar_asignatura)
        self.agregar_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para guardar edición (oculto por defecto)
        self.guardar_edicion_button = ttk.Button(marco_formulario, text='Guardar edición', command=self.guardar_edicion)
        self.guardar_edicion_button.grid(row=3, column=0, columnspan=2, pady=5)
        self.guardar_edicion_button.grid_remove()  # Ocultar al inicio

        # Lista de asignaturas
        marco_lista = ttk.LabelFrame(self, text='Asignaturas Cargadas', padding=10)
        marco_lista.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.tree = ttk.Treeview(marco_lista, columns=('asignatura', 'curso'), show='headings', height=10)
        self.tree.heading('asignatura', text='Asignatura')
        self.tree.heading('curso', text='Curso')
        self.tree.column('asignatura', width=180)
        self.tree.column('curso', width=100)
        self.tree.pack(fill='both', expand=True)

        # Botones de edición debajo del treeview
        frame_botones = ttk.Frame(marco_lista)
        frame_botones.pack(fill='x', pady=(8,0))
        self.editar_button = ttk.Button(frame_botones, text='Editar', command=self.editar_asignatura)
        self.editar_button.pack(side='left', padx=5, expand=True)
        self.eliminar_button = ttk.Button(frame_botones, text='Eliminar', command=self.eliminar_asignatura)
        self.eliminar_button.pack(side='left', padx=5, expand=True)

        # Estilo visual
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        style.configure('Treeview', font=('Arial', 10), rowheight=25)

        #Cargar asignaturas existentes
        for asignatura in self.gestor_escolar.asignaturas:
            self.tree.insert('', tk.END, values=(asignatura.nombre, asignatura.curso))

    def agregar_asignatura(self):
        asignatura = self.asignatura_entry.get().strip()
        curso = self.curso_entry.get().strip()

        if asignatura and curso:
            nueva_asignatura = Asignatura(asignatura, curso)
            self.gestor_escolar.agregar_asignatura(nueva_asignatura)
            self.tree.insert('', tk.END, values=(asignatura, curso))
            self.asignatura_entry.delete(0, tk.END)
            self.curso_entry.delete(0, tk.END)
            self.asignatura_entry.focus()
        else:
            messagebox.showerror('Error', 'Por favor, complete todos los campos.')

    def editar_asignatura(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una asignatura para editar.")
            return
        item = seleccionado[0]
        valores = self.tree.item(item, 'values')

        nombre_asignatura = valores[0]
        curso_asignatura = valores[1]
        # Buscar la asignatura en el gestor
        for asignatura in self.gestor_escolar.asignaturas:
            if asignatura.nombre == nombre_asignatura and asignatura.curso == curso_asignatura:
                self.asignatura_en_edicion = asignatura
                break
        else:
            messagebox.showerror("Error", "Asignatura no encontrada.")
            return

        # Cargar en el formulario
        self.asignatura_entry.delete(0, tk.END)
        self.curso_entry.delete(0, tk.END)
        self.asignatura_entry.insert(0, nombre_asignatura)
        self.curso_entry.insert(0, curso_asignatura)
        self.agregar_button['state'] = 'disabled'
        self.guardar_edicion_button.grid()  # Mostrar botón

    def guardar_edicion(self):
        if not self.asignatura_en_edicion:
            return
        nuevo_nombre = self.asignatura_entry.get().strip()
        nuevo_curso = self.curso_entry.get().strip()
        if not nuevo_nombre or not nuevo_curso:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        # Actualizar en la lista del gestor
        self.asignatura_en_edicion.nombre = nuevo_nombre
        self.asignatura_en_edicion.curso = nuevo_curso

        # Actualizar en el treeview
        selected = self.tree.selection()[0]
        self.tree.item(selected, values=(nuevo_nombre, nuevo_curso))

        # Limpiar
        self.asignatura_entry.delete(0, tk.END)
        self.curso_entry.delete(0, tk.END)
        self.asignatura_en_edicion = None
        self.guardar_edicion_button.grid_remove()
        self.agregar_button['state'] = 'normal'

    def eliminar_asignatura(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione una asignatura para eliminar.")
            return
        item = selected[0]
        valores = self.tree.item(item, 'values')
        confirm = messagebox.askyesno("Eliminar", f"¿Eliminar la asignatura '{valores[0]}' del curso '{valores[1]}'?")
        if not confirm:
            return
        # Eliminar de gestor
        self.gestor_escolar.asignaturas = [
            a for a in self.gestor_escolar.asignaturas if not (a.nombre == valores[0] and a.curso == valores[1])
        ]
        # Eliminar de treeview
        self.tree.delete(item)
