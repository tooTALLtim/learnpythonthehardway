from cgi import FieldStorage
import time


print("#" * 50)
time.sleep(1)
print("#" * 50)
time.sleep(1)
print("#" * 50)
time.sleep(1)
print("#" * 50)
time.sleep(1)
enter = " Entering the Dungeons of Araketh "
print(enter.center(50, "#")) #can't have a value lower than 40 or it breaks
time.sleep(1)
print("#" * 50)
time.sleep(1)
print("#" * 50)
time.sleep(1)
print("#" * 50)
time.sleep(1)
print("#" * 50, "\n\n")
time.sleep(1)

input("""Are you sure you want to enter?!?!
Hit RETURN if you're ready or Ctrl-C if not. No judgements :P\n""")

intro1 = ("""\n
Ok then, and hello! I'm your friendly guide \'Dude\' to the Dungeons of Araketh!
No need to worry, no matter what dangers we encounter
I won't be in the slightest trouble as I'm just a faerie""")
intro2 = ("""
You, however, will be in grave danger of grevious harm.
Don't mess up and think fast so you'll come out with some treasure and a good story!
""")
print(intro1)
time.sleep(8)
print(intro2)
time.sleep(5)

name = input("And adventurer, what should I call you?\n>>>>> ")
print(f"Hmmm, {name} is sure an odd name, never heard that before. We'll just go with it ")

time.sleep(8)

def antichamber(var):
    print(f"""
So, {name} you're in the antichamber looking 
around in the gloom and see a few ways to go. There's a:
Hallway on the left
Trapdoor in front of you
Stairs winding their way up the darkness
Which way do you want to go?
""")
    time.sleep(10)
    first_choice = input("So what'll it be? The hallway, trapdoor, or stairs?\n>>>>> ")
    one(first_choice)



def hallway(var):
    print("Walking down the the hallway")
    time.sleep(2)
    print("There are torches along the wall, do you want to grab one?")
    time.sleep(2)
    second_choice = input("yes or no?\n>>>>> ")
    if second_choice == "yes" or second_choice == 'y':
        print("You have a light!")
        time.sleep(3)    
        print("But now your hand is covered in spiders, ewww!")
        print("You run back to the antichamber...")
        time.sleep(5)
        antichamber(var)
    elif second_choice == "no" or second_choice == 'n':
        print("You didn't grab a torch, good thing you didn't as there are spiders all over them!!")
        time.sleep(2)
        print("You win! You catch the Melmetal pokmon and find a sweet NFT!")
        input("Hit return to see the NFT...")
        import antigravity
    else:
        print("\nDang it's hard to hear in here! Let's try that again...\n")
        hallway(second_choice)



def trapdoor(var):
    print("You grab the large, steel ring and pull up the trapdoor.")
    time.sleep(3)
    print("""
    AAAAAHHHHHH! There are a sea of spiders down there!!
    You run back to the antichamber to choose again.
    """)
    time.sleep(5)
    antichamber(var)

def stairs(var):
    print("Going up the stairs, boy are they creaky!")
    time.sleep(3)
    print("""
    *BOOOM* Your feet punch through the floor and 
    you tumble back to the antichamber!
    """)
    time.sleep(5)
    antichamber(var)

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

antichamber(vars)