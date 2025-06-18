import tkinter as tk
from tkinter import ttk, Menu, messagebox

from classes.estudiante import Estudiante

class EstudianteForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar       

        self.estudiante_editando = None  # Guardará el DNI del estudiante en edición 
       
        self.crear_widgets()


    def crear_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=0)

      

        # ======= Formulario Estudiante (Izquierda) =======
        frm_formulario = ttk.LabelFrame(self, text='Datos del Estudiante', padding=15)
        frm_formulario.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        ttk.Label(frm_formulario, text='Nombre:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.nombre_entry = ttk.Entry(frm_formulario, width=30)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm_formulario, text='Apellido:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.apellido_entry = ttk.Entry(frm_formulario, width=30)
        self.apellido_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frm_formulario, text='DNI:').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.dni_entry = ttk.Entry(frm_formulario, width=30)
        self.dni_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frm_formulario, text='Fecha de Nac.:').grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.fecha_nacimiento_entry = ttk.Entry(frm_formulario, width=30)
        self.fecha_nacimiento_entry.insert(0, 'DD/MM/AAAA')
        self.fecha_nacimiento_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frm_formulario, text='Tutor:').grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.tutor_entry = ttk.Entry(frm_formulario, width=30)
        self.tutor_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botones acción (debajo del formulario)
        frm_botones = ttk.Frame(frm_formulario)
        frm_botones.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        self.submit_button = ttk.Button(frm_botones, text='Agregar', command=self.guardar)
        self.submit_button.grid(row=0, column=0, padx=5)

        
        ttk.Button(frm_botones, text='Cerrar', command=self.cerrar).grid(row=0, column=1, padx=5)

        self.nombre_entry.focus()

        # ======= Tabla de Estudiantes (Derecha) =======
        frm_lista = ttk.LabelFrame(self, text='Lista de Estudiantes', padding=10)
        frm_lista.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # Campo de búsqueda
        ttk.Label(frm_lista, text='Buscar por apellido o DNI:').grid(row=0, column=0, padx=5, pady=(0, 5), sticky='w')
        self.entry_buscar = ttk.Entry(frm_lista, width=30)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=(0, 5), sticky='e')
        self.entry_buscar.bind('<KeyRelease>', self.buscar_estudiantes)

        # Treeview
        self.tree_estudiantes = ttk.Treeview(frm_lista, columns=('dni', 'apellido', 'nombre'), show='headings', height=7)
        self.tree_estudiantes.heading('dni', text='DNI')
        self.tree_estudiantes.heading('apellido', text='Apellido')
        self.tree_estudiantes.heading('nombre', text='Nombre')
        self.tree_estudiantes.column('dni', width=100)
        self.tree_estudiantes.column('apellido', width=150)
        self.tree_estudiantes.column('nombre', width=150)
        self.tree_estudiantes.grid(row=1, column=0, columnspan=2, sticky='nsew', pady=5)

        # Cargar estudiantes
        self.actualizar_lista()

        # Botones debajo del Treeview
        frm_botones_tabla = ttk.Frame(frm_lista)
        frm_botones_tabla.grid(row=2, column=0, columnspan=2, pady=10)

        btn_editar = ttk.Button(frm_botones_tabla, text='Editar', command=self.editar)
        btn_editar.grid(row=0, column=0, padx=10)
        ttk.Button(frm_botones_tabla, text='Eliminar', command=self.eliminar).grid(row=0, column=1, padx=10)

        # Expandir automáticamente
        frm_lista.columnconfigure(1, weight=1)

    def actualizar_lista(self):
        '''Actualiza el Treeview con los estudiantes actuales'''
        for item in self.tree_estudiantes.get_children():
            self.tree_estudiantes.delete(item)

        for estudiante in self.gestor_escolar.estudiantes:
            self.tree_estudiantes.insert('', tk.END, values=(estudiante.dni, estudiante.apellido, estudiante.nombre))

    def eliminar(self):      
        estudiante_seleccionado = self.tree_estudiantes.selection() # Obtiene el elemento seleccionado en el Treeview            
        dni = ''

        if not estudiante_seleccionado:
            
            messagebox.showwarning('Advertencia!', 'Debe seleccionar un estudiante para eliminar')
            return
        
        for item in estudiante_seleccionado:
        
            # Obtenemos el DNI del estudiante seleccionado del treeview
            dni = self.tree_estudiantes.item(item, 'values')[0]
            self.tree_estudiantes.delete(item)
        # 
        self.gestor_escolar.eliminar_estudiante(dni)
        
    def cerrar(self):
        self.destroy()

    


    def editar(self):
        seleccion = self.tree_estudiantes.selection()
        if not seleccion:
            messagebox.showwarning('Advertencia', 'Seleccione un estudiante para editar.')
            return

        item = seleccion[0]
        valores = self.tree_estudiantes.item(item, 'values')
        dni = valores[0]

        estudiante = next((e for e in self.gestor_escolar.estudiantes if e.dni == dni), None)
        if estudiante:
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, estudiante.nombre)

            self.apellido_entry.delete(0, tk.END)
            self.apellido_entry.insert(0, estudiante.apellido)

            self.dni_entry.delete(0, tk.END)
            self.dni_entry.insert(0, estudiante.dni)
            self.dni_entry.config(state='disabled')  # No permitir editar DNI

            self.fecha_nacimiento_entry.delete(0, tk.END)
            self.fecha_nacimiento_entry.insert(0, estudiante.fecha_nacimiento)

            self.tutor_entry.delete(0, tk.END)
            self.tutor_entry.insert(0, estudiante.tutor)

            self.submit_button.config(text='Guardar')  #Cambiar texto del botón de "Agregar" a "Guardar"
            self.estudiante_editando = dni

            
            
    def guardar(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dni = self.dni_entry.get()
        tutor = self.tutor_entry.get()
        fecha_nacimiento = self.fecha_nacimiento_entry.get()

        if not nombre or not apellido or not dni:
            tk.messagebox.showerror('Error', 'Los campos Nombre, Apellido y DNI son obligatorios.')
            self.nombre_entry.focus()
            return

        if not dni.isdigit() or len(dni) < 8:
            tk.messagebox.showerror('Error', 'El DNI debe ser un número de 8 dígitos.')
            self.dni_entry.focus()
            return

        if self.estudiante_editando:  # Modo edición
            for estudiante in self.gestor_escolar.estudiantes:
                if estudiante.dni == self.estudiante_editando:
                    estudiante.nombre = nombre
                    estudiante.apellido = apellido
                    estudiante.fecha_nacimiento = fecha_nacimiento
                    estudiante.tutor = tutor
                    break

            
            self.actualizar_lista()
            messagebox.showinfo('Éxito', 'Estudiante actualizado correctamente.')
        
            self.submit_button.config(text='Agregar')
            self.dni_entry.config(state='normal')
            self.estudiante_editando = None

        else:  # Modo agregar
            estudiante = Estudiante(nombre, apellido, dni, fecha_nacimiento, tutor)
            self.gestor_escolar.agregar_estudiante(estudiante)
            self.tree_estudiantes.insert('', tk.END, values=(dni, apellido, nombre))
            messagebox.showinfo('Éxito', 'Estudiante agregado correctamente.')

        # Limpiar campos
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.fecha_nacimiento_entry.delete(0, tk.END)
        self.tutor_entry.delete(0, tk.END)
        self.nombre_entry.focus()



    def buscar_estudiantes(self, event=None):
        termino = self.entry_buscar.get().lower()

        # Limpiar Treeview
        for row in self.tree_estudiantes.get_children():
            self.tree_estudiantes.delete(row)

        # Agregar los que coinciden
        for estudiante in self.gestor_escolar.estudiantes:
            if (termino in estudiante.apellido.lower()) or (termino in estudiante.dni):
                self.tree_estudiantes.insert('', tk.END, values=(estudiante.dni, estudiante.apellido, estudiante.nombre))