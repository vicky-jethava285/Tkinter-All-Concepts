from tkinter import *;

root = Tk()

def submit():
  print("Submitting Form !")
  print(f"{namevalue.get(),rollvalue.get(),agevalue.get(),Standardvalue.get(),cityvalue.get()}")
  root.destroy()

  with open("Student_detail.txt","a")as f:
    f.write(f"{namevalue.get(),rollvalue.get(),agevalue.get(),Standardvalue.get(),cityvalue.get()}\n")

root.title("Student Detail")
root.geometry("300x300")
Label(root,text="Welcome To School",font="italic 13 bold",).grid(row=0,column=3)

name = Label(root,text="Name")
name.grid(row=1,column=2)

Rno = Label(root,text="RollNumber")
Rno.grid(row=2,column=2)

Age = Label(root,text="Age")
Age.grid(row=3,column=2)

Standard = Label(root,text="Standard")
Standard.grid(row=4,column=2)

city = Label(root,text="city")
city.grid(row=5,column=2)

namevalue =StringVar()
rollvalue =StringVar()
agevalue =StringVar()
Standardvalue =StringVar()
cityvalue =StringVar()


nameentry = Entry(root,textvariable=namevalue)
rollentry = Entry(root,textvariable=rollvalue)
ageentry = Entry(root,textvariable=agevalue)
standarentry = Entry(root,textvariable=Standardvalue)
cityentry = Entry(root,textvariable=cityvalue)

nameentry.grid(row=1,column=3)
rollentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
standarentry.grid(row=4,column=3)
cityentry.grid(row=5,column=3)

gender1 = Checkbutton(text="Male")
gender2 =Checkbutton(text="Female")

gender1.grid(row=7,column=2)
gender2.grid(row=7,column=3)


Button(text=" Submit",command=submit).grid(row=8,column=3)
root.mainloop()