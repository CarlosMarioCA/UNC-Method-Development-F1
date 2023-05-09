import tkinter as tk
from data import style
from screen import *
from PIL import ImageTk, Image
import os

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title(" - Formula1 Administrator - ")
        self.geometry(style.DIMENSIONS)
        self.resizable(False,False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0,weight=1) #This can define how many columns are on the screen.
        container.grid_rowconfigure(0,weight=1)
        self.frames= {} #Dictionary that contains all the frames that will be shown in the screen at some time.

        for F in (Start,Pilot):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Start)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise() # Use this to put the frame in front, frame shown at this point.