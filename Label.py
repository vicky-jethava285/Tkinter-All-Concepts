from tkinter import *
root = Tk()

root.geometry("600x600")
# Label : just a widget used to display text or images.
My_Label = Label(text="What is your name")

My_Label.pack() # simplest geometry manager
root.mainloop()