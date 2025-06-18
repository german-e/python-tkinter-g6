import tkinter as tk
from tkinter import ttk

def mostrar_acerca_de():
    ventana = tk.Toplevel()
    ventana.title('Acerca del proyecto')
    ventana.geometry('400x300')
    ventana.resizable(False, False)

    # Frame principal
    frame = ttk.Frame(ventana, padding=20)
    frame.pack(fill='both', expand=True)

    # Título
    lbl_titulo = ttk.Label(frame, text='Sistema de Gestión Escolar', font=('Arial', 14, 'bold'))
    lbl_titulo.pack(pady=(0, 10))

    # Separador
    ttk.Separator(frame, orient='horizontal').pack(fill='x', pady=5)

    # Contenido
    descripcion = (
        'Este sistema permite registrar y consultar notas de estudiantes.\n\n'
        '🧰 Tecnologías utilizadas:\n'
        '  • Python 3\n'
        '  • Tkinter (GUI)\n'
        '  • POO (Programación Orientada a Objetos)\n\n'
        '👨‍💻 Desarrollado por:\n'
        '   • Alderete, Federico Eudes\n'
        '   • Espindola, Germán Leonel\n'
        '   • Petroff Yañuk, Matías Daniel\n'
        '   • Weisgerber, Gladys Ester\n\n'
        '📅 Versión: 1.0 - Junio 2025'
    )
    lbl_descripcion = ttk.Label(frame, text=descripcion, justify='left')
    lbl_descripcion.pack(anchor='w', fill='x')

    # Botón cerrar
    ttk.Button(frame, text='Cerrar', command=ventana.destroy).pack(pady=15)

    # Centrar respecto a la ventana principal
    ventana.transient()
    ventana.grab_set()
    ventana.focus_set()
