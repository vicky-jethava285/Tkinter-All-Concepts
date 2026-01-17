# RedioButton 

# A RadioButton lets the user choose ONE option from MANY.If you’re using checkboxes for this, you’re doing it wrong.

import tkinter as tk

root = tk.Tk()
root.title("Radio Button Demo")

choice = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=choice, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=choice, value="Female").pack()

root.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def show_choice():
#    messagebox.showinfo("Info", f"Hello! you selected {choice.get()}")
    

# root = tk.Tk()

# choice = tk.StringVar()

# tk.Radiobutton(root, text="Python", variable=choice, value="Python").pack()
# tk.Radiobutton(root, text="Java", variable=choice, value="Java").pack()
# tk.Radiobutton(root, text="C++", variable=choice, value="C++").pack()

# tk.Button(root, text="Submit", command=show_choice).pack()

# root.mainloop()



# choice.get() → returns selected option

# No selection → empty string ("")



# Set default selected option 

# choice.set("Python")

# Put this after creating the variable, before mainloop().




# import tkinter as tk

# root = tk.Tk()

# rating = tk.IntVar()

# tk.Radiobutton(root, text="1 Star", variable=rating, value=1).pack()
# tk.Radiobutton(root, text="2 Star", variable=rating, value=2).pack()
# tk.Radiobutton(root, text="3 Star", variable=rating, value=3).pack()

# root.mainloop()

# Rule:

# Text → StringVar

# Numbers → IntVar








# def changed():
#     print(choice.get())

# tk.Radiobutton(root, text="Light", variable=choice, value="Light", command=changed).pack()
# tk.Radiobutton(root, text="Dark", variable=choice, value="Dark", command=changed).pack()







