import tkinter as tk
from tkinter import ttk
from data import style, info
from PIL import ImageTk, Image
from manager import *
import os

class Start(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[0]
        im = ""
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)
    
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
        self.container = container
        self.init_widget(container)
        self.pack(side = "left",fill="both",expand=True)

    def init_widget(self,container):
        frame = tk.Frame(container)
        frame.pack(side="top", fill="both",expand=True)
        
        #Left side of the screen.
        left = tk.Frame(frame)
        left.configure(bg=style.TEAMS)
        tk.Label(left, text=" Teams Menu ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Button(left, text=" Create new team ", relief="flat", command=lambda: self.showMenu(bot,"create")).pack(side="top", pady = 10)
        tk.Button(left, text=" Update team ", relief="flat").pack(side="top", pady = 10)
        tk.Button(left, text=" Delete ", relief="flat").pack(side="top", pady = 10)
        left.pack(side="left",fill="both",expand=True)

        #Right side of the screen.
        right = tk.Frame(frame)
        tree = ttk.Treeview(right, columns=('Teams'))
        scrollbar_vertical = ttk.Scrollbar(right, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)

        # Agregar encabezados de columna
        number = list(range(1,len(info.TEAMS)+1))
        teams = sorted(info.TEAMS)
        tree.heading('#0', text='ID')
        tree.heading('Teams', text='Teams')
        tree.column("#0", width=20)
        tree.column("Teams", width=200)
        for a,b in zip(number, teams):
            tree.insert('', 'end', text=str(a), values=b)
        
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

class Pilots(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
        self.container = container
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)


    def init_widget(self,container):
        frame = tk.Frame(container)
        frame.pack(side="top", fill="both",expand=True)
        
        #Left side of the screen.
        left = tk.Frame(frame)
        left.configure(bg=style.PILOTS)
        tk.Label(left, text=" Pilots Menu ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Button(left, text=" Create new Pilot ", relief="flat", command=lambda: self.showMenu(bot,"create")).pack(side="top", pady = 10)
        tk.Button(left, text=" Update Pilot ", relief="flat").pack(side="top", pady = 10)
        tk.Button(left, text=" Delete ", relief="flat").pack(side="top", pady = 10)
        left.pack(side="left",fill="both",expand=True)

        #Right side of the screen.
        right = tk.Frame(frame)
        right.pack(side="right",fill="both",expand=True)
        tree = ttk.Treeview(right, columns=("Teams"))
        scrollbar_vertical = ttk.Scrollbar(right, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)

        # Agregar encabezados de columna
        number = list(range(1,len(info.PILOTS)+1))
        pilots = sorted(info.PILOTS.keys())
        tree.heading('#0', text='Pilots')
        tree.heading('Teams', text='Team')
        tree.column("#0", width=150)
        tree.column("Teams", width=150)
        for a,b in zip(number, pilots):
            tree.insert('', 'end', text = b, values = info.PILOTS[b])
        
        # Agregar elementos
        tree.pack(side="left", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

class Classification(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
        self.container = container
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)

    def init_widget(self,container):
        frame = tk.Frame(container)
        frame.pack(side="top", fill="both",expand=True)
        
        #Left side of the screen.
        right = tk.Frame(frame)
        right.configure(bg=style.CLASSIFICATION)
        tk.Label(right, text=" Menu Classification ", relief="flat").pack(side="top", fill="x", pady = 20)
        right.pack(side="right",fill="both",expand=True)

        #Right side of the screen.
        left = tk.Frame(frame)
        left.pack(side="left",fill="both",expand=True)
        tree = ttk.Treeview(left, columns=("Points","Pilots","Teams"))
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)

        # Agregar encabezados de columna
        number = list(range(1,len(info.PILOTS)+1))
        score = sorted(info.POINTS.items(), key=lambda x: x[1], reverse=True)
        cont = 0
        tree.heading('#0', text='Position')
        tree.heading('Points', text='Points')
        tree.heading('Pilots', text='Pilots')
        tree.heading('Teams', text='Teams')
        tree.column("#0", width=20)
        tree.column("Points", width=20)
        tree.column("Pilots", width=100)
        tree.column("Teams", width=100)

        for a in score:
            cont += 1
            tree.insert('', 'end', text=cont, values=(a[1],a[0],info.PILOTS[a[0]]))
            
        
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

class Carrers(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
        self.container = container
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)

    def init_widget(self,container):
        frame = tk.Frame(container)
        frame.pack(side="top", fill="both",expand=True)
        
        #Left side of the screen.
        right = tk.Frame(frame)
        right.configure(bg=style.CARRERS)
        tk.Label(right, text=" Menu Carrers ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Button(right, text=" Create new team ", relief="flat", command=lambda: self.showMenu(bot,"create")).pack(side="top", pady = 10)
        tk.Button(right, text=" Update team ", relief="flat").pack(side="top", pady = 10)
        tk.Button(right, text=" Delete ", relief="flat").pack(side="top", pady = 10)
        right.pack(side="right",fill="both",expand=True)

        #Right side of the screen.
        left = tk.Frame(frame)
        tree = ttk.Treeview(left)
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)
        left.pack(side="left",fill="both",expand=True)

        # Agregar encabezados de columna
        number = list(range(1,len(info.CARRERS)+1))
        circuits = info.CARRERS
        tree.heading('#0', text='Circuit')
        tree.column("#0", width=200)

        for a,b in zip(number, circuits):
            tree.insert('', 'end', text=b)
        
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

class History(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
        self.container = container
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)

    def init_widget(self,container):
        frame = tk.Frame(container)
        frame.pack(side="top", fill="both",expand=True)
        
        #Left side of the screen.
        right = tk.Frame(frame)
        right.configure(bg=style.CARRERS)
        tk.Label(right, text=" Menu Carrers ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Button(right, text=" Create new team ", relief="flat", command=lambda: self.showMenu(bot,"create")).pack(side="top", pady = 10)
        tk.Button(right, text=" Update team ", relief="flat").pack(side="top", pady = 10)
        tk.Button(right, text=" Delete ", relief="flat").pack(side="top", pady = 10)
        right.pack(side="right",fill="both",expand=True)

        #Right side of the screen.
        left = tk.Frame(frame)
        tree = ttk.Treeview(left)
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)
        left.pack(side="left",fill="both",expand=True)

        # Agregar encabezados de columna
        number = list(range(1,len(info.CARRERS)+1))
        circuits = info.CARRERS
        tree.heading('#0', text='Circuit')
        tree.column("#0", width=200)

        for a,b in zip(number, circuits):
            tree.insert('', 'end', text=b)
        
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

class Live(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        name = info.TABS[1]
        im = ""
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
 