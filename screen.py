import tkinter as tk
from data import style, info
from PIL import ImageTk, Image
from manager import *
import os

class Start(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[0]
        im = ""
        self.configure(bg="yellow")
        self.activation(container)

    def activation(self, container):
        self.init_widget(container)
        self.pack(side="bottom",fill="both",expand=True)
    
    def init_widget(self,container):
        #Loading the image
        imFrame = tk.Frame(container)
        im = ImageTk.PhotoImage(Image.open("images/front.jpg").resize((400,350),resample=Image.BICUBIC))
        self.im = im
        lbim = tk.Label(imFrame, image = im).pack(side="left", fill="both", expand=True)
        lbtext = tk.Label(imFrame, text=style.ABOUT_US_DESCRIPTION, wraplength=300,justify="center").pack(side="right",fill="both",expand=True)
        imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)
        
class Teams(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
        self.activation(container)

    def activation(self,container):
        self.init_widget(container)
        self.pack(side="bottom",fill="both",expand=True)

    def init_widget(self,container):
        #Loading the image
        imFrame = tk.Frame(container)
        im = ImageTk.PhotoImage(Image.open("images/love.jpg").resize((400,350),resample=Image.BICUBIC))
        self.im = im
        lbim = tk.Label(imFrame, image = im).pack(side="left", fill="both", expand=True)
        lbtext = tk.Label(imFrame, text=style.ABOUT_US_DESCRIPTION, wraplength=300,justify="center").pack(side="right",fill="both",expand=True)
        imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)


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
