#Event Listernets and 
#higher order functions (functions that cal call other functions )
#ETCH-A-SKETCH
#W ==> FORWARD
#S===>BACKWARDS
#A==>COUNTER-CLOCKWISE
#D==>CLOCKWAISE
#C==>CLEAR DRAWING

from turtle import Turtle,Screen

tim=Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_counter_clock():
    tim.left(20)

def move_clockwise():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward,"w") # onkey is a higher order function that can call another function called move_forward
screen.onkey(move_backward,"s")
screen.onkey(move_counter_clock,"a")
screen.onkey(move_clockwise,"d")
screen.onkey(clear,"c")

screen.exitonclick()
