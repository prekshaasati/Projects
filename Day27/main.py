from tkinter import * 
import math
#---------------------------------------CONSTANTS----------------------------------------------#
#HEX CODES TAKEN FROM THE WEBSITE CALLED "COLOUR HUNT.CO"
PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME="Courier"
WORK_MIN= 1 #25
SHORT_BREAK_MIN= 1#5
LONG_BREAK_MIN= 2 #20
reps= 0 
timer= NONE 
#------------------------------JUMP SCREEN TO FRONT-------------------------------------------------------#
def bring_to_front():
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)


#--------------------------------TIMER RESET--------------------------------------------------------------#

def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00.00")
    check_labels.config(text= "")
    global reps
    reps = 0


#--------------------------------TIMER MECHANISM----------------------------------------------------------#
def start_timer():
    global reps
    reps+=1 
    work_sec= WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60
    #25 5 25 5 25 5 25 20
    if reps >=9:
        reset_timer()
    elif reps%2!=0:
        label_timer.config(text="Work",fg=GREEN)
        count_down(work_sec)
        
    elif reps==8:
        bring_to_front()
        label_timer.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
        
    elif reps%2==0:
        bring_to_front()
        label_timer.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)


     # get minutes ==> min * sec
    


#---------------------------------COUNDOWN MECHANISM------------------------------------------------------#

def count_down(count):
    #get minutes : 300sec / 60 ==> 4 min
    # 245/60==> 4 min with some sec..
    # how to get those remaining sec==> with % ==> 245%60=0.4

    count_min = math.floor(count/60)
    count_sec=count%60
    # 5%60 == 0 --> in timer we would like to see it as 00 and hence below code..

    #here we are taking int and assigneing it to string... whatttt...
    # So python is strongly types lang( means 3 + "3" is not allowed ..it remembers the type of varialbe) but dynamically types as well.
    #in python .. chainging the type of variable by changing the content in that variable is called DYNAMIC TYPING

    if count_sec < 10 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")# to changes the configuration of any item in canvas (item , element you want to change)

    if(count>=0):
        global timer
        timer = window.after(1000,count_down,count-1)#.after will allow to 
    else:
        start_timer()
        marks= ""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✓"
        check_labels.config(text=marks)

#----------------------------------UI SETUP --------------------------------------------------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
#window.after(1000,count_down,5)
#canvas widget : allows us to layer thingss on top of the others (image/text.etc)

label_timer= Label(text="Timer",fg=GREEN,font=(FONT_NAME,"37","bold"),bg=YELLOW)
label_timer.grid(column=1,row=0)

canvas=Canvas(width=400,height=400,bg=YELLOW ,highlightthickness=0)
tomato_img=PhotoImage(file="C:\\Users\\Preksha Asati\\PY\\Day 28\\Tomato.png")#reading file in tkinter 
canvas.create_image(200,200,image=tomato_img)
timer_text=canvas.create_text(200,230,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)

start_button= Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=3)

reset_button= Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=3)

check_labels=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
check_labels.grid(column=1,row=4)


window.mainloop()