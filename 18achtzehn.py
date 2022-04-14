# this is making a function using 'def' (the define function) called 'print_two' with an unknown number of arguments
def print_two(*args): #this colon is super important as everything indented after will be part of the function!
    arg1, arg2 = args # now I tell the function that there are two arguemnts and it unpacks them
    print(f"This is the first argument {arg1} and this is the second {arg2}.")

# a different way to do the above when I know I only have two arguments
def print_two_again(arg1, arg2): # no unpacking here since we put the args in the parentheses
    print(f"This is a better way to print {arg1} (arg1) and {arg2} (arg2).") 

# this function only takes one arguemnt
def print_one(arg1):
    print(f"This is argument one: {arg1}.")

# and this one will take none!
def print_none():
    print("Move along, nothing to see here!")

print_two("Timmay", "codes!!")
print_two_again("Like a", "boss man!")
print_one("Here's that one string in the function.")
print_none()