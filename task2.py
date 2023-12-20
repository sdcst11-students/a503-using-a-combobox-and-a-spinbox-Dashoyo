#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""

import tkinter
from tkinter import ttk
from tkinter import *
import random

win = tkinter.Tk()
win.attributes('-topmost',True)
win.geometry("400x300")

def multiply():
    data = numOne.get()
    data2 = numTwo.get()

    intdata = int(data)
    intdata2 = int(data2)

    ans = intdata*intdata2
    final.delete(0,END)
    final.insert(0,f"{ans}")

def add():
    data = numOne.get()
    data2 = numTwo.get()

    intdata = int(data)
    intdata2 = int(data2)

    ans = intdata+intdata2
    final.delete(0,END)
    final.insert(0,f"{ans}")

def subtract():
    data = numOne.get()
    data2 = numTwo.get()

    intdata = int(data)
    intdata2 = int(data2)

    ans = intdata-intdata2
    final.delete(0,END)
    final.insert(0,f"{ans}")

def divide():
    data = numOne.get()
    data2 = numTwo.get()

    intdata = int(data)
    intdata2 = int(data2)

    ans = intdata/intdata2
    final.delete(0,END)
    final.insert(0,f"{ans}")
    
def calculate(e):
    #find out what operation is being shown
    #use that to decide which calculation to do
    #if operator is x then run multipl()
    op = calc.get()
    
    if op == "x":
        multiply()

    if op == "+":
        add()
    
    if op == "/":
        divide()

    if op == "-":
        subtract()

numOne = Entry(win, )
numOneLB = Label(win, text = "Enter First Number:")

numTwo = Entry(win, )
numTwoLB = Label(win, text = "Enter Second Number:")

calcLB = Label(win, text = "Select Operation:")
calc = ttk.Spinbox(win, values = ["x","+","-","/"])
calc.set("Operation:")

final = Entry(win,)

b1 = Button(win, text = "Calculate")

b1.bind("<Button>", calculate)




numOne.place(x=150,y=20)
numOneLB.place(x=10,y=20)

numTwo.place(x=150,y=80)
numTwoLB.place(x=10,y=80)

calcLB.place(x=10,y=50)
calc.place(x = 150, y =50)

final.place(x = 150, y=140)

b1.place(x =150, y=105)


win.mainloop()