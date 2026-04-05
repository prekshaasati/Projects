import colorgram # pip install colorgrapm.py
import turtle as t 
import random
image_path = 'C:\\Users\\Preksha Asati\\PY\\Day18\\hirst-painting\\hiest.jpg'
num_colors_to_extract = 10

colors = colorgram.extract(image_path, num_colors_to_extract)

# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# print(rgb)

colorhiest=[]

# for color in colors :
#     a =color.rgb
#     tup = (a[0],a[1],a[2])
#     colorhiest.append(tup)
#     print( colorhiest)

colorhiest = [(254, 254, 253), (249, 254, 252), (254, 249, 252), (237, 247, 252), (226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215)]
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(200)
tim.setheading(0)


def draw () :
 for _ in range(10): 
  tim.dot(15,random.choice(colorhiest))
  tim.forward(30)

def move ():
#  draw() 
 tim.setheading(180)
 tim.forward(300)

 tim.setheading(90)
 tim.forward(35)
 tim.setheading(0)
#  draw()

# move()

for _ in range(8):
 draw()
 move()

screen= t.Screen()
screen.exitonclick()



