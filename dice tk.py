from tkinter import *
import random
top=Tk()
def dice():
	a=random.randrange(1,7)
	c.configure(text=str(a))
d=Label(top,text="Welcome to roll dice",fg="red")
d.pack()
e=Label(top,text="click the \"roll dice\" button to roll the dice",fg="green")
e.pack()
b=Button(top,text="roll dice ",command=dice,relief="raise",bd=25,bg="white",fg="red")
b.pack(side="left")
c=Label(top,text="",fg="white",bg="black")
c.pack(side="right")
top.mainloop()


#program to roll a dice
#using tkinter
