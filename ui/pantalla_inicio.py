import tkinter as tk
from tkinter import Menu
import locale
import datetime
import time

from classes.gestor_escolar import Gestor

from ui.pantalla_estudiante import EstudianteForm
from ui.pantalla_inscriptos_por_asignatura import NotasPorAsignaturaForm
from ui.pantalla_notas import NotaForm
from ui.pantalla_ver_notas import VerNotasForm
from ui.pantalla_asignatura import AsignaturaForm
from ui.pantalla_acercade import mostrar_acerca_de
from ui.pantalla_inscripciones import InscripcionAsignaturaForm  # Asegúrate de que este módulo exista y esté implementado correctamente

class PantallaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Sistema de gestión Escolar')
        self.geometry('800x600')
       
        self.crear_menu()
        self.crear_reloj();

        self.crear_botones_opciones()    
        self.ventana_abierta = None
        self.gestor_escolar = Gestor() # Aquí se debería inicializar tu gestor escolar

        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configurar el locale para español


    def crear_botones_opciones(self):
        

       # Botones principales
        frame_botones = tk.Frame(self)
        frame_botones.pack()

        # Colocar los botones uno al lado del otro con pack
        btn_estudiante = tk.Button(frame_botones, text='Estudiante', width=15, height=2, bg='#ADD8E6',   fg='black', command=self.abrir_pantalla_estudiantes)
        
        btn_estudiante.pack(side=tk.LEFT, padx=5, pady=5)
        btn_asignatura = tk.Button(frame_botones, text='Asignatura', width=15, height=2, bg='#ADD8E6',   fg='black', command=self.abrir_pantalla_asignaturas)
        btn_asignatura.pack(side=tk.LEFT, padx=5, pady=5)
        btn_inscripcion = tk.Button(frame_botones, text='Inscripción', width=15, height=2, bg='#ADD8E6',   fg='black', command=self.abrir_pantalla_inscripciones)
        btn_inscripcion.pack(side=tk.LEFT, padx=5, pady=5)
        btn_profesor = tk.Button(frame_botones, text='Notas', width=15, height=2, bg='#ADD8E6',   fg='black', command=self.abrir_pantalla_notas)  # Aquí deberías cambiar a la pantalla de profesores
        btn_profesor.pack(side=tk.LEFT, padx=5, pady=5)


    def crear_reloj(self):
        # Frame dedicado al reloj, en parte inferior
        frame_reloj = tk.Frame(self, bg='#f0f0f0')
        frame_reloj.pack(side='bottom', fill='x')

        self.lbl_reloj = tk.Label(
            frame_reloj,
            text='',
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0',
            fg='#333'
        )
        self.lbl_reloj.pack(side='right', padx=10, pady=5)

        self.actualizar_reloj()

    def actualizar_reloj(self):
        hora = time.strftime('%H:%M:%S')
        fecha = datetime.datetime.now().strftime('%d de %B')
        self.lbl_reloj.config(text=f'{fecha} | {hora}')
        self.after(1000, self.actualizar_reloj)  # Sin hilos



    def crear_menu(self):
        barra_menu = Menu(self)
        self.config(menu=barra_menu)

        # Menú 'Inicio'
        menu_inicio = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
        menu_inicio.add_command(label='Registrar Estudiante', command=self.abrir_pantalla_estudiantes)
        menu_inicio.add_command(label='Registrar Asignatura', command=self.abrir_pantalla_asignaturas)
        menu_inicio.add_command(label='Inscribir estudiante', command=self.abrir_pantalla_inscripciones)
        menu_inicio.add_command(label='Cargar Notas', command=self.abrir_pantalla_notas)
        # Separador
        menu_inicio.add_separator()
        
        menu_inicio.add_command(label='Salir', command=self.quit)

        # Menú 'Consulta'
        menu_consulta = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Consulta', menu=menu_consulta)
        
        # menu_consulta.add_command(label='Lista Profesores')
        menu_consulta.add_command(label='Notas por Estudiante', command=self.abrir_ver_notas)
        menu_consulta.add_command(label='Notas por Asignatura', command=self.abrir_notas_por_asignatura)
        
        

        # Menú 'Ayuda'
        menu_ayuda = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
        menu_ayuda.add_command(label='Acerca de', command=self.mostrar_acerca_de)
    
    def mostrar_acerca_de(self):
        mostrar_acerca_de()
    

    
    def abrir_pantalla_notas(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()
        self.ventana_abierta = NotaForm(self, self.gestor_escolar)       
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=10)
        
    def abrir_ver_notas(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()
        
        self.ventana_abierta = VerNotasForm(self, self.gestor_escolar)
        
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)

    def abrir_pantalla_estudiantes(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()

        self.ventana_abierta = EstudianteForm(self, self.gestor_escolar)        
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)

    
    
    def abrir_notas_por_asignatura(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()
        # Aquí se debería abrir la pantalla de notas por asignatura
        self.ventana_abierta = NotasPorAsignaturaForm(self, self.gestor_escolar)
        
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)
        

    def abrir_pantalla_asignaturas(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()
        
        self.ventana_abierta = AsignaturaForm(self, self.gestor_escolar)        
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)
                

    def abrir_pantalla_inscripciones(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()

        self.ventana_abierta = InscripcionAsignaturaForm(self, self.gestor_escolar)
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)

    
        