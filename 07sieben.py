#simple printing here
print("Mary had a little lamb.")

# a third way to make a format string below!!
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 100)

#making lots of variables below
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
space = " "

#cannot add the variables together and add end=" ", get error!
#must have comma between them, why? this keeps the Cheese and Burger on the same line
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)

#splitting Cheese and Burger to diffent lines
print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

#fun to repeat some of these words and letters. It wouldn't repeat "Cheese" with
#the variable in there as it's originally written, had to make "space" variable
print((end1 + end2 + end3 + end4 + end5 + end6 + space) * 10)
print((end7 + end8 + end9 + end10 + end11 + end12 * 10 + space) * 10)