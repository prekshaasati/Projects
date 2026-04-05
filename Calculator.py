
def add(num1,num2):
    return (num1+ num2)

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide (num1,num2):
    return num1/num2


operations ={"+": add , "-": subtract , "*": multiply , "/" : divide,}

operations["+"]

print(operations["*"](4,8))
again = True
calc= True 
while calc == True : 

     print("*********** WELCOME TO CALCULATOR ****************")
     n1 = int(input("Enter your first number\n"))
     again = True
     while again is True :
         operation = input("Type the operation you want to perform (+ , - , * , / ) \n")
         n2 = int(input("Enter your Second number\n"))
         result = operations[operation](n1,n2)
         print ( f"result of the above operation is {result}")

         prev = input ("Would you like to continue with previous result y/n\n").lower()
         if prev =='y': 
          n1=result  
          again =True
         else :
          again = False 






