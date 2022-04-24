people = int(input("How many people are riding today? >> "))
cars = int(input('And how many cars are availble? >> '))
trucks = int(input("Just in case, how many trucks are around? >> " ))

print("""Ok you're telling me there are {} people here, we have {} cars available, 
and {} trucks just in case.""".format(people, cars, trucks))


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
elif cars == people: 
    print("What, did everyone drive?!?!?")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
elif trucks == cars:
    print("Why are there an equal number of cars and trucks?!?!?")
else: 
    print("We still can't decide.")

if people > trucks:
    print("Too many people around, who's walking?.")
# the below line will never print since they will both return the same value
# and only the first 'True' result will be printed
elif people > trucks:
    print("This line won't ever print.")
else:
    print("Fine, let's stay home then.")


# people = 30
# cars = 40
# trucks = 15


# if cars > people:
#     print("We should take the cars.")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide.")

# if trucks > cars:
#     print("That's too many trucks.")
# elif trucks < cars:
#     print("Maybe we could take the trucks.")
# else: 
#     print("We still can't decide.")

# if people > trucks:
#     print("Alright, let's just take the trucks.")
# else:
#     print("Fine, let's stay home then.")