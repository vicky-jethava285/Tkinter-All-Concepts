from tkinter import *
root = Tk()

# geometry is used to set the size and position of your main windwow
root.geometry("600x600")

# Minimum window size
root.minsize(300,300)

# Maximum window size
root.maxsize(900,900)

# fixed-size window
root.resizable(False, False)

root.mainloop()