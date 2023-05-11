import tkinter as tk

root = tk.Tk()

def get_button_text():
    text = my_button.cget('text')
    print(text)

my_button = tk.Button(root, text='Haz clic aquí', command=get_button_text)
my_button.pack()

root.mainloop()