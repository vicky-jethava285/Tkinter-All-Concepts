from tkinter import messagebox
from tkinter import *
import mysql
import mysql.connector

def fun1():
  user =E1.get()
  passw =E2.get()
  if user == "admin" and passw == "admin":
    messagebox.showinfo("Message","Login successfully...")
  else:
    messagebox.showerror("Alert","Login unsuccessfully...")



root =Tk()
root.title("Login Form")
root.geometry("400x400")
l1=Label(root,text="Login Form").pack(pady=10)
l2=Label(root,text="UserName").pack(pady=20)
E1=Entry(root)
E1.pack()
L3=Label(root,text="PassWord").pack(pady="10")
E2=Entry(root,show="*")
E2.pack()
b1=Button(root,text="Submit",command=fun1).place(x=170,y=200)


root.mainloop()
