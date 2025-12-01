from tkinter import *

from PIL import Image, ImageTk

root = Tk()

root.title('image')

root.geometry('400x400')

upload = Image.open(r"C:\Users\Haider Khan\Desktop\codingal\python3\zaidi.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)

label.place(x=50, y=0)

label2 = Label(root, text="This is how you add image in Tkinter Window")

label2.place(x=40, y=360)

root.mainloop()

# Import necessary libraries

from tkinter import *

from tkinter import messagebox

# Setup Tkinter Window

root = Tk()

root.geometry("200x200")

# Function for Displaying Warning Message

# This will be called once the button is clicked

# messagebox.showwarning("Window Name", "Text to be displayed")

def msg():

 messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window

button = Button(root, text="Scan for Virus", command=msg)

button.place(x=40, y=80)

# Entering main event loop

root.mainloop()

# Import necessary libraries

from tkinter import *


# Setting up Main Window

root = Tk()

root.geometry("400x300")

root.title("main")

# Function to open New (Top Level) Window

def topwin():

# Setting up Top Window

top = Toplevel()

top.geometry("180x100")

top.title("toplevel")

# Adding a label widget to Top Window

l2 = Label(top, text = "This is toplevel window")

l2.pack()

top.mainloop()

# Adding a label and button Widget to Root (Main) Window

l = Label(root, text = "This is root window")

btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets

l.pack()

btn.pack()
