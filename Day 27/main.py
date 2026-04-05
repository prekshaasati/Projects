#MILES TO KILOMETER CONVERTER
#import tkinter
from tkinter import *

window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=400,height=300)
window.config(padx=10,pady=10)


input_miles = Entry()
#input.pack()
input_miles.grid(column=1,row=2)

In_km = Label(text = "0",font = ("Arial",16,))
#input.pack()
In_km.grid(column=1,row=4)

Miles = Label(text = "Miles",font = ("Arial",16,)) # component of label 
#my_label.place(x=100,y=0) # for precise location and placement 
Miles.grid(column=3,row=2)

equal = Label(text = "is equal to",font = ("Arial",14,)) # component of label 
#my_label.place(x=100,y=0) # for precise location and placement 
equal.grid(column=0,row=4)


km = Label(text = "km",font = ("Arial",16,)) # component of label 
#my_label.place(x=100,y=0) # for precise location and placement 
km.grid(column=3,row=4)


def calculate() :
   km = round(float(input_miles.get())*1.609)
   In_km.config(text=f"{km}")
   


calculate=Button(text="Calculate",command=calculate)
calculate.grid(column=1,row=5)















window.mainloop()