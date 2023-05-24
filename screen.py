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
        lbtext = tk.Label(imFrame, text=info.ABOUT_US_DESCRIPTION, wraplength=300,justify="center").pack(side="right",fill="both",expand=True)
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
        tk.Button(left, text=" Create new team ", relief="flat", command= lambda: self.openNewTeam(left)).pack(side="top", pady = 10)
        tk.Button(left, text=" Update team ", relief="flat", command= lambda: self.openUpdateTeam(left)).pack(side="top", pady = 10)
        tk.Button(left, text=" Delete team ", relief="flat", command= lambda: self.openDeleteTeam(left)).pack(side="top", pady = 10)
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

    def openNewTeam(self, container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x500")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" NEW TEAM CREATION ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text=" Team name ").grid(row=1,column=0,padx=20,pady=10)
        name = tk.Entry(newWindow).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=" Team budget ").grid(row=2,column=0,padx=20,pady=10)
        budget = tk.Entry(newWindow).grid(row=2,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=" Team logotype ").grid(row=3,column=0,padx=20,pady=10)
        logotype = tk.Button(newWindow, text= " Upload logotype ").grid(row=3,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=info.DISCLAIMER_TEAM_CREATION, wraplength=300,justify="center").grid(row=4,column=0,padx=20,pady=10,columnspan=3)
        tk.Button(newWindow, text= " Create Team ",command= lambda: newWindow.destroy()).grid(row=5,column=0,padx=20,pady=10,columnspan=3)
    
    def openUpdateTeam(self,container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x300")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" UPDATE TEAM ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text= " Select team to Update ").grid(row=1,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.TEAMS).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text=" Update Team ",command= lambda: newWindow.destroy()).grid(row=2,column=0,padx=20,pady=10, columnspan=3)

    def openDeleteTeam(self,container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x300")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" DELETE TEAM ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text= " Select team to Delete ").grid(row=1,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.TEAMS).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text=" Delete Team ",command= lambda: newWindow.destroy()).grid(row=2,column=0,padx=20,pady=10, columnspan=3)


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
        tk.Button(left, text=" Create new pilot ", relief="flat", command=lambda: self.openNewPilot(left)).pack(side="top", pady = 10)
        tk.Button(left, text=" Update pilot ", relief="flat", command=lambda: self.openUpdatePilot(left)).pack(side="top", pady = 10)
        tk.Button(left, text=" Delete pilot ", relief="flat", command=lambda: self.openDeletePilot(left)).pack(side="top", pady = 10)
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

    def openNewPilot(self, container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x500")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" NEW PILOT CREATION ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text=" Pilot name ").grid(row=1,column=0,padx=20,pady=10)
        name = tk.Entry(newWindow).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=" Team ").grid(row=2,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.TEAMS).grid(row=2,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=" Nationality ").grid(row=3,column=0,padx=20,pady=10)
        varNationality = tk.StringVar()
        optionNationality = tk.OptionMenu(newWindow, varNationality, *info.COUNTRIES).grid(row=3,column=1,padx=10,pady=10, columnspan=2)
        tk.Label(newWindow, text=info.DISCLAIMER_PILOT_CREATION, wraplength=300,justify="center").grid(row=4,column=0,padx=20,pady=10,columnspan=3)
        tk.Button(newWindow, text= " Create Pilot ").grid(row=5,column=0,padx=20,pady=10,columnspan=3)

    def openUpdatePilot(self,container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x300")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" UPDATE PILOT ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text= " Select pilot to Update ").grid(row=1,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.PILOTS).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text=" Update Pilot ",command= lambda: newWindow.destroy()).grid(row=2,column=0,padx=20,pady=10, columnspan=3)


    def openDeletePilot(self,container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x300")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" PILOT TEAM ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text= " Select pilot to Delete ").grid(row=1,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.PILOTS).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text=" Delete Pilot ",command= lambda: newWindow.destroy()).grid(row=2,column=0,padx=20,pady=10, columnspan=3)



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
        im = ImageTk.PhotoImage(Image.open("images/history.jpg").resize((400,350),resample=Image.BICUBIC))
        self.im = im
        lbim = tk.Label(imFrame, image = im).pack(side="left", fill="both", expand=True)
        lbtext = tk.Label(imFrame, text=style.ABOUT_US_DESCRIPTION, wraplength=300,justify="center").pack(side="right",fill="both",expand=True)
        imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)
 