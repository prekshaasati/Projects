#DEFAULT AGRUMENTS 
# many functions have default values set to them , such that if paramerets are not provided expilictly the still work with default values .else
# these values can be overrriden by explicly providing the value at the time of calling the function

def foo (a=2,b=5,c=7):
    print(a,b,c)

foo()
foo(1)
foo(1,9)
foo(7,c=10)

# POSTIONAL AGUMENTS : * 
#unlimited arguments : to accept ant number of arguments 
# * collects all the arguments as tuple and that is sent as an input 
# Since position of input matters here it's also called as POSITIONAL ARGUMETNS 
def add(*args):
    print(type(args))
    print(args[0])# position of 1st element in tuple i.e. 1st input 
    sum = 0 
    for n in args :
        sum = sum + n
    return sum

print(add(1,2,4,5,6,7,8,9))

#KEYWORD ARGUMENT : **
#name the values that we can pass in a function
#** takes the named arguments and converts into a key , value pair of dict with key beings the arguments and value being it's passed value 

def calculate(n,**kwargs):
    print(kwargs)#dictionary form of input will get printed 
    print(type(kwargs))# dict
    n+= kwargs["add"]# accessing the value of a dict item with it's key
    n*=kwargs['multiply']
    print(n)
calculate(4, add = 3 , multiply=5)

# Creatinf a class with keword arguments 
class Car:

    def __init__(self,**kw):
        self.model = kw["model"]
        self.make= kw["make"]
        self.color=kw.get("color")# this way even if we didn't pass color args in the initialisation of class , code won't break , it will simplt return none 

my_car = Car(model='Honda',make='City',color='White')
print(my_car.color)
print(my_car.make)
print(my_car.model)



#import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI project")
window.minsize(width=400,height=300)
window.config(padx=10,pady=10)
#LABEL
my_label = Label(text = "I am a label",font = ("Arial",24,"bold")) # component of label 
#my_label.pack()#will place the component in the secree and place it in center
#my_label.pack(side="left")
my_label["text"]="new text"
my_label.config(text="new text")
#my_label.place(x=100,y=0) # for precise location and placement 
my_label.grid(column=0,row=0)
my_label.config(padx=10,pady=10)#to change padding / adding space in the widget


def button_clicked():
    input.get()
    my_label.config(text=input.get())
    #my_label.config(text="I got Clicked")

#BUTTON
#CREATING a button with text and command keyword
#command : will take NAME OF FUNCTION(not calling the function and no need for () at end ) 
# and perform that function when the button is clickied 
button= Button(text="Click me",command=button_clicked) 
#button.pack() # pack the element in screen 
button.grid(column=1,row=1)# GRID IS RELETIVE TO OTHER COMPONENT
# either use grid or pack /can't use both 

new_button=Button(text="new button")
new_button.grid(column=2,row=0)

#ENTRY
#input = Entry(width=10)
input = Entry()
#input.pack()
input.grid(column=3,row=1)




window.mainloop()