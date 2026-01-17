# Function

from tkinter import *

def fun1():
  print("clicked")

root = Tk()
root.geometry("300x300")
frm = Frame(root,borderwidth=6,bg="blue",relief=SUNKEN)
frm.pack(side=LEFT,anchor=NW)

# command use to call the function when we click the button
btn1 = Button(frm,fg="red",text="Click here",command=fun1)
btn1.pack(side=LEFT,padx=23)

btn2 = Button(frm,fg="red",text="Click here",command=fun1)
btn2.pack(side=LEFT,padx=23)

root.mainloop()