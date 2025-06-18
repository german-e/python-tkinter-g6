import tkinter as tk
from tkinter import ttk, messagebox

class InscripcionAsignaturaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar
        self.crear_widgets()

    def crear_widgets(self):
        self.config(padx=20, pady=20)

        ttk.Label(self, text='Inscripción a Asignaturas', font=('Arial', 14, 'bold')).pack(pady=(0, 10))

        # === Selector de estudiante ===
        frame_form = ttk.Frame(self)
        frame_form.pack(fill='x', pady=10)

        ttk.Label(frame_form, text='Estudiante:').grid(row=0, column=0, sticky='e', padx=5)
        self.cmb_estudiante = ttk.Combobox(frame_form, state='readonly', width=45)
        self.cmb_estudiante['values'] = [str(e) for e in self.gestor_escolar.estudiantes] #[f'{e.apellido}, {e.nombre} ({e.dni})' for e in self.gestor_escolar.estudiantes]
        self.cmb_estudiante.grid(row=0, column=1, padx=5)
        self.cmb_estudiante.bind('<<ComboboxSelected>>', self.actualizar_lista_asignaturas)

        # === Asignaturas disponibles ===
        ttk.Label(self, text='Asignaturas disponibles:').pack(anchor='w', padx=5)
        self.lst_asignaturas = tk.Listbox(self, selectmode='multiple', height=10, exportselection=False, width=50)
        self.lst_asignaturas.pack(padx=10, pady=5)

        # === Botón Inscribir ===
        btn_inscribir = ttk.Button(self, text='Inscribir', command=self.inscribir)
        btn_inscribir.pack(pady=10)

    def actualizar_lista_asignaturas(self, event=None):
        self.lst_asignaturas.delete(0, tk.END)

        

        estudiante_seleccionado = next((e for e in self.gestor_escolar.estudiantes if str(e) == self.cmb_estudiante.get()), None)

        # estudiante_info = self.cmb_estudiante.get()
        # if not estudiante_info:
        #     return
        if not estudiante_seleccionado:
            # messagebox.showwarning('Advertencia', 'Seleccione un estudiante válido.')
            return

        # dni = estudiante_info.split('(')[-1].replace(')', '').strip()
        dni = estudiante_seleccionado.dni

        disponibles = self.gestor_escolar.obtener_asignaturas_disponibles_para(dni)
        for asig in disponibles:
            self.lst_asignaturas.insert(tk.END, f'{asig.nombre} - {asig.curso}')

        if not disponibles:
            self.lst_asignaturas.insert(tk.END, 'Ya está inscripto en todas las asignaturas o no hay asignaturas disponibles.')

    def inscribir(self):
        #estudiante_info = self.cmb_estudiante.get()
        estudiante_info = next((e for e in self.gestor_escolar.estudiantes if str(e) == self.cmb_estudiante.get()), None)
        seleccionados = self.lst_asignaturas.curselection()

        if not estudiante_info or not seleccionados:
            messagebox.showwarning('Advertencia', 'Seleccione un estudiante y al menos una asignatura.')
            return

        dni = estudiante_info.dni
        disponibles = self.gestor_escolar.obtener_asignaturas_disponibles_para(dni)
        asignaturas_a_inscribir = [disponibles[i] for i in seleccionados]

        if not asignaturas_a_inscribir:
            messagebox.showinfo('Aviso', 'No hay asignaturas disponibles para inscribir.')
            return

        # Actualizar inscripciones
        anteriores = self.gestor_escolar.obtener_inscripciones(dni)
        nuevas = anteriores + [a for a in asignaturas_a_inscribir if a not in anteriores]
        self.gestor_escolar.inscribir_estudiante(dni, nuevas)

        messagebox.showinfo('Éxito', f'Inscripción realizada a {len(asignaturas_a_inscribir)} asignatura(s).')
        self.actualizar_lista_asignaturas()
