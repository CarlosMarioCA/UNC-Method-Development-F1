import tkinter as tk
from data import style

class Start(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value=" Letrero ") #Self indicates where the String will be placed
        self.init_widget()
    
    def init_widget(self):
        lb = tk.Label(self, text=" Probando cosas ", justify="center", )

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        