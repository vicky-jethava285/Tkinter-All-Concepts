# SliderBar 

# In Tkinter, a slider = Scale widget.It lets the user pick a number by dragging. That’s it. No magic.




# import tkinter as tk

# root = tk.Tk()
# root.title("Simple Slider")

# slider = tk.Scale(root, from_=0, to=100)
# slider.pack()

# root.mainloop()


# from_ → starting value

# to → ending value

# Default direction → vertical







# import tkinter as tk

# root = tk.Tk()

# slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
# slider.pack(padx=20, pady=20)

# root.mainloop()

# Fact:
# set orient="horizontal", it stays vertical. Tkinter doesn’t guess.



# import tkinter as tk

# def show_value():
#     print(slider.get())

# root = tk.Tk()

# slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
# slider.pack()

# btn = tk.Button(root, text="Get Value", command=show_value)
# btn.pack()

# root.mainloop()


# Slider that updates label LIVE

import tkinter as tk

def update_label(value):
    label.config(text=f"Value: {value}")

root = tk.Tk()

slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    command=update_label
)
slider.pack()

label = tk.Label(root, text="Value: 0")
label.pack()

root.mainloop()


#  Set default value 
# slider.set(50)

# Without this, Tkinter starts at from_. Don’t complain later.


# slider = tk.Scale(
#     root,
#     from_=0,
#     to=10,
#     orient="horizontal",
#     resolution=0.5
# )


