#Activity 1. Tkinter in python 
from tkinter import * 
window = Tk ()
window.title("Tkinter sample")
window.geometry("350x200")

greeting = Label (text="Hello, Tkinter!", fg="black", bg="white")
button= Button (text="Click Me", fg="black", bg="yellow")
entry= Entry (text="enter text here", bg="red", fg="white", width=50)

greeting.pack()
button.pack()
entry.pack()

textbox = Text (fg="green", bg="yellow")
textbox.pack()

window.mainloop()

#Activity 2
import tkinter as tk

window = tk.Tk()

for i in range(3): 

  for j in range(3):
    frame= tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1

)

frame.grid(row=i, column=j, padx=5, pady=5)

label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

label.pack()

window.mainloop()

import ipywidgets as widgets
from IPython.display import display

grid = []

for i in range(3):
    row = []
    for j in range(3):
        btn = widgets.Button(description=f'Button {i},{j}', layout=widgets.Layout(width='80px'))
        row.append(btn)
        grid.append(widgets.HBox(row))

display(widgets.VBox(grid))