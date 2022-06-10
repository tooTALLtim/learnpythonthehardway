# this doesn't work as intended, but was fun to try and make work
# user_def = int(input("How high do you want to count today?\n>>>>> "))
# incre = int(input("And by what increment? 1's, 2's, 8's?\n>>>>> "))

# a = 0
# numbers = []

# for i in range(0, user_def):

#     print(f"At the top a is {a}")
#     print(f"Now the numbers list contains ", numbers)
#     a = a + incre
#     print(f"I'll increment by your chosen number so a is now: {a}\n")
#     numbers.append(a)
#     print("And now the list of numbers is: ", numbers)
#     print()
# print("The numbers: ")
# for var in numbers:
#     print(var, end=' ')
# print()



def wloop(var):
    i = 0
    numbers = []
    user_def = int(input("How high do you want to count today?\n>>>>> "))
    incre = int(input("And by what increment? 1's, 2's, 8's?\n>>>>> "))
    while i < user_def:
        print(f"At the top i is {i}")
        numbers.append(i)
        print(f"Now the numbers list contains ", numbers)
        i += incre
        print(f"After all that i is now: {i}\n")
    
    print("The numbers: ")
    for var in numbers:
        print(var, end=' ')
    print()

wloop(vars)



# def wloop(var):
#     i = 0
#     numbers = []
#     while i < var:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#         print(f"Now the numbers list contains ", numbers)
#         i += 1
#         print(f"After all that i is now: {i}\n")
#     print("The numbers: ")

#     for var in numbers:
#         print(var, end=' ')
#     print()

# wloop(int(input("How integers do you want to count today?\n>>>>> ")))



# def wloop(var):
#     i = 0
#     numbers = []
#     while i < var:
#         print("Now let's just use 12.")
#         print(f"At the top i is {i}")
#         numbers.append(i)
#         print(f"Now the numbers list contains ", numbers)
#         i += 1
#         print(f"After all that i is now: {i}\n")
#     print("The numbers: ")

#     for var in numbers:
#         print(var, end=' ')
#     print()

# wloop(12)


# original lesson
# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1    
#     print("Numbers are now: ", numbers)
#     print(f"At the bottom i is: {i}\n")


# print("The numbers: ")

# for var in numbers:
#     print(var)