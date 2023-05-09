import tkinter as tk
from data import style, info
from PIL import ImageTk, Image
import os


class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.load_image()
        self.im

    def create_widgets(self):
        # Crea el botón y el frame de imagen
        self.button = tk.Button(self, text="Click me", command=self.load_image)
        self.button.pack(side="top", pady=10)

        self.image_frame = tk.Frame(self)
        self.image_frame.pack(side="top")

        # Crea un label en el frame de imagen
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

    def load_image(self):
        # Carga la imagen utilizando PIL
        image = Image.open("path/to/image.jpg")

        # Convierte la imagen a un objeto tkinter PhotoImage
        self.photo = ImageTk.PhotoImage(image)

        # Asigna la imagen al label de imagen
        self.image_label.config(image=self.photo)