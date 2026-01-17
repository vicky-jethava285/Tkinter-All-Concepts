# More Tkinter Tips_Tricls 

from tkinter import *

root = Tk()

root.geometry("400x300")

# iconbitmap is use to set the icon of the window
root.wm_iconbitmap("backgrund.svg.svg")

# config is use to set the background color of the window
root.config(bg="lightblue")

# winfo use to get the width and height of the screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"Width: {width}, Height: {height}")

# Destroy is use to close the window
Button(text='close', command=root.destroy).pack()
root.mainloop()