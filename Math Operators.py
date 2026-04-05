
#BASIC OPERATORS : + - * / ** // ____ PEMDAS

print(1+2)
print(1-2)
print(1*2)
print(2**4)
print(4/2)# implicit casting is done by python , it considers int as float only 
print(5//3)#1
print(5//3.0)#1.0

print(3*3+3/3-3) # P E D M A S
print((3*3)+((3/3)-3))
#BMI Calculator : weight/(height)**

bmi= 54/(1.58496)**2

#DATA MANIPULATION

print(round(bmi,2) ) # round function 

# += , -= , *= , /=

# f- string 
# f string is used to easily insert diffrent types of variables in a string 
# put f in front of sting
# put variables inside {}
# and see how easy it is 

score=0
height=1.4
is_winning = True
print (f"Since your height is {height} and your score is { score} , you are winning : {is_winning}")
