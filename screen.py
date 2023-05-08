import tkinter as tk
from data import style, config

class Start(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value=" Letrero ") #Self indicates where the String will be placed
        self.init_widget()
    
    def init_widget(self):
        lb = tk.Label(self, text=" Probando cosas ", justify="center",**style.STYLE)
        lb.pack(side="top", fill="both", expand=True, padx=22,pady=11)
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack(side="top",fill="both",expand=True, padx=22, pady=11)
        tk.Label(optionsFrame, text= "Prueba", justify="center",**style.STYLE).pack(side="top", fill="x", expand=True)

        for(key, values) in config.MODES.items():
            tk.Radiobutton(optionsFrame, text = "Und")

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        