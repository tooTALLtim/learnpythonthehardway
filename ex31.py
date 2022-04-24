from cgi import FieldStorage
import time

print("#" * 50)
enter = " Entering the Dungeons of Araketh "
print(enter.center(50, "#")) #can't have a value lower than 40 or it breaks
print("#" * 50)

input("Are you sure you want to enter?!?! Hit RETURN if you're ready or Ctrl-C if not. No judgement.")

intro = ("""\n
Ok then, and hello! I'm your friendly guide \'Dude\' to the Dungeons of Araketh!
No need to worry, no matter what dangers we encounter
I won't be in the slightest trouble as I'm just a faerie
.....
You, however, will be in grave danger of grevious harm.
Don't mess up and think fast so you'll come out with some treasure and a good story!
""")
print(intro.center(50, "#")) #prints as normal, doesn't work with triple quotes, hmmmm

print("""
So you're in the antichamber looking around in the gloom and see a few ways to go. There's a:
Hallway on the left
Trapdoor in front of you
Stairs winding their way up the darkness
Which way do you want to go?
""")

first_choice = input("So what'll it be? The hallway, trapdoor, or stairs?\n>>>>> ")


def hallway(var):
    print("Walking down the the hallway")
    print("There are torches along the wall, do you want to grab one?")
    second_choice = input("yes or no?\n>>>>> ")
    if second_choice == "yes" or second_choice == 'y':
        print("You have a light!")
        time.sleep(3)    
        print("But now your hand is covered in spiders, ewww!")
    elif second_choice == "no" or second_choice == 'n':
        print("You didn't grab a torch, good thing you didn't as there are spiders all over them!!")
        print("You win! You catch the Melmetal pokmon and find a sweet cartoon!")
        input("Hit return to see the cartoon...")
        import antigravity
    else:
        print("\nDang it's hard to hear in here! Let's try that again...\n")
        hallway(second_choice)



def trapdoor(var):
    print("You grab the large, steel ring and pull up the trapdoor.")
    time.sleep(3)
    print("""AAAAAHHHHHH! There are a sea of spiders down there!!
    You run back to the antichamber to choose again.
    """)

def stairs(var):
    print("Going up the stairs, boy are they creaky!")
    time.sleep(3)
    print("""
    *BOOOM* Your feet punch through the floor and 
    you tumble back to the antichamber!
    """)

def one(var):
    if var == "hallway" or var == "h":
        print("Hallway chosen.")
        hallway(var)
    elif var == "trapdoor" or var == "t":
        print("Trapdoor chosen.")
        trapdoor(var)
    elif var == "stairs" or var == "s":
        print("Stairs chosen.")
        stairs(var)
    else:
        print("Ooops, sorry adventurer, I didn't quite hear you over the bats, say that again?")
        first_choice = input("Please just type h for hallway, t for trapdoor, or s for stairs. \n>>>>>")
        one(first_choice)
one(first_choice)




# print("""You enter a dark room with two doors.
# Do you go through door 1 or door 2?""")

# door = input(">>> ")

# if door == "1":
#     print("""There's a giant bear here eating a cake.
#     What do you do?
#     1. Take the cake.
#     2. Scream at the bear.""")

#     bear_reaction = input(">>> ")

#     if bear_reaction == "1":
#         print("The bear eats your face off, oh no!")
#     elif bear_reaction == "2":
#         print("The bear eats your legs, didn't need those anyways.")
#     else:
#         print(f"Well doing {bear_reaction} was probably the better decision.")
#         print("You and the bear make a hasty retreat.")

# elif door == "2":
#     print("You encounter the endless abyss that is Cthulhu's right retina.")
#     print("You're shocked and can only think of:")
#     print("1. Blueberries.")
#     print("2. Yellow jacket clothespins.")
#     print("3. Understanding revolvers yelling melodies.")
    
#     insanity = input("What do you choose? >>>")

#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello.")
#         print("This is good!")
#     else:
#         print("The insanity rots your eyes into a pool of muck.")
#         print("Probably better than the alternative.")

# else:
#     print("You stumble around in the darkness and get completely lost!")
#     print("The end. You should have chosen 1 or 2!")