from tkinter import *

def click(e): # e - e is event object
  print(f"clicked {e.x},{e.y}")


root = Tk()
root.title("My GUI")
root.geometry("300x300")

b1 = Button(root,text="Click here")
b1.pack()

b1.bind('<Button-1>',click)  # <Button - 1> - Left Click
b1.bind('<Double-1>',quit) # < Double-1> - Double Click 

root.mainloop()