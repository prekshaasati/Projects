from turtle import Turtle,Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title(" Preksha's Snake game ")
screen.tracer(0)
#create snake body 
snake = Snake()
food = Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#screen.update()

game_is_on= True
while game_is_on :
    screen.update()
    snake.move()
    time.sleep(0.08)
    #collision with food 
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
    #collision with walls
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        #game_is_on=False
        scoreboard.reset()
        snake.reset()
    #detecting the colllision with tail
    for segment in snake.segments[1:] :
        if snake.head.distance(segment)<10 :
             #game_is_on =False
             scoreboard.reset()
             snake.reset()
        
screen.exitonclick()