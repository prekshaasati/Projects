#ROCK - PAPER - SCISSIORS

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
#print ( rock +"\n "+ paper +"\n "+ scissors +"\n ")

set = [rock , paper , scissors]
computer_choice = random.choice(set)
user_choice = input(" choose between rock , paper , scissors :\n").lower()
print("computer" + computer_choice)

if (computer_choice==rock and user_choice == "paper"):
    print("you won ")
elif(computer_choice == paper and user_choice == "rock"):
    print("you lost ")
elif( computer_choice==paper and user_choice == "scissors") : 
    print("you lost ")
elif (computer_choice==scissors and user_choice =="paper"):
    print("you won")
elif(computer_choice==rock and user_choice=="scissors"):
    print("you lost")
elif(computer_choice==scissors and user_choice =="rock"):
    print("you won")
else : 
    print("Tie")


