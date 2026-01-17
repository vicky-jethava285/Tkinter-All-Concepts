# Frame 

from tkinter import *
root =Tk()
root.geometry("600x300")

# Frame use to organize the widgets in blocks before placing them in the main window
f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=RIGHT,fill=Y)

Lbl =Label(f1,text="My github program")
Lbl.pack(pady=300)

root.mainloop()