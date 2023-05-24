
import tkinter as tk

def mostrar_seleccion():
    seleccion = opciones.get()
    etiqueta.config(text="Seleccionaste: " + seleccion)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Recuadro de Opciones")

# Variable para almacenar la selección
opciones = tk.StringVar()

# Crear el recuadro de opciones
recuadro_opciones = tk.OptionMenu(ventana, opciones, "Opción 1", "Opción 2", "Opción 3")
recuadro_opciones.pack()

# Botón para mostrar la selección
boton_mostrar = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Etiqueta para mostrar la selección
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Iniciar el bucle principal
ventana.mainloop()