import tkinter as tk

def set_default_text():
    entry.delete(0, tk.END)  # Elimina el texto actual del Entry
    entry.insert(0, "Texto predeterminado")  # Inserta el texto predeterminado

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Establecer texto predeterminado", command=set_default_text)
button.pack()

root.mainloop()