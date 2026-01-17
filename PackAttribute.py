#Attribute Pack 

from tkinter import *;

root = Tk()
root.title("My GUI")
root.geometry("600x600")

# Import Label Option 
Lbl = Label(text="hello vicky",bg="blue",fg="white",padx=100,pady=100,font="bold",borderwidth=3, relief=SUNKEN) 

# Import Pack Option 

# anchor = nw , ne (Capital)
# side = top,bottom,left,right (By Default = top) (Capital)
# fill = x,y (Capital)
# padx 
# pady

Lbl.pack(anchor=NE,side=TOP,fill=X)  

root.mainloop()
