#Comparing A OR B , who has gier wins ---> untillyou get wrong ans 
# untill they get wrong loop shouls continue
# compare whosw count is greater 
# keep score 


from game_data import data
import random

#A = random.choice(data)
#B= random.choice(data)
#print(A)
#print(B)
score = 0
Correct = True  
while Correct is True : 
    A = random.choice(data)
    B= random.choice(data)
    #print(A)
    #print(B)
    print (f"A : {A['name']} is a {A['description']} from country {A['country']} .")
    print (f"B : {B['name']} is a {B['description']} from country {B['country']} .")
    guess = input("Whose Followers are more A OR B ? :" ).lower()
    if A['follower_count'] > B['follower_count']  and guess =='a':
        score+=1
    elif A['follower_count'] < B['follower_count']  and guess =='b':
        score+=1
    elif A['follower_count'] == B['follower_count'] :
        score+=1
    else :
        Correct = False
print(f"Sorry that's Wrong , Your total score is {score}")
