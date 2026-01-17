# Entry Widget 

from tkinter import *

def val():
  print("This is Entry widget & Grid layout")

root = Tk()
root.geometry("200x100")

user = Label(root,text="UserName")
user.grid() #grid - grid layout manager

password = Label(root,text="PassWord")
password.grid(row=1) #row - specify the row number

uservalue = StringVar()
passvalue = StringVar()

userety = Entry(root,textvariable=uservalue,bg="grey",fg="white")
userety.grid(row=0,column=2) # column - specify the column number

passety =Entry(root,textvariable=passvalue,bg="grey",fg="white")
passety.grid(row=1,column=2)

Button(text="Submit",command=val).grid()

root.mainloop()