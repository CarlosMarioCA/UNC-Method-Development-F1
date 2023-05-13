import tkinter as tk
from data import style
from screen import *
from PIL import ImageTk, Image
import os

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        #Window settings
        self.title(" - Formula1 Administrator - ")
        self.geometry(style.DIMENSIONS)
        self.resizable(False,False)
        self.configure(bg="yellow")

        #Frame settings
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_columnconfigure(0,weight=1) #This can define how many columns are on the screen.
        self.container.grid_rowconfigure(0,weight=1)
        self.container.configure(background=style.BACKGROUND)
        
        #Initialization of buttons frame
        self.init_buttons(self.container)
        self.frames= {info.TABS[0]: Start, info.TABS[1]: Teams, 
                    info.TABS[2]: Pilots, info.TABS[3]: Classification,
                    info.TABS[4]: Carrers, info.TABS[5]: History,
                    info.TABS[6]: Live
                    } #Dictionary that contains all the frames that will be shown in the screen at some time.
        self.show_frame(self.frames[info.TABS[0]](self.container))

    def init_buttons(self, container):
        buttonFrame = tk.Frame(container)
        tk.Button(buttonFrame, text=info.TABS[0], relief="flat", command= lambda: self.click_button(info.TABS[0])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[1], relief="flat", command= lambda: self.click_button(info.TABS[1])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[2], relief="flat", command= lambda: self.click_button(info.TABS[2])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[3], relief="flat", command= lambda: self.click_button(info.TABS[3])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[4], relief="flat", command= lambda: self.click_button(info.TABS[4])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[5], relief="flat", command= lambda: self.click_button(info.TABS[5])).pack(side="left", fill="x", expand=True)
        tk.Button(buttonFrame, text=info.TABS[6], relief="flat", command= lambda: self.click_button(info.TABS[6])).pack(side="left", fill="x", expand=True)
        buttonFrame.pack(side="top", fill="x", pady= 20)

    def show_frame(self, frame):
        frame.tkraise() # Use this to put the frame in front, frame shown at this point.
    
    def click_button(self,text):
        for a in self.container.winfo_children():
            a.destroy()
        self.init_buttons(self.container)
        self.show_frame(self.frames[text](self.container))