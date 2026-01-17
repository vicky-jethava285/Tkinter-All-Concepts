# ListBox 

from tkinter import *


root = Tk()
root.geometry("600x400")

def add():
  global i
  lbx.insert(ACTIVE,f"{i}")
  i+=1

i=0
root.title("ListBox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")
Button(root,text="ADD",command=add).pack()

root.mainloop()