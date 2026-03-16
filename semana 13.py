import tkinter as tk
from tkinter import ttk

# -----------------------------
# MODELO
# -----------------------------

class Vehiculo:
    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
        return f"{self.placa} - {self.marca} - {self.propietario}"


# -----------------------------
# SERVICIO
# -----------------------------

class GarajeServicio:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self.vehiculos


# -----------------------------
# INTERFAZ GRAFICA
# -----------------------------

class AppGaraje:

    def __init__(self, root):

        self.servicio = GarajeServicio()

        self.root = root
        self.root.title("Sistema de Garaje")
        self.root.geometry("400x400")

        # Titulo
        titulo = tk.Label(root, text="Registro de Vehículos", font=("Arial", 16))
        titulo.pack(pady=10)

        # Frame formulario
        frame_form = tk.Frame(root)
        frame_form.pack()

        # Placa
        tk.Label(frame_form, text="Placa").grid(row=0, column=0, padx=5, pady=5)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1)

        # Marca
        tk.Label(frame_form, text="Marca").grid(row=1, column=0, padx=5, pady=5)
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1)

        # Propietario
        tk.Label(frame_form, text="Propietario").grid(row=2, column=0, padx=5, pady=5)
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1)

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        boton_agregar = tk.Button(frame_botones, text="Agregar Vehículo", command=self.agregar_vehiculo)
        boton_agregar.grid(row=0, column=0, padx=10)

        boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos)
        boton_limpiar.grid(row=0, column=1)

        # Tabla
        columnas = ("placa", "marca", "propietario")

        self.tabla = ttk.Treeview(root, columns=columnas, show="headings")
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        self.tabla.pack(pady=10, fill="x")

    # -----------------------------
    # FUNCIONES
    # -----------------------------

    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa and marca and propietario:

            vehiculo = Vehiculo(placa, marca, propietario)

            self.servicio.agregar_vehiculo(vehiculo)

            self.tabla.insert("", "end", values=(placa, marca, propietario))

            self.limpiar_campos()

    def limpiar_campos(self):

        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()
    app = AppGaraje(root)
    root.mainloop()