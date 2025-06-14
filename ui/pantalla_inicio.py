import tkinter as tk
from tkinter import ttk, Menu
import datetime
import time
import threading

from classes.gestor_escolar import Gestor
from ui.pantalla_estudiante import EstudianteForm
from ui.pantalla_notas import NotaForm
from ui.pantalla_ver_notas import VerNotasForm
from ui.pantalla_asignatura import AsignaturaForm

class PantallaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de gestión Escolar")
        self.geometry("600x400")
        self.crear_menu()
        self.actualizar_hora();

        self.crear_botones_opciones()    
        self.ventana_abierta = None
        self.gestor_escolar = Gestor() # Aquí se debería inicializar tu gestor escolar


    def crear_botones_opciones(self):
        

       # Botones principales
        frame_botones = tk.Frame(self)
        frame_botones.pack()

        # Colocar los botones uno al lado del otro con pack
        btn_estudiante = tk.Button(frame_botones, text="Estudiante", width=20, height=2, bg="#ADD8E6",   fg="black", command=self.abrir_pantalla_estudiantes)
        btn_estudiante.pack(side=tk.LEFT, padx=5, pady=5)
        btn_asignatura = tk.Button(frame_botones, text="Asignatura", width=20, height=2, bg="#ADD8E6",   fg="black", command=self.abrir_pantalla_asignaturas)
        btn_asignatura.pack(side=tk.LEFT, padx=5, pady=5)

        # btn_profesor = tk.Button(frame_botones, text="Profesor", width=20, height=2, bg="#ADD8E6",   fg="black", command=self.abrir_pantalla_asignaturas)  # Aquí deberías cambiar a la pantalla de profesores
        # btn_profesor.pack(side=tk.LEFT, padx=5, pady=5)


    def actualizar_hora(self):
        # Reloj
        reloj = tk.Label(self, text="", font=("Consolas", 14, "bold"), bg="yellow", fg="black")
        #Ubicar el reloj en esquina inferior derecha
        reloj.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
        
        def update():
            while True:
                hora = time.strftime('%I : %M %p')
                fecha = datetime.datetime.now().strftime('%d-%m-%Y')
                reloj.config(text=f'{fecha} | {hora}')
                time.sleep(1)
        hilo = threading.Thread(target=update, daemon=True)
        hilo.start()

    def crear_menu(self):
        barra_menu = Menu(self)
        self.config(menu=barra_menu)

        # Menú "Inicio"
        menu_inicio = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Cargar Notas", command=self.abrir_pantalla_notas)
        menu_inicio.add_command(label="Cargar Asignaturas")
        menu_inicio.add_command(label="Salir", command=self.quit)

        # Menú "Consulta"
        menu_consulta = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Consulta", menu=menu_consulta)
        menu_consulta.add_command(label="Lista Estudiantes", command=self.abrir_pantalla_estudiantes)
        menu_consulta.add_command(label="Lista Asignaturas",command=self.abrir_pantalla_asignaturas)
        # menu_consulta.add_command(label="Lista Profesores")
        menu_consulta.add_command(label="Notas por Estudiante", command=self.abrir_ver_notas)

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

        
        

    def abrir_pantalla_asignaturas(self):
        if self.ventana_abierta:
            self.ventana_abierta.destroy()
        # Aquí se debería abrir la pantalla de asignaturas  

        self.ventana_abierta = AsignaturaForm(self, self.gestor_escolar)
        
        self.ventana_abierta.pack(fill=tk.BOTH, padx=10, pady=5)
        

        

    
        