class User:# writing a class # FirstLetterCapital-->PascalCase   and snake case for everything else snake_case
    def __init__(self,user_id,username):#self -->actual object being initialised
        self.id=user_id
        self.username=username 
        self.follower=0 # since this attribute will always be constant at time of initialisation of an object , we can make it default in our constructor and son'r jave to pass it in aur init function's parameter 
        self.following = 0

    def follow(self,user): # a method , unlike a function has SELF as the first parameter , so that it knows what object is calling this method
        user.follower+=1
        self.following+=1


#what should happen when an object is created : Contrustor / initailaise attributrs of an object

#user_1=User()#creating object of User----> this will error since arguments not passed
# user_1.name ="preksha" # creating attribute of an object
# user_1.id="001"




user_2 = User('001','preksha') # these parameters have become necessary now since  
print(user_2)
print(user_2.id)
print(user_2.username)
print(user_2.follower)

user_3 = User('002','pragya') 

user_2.follow(user_3)
print(user_2.follower)
print(user_2.following)
print(user_3.follower)
print(user_3.following)

