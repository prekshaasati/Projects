import turtle as t

import random

tim=t.Turtle()
#tim.shape("turtle")
tim.color("red")

# for i in range(4): 
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     # tim.color("black")
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     #tim.color("white")

#make all shapes from triangle to nonagon all starting from same side 
color = ['red','orange','blue','pink','purple','yellow','black','brown']

# for i in range (3,10):
#  tim.color(random.choice(color))
#  for _ in range (i):
#     angle = 360 / i 
#     tim.forward(100)
#     tim.right(angle)
    


#tim.shape("arrow")
#RANDOM WALK
t.colormode(255)
def randomcolor():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  return ((r,g,b))

# #print(randomcolor())
# directions = [0 , 90,180 ,270]
# tim.width(3)
tim.speed("fastest")
# for _ in range(200): 
#   tim.color(randomcolor())
#   tim.forward(10)
#   tim.setheading(random.choice(directions)) # setting direction 



#Spirograph

#tim.circle(100)
def spirogaph (no_of_ofset): 
  for i in range(int(360/no_of_ofset)):
   tim.color(randomcolor()) 
   tim.left(5)
   tim.circle(100)

spirogaph(5)
  

  
























screen=t.Screen()
screen.exitonclick()