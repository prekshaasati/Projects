#Functions : packaging a block of code for reusing 
#functions with input allow functions to have some variations based on parameters 
'''
def greet(name):
    print(f"Hi {name}, Good Morning ! ")
    print("My Name is Preksha ")
    print("Hope you have a lovely Day !")


name = input(" What is Your Name dear ? \n")
greet(name) '''
#greet("Pragya") #CAN ALSO BE PASSED DIRECLTY


# PARAMERTER VS ARGUMENT
# PARAMETER IS THE VARIALBE PASSED TO A FUNCTION 
# EG : name 
# ARGUMENT IS THE ACTUAL VALUE PASSED TO A FUNCTION EITHER DIRECTLY OF BY A PARAMETER
# EG: "PRAGYA"

#FUNCTIONS WITH more than than 1 input 

def greet_with(name,location):
    print (f"Hi {name}!")
    print( f"How is the weather in {location} ?")

greet_with('Preksha','Delhi')#positional argument
greet_with(location='delhi',name='Preksha') #keyword agrument


             
                     

