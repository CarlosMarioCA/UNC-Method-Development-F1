import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from Manager import Manager
from data import *




def settingFrame(self):
    
    #Setting the relative size of COLUMNS in the tabs on window
    self.frame.columnconfigure(0, weight=1)
    self.frame.columnconfigure(1, weight=1)
    self.frame.columnconfigure(2, weight=1)
    self.frame.columnconfigure(3, weight=1)
    self.frame.columnconfigure(4, weight=1)
    self.frame.columnconfigure(5, weight=1)
    self.frame.columnconfigure(6, weight=1)

    # Setting the relative size of ROWS in the tabs on window
    self.frame.grid_rowconfigure(0, weight=1)
    self.frame.grid_rowconfigure(1, weight=1)
    self.frame.grid_rowconfigure(2, weight=1)
    self.frame.grid_rowconfigure(3, weight=1)
    self.frame.grid_rowconfigure(4, weight=1)
    self.frame.grid_rowconfigure(5, weight=1)
    self.frame.grid_rowconfigure(6, weight=1)

def start():

    # Create and setting window
    window = tk.Tk()
    window.resizable(1, 1)
    window.title(" Formula 1 Administrator ")
    window.geometry("1000x600")

    #Frame for Window: Create and configure the frame that contains all the elements displayed at that moment.
    main = tk.Frame(window)
    main.pack(fill=tk.BOTH)
    main.config(bg="yellow")

    #Frame for Buttons: Positioning the frame that contains buttons at the top
    buttons = tk.Frame(main)
    buttons.grid(row=0, column=0, columnspan=7, sticky="nsew")
    x = buttons

    #Frame for Screen: Contains element shown at the botton screen
    screen = tk.Frame(main)
    screen.grid(row=1, column=0, columnspan=7, sticky="nsew")
    screen.config(bg="yellow")

    # Create buttons for tabs
    button1 = tk.Button(x, text=" About us ",) #, command=tab7.tkraise
    button2 = tk.Button(x, text=" Teams ")
    button3 = tk.Button(x, text=" Pilots ")
    button4 = tk.Button(x, text=" Clasification ")
    button5 = tk.Button(x, text=" Circuits ")
    button6 = tk.Button(x, text=" History ")
    button7 = tk.Button(x, text=" Live ")

    # Position the buttons in the tabs
    button1.grid(row=0, column=0, sticky="nsew")
    button2.grid(row=0, column=1, sticky="nsew")
    button3.grid(row=0, column=2, sticky="nsew")
    button4.grid(row=0, column=3, sticky="nsew")
    button5.grid(row=0, column=4, sticky="nsew")
    button6.grid(row=0, column=5, sticky="nsew")
    button7.grid(row=0, column=6, sticky="nsew")

    #Setting frames
    main.settingFrame()
    main.tkraise()
    
    main.settingFrame()
    buttons.tkraise()
    
    main.settingFrame()
    screen.tkraise()

    # Show the window
    window.mainloop()

    # Loading the image
    #im = ImageTk.PhotoImage(Image.open("E:/GIT/UNC-Method-Development-F1/images/front.jpg"))
    #lbim = tk.Label(marcoButtons, image=im)
    #lbim.pack()

if __name__ == "__main__":
    app = Manager()
    app.mainloop()