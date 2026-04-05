# make 3 falvors of coffee
# manage resources 
# coin operated

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    #print(resources)
    print ("the current_resources are : \n")
    print (f"Water :{resources['water']}ml ")
    print (f"Milk :{resources['milk']}ml ")
    print (f"Coffee :{resources['coffee']}g ")
    print (f"Money :rs.{profit} ")


def is_resources_sufficient(user) :
    required= {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}
   # print (MENU[user]['ingredients']['coffee'])
    for item in MENU[user]['ingredients']:
        #print (item)
        #print(MENU[user]['ingredients'][item])
        required[item]= (MENU[user]['ingredients'][item])
    #print (required)
    for item in resources :
        #print(item)
        #print(resources[item])
        #print(required[item])
        if resources[item] < required[item]:
            print (f"Sorry , there is not enough {item}")
            return False
        else :
            return True
            
def process_coins(no_quarters,no_dimes,no_nickles,no_pennies):
    quarters=0.25
    dimes=0.10
    nickles=0.05
    pennies=0.01

    Money = quarters*no_quarters + dimes*no_dimes + nickles*no_nickles + pennies* no_pennies
    print(f"money : {Money}")
    return Money
 
def enough_money (money ,user ):
    drink_cost = MENU[user]['cost']
    print(f" drink_cost: {drink_cost}")
    if money >= drink_cost :
        if money > drink_cost :
            change = round(money - drink_cost , 2)
            print (f" Here is Rs {change} rupees in change")
        return True
    else :
        print("Sorry , you have not entered enough coins ")
        return False
    
def recalculate_resources(user,profit):
    drink_cost = MENU[user]['cost']
    profit+=drink_cost
    print(f"profit : {profit}")
    required= {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}
    for item in MENU[user]['ingredients']:
        #print (item)
        #print(MENU[user]['ingredients'][item])
        required[item]= (MENU[user]['ingredients'][item])
    print (required)
    print(resources)
    for item in resources :
        #print(item)
        #print(resources[item])
        #print(required[item])
        resources[item] = resources[item] - required[item]
        return profit
        #print(resources[item])










        
    
# ask user 
secret_code = 'on'
while secret_code != 'off' : 
    user = input ("What would you like ? (espresso / latte / cappuccino) \n")
    if user !='off': 
     print_report()
     sufficient = is_resources_sufficient(user)
     if sufficient is True :
        ("Please insert coins below :\n")
        quarters = float(input("Quarters :"))
        dimes = float(input("Dimes :"))
        nickles = float(input("Nickles :"))
        pennies = float(input("Pennies :"))
        money_inserted = process_coins(quarters,dimes,nickles,pennies)
        if enough_money (money_inserted ,user):
            profit= recalculate_resources(user,profit)
            print ( f" Here is your {user}, Enjoy !")
            print_report()
    if user == 'off' : 
     print("Turning off !")
     secret_code='off'




