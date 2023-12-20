"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font

win = tkinter.Tk()
win.attributes('-topmost', True)
win.geometry("400x600")
win.configure(bg="lightblue")
title_font = font.Font(family="Helvetica", size=20, weight="bold", )

bday = Label(win, text ="YOUR BIRTHDAY!!!", font=title_font)

monthLB = Label(win, text = "Select Month:")
month = ttk.Combobox(win, values = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "GUEY"])
month.set('January')
dayLB = Label(win, text = "Select Day:")
day = ttk.Combobox(win, values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
day.set('1')
yearLB = Label(win,text="Select Year:")
year = ttk.Combobox(win, values = ["1900", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909",
"1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919",
"1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929",
"1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939",
"1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949",
"1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959",
"1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969",
"1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979",
"1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989",
"1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999",
"2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
"2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
"2020", "2021", "2022", "2023", "2024"])
year.set('1900')

save = Button(win,text= "Save Birthday")

showSave= Entry(win, )

def showFunction(e):
    monthData = month.get()
    month.delete(0,END)
    dayData = day.get()
    day.delete(0,END)
    yearData = year.get()
    year.delete(0,END)

    date = (monthData, dayData, yearData)
    showSave.insert(0,f"{monthData}, {dayData}, {yearData}")




bday.place(relx=0.5, rely=0.05, anchor=CENTER)
monthLB.place(x = 10, y = 70)
month.place(x = 90,y=70)
dayLB.place(x=10,y =100)
day.place(x = 90, y = 100)
yearLB.place(x=10,y = 130)
year.place(x=90,y=130)
save.place(x = 117, y=160)
showSave.place(x = 90,y =190)

save.bind("<Button>", showFunction)
win.mainloop()

