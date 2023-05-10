import tkinter as tk
from data import style, info
from PIL import ImageTk, Image
from Manager import *
import os

class Start(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widget(controller)
        self.pack(side="top",fill="both",expand=True)
        self.im
    
    def init_widget(self,controller):
        buttonFrame = tk.Frame(self)
        tabs = []
        counter = 0
        for i in info.TABS:
            button = tk.Button(buttonFrame, text=i, relief="flat",command = lambda: self.show_pilot())
            button.pack(side="left", fill="x", expand=True)
            tabs.append(button)
            counter += 1 
        buttonFrame.pack(side="top", fill="x", expand=True)

        #Loading the image
        imFrame = tk.Frame(self)
        imFrame.configure(background=style.BACKGROUND)
        im = ImageTk.PhotoImage(Image.open("images/front.jpg").resize((400,350),resample=Image.BICUBIC))
        self.im = im
        lbim = tk.Label(imFrame, image = im).pack(side="left", fill="both", expand=True)
        lbtext = tk.Label(imFrame, text=style.ABOUT_US_DESCRIPTION, wraplength=300,justify="center").pack(side="right",fill="both",expand=True)
        imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)
    
def show_pilot(self):
    self.controller.show_frame(Pilot)

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
"""
    def show_teams(self):
        self.controller.show_frame(Pilot)

    def show_pilot(self):
        self.controller.show_frame(Pilot)

    def show_pilot(self):
        self.controller.show_frame(Pilot)

    def show_pilot(self):
        self.controller.show_frame(Pilot)

    def show_pilot(self):
        self.controller.show_frame(Pilot)

    def show_pilot(self):
        self.controller.show_frame(Pilot)


"""
"""
class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Pilot(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
"""
