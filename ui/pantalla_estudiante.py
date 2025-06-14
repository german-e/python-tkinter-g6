import tkinter as tk
from tkinter import ttk, Menu, messagebox

from classes.estudiante import Estudiante

class EstudianteForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar        
       
        self.crear_widgets()

    def crear_widgets(self):
       
        
        self.label = tk.Label(self, text="Nuevo Estudiante")
        self.label.config(font=("Arial", 16, "bold"))
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)


        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.nombre_entry = tk.Entry(self, width=25)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=10)
        

        self.apellido_label = tk.Label(self, text="Apellido:")
        self.apellido_label.grid(row=2, column=0, sticky='e')      
        self.apellido_entry = tk.Entry(self, width=25)
        self.apellido_entry.grid(row=2, column=1, padx=10, pady=5)

        self.dni_label = tk.Label(self, text="DNI:")
        self.dni_label.grid(row=3, column=0, sticky='e')
        self.dni_entry = tk.Entry(self, width=25)
        self.dni_entry.grid(row=3, column=1, padx=10, pady=5)

        self.fecha_nacimiento_label = tk.Label(self, text="Fecha de Nac.:")
        self.fecha_nacimiento_label.grid(row=4, column=0, sticky='e')
        self.fecha_nacimiento_entry = tk.Entry(self, width=25)
        self.fecha_nacimiento_entry.insert(0, "DD/MM/AAAA")  # Placeholder
        self.fecha_nacimiento_entry.grid(row=4, column=1, padx=10, pady=5)

        self.tutor_label = tk.Label(self, text="Tutor:")
        self.tutor_label.grid(row=5, column=0, sticky='e')
        self.tutor_entry = tk.Entry(self, width=25)
        self.tutor_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self, text='Cerrar', command=self.cerrar).grid(row=6,column=1)
        



        self.submit_button = tk.Button(self, text="Agregar", command=self.guardar)
        self.submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # colocar treeview en el lado derecho de la pantalla  que contenga dni, apellido y nombre de los estudiantes
        self.lista_estudiantes = tk.Listbox(self)
        self.lista_estudiantes.grid(row=1, column=2, rowspan=5, padx=10, pady=10)
        self.lista_estudiantes.config(width=50)
        self.lista_estudiantes.grid(row=1, column=3, rowspan=5)

        # self.tree_estudiantes = ttk.Treeview(self, columns=("dni", "apellido", "nombre"), show="headings", height=10)
        # self.tree_estudiantes.heading("dni", text="DNI")
        # self.tree_estudiantes.heading("apellido", text="Apellido")
        # self.tree_estudiantes.heading("nombre", text="Nombre")

        # self.tree_estudiantes.column("dni", width=100)
        # self.tree_estudiantes.column("apellido", width=150)
        # self.tree_estudiantes.column("nombre", width=150)

        # # Colocamos el Treeview en el lado derecho del frame
        # self.tree_estudiantes.grid(row=1, column=3, rowspan=5, padx=10, pady=10)
        #Si hay estudiantes en el gestor, los muestra en la lista
        for estudiante in self.gestor_escolar.estudiantes:
            self.tree_estudiantes.insert(tk.END, estudiante.mostrar_informacion())
        boton_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar )

        boton_eliminar.grid(row=6, column=2, columnspan=2)

        self.nombre_entry.focus()

    def eliminar(self):
        #extraer el estudiante seleccionado de la lista
        if not self.lista_estudiantes.size():
            messagebox.showwarning('Advertencia!', 'No hay estudiantes para eliminar')
            return
        #obtener el objeto estudiante seleccionado
        
        estudiante_seleccionado = self.lista_estudiantes.curselection()

        if not estudiante_seleccionado:
            
            messagebox.showwarning('Advertencia!', 'Debe seleccionar un estudiante para eliminar')
            return
        
        self.lista_estudiantes.delete(estudiante_seleccionado)
        self.gestor_escolar.eliminar_estudiante(estudiante_seleccionado.dni)
        
    def cerrar(self):
        self.destroy()

    def guardar(self):                 

    
        
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dni = self.dni_entry.get()
        tutor = self.tutor_entry.get()
        fecha_nacimiento = self.fecha_nacimiento_entry.get()
        
        if not nombre or not apellido or not dni:
            tk.messagebox.showerror("Error", "Los campos Nombre, Apellido y DNI son obligatorios.")
            self.nombre_entry.focus()
            return
        
        #DNI es numérico y debe tener al menos 8 dígitos
        if not dni.isdigit() or len(dni) < 8:
            tk.messagebox.showerror("Error", "El DNI debe ser un número de 8 dígitos.")
            self.dni_entry.focus()
            return

        estudiante = Estudiante(nombre, apellido, dni, fecha_nacimiento, tutor)

        self.gestor_escolar.agregar_estudiante(estudiante)

        self.lista_estudiantes.insert(tk.END, estudiante.mostrar_informacion())

        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)

        self.dni_entry.delete(0, tk.END)
        self.fecha_nacimiento_entry.delete(0, tk.END)
        self.tutor_entry.delete(0, tk.END)
        self.nombre_entry.focus()
        # Aquí podrías agregar la lógica para guardar el estudiante
        
        