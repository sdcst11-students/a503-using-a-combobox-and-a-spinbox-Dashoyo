#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""

import tkinter
from tkinter import ttk
from tkinter import *

win = tkinter.Tk()

win.attributes('-topmost',True)
win.geometry("400x300")

def calculate(e):
    ini = initial.get()
    p= int(ini)

    rat = rate.get()
    r1 = int(rat)
    r = r1/100

    comp = compounding.get()
    n = int(comp)

    yea = years.get()
    t = int(yea)

    #P(1+r/n)^(n*t)

    final = ((1+r) / n)*p **(n*t)

    answer.insert(0,final)
   


initialLB = Label(win, text = "Enter Initail Investment:")
initial = Entry(win, )

initial.place(x =140, y=40)
initialLB.place(x=10, y=40)

rateLB = Label(win, text = "Intrest Rate as Decimal:")
rate = ttk.Combobox(win, values = ["1","2","3","4","5","6","7","8","10"])
rate.set("1")

rateLB.place(x =10, y=70)
rate.place(x=140, y=70)

compoundingLB= Label(win, text = "Compounding Periods:")
compounding= Entry(win, )

compounding.place(x =140, y=100)
compoundingLB.place(x=10, y=100)

yearsLB = Label(win, text ="Number of Years:")
years = ttk.Spinbox(win, values = ["1","2","3","4","5","6","7","8","9","10"])
years.set("1")

yearsLB.place(x=10, y=130)
years.place(x =140, y=130)

calc = Button(win, text="Calculate Compound Intrest")

calc.place(x=100,y =160)

calc.bind("<Button>", calculate)

answer = Entry(win,)

answer.place(x = 140, y =190)

win.mainloop()
