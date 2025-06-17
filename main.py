# from ui.pantalla_inicio import PantallaInicio


# if __name__ == "__main__":
#     app = PantallaInicio()
#     app.mainloop() 
import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# -------------------------- CLASES --------------------------
class Alumno:
    def __init__(self, nombre, apellido, curso, nota=0, asistencia=0):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.nota = nota
        self.asistencia = asistencia

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - Curso: {self.curso} - Nota: {self.nota} - Asistencia: {self.asistencia}%"

# -------------------------- FUNCIONES --------------------------
def agregar_alumno():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    curso = entrada_curso.get()

    if not nombre or not apellido or not curso:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    nuevo_alumno = Alumno(nombre, apellido, curso)
    alumnos.append(nuevo_alumno)
    lista_alumnos.insert(tk.END, str(nuevo_alumno))

    entrada_nombre.delete(0, tk.END)
    entrada_apellido.delete(0, tk.END)
    entrada_curso.delete(0, tk.END)

def eliminar_alumno():
    seleccion = lista_alumnos.curselection()
    if not seleccion:
        messagebox.showwarning("Error", "Seleccioná un alumno para eliminar")
        return
    alumnos.pop(seleccion[0])
    lista_alumnos.delete(seleccion[0])

def editar_alumno():
    seleccion = lista_alumnos.curselection()
    if not seleccion:
        messagebox.showwarning("Error", "Seleccioná un alumno para editar")
        return

    idx = seleccion[0]
    alumno = alumnos[idx]

    try:
        nueva_nota = float(entry_nota.get())
        nueva_asistencia = float(entry_asistencia.get())
    except:
        messagebox.showwarning("Error", "Nota y asistencia deben ser numéricos")
        return

    alumno.nota = nueva_nota
    alumno.asistencia = nueva_asistencia
    lista_alumnos.delete(idx)
    lista_alumnos.insert(idx, str(alumno))
    entry_nota.delete(0, tk.END)
    entry_asistencia.delete(0, tk.END)

def buscar_por_curso():
    curso_buscado = entry_busqueda.get()
    lista_alumnos.delete(0, tk.END)
    for alumno in alumnos:
        if alumno.curso == curso_buscado:
            lista_alumnos.insert(tk.END, str(alumno))

def exportar_csv():
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not archivo:
        return
    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Apellido", "Curso", "Nota", "Asistencia"])
        for alumno in alumnos:
            writer.writerow([alumno.nombre, alumno.apellido, alumno.curso, alumno.nota, alumno.asistencia])
    messagebox.showinfo("Exportación completa", "Los datos fueron guardados exitosamente.")

# -------------------------- VENTANA PRINCIPAL --------------------------
ventana = tk.Tk()
ventana.title("Gestor de Alumnos - Escuela Secundaria")
ventana.geometry("700x550")

# Menú desplegable
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Exportar a CSV", command=exportar_csv)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Frame formulario
frame_form = tk.Frame(ventana)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0)
tk.Label(frame_form, text="Apellido:").grid(row=1, column=0)
tk.Label(frame_form, text="Curso:").grid(row=2, column=0)

entrada_nombre = tk.Entry(frame_form)
entrada_apellido = tk.Entry(frame_form)
entrada_curso = tk.Entry(frame_form)

entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
entrada_apellido.grid(row=1, column=1, padx=5, pady=5)
entrada_curso.grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame_form, text="Agregar alumno", command=agregar_alumno).grid(row=3, column=0, columnspan=2, pady=10)

# Frame edición
frame_editar = tk.Frame(ventana)
frame_editar.pack(pady=5)

entry_nota = tk.Entry(frame_editar, width=5)
entry_asistencia = tk.Entry(frame_editar, width=5)
entry_nota.grid(row=0, column=1)
entry_asistencia.grid(row=0, column=3)

tk.Label(frame_editar, text="Nueva nota:").grid(row=0, column=0)
tk.Label(frame_editar, text=" Asistencia:").grid(row=0, column=2)

btn_editar = tk.Button(frame_editar, text="Actualizar datos", command=editar_alumno)
btn_editar.grid(row=0, column=4, padx=5)

# Frame búsqueda
frame_buscar = tk.Frame(ventana)
frame_buscar.pack(pady=5)

entry_busqueda = tk.Entry(frame_buscar)
entry_busqueda.grid(row=0, column=1)
tk.Label(frame_buscar, text="Buscar por curso:").grid(row=0, column=0)
tk.Button(frame_buscar, text="Buscar", command=buscar_por_curso).grid(row=0, column=2)

# Lista con scrollbar
frame_lista = tk.Frame(ventana)
frame_lista.pack()

scroll = tk.Scrollbar(frame_lista)
lista_alumnos = tk.Listbox(frame_lista, width=90, yscrollcommand=scroll.set)
scroll.config(command=lista_alumnos.yview)

lista_alumnos.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

tk.Button(ventana, text="Eliminar seleccionado", command=eliminar_alumno).pack(pady=10)

# -------------------------- VARIABLES GLOBALES --------------------------
alumnos = []

# -------------------------- INICIO --------------------------
ventana.mainloop()
