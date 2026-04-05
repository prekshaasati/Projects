#BETTING GAME 
from turtle import Turtle,Screen
import random

is_race_on = False
screen =Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a colour to choose your turle")
colours = ["red","blue","green","yellow","purple","pink"]
players=[]
for colour in colours :
    col=colour
    colour= Turtle(shape="turtle")
    colour.color(col)
    players.append(colour)
    
#print(players)
i=100
for player in players:
    player.penup()
    player.goto(x=-230,y=-i)
    i-=30

if user_bet:
    is_race_on =True
    
while is_race_on :
    for player in players:
        if player.xcor()>230:
            is_race_on=False
            winning_turtle = player.pencolor()
            if winning_turtle == user_bet:
                #screen.
                 print(f"you've won ! the {winning_turtle} is the winner")
            else : 
                print(f"you've lost ! the {winning_turtle} is the winner")
                
            #print(player.color())
            
        rand_speed=random.randint(1,10)
        player.forward(rand_speed)
        
    
   

# tim=Turtle(shape="turtle")
# tim.penup()
# tim
# # tim.goto(x=-230,y=0)
# screen.exitonclick()