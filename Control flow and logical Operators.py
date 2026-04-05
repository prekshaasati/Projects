#Conditional Statements : if else /nested /elif
#Logical Operators : and /or  / not 
#Code Blcoks
#Scope Global and local namespaces


'''print ("Welcome to the rollercoaster")
height = int(input("What is your Height in cm ?: "))
bill=0
if height >=120 : 
     print("Yes , You can ride")
     age = int(input("Please enter toyr age : "))
     if age <= 12:
         bill=50
         print("please pay 50 rs")
     elif age >12 and age <18 :
         bill=70
         print ("please pay 70 rs")
     else :
         bill=180
         print("please pay 180 rs") 
     want_photo = input("want photos ? y/n : ")
     if want_photo =="y":
         bill+=3
     print(f" your total bill is {bill}")  
else :                                               
    print("oh no, You need to drink more complan ")

#comparison opeprators : 
# > --> greater than || >= --> greater than or equal to 
# < ---> lesser than || <= ---> lesser than or equal to 
# == ---> equals to  || != ---> not equals to 

# MODULO OPERATOR : % -->remainder of the division

# Odd or even number 
print("\nlet's find out if the number is even or odd")
num= int(input("Enter a number: "))
if num%2 == 0 :
    print (f" {num} is an even number ")
else :
    print (f" {num} is a Odd number ")'''




#PYTHON PIZZA 
'''print("Welcome to thr Python pizza Deliveries!")
size=input("Size of the pizza : S , M or L : ")
peperroni = input ("Do you want to add pepperoni ? Y / N")
extra_cheese = input ("Do you want extra cheese ? Y/N ")
bill=0
if size =='S':
    bill=15
    if peperroni =='Y':
     bill+=2
elif size =='M':
    bill = 20
    if peperroni =='Y':
       bill+=3 
else :
    bill = 25
    if peperroni =='Y':
       bill+=3
if extra_cheese =='Y':
   bill+=1

print (f"your total bill is {bill}")'''

