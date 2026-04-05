from turtle import Turtle,Screen
import time

MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake :
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]


    def create_snake(self):
        for  i in range (0,3):
            j=i*20
            x,y=i,-j
            self.add_snake(x,y)

    def add_snake(self,x,y):
            snake =Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x,y)
            self.segments.append(snake)
       

    def extend(self):
        self.add_snake(self.segments[-1].xcor(),self.segments[-1].ycor())


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


 

    def move(self):
            for seg_no in range (len(self.segments)-1 ,0 ,-1):
                new_x=self.segments[seg_no-1].xcor()
                new_y=self.segments[seg_no-1].ycor()
                self.segments[seg_no].goto(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)
                #self.segments[0].left(90)

    def up(self):
         if self.head.heading()!=DOWN :
           self.head.setheading(UP)


    def down(self):
         if self.head.heading()!=UP :
          self.segments[0].setheading(DOWN)


    def left(self):
         if self.head.heading()!=RIGHT :
          self.segments[0].setheading(LEFT)


    def right(self):
         if self.head.heading()!=LEFT :
          self.segments[0].setheading(RIGHT)

    





#screen.update()

