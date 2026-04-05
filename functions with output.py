#function with outputs
#defining a function with RETURN Statement
# we can store the output / result of function in a variable 

def format_name(f_name,l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return (f"{formatted_fname} {formatted_lname}")

name = format_name('preksha','asati')
print(name)

# Multiple Return Functions
def format_name(f_name,l_name):
    '''take first name and last name and capitise it '''
    if f_name =="" or l_name =="": 
        return "wrong input"
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return (f"{formatted_fname} {formatted_lname}")

name = format_name('preksha','asati')
print(name)