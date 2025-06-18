import tkinter as tk
from tkinter import ttk

class NotasPorAsignaturaForm(tk.Frame):
    def __init__(self, master, gestor_escolar):
        super().__init__(master)
        self.gestor_escolar = gestor_escolar
        self.configure(padx=15, pady=15)

        estilo = ttk.Style()
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        estilo.configure("Treeview", rowheight=25, font=("Arial", 10))

        marco = ttk.LabelFrame(self, text="Notas por Asignatura", padding=15)
        marco.pack(fill="both", expand=True)

        ttk.Label(marco, text="Asignatura:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.cmb_asignatura = ttk.Combobox(marco, state="readonly", width=40)
        self.cmb_asignatura.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_asignatura.bind("<<ComboboxSelected>>", self.mostrar_notas)

        self.tree = ttk.Treeview(marco, columns=("dni", "nombre", "apellido", "nota"), show="headings", height=12)
        self.tree.heading("dni", text="DNI")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("apellido", text="Apellido")
        self.tree.heading("nota", text="Nota")

        self.tree.column("dni", width=100)
        self.tree.column("nombre", width=150)
        self.tree.column("apellido", width=150)
        self.tree.column("nota", width=80, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=10, sticky="nsew")

        # Scrollbar
        scrollbar = ttk.Scrollbar(marco, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky="ns")

        # Promedio
        self.lbl_promedio = ttk.Label(marco, text="Promedio: -", font=("Arial", 10, "bold"))
        self.lbl_promedio.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        marco.columnconfigure(1, weight=1)
        marco.rowconfigure(1, weight=1)

        self.cargar_asignaturas()

    def cargar_asignaturas(self):
        self.cmb_asignatura["values"] = [a.nombre for a in self.gestor_escolar.asignaturas]
        if self.cmb_asignatura["values"]:
            self.cmb_asignatura.current(0)
            self.mostrar_notas()

    def mostrar_notas(self, event=None):
        asignatura_nombre = self.cmb_asignatura.get()
        notas = self.gestor_escolar.obtener_notas_por_asignatura(asignatura_nombre)

        for row in self.tree.get_children():
            self.tree.delete(row)

        total = 0
        cantidad = 0

        for nota in notas:
            estudiante = nota.estudiante
            self.tree.insert("", tk.END, values=(estudiante.dni, estudiante.nombre, estudiante.apellido, nota.nota))
            total += nota.nota
            cantidad += 1

        promedio = round(total / cantidad, 2) if cantidad else "-"
        self.lbl_promedio.config(text=f"Promedio: {promedio}")

        
