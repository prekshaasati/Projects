 # Black Jack 
# enter your cards : get 2 pair of cards from list 1 to 10 
# show both to user
# computer generates a pair , 
# we reveal one of the selected
# ask user if they want another card [y,n]
# if y , then pick one more random number from the list 
# calculate sum of the items in list : if user_sum > 21 then user looses its called bust 
# if we say n 
# we will print computer's second number , we calculate the sum_comp 
# if comp_sum == user_summ --> draw
# if comp_sum <=17 then they must draw another card
# who ever sum is lesser wins
# Ace will be started as 11 but if sum >21 then we will assume it as 1 
# cards in infinite here 
# jack , queen , king are counted as 10

black = '''
                                      .------.  
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'    
                         `------'

'''
jack= ''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 '''

blackjack = black + jack
print(blackjack)

import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def score(user_picks):
    sum = 0
    count=0
    index=0
    count_ii=[]
    for number in user_picks:
        sum+=number
        if number== 11 : 
            count+=1
            count_ii.append(index)
            print(count_ii)

    index+=1
    if sum > 21 and count > 1 :
        user_picks[max(count_ii)] = 1
        score(user_picks)

    return sum

def is_bust (sum):
    if sum > 21 :
        return True 
    else :
        return False 
def is_computer_draw_another (sum):
    if sum <=17 :
        return True
    else :
        return False

user_picks = random.choices(cards,k=2)
comp_picks = random.choices(cards,k=2)
print(f"Computer's first number : {comp_picks[0]}")
again = True 
while again is True : 
    usr_score = score(user_picks)
    if usr_score > 21 :
        print ("**********  You lost , yuor sum is greater than 21 *****************")
        break
    print (f"your cards are {user_picks}, current score is {usr_score}")
    choice = input("Type 'y' to get another card , type 'n' to pass....... : ").lower()
    if choice == 'y':
        again = True 
        user_new_pick = random.choice(cards)
        user_picks.append(user_new_pick)
        print (f"You drew :  {user_new_pick}")
    elif choice == 'n':
        print (f"Computer picks {comp_picks}")
        again = False
        comp_score = score(comp_picks)
        if comp_score > 21 :
            print (f" **********You Won , Computer score {comp_score} exceeded 21 *************")
            break
        elif is_computer_draw_another(comp_score) is True :
                comp_new_pick = random.choice(cards)
                comp_picks.append(comp_new_pick)
                comp_score = score(comp_picks)
                print (f"Comp drew :  {comp_new_pick}")
                if is_bust(comp_score) is True : 
                    print ("**************You Won ! ****************************")
                else :
                    print ("**************Computer Won ! ************************* ")





        


else :
    again = False 



