import tkinter as tk
from tkinter import ttk

class Formula1App:

    def __init__(self, root):
        self.root = root
        self.root.title("Administración de Fórmula 1")
        self.root.geometry("800x600")

        # Crear notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Crear pestañas
        self.create_about_us_tab()
        self.create_teams_tab()
        self.create_pilots_tab()
        self.create_classification_tab()
        self.create_circuits_tab()
        self.create_history_tab()
        self.create_live_tab()

    def create_about_us_tab(self):
        # Crear pestaña de "About Us"
        about_us_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(about_us_tab, text="About Us")

        # Agregar widgets a la pestaña de "About Us"
        about_us_label = ttk.Label(about_us_tab, text="Pestaña de About Us")
        about_us_label.pack(pady=20)

    def create_teams_tab(self):
        # Crear pestaña de equipos
        teams_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(teams_tab, text="Equipos")

        # Agregar widgets a la pestaña de equipos
        team_label = ttk.Label(teams_tab, text="Pestaña de equipos")
        team_label.pack(pady=20)

    def create_pilots_tab(self):
        # Crear pestaña de pilotos
        pilots_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(pilots_tab, text="Pilotos")

        # Agregar widgets a la pestaña de pilotos
        pilot_label = ttk.Label(pilots_tab, text="Pestaña de pilotos")
        pilot_label.pack(pady=20)

    def create_classification_tab(self):
        # Crear pestaña de clasificación
        classification_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(classification_tab, text="Clasificación")

        # Agregar widgets a la pestaña de clasificación
        classification_label = ttk.Label(classification_tab, text="Pestaña de clasificación")
        classification_label.pack(pady=20)

    def create_circuits_tab(self):
        # Crear pestaña de circuitos
        circuits_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(circuits_tab, text="Circuitos")

        # Agregar widgets a la pestaña de circuitos
        circuit_label = ttk.Label(circuits_tab, text="Pestaña de circuitos")
        circuit_label.pack(pady=20)

    def create_history_tab(self):
        # Crear pestaña de historia
        history_tab = ttk.Frame(self.notebook, width=800, height=550)
        self.notebook.add(history_tab, text="Historia")

        # Agregar widgets a la pestaña de historia
        history_label = ttk.Label