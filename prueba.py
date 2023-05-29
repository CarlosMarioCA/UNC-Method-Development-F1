import tkinter as tk

# Crear una ventana principal
ventana_principal = tk.Tk()

# Crear un Frame
frame = tk.Frame(ventana_principal, width=200, height=200)
frame.pack()

# Agregar widgets al Frame
label = tk.Label(frame, text="Hola, este es el contenido del Frame")
label.pack()

boton = tk.Button(frame, text="Aceptar")
boton.pack()

# Guardar el Frame y su contenido en una variable
contenido_frame = frame

# Cerrar la ventana principal
ventana_principal.destroy()

# Crear una nueva ventana para mostrar el Frame guardado
ventana_secundaria = tk.Tk()

# Mostrar el Frame guardado en la nueva ventana
contenido_frame.pack(in_=ventana_secundaria)

# Ejecutar el bucle principal de la nueva ventana
ventana_secundaria.mainloop()
