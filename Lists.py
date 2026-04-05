# PYTHON LISTS
#list.append(data)
#list.extend(data1,data2,...)
#len(list)
import random
#Banker Roulette
# get random name from a list of items to choose who will pay the bill 
friends = ["Preksha","Shreya","Bulbul","Rushikesh","Jatin"]
print(friends[0] + " "+ friends[-1])
random_friends = random.randint(0,len(friends)-1)
print(random_friends)
print(friends[random_friends])

# OR 

print(random.choice(friends)) # getting random item from a list 


# NESTED LIST : LIST WITHIN A LIST
fruits = ["apple","banana"]
vegies = ["spinich","potato"]
my_diet=[fruits,vegies]
print(my_diet)

