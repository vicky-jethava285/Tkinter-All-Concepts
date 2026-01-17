# Menus & submenus 
from tkinter import *

def function():
  print("hello")

def dst():
  root.destroy()
  
root = Tk()
root.title("My GUI")
root.geometry("444x333")
root.resizable(False, False)

mainmenu =Menu(root)
main = Menu(mainmenu)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New ",command=function)
m1.add_separator()
m1.add_command(label="open",command=function)
m1.add_command(label="Save",command=function)
m1.add_command(label="Save As",command=function)
m1.add_command(label="Exit",command=dst)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Zoom",command=function)
m2.add_command(label="Status Bar",command=function)
m2.add_command(label="Word Wrap",command=function)
m2.add_separator()
m2.add_command(label="MarkDown",command=function)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="View",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Undo",command=function)
m3.add_separator()
m3.add_command(label="Copy",command=function)
m3.add_command(label="Cut",command=function)
m3.add_command(label="Paste",command=function)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m3)


root.mainloop()


