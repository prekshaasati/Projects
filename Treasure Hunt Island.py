# Treasure hunt 
# below art we can print by searcing relevent image in ASCII art from google 

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasure Island")
print("your mission is to find the treasure")
choice1 = input("you're at the cossroad ,where would you want to go ? type \"left\" or \"right\" ").lower()
# if we use \ in front of a " , it tells the compiler to not interpret it separelty ...uses as an ESCAPE CHARACTER
# .lower --> to maintain consistency in code 

if choice1=='left':
    choice2=input("you've found a lake  ,where would you like to swin or wait ? type \"swim\" or \"wait\" \n").lower()
    if choice2=='wait':
        choice3=input("you have arrived at a dark cave with a big dragon sleeping in front of it" \
        " ,Would you like to wake it up or try to sneak past it  ? type \"wake\" or \"sneak\" \n").lower()
        if choice3=='sneak':
            print ("You managed to sneak past him \n")
            choice4=input("you have 3 chests in front of you " \
            " ,Which one would you open   ? type \"red\" or \"blue\" or \"green\" \n" ).lower()
            if choice4=="green":
                print("Congratulations master ! you won !")
            elif choice4 =="blue":
                print("oh no  ,This Chest was filled with snakes . Game Over")
            elif choice4=="red":
                print("oh no , you've unlocked the unholy spirit locked throught the years. Game Over brother")
            else :
                print("huh , That seems like an invisible chest to us , Game Over")
        else : 
            print ("You've woken up the monster , he got angry at you and killed you . Game Over")



    else : 
        print(" oh no..you were eaten by a Shark , Game Over ! ")
else : 
    print("ooh noo..Game Over ! you were bitten by a giant spider !")
