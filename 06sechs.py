#this is a variable
types_of_people = 10
#this is a variable that is equal to a "format string"
x = f"There are {types_of_people} types of people."

#variables babay
binary = "binary"
do_not = "don't"
#another variable that's equal to a format string
y = f"Those who know {binary} and those who {do_not}."

#display this stuff!
print(x)
print(y)

#here are format strings that have format strings in them!
print(f"I said: {x}")
print(f"I also said: '{y}'")

#aww, this variable is sad, changing to True
hilarious = True
#very interesting format string below
joke_evaluation = "Isn't that joke so funny?! {}"
#super cool format string, could use this format when having different outcomes withtout writing several strings
print(joke_evaluation.format(hilarious))
print("Yep, that's what I thought too!")

#love me some variables
w = "This is the left side of..."
e = "a string with a right side."

#now this is a clever way to join two strings
print(w + e)