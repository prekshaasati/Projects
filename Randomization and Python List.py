#Random Module
#Psudo Random Number Generators : python uses Random Module for it : mersenner twister is an algo used for it 
# module consists of a lot of functions for us to use
import random # importing a module 

random_int = random.randint(1,10)# random whole number bewteen 1 and 10 including both 1 and 10
print(random_int)

#module.function needs a () to execute 
randdom_no_0_to_1=random.random()
randdom_no_0_to_10=random.random()*10 # not including 10
random_float = random.uniform(1,10)# can include 10 
print(randdom_no_0_to_1)
print(randdom_no_0_to_10)
print(random_float)

#HEADS OR TAILS
toss= random.randint(0,1) # so either o or 1 
if toss==0:
    print("Heads")
else : 
    print("Tails")


