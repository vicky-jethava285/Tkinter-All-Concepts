# Message box 

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()  # hides the main window

# messagebox.showinfo("Info", "Hello! This is a message box.")

# root.mainloop()



# tk.Tk() → creates a hidden Tkinter app (required)

# withdraw() → hides the useless empty window

# showinfo() → pops up a message box

# mainloop() → keeps the app alive


# import tkinter as tk
# from tkinter import messagebox

# def show_msg():
#     messagebox.showwarning("Warning", "This is a warning message!")

# root = tk.Tk()
# root.title("MessageBox Demo")

# btn = tk.Button(root, text="Click Me", command=show_msg)
# btn.pack(padx=20, pady=20)

# root.mainloop()



import tkinter as tk
from tkinter import messagebox

def confirm():
    result = messagebox.askyesno("Confirm", "Do you want to exit?")
    if result:
        root.destroy()

root = tk.Tk()
tk.Button(root, text="Exit", command=confirm).pack(pady=20)
root.mainloop()






# Function :

# showinfo()	Normal info
# showwarning()	Warning
# showerror()	Error
# askyesno()	Yes / No
# askokcancel()	OK / Cancel

