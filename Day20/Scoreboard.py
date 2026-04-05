from turtle import Turtle
ALIGNMENT="center"
FONT= ("Arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        #using file to read high score
        with open("C:\\Users\\Preksha Asati\\PY\\Day20\\high_score.txt") as data :
            self.highscore=int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.update_scoreboard()
    
        
    def update_scoreboard(self):
      self.clear()
      self.write(f"Score:{self.score} HighScore:{self.highscore}",align=ALIGNMENT,font= FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align=ALIGNMENT,font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            #wrting on file new score
            with open("C:\\Users\\Preksha Asati\\PY\\Day20\\high_score.txt",mode="w") as data:
               data.write(f"{self.highscore}")
            
        self.score=0
        self.update_scoreboard()

    def inc_score(self):
        self.score=self.score+1
        self.update_scoreboard()
        
        
    
    