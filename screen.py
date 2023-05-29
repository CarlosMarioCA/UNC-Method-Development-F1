import tkinter as tk
from tkinter import ttk
from data import style, info
from PIL import ImageTk, Image
from manager import *
import random
import time
import threading
import os

class Start(tk.Frame):

    def __init__(self, container, season_started, start_season):
        super().__init__(container)
        self.container = container
        self.start_season = start_season
        self.season_started = season_started
        self.frameProgress = tk.Frame(container)
        name = info.TABS[0]
        im = ""
        self.init_widget(container)
        self.pack(side="left",fill="both",expand=True)

    def set_progress(self, frame):
        self.frameProgress = frame
    
    def get_progress(self):
        return self.frameProgress

    def init_widget(self,container):
        #Loading the image
        imFrame = tk.Frame(container)
        imFrame.configure(bg=style.START)
        if self.season_started:
            imFrame = self.get_progress()
            imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)
            tk.Label(imFrame,text="Ya había comenzado").pack()
        else:
            im = ImageTk.PhotoImage(Image.open("images/main.jpg").resize((400,350),resample=Image.BICUBIC))
            self.im = im
            lbim = tk.Label(imFrame, image = im).pack(side="left", expand=True)
            tk.Button(imFrame, text=" Start Season ", command=lambda: self.showLogisticsPanel(imFrame)).pack(side="right", pady = 60,padx=60,expand=True, fill="both")
            imFrame.pack(side="top", fill="both",expand=True,padx=20,pady=10)

    def showLogisticsPanel(self,container):
        self.start_season()
        newWindow = tk.Toplevel(container)
        newWindow.geometry("500x300")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" ORGANIZING THE F1 CHAMPIONSHIP AND STABLISHING LOGISTICS ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        var = tk.IntVar()
        tk.Label(newWindow, text= " Establishing F1 Championship ").grid(row=1,column=0,padx=20,pady=10)
        tk.Checkbutton(newWindow, text=" Accept ", variable=var).grid(row=1,column=1,padx=20,pady=10)
        varDHL = tk.IntVar()
        tk.Label(newWindow, text= " Sign logistic contract with DHL ").grid(row=2,column=0,padx=20,pady=10)
        tk.Checkbutton(newWindow, text=" Accept ", variable=varDHL).grid(row=2,column=1,padx=20,pady=10)
        varEmployee = tk.IntVar()
        tk.Label(newWindow, text= " The employees  of each team already developed the single-seaters ", wraplength=300).grid(row=3,column=0,padx=20,pady=10)
        tk.Checkbutton(newWindow, text=" Accept ", variable=varEmployee).grid(row=3,column=1,padx=20,pady=10)
        tk.Button(newWindow, text=" Complete ",command= lambda:self.showChampionship(container, var, varDHL,varEmployee)).grid(row=4,column=0,padx=20,pady=10, columnspan=3)

    def showChampionship(self,container,var1,var2,var3):
        if var1.get() == 1 and var2.get() == 1 and var3.get()==1:
            for a in container.winfo_children():
                a.destroy()

            frame = container
            frame.grid_columnconfigure(0,weight=1)
            frame.grid_columnconfigure(1,weight=2)
            self.showGrandPrix(0,frame)
        
    def showGrandPrix(self,order,frame):
        frame.configure(bg=style.CHAMPIONSHIP)
        tk.Label(frame,text=" FORMULA 1 CHAMPIONSHIP ADMINISTRATOR ", font=("Arial",14)).grid(row=0,column=0,padx=20,pady=10,columnspan=3)
        tk.Label(frame,text=" No. of the Circuit:").grid(row=1,column=0,padx=20,pady=10)
        tk.Label(frame,text=order+1).grid(row=1,column=1,padx=20,pady=10)
        tk.Label(frame,text=" Name of the Circuit:").grid(row=2,column=0,padx=20,pady=10)
        tk.Label(frame,text=info.CARRERS[order]).grid(row=2,column=1,padx=20,pady=10)
        tk.Label(frame,text="Grand Prix directives endorsement",justify="center").grid(row=3,column=0,padx=20,pady=10)
        var = tk.IntVar()
        tk.Checkbutton(frame, variable=var).grid(row=3,column=1,padx=20,pady=10)
        tk.Button(frame,text=" RUN A GRAND PRIX", command=lambda: self.runGP(frame,var,order)).grid(row=4,column=0,padx=20,pady=10,columnspan=3)
        
        #Right side of the screen.
        left = tk.Frame(frame)
        left.grid(row=5,column=0,padx=20,pady=10,columnspan=3,sticky=tk.NSEW)
        tree = ttk.Treeview(left, columns=("Points","Pilots","Teams"))
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)

        # Agregar encabezados de columna
        pilots = list(info.POINTS.items())
        random.shuffle(pilots)
        classification = dict(pilots)

        number = list(range(1,len(classification)+1))
        cont = 0
        tree.heading('#0', text='Position')
        tree.heading('Points', text='Points')
        tree.heading('Pilots', text='Pilots')
        tree.heading('Teams', text='Teams')
        tree.column("#0", width=20)
        tree.column("Points", width=20)
        tree.column("Pilots", width=100)
        tree.column("Teams", width=100)

        list_podium = []

        for a,b in zip(classification, info.SCORE_POR_POSITION):
            classification[a] = b
            info.POINTS[a] = info.POINTS[a] + b
            team = info.PILOTS[a]
            info.TEAMS_ATRIBUTES[team]["points"] = info.TEAMS_ATRIBUTES[team]["points"] + b
            cont += 1
            tree.insert('', 'end', text=cont, values=(classification[a],a,info.PILOTS[a]))
            if cont < 4:
                list_podium.append(a)

        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        tk.Label(frame, text=" PODIUM: 1. " + list_podium[0] + " 2. " + list_podium[1] + " 3. " + list_podium[2]).grid(row=6,column=0,padx=20,pady=10,columnspan=3)

        self.set_progress(frame)


    def runGP(self, frame, var, order):
        order = order + 1 #Pilas acá
        if order < len(info.CARRERS):
            if var.get()==1:
                for a in frame.winfo_children():
                    a.destroy()
                self.showGrandPrix(order,frame)
        elif order >= len(info.CARRERS):
            self.awardingSeason(frame)
    
    def awardingSeason(self, frame):
        for a in frame.winfo_children():
            a.destroy()

        frame.configure(bg=style.AWARDING)
        pilot_champion = max(info.POINTS, key=lambda k: info.POINTS[k])
        point_pilot_champion = info.POINTS[pilot_champion]

        constructor_champion = None
        point_contructor_champion = 0

        for const, atributes in info.TEAMS_ATRIBUTES.items():
            aux = atributes["points"]
            if aux > point_contructor_champion:
                point_contructor_champion = aux
                constructor_champion = const

        tk.Label(frame,text = " RESULTS FOR FORMULA 1 CHAMPIONSHIP ", font=("Arial",14)).grid(row=0,column=0,padx=20,pady=10,columnspan=3)
        tk.Label(frame, text = " Pilot's Championship Winner : ").grid(row=1,column=0,padx=20,pady=10)
        tk.Label(frame, text = pilot_champion).grid(row=1,column=1,padx=20,pady=10, columnspan=2)
        tk.Label(frame, text = " Points : ").grid(row=2,column=0,padx=20,pady=10)
        tk.Label(frame, text = point_pilot_champion).grid(row=2,column=1,padx=20,pady=10, columnspan=2)
        tk.Label(frame, text = " Constructor's Championship Winner : ").grid(row=3,column=0,padx=20,pady=10)
        tk.Label(frame, text = constructor_champion).grid(row=3,column=1,padx=20,pady=10, columnspan=2)
        tk.Label(frame, text = " Points : ").grid(row=4,column=0,padx=20,pady=10)
        tk.Label(frame, text = point_contructor_champion).grid(row=4,column=1,padx=20,pady=10, columnspan=2)
        tk.Button(frame, text=" END SEASON ").grid(row=5,column=0,padx=20,pady=10, columnspan=3)


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
        tk.Button(newWindow, text=" Update Team ",command= lambda: self.updateTeam(newWindow,varTeam.get())).grid(row=2,column=0,padx=20,pady=10, columnspan=3)

    def updateTeam(self,container,varTeam):
        teamToUpdate = info.TEAMS_ATRIBUTES[varTeam]
        print(teamToUpdate)
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x500")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)

        tk.Label(newWindow, text=" UPDATE TEAM ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)

        tk.Label(newWindow, text=" Team name ").grid(row=1,column=0,padx=20,pady=10)
        varName = tk.StringVar()
        varName.set(teamToUpdate["Name"])
        name = tk.Entry(newWindow, textvariable=varName).grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        tk.Label(newWindow, text="Team Budget").grid(row=2,column=0,padx=20,pady=10)
        varBudget = tk.StringVar()
        varBudget.set(teamToUpdate["Budget"])
        budget = tk.Entry(newWindow, textvariable=varBudget).grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        tk.Label(newWindow, text="Trophy Case").grid(row=3,column=0,padx=20,pady=10)
        varCase = tk.StringVar()
        varCase.set(teamToUpdate["Trophies"])
        budget = tk.Entry(newWindow, textvariable=varCase).grid(row=3,column=1,padx=10,pady=10, columnspan=2)

        tk.Label(newWindow, text=" Existing Logotype ").grid(row=4,column=0,padx=20,pady=10)
        logotype = tk.Button(newWindow, text= " Change Logotype ").grid(row=4,column=1,padx=10,pady=10, columnspan=2)

        tk.Button(newWindow, text= " Create Team ",command= lambda: newWindow.destroy()).grid(row=5,column=0,padx=20,pady=10,columnspan=3)


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
        tk.Button(newWindow, text= " Create Pilot ",command= lambda: newWindow.destroy()).grid(row=5,column=0,padx=20,pady=10,columnspan=3)

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



class Classification_pilots(tk.Frame):

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

        leader = score[0][0]

        for a in score:
            cont += 1
            tree.insert('', 'end', text=cont, values=(a[1],a[0],info.PILOTS[a[0]]))
            
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)

        #Right side of the screen.
        right = tk.Frame(frame)
        right.configure(bg=style.CLASSIFICATION)
        tk.Label(right, text=" Pilots Classification ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Label(right, text=" Leader: ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Label(right, text=leader, relief="flat").pack(side="top", fill="x", pady = 20)
        right.pack(side="right",fill="both",expand=True)

class Classification_constructor(tk.Frame):

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

        #Right side of the screen.
        left = tk.Frame(frame)
        left.pack(side="left",fill="both",expand=True)
        tree = ttk.Treeview(left, columns=("Points", "Teams"))
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)

        # Agregar encabezados de columna
        number = list(range(1,len(info.PILOTS)+1))
        score = sorted(info.TEAMS_ATRIBUTES.items(), key=lambda x: x[1]["points"], reverse=True)
        cont = 0
        tree.heading('#0', text='Position')
        tree.heading('Points', text='Points')
        tree.heading('Teams', text='Teams')
        tree.column("#0", width=20)
        tree.column("Points", width=40)
        tree.column("Teams", width=150)

        for a in score:
            cont += 1
            points = info.TEAMS_ATRIBUTES[a[0]]["points"]
            team = info.TEAMS_ATRIBUTES[a[0]]["Name"]
            tree.insert('', 'end', text=cont, values=(points,team))
            
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        
        #Right side of the screen.
        leader = score[0][0]
        right = tk.Frame(frame)
        right.configure(bg=style.CLASSIFICATION2)
        tk.Label(right, text=" Constructor Classification ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Label(right, text=" Leader: ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Label(right, text=leader, relief="flat").pack(side="top", fill="x", pady = 20)
        right.pack(side="right",fill="both",expand=True)


class Circuits(tk.Frame):

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
        tk.Label(right, text=" Menu Circuits ", relief="flat").pack(side="top", fill="x", pady = 20)
        tk.Button(right, text=" Create new circuit ", relief="flat", command=lambda: self.new_circuit(frame)).pack(side="top", pady = 10)
        tk.Button(right, text=" Delete Circuits ", relief="flat", command=lambda: self.delete_circuit(frame)).pack(side="top", pady = 10)
        right.pack(side="right",fill="both",expand=True)

        #Right side of the screen.
        left = tk.Frame(frame)
        tree = ttk.Treeview(left, columns="Order")
        scrollbar_vertical = ttk.Scrollbar(left, orient='vertical', command=tree.yview)
        scrollbar_vertical.pack(side='left', fill='y')
        tree.configure(yscrollcommand=scrollbar_vertical.set)
        left.pack(side="left",fill="both",expand=True)

        # Agregar encabezados de columna
        number = list(range(1,len(info.CARRERS)+1))
        circuits = info.CARRERS
        tree.heading('#0', text='Circuits')
        tree.heading('Order', text='Order')
        tree.column("#0", width=200)
        tree.column("Order", width=200)

        for a,b in zip(number, circuits):
            tree.insert('', 'end', text=b, value=a)
        
        # Agregar elementos
        tree.pack(side="right", fill="both", expand=True)
        right.pack(side="right",fill="both",expand=True)

    def new_circuit(self, container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x200")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" NEW CIRCUIT CREATION ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text=" Circuit name ").grid(row=1,column=0,padx=20,pady=10)
        name = tk.Entry(newWindow).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text= " Create Circuit ",command= lambda: newWindow.destroy()).grid(row=5,column=0,padx=20,pady=20,columnspan=3)

    def delete_circuit(self,container):
        newWindow = tk.Toplevel(container)
        newWindow.geometry("400x200")
        newWindow.grid_columnconfigure(0,weight=1)
        newWindow.grid_columnconfigure(1,weight=2)
        tk.Label(newWindow, text=" DELETE CIRCUIT ").grid(row=0,column=0,padx=20,pady=30,columnspan=3)
        tk.Label(newWindow, text= " Select circuit to Delete ").grid(row=1,column=0,padx=20,pady=10)
        varTeam = tk.StringVar()
        optionTeam = tk.OptionMenu(newWindow, varTeam, *info.CARRERS).grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        tk.Button(newWindow, text=" Delete Circuit",command= lambda: newWindow.destroy()).grid(row=2,column=0,padx=20,pady=10, columnspan=3)
    

 