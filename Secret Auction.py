#add logo
#welcome to game : ..
# ask for user name
#what is your bid
#clear screen : print("\n"*10)
# loop through untill they say no to continue 
# add all names and bid as key value
#print highest amt

print("Welcome to the Silent bid\n")
auction_Dict = {}
name1 = input("What is your name ?\n")
bid1= int(input("What is your bid : Rs.")) 
auction_Dict[name1]=bid1
more = input("Are there any more bidders ? Y/N\n").lower()
if more=='y':
    while more=='y': 
        print("Please pass the screen to the next bidder")
        print("\n"*50) # trick for creating an illusion of a new page 
        name= input("What is your name ?\n")
        bid= int(input("What is your bid : Rs.")) 
        auction_Dict[name]=bid
        more = input("Are there any more bidders ? Y/N\n").lower()
        if more =='n':
            break
if more=='n':
    #print(auction_Dict)
    max_bid=0
    winner=""
    for key in auction_Dict:
        if auction_Dict[key] > max_bid:
            max_bid=auction_Dict[key]
            winner=key
            #print(max_bid)
            #print(winner)

    
print(f" {winner} Won the bid with rs.{max_bid}")







