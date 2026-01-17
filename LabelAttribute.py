#Attribute Label  


from tkinter import *;

root = Tk()
root.title("My GUI")
root.geometry("200x200")

# Import Label Option 

# bg - background color
# fg - foreground color
# padx - x axis padding
# pady - y axis padding
# font - font style
# borderwidth - provide border width 
# relif -  set border style

Lbl = Label(text="hello vicky",bg="blue",fg="white",padx=100,pady=100,font="bold",borderwidth=3, relief=SUNKEN) 
Lbl.pack()

root.mainloop()
