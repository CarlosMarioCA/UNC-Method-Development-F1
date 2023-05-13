import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

# Crear un objeto Treeview
tree = ttk.Treeview(root, columns=("Name", "Age", "Selected"))

# Configurar las columnas
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Selected", text="Selected")

# Agregar algunos datos
tree.insert("", "end", text="1", values=("Alice", "25", ""))
tree.insert("", "end", text="2", values=("Bob", "30", ""))
tree.insert("", "end", text="3", values=("Charlie", "35", ""))

# Agregar casillas de verificación a la columna "Selected"
def toggle_checkbox(item_id):
    value = tree.item(item_id)["values"][2]
    if value == "":
        tree.set(item_id, "Selected", "X")
    else:
        tree.set(item_id, "Selected", "")

for item_id in tree.get_children():
    tree.set(item_id, "Selected", "")
    checkbox = ttk.Checkbutton(tree, command=lambda item_id=item_id: toggle_checkbox(item_id))
    tree.window_create(item_id, column="Selected", window=checkbox)

# Mostrar el Treeview
tree.pack(expand=True, fill="both")

root.mainloop()
