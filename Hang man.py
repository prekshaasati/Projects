# Flow chart 

# Step 1 : Picking a Random word and checking ans // it should only accept chr not complete words
import random
from hangman_support import word_list , logo ,acsii_hangman
#from hangman_suppot import acsii_hangman
#word_list=["aardvark","baboon","camel"]
list_guess = []  
Won = False
Correct_len = 0
display= "" 

print ( '*************************Welcome to THE HANGMAN game *******************************')
print (logo)

chosen_word= random.choice(word_list)
#print(chosen_word)
len_word = len(chosen_word)
lives = 6 


# replacing blanks with guesses

# for each letter in chosen word add a - 
current_guesss = ""
for letter in chosen_word : 
    current_guesss+="-"
print(current_guesss)
while  Won is False : 

    guess = input("Guess a letter : ")
    if len(guess)>1:
        print ("enter only 1 character")
        continue
    print("Your guess : "+ guess)


# replacing blanks with guess
    found = False
    if guess in list_guess : 
        print (" You've already guessed it ")
        found = True
    display = ""    
    for letter in chosen_word:
        if guess == letter and guess not in list_guess:
            found = True
            Correct_len+=1
            display+=letter
            list_guess.append(letter)
        elif letter in list_guess : 
                display+=letter
        else:
            display+='-'
    print ( display)
    if (found is False):
         lives -=1
         print (acsii_hangman[lives])
         print(f"Wrong Guess you have {lives}/6 lives remaining ")

    # below if will overwrite this Won
    ''' if chosen_word == display:  
      print ("YOU WON here but ! ")
      Won = True '''


    #print(Correct_len)
    if len_word == Correct_len  :# not required anymore 
        print ("YOU WON ! ")
        Won = True
    elif chosen_word == display:
        print ("****************** Congrates YOU WON ! :) *****************************************")
        Won = True
    elif lives == 0 :
        Won = True
        print (f"****************** Game Over !, Word was {chosen_word} **********************")
    else : 
        #print ("continue ")
        Won = False 
         




