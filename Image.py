# PIL : pip install pillow 
from tkinter import *
from PIL import Image , ImageTk

root = Tk()
img= Image.open("v7g6ime1wtk61.jpg")
photo = ImageTk.PhotoImage(img)
My_Label = Label(image=photo)
My_Label.pack()
root.mainloop()