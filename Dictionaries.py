#Dictionaries 
# key and value 
#dict = {key : value} / {key : value,}
#Dictionaries are MUTABLE : EDITABLE like a list and unlike strings

#NESTED DICT

# {key : [list],
#key2 : {Dict},}

programming_dict= {
    "Bug" : "An error in an program",
    "function": "A peice of code that can be called over again",
    123 : "defining proper data type is imp ",
}

print(programming_dict["Bug"])
print(programming_dict[123])

#ADDING A NEW ITEM
programming_dict["loop"] ="Action of doing same this again and again " # dict[new_key]=new_value
print(programming_dict)
#EDIT AN EXISTING ITEM
programming_dict[123] =  "this is changed now"   #dict[existing_key]=new_value
print(programming_dict)

# LOOP IN DICT WILL ONLY RETURN KEY not key and it's value

for item in programming_dict:
    print(item) # only prints key 

for key in programming_dict:
    print(key)
    print(programming_dict[key])#value of the key in the dict

# NESTED LIST IN DICT

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"],
}

# print lille
print(travel_log["France"][1])

#nested list in a list 
nested_list = [1,2,[3,4]]
#print 4 
print(nested_list[2][1])


#NESTED DIC IN A DICT

travel_log = {
    "France": {
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visits" : 12,
    },
    "Germany": {
    "cities_visited": ["Stuttgart","Berlin"],
    "total_visits" : 8,
    }
}

# print Berlin
print(travel_log["Germany"]["cities_visited"][1])

