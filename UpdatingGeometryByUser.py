# Updating geometry by user enter value  

from tkinter import *

def update():
  print("Updating the GUI")
  root.geometry(f"{width.get()}x{height.get()}")

root = Tk()

root.title("My GUI")
root.geometry("344x233")
width = StringVar()
height = StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="Apply Updating",command=update).pack()

root.mainloop()


