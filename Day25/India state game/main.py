import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image = "C:\\Users\\Preksha Asati\\PY\\Day25\\India state game\\indian_states.gif"

screen.addshape(image)# we can add image as shape of turtlr
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

t = turtle.Turtle()
t.hideturtle()
t.penup()

import pandas as pd
score = 0
data = pd.read_csv("C:\\Users\\Preksha Asati\\PY\\Day25\\India state game\\indian_states.csv")
#print(data.columns)
#print(data["state"])
game_still_on = True
guessed_states=[]
missed_state=[]
while score != 28 or game_still_on :  
    answer_State = screen.textinput(title=f"{score}/28, guess another state",prompt="Guess a state ")
    print(answer_State)
    State_list = data["state"].to_list()
    states_lower = [state.lower() for state in State_list]
    print(states_lower)
    if answer_State.lower()=="exit":
        # for state in states_lower:
        #    if state not in guessed_states: 
        #     missed_state.append(state)
        # or
        missed_state = [state for state in states_lower if state not in guessed_states]
        print(missed_state)
        new_data = pd.DataFrame(missed_state)
    
        print(new_data)
        new_data.to_csv("C:\\Users\\Preksha Asati\\PY\\Day25\\India state game\\States_to_learn.csv")
        t.setposition(0,200)
        t.write(f" Congrates!You guessed {score} correct states.Learn remaining in the excel saved !",align="center")
        screen.exitonclick()

    if answer_State.lower() in states_lower :
        guessed_states.append(answer_State.lower())
        row_state =data [data["state"].str.lower()==answer_State.lower()]
        print(row_state)
        x= row_state.iloc[0]["x"]
#print(x)
        y= row_state.iloc[0]["y"]
#print(y)
        t.setposition(x,y)
        t.write(answer_State,align="center")
        score=score+1
    else :
        pass





turtle.mainloop()
#screen.exitonclick()