# Create A calculator 

import tkinter as tk
from tkinter import messagebox


# tk.Tk means: “this class is a Tkinter window”

class Calculator(tk.Tk):
    def __init__(self):
        # super().__init__() starts the Tkinter window
        super().__init__()

        self.title("Tkinter Calculator")
        self.geometry("320x420")
        self.resizable(False, False)

        self.expression = ""

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display_var = tk.StringVar()

        entry = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        entry.pack(fill="x", padx=10, pady=10)

    def create_buttons(self):
        btn_frame = tk.Frame(self)
        btn_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("⌫", 5, 1)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                width=6,
                height=2,
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Make C and Backspace span columns
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.clear()
        elif char == "⌫":
            self.backspace()
        elif char == "=":
            self.calculate()
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            # eval is dangerous if you allow arbitrary input.
            # Here it's safe because buttons control input.
            result = eval(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)

        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()

        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
