import tkinter as tk
from tkinter import ttk

class VerNotasForm(tk.Frame):
    def __init__(self, master, gestor_datos):
        super().__init__(master)
        self.gestor_datos = gestor_datos
        self.configure(padx=15, pady=15)

        # Estilos para la tabla
        estilo = ttk.Style()
        estilo.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        estilo.configure('Treeview', rowheight=25, font=('Arial', 10))

        # Marco principal
        marco = ttk.LabelFrame(self, text='Consulta de Notas', padding=10)
        marco.pack(fill='both', expand=True)

        # ComboBox de estudiantes
        label_combo = ttk.Label(marco, text='Seleccionar Estudiante:')
        label_combo.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.cmb_estudiante = ttk.Combobox(marco, state='readonly', width=35)
        self.cmb_estudiante.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_estudiante.bind('<<ComboboxSelected>>', self.mostrar_notas)  # Ejecutar mostrar_nota al evento al seleccionar un estudiante

        # Botón refrescar
        ttk.Button(marco, text='Refrescar', command=self.actualizar_estudiantes).grid(row=0, column=2, padx=5)

        # Treeview de notas
        self.tree = ttk.Treeview(marco, columns=('asignatura', 'nota'), show='headings', height=10)
        self.tree.heading('asignatura', text='Asignatura')
        self.tree.heading('nota', text='Nota')
        self.tree.column('asignatura', width=220)
        self.tree.column('nota', width=80, anchor='center')
        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=10, sticky='nsew')

        # Scroll vertical
        scrollbar = ttk.Scrollbar(marco, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky='ns')

        # Promedio
        self.lbl_promedio = ttk.Label(marco, text='Promedio: -', font=('Arial', 10, 'bold'))
        self.lbl_promedio.grid(row=2, column=0, columnspan=3, sticky='w', padx=5, pady=(0, 10))

        # Ajustes de expansión
        marco.columnconfigure(1, weight=1)
        marco.rowconfigure(1, weight=1)

        self.actualizar_estudiantes()

    def actualizar_estudiantes(self):
        '''Llena el combo con estudiantes y selecciona el primero automáticamente'''
        self.cmb_estudiante['values'] = [
            f'{e.apellido}, {e.nombre} ({e.dni})' for e in self.gestor_datos.estudiantes
        ]
        if self.cmb_estudiante['values']:
            self.cmb_estudiante.current(0)
            self.mostrar_notas()

    def mostrar_notas(self, event=None):
        '''Muestra notas por estudiante seleccionado'''
        seleccionado = self.cmb_estudiante.get()
        if not seleccionado:
            return
        
        # Extraer DNI del estudiante seleccionado
        dni = seleccionado.split('(')[-1].replace(')', '').strip()
        notas = self.gestor_datos.obtener_notas_por_estudiante(dni)

        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        total, cantidad = 0, 0

        for i, nota in enumerate(notas):
            color = 'nota_baja' if nota.nota < 6 else 'normal'
            self.tree.insert('', 'end', values=(nota.asignatura.nombre, nota.nota), tags=(color,))
            total += nota.nota
            cantidad += 1

        self.tree.tag_configure('nota_baja', foreground='red')
        self.tree.tag_configure('normal', foreground='black')

        if cantidad > 0:
            promedio = round(total / cantidad, 2)
            self.lbl_promedio.config(text=f'Promedio: {promedio}')
        else:
            self.lbl_promedio.config(text='Promedio: -')
