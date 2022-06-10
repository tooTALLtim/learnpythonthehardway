# this imports antigravity (XKCD)
from cgi import FieldStorage
# this imports the time function
import time

# give them that slow roll baby!
print("#" * 50)
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
enter = " Entering the Dungeons of Araketh "
print(enter.center(50, "#")) #can't have a value lower than 40 or it breaks
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
print("#" * 50)
time.sleep(0.5)
print("#" * 50, "\n\n")
time.sleep(0.5)

# Why the hell not
input("""Are you sure you want to enter?!?!
Hit RETURN if you're ready or Ctrl-C if not. No judgements :P\n""")

# INTRODUCTION
intro1 = ("""\n
Dude: \"Ok then, and hello! I'm your friendly guide \'Dude\' to the Dungeons of Araketh!
No need to worry, no matter what dangers we encounter
I won't be in the slightest trouble as I'm just a faerie""")
intro2 = ("""
You, however, will be in grave danger of grevious harm.
Don't mess up and think fast so you'll come out with some treasure and a good story!\"
""")
print(intro1)
#time.sleep(8)
print(intro2)
#time.sleep(5)


# CHOOSE A NAME, GET A NICKNAME
name = 'default user'
def naming(var):
    global name
    print(f"Dude: \"Hmmm, \'{var}\' sure is an odd name, never heard that one before.\"")
    var = list(var)
    var = var[:3]
    name = ''.join([str(item) for item in var])
    print(f"Dude: \"I'll just call you \'{name}\' for short since we're now friends.\"")

naming(input("Dude: \"And adventurer, what should I call you?\"\n>>>>> "))
#time.sleep(3)


# ANTICHAMBER Get kicked back here if you choose trapdoor or stairs
def antichamber(var):
    print(f"""
Dude: \"So, {name}, you're in the antichamber looking 
around in the gloom and see a few ways to go:\"\n
Hallway on the left
Trapdoor in front of you
Stairs winding their way up the darkness
""")
#    time.sleep(2)
    first_choice = input("Dude: \"So what'll it be? The hallway, trapdoor, or stairs?\"\n>>>>> ")
    one(first_choice)


# first choice
def one(var):

    if var == "hallway" or var == "h":
        print("[hallway chosen]")
        hallway(var)
    elif var == "trapdoor" or var == "t":
        print("[trapdoor chosen]")
        trapdoor(var)
    elif var == "stairs" or var == "s":
        print("[stairs chosen]")
        stairs(var)
    else:
        time.sleep(2)
        print(f"\nDude: \"Ooops, sorry {name}, I didn't quite hear you over the bats, say that again?")
        first_choice = input("Please just type h for hallway, t for trapdoor, or s for stairs.\" \n>>>>>")
        one(first_choice)

# this option will continue the journey from the first choice 'one'
def hallway(var):
    print("[walking down the the hallway]")
#    time.sleep(2)
    print("Dude: \"There are torches along the wall, do you want to grab one?\"")
#    time.sleep(2)
    second_choice = input("yes or no?\n>>>>> ")

    if second_choice == "yes" or second_choice == 'y':
        print("Dude: \"You grab a torch. You now have a light!\"")
        time.sleep(3)    
        print(f"Dude: \"But now your hand is covered in spiders, ewww! Sorry {name} that was kinda mean on my part...\"")
        print("[run back to the antichamber]")
        time.sleep(5)
        antichamber(var)
    elif second_choice == "no" or second_choice == 'n':
        print("Dude: \"You didn't grab a torch, good thing you didn't as there are spiders all over them!!\"")
#        time.sleep(2)
        print("[you continue down the hallway into a large, dimly lit room]")
        room(var)
    else:
        print("\nDude: \"Dang it's hard to hear in here! Let's try that again...\"\n")
        hallway(second_choice)

# choose trapdoor and get kicked back to Antichamber
def trapdoor(var):
    print("[you grab the large, steel ring and pull up the trapdoor]")
    print("Dude: \"What are you doing?!?! It's called a \'TRAPdoor\' for a reason!\"")
    time.sleep(3)
    print(f"""
    {name}: \"AAAAAHHHHHH! There are a sea of spiders down there!!\""
    [you run back to the antichamber]
    """)
    time.sleep(5)
    antichamber(var)

# choose stairs and get kicked back to Antichamber
def stairs(var):
    print("[going up the very creaky stairs]")
    time.sleep(3)
    print(f"Dude: \"Yo {name}, I don't think that...")
    print("""
    [*BOOOM* your feet punch through the floor and 
    you tumble back to the antichamber!]
    """)
    time.sleep(5)
    antichamber(var)

# Room, go here after the hallway
def room(var):
    print("[you enter the dimly lit room and look around while your eyes slowly adjust]")
#    time.sleep(4)
    print("""
    [you see a large banquet table, resplendent with fine crystal vessels,
    fine silver cutlery, and golden plates. it looks like the table was being
    set for a large meal for many guests, and was.....interrupted]
    """)
    print(f"Dude: \"Yo {name}, I think you scared them all away!")
    print("""
    [out of a dark corner of the ceiling, a small bat flies down and lands 
    on the table in front of you and Dude]
    """)
    print(f"Bat: \"Hey Dude, hey {name}.\"")
    print(f"{name}: \"How do you know my name?\"")
    print("Bat: \"The place emptied out when they heard you walking down the hall.\"")
    print(f"\"And Dude literally just said your name, {name}.\"")
    print("\"Aaaaanyways, want to know where they all went? Well, of course you do.\"")
    print("""\
    \"I'll tell you, but they dislike dumb people so
    I gotta ask you some questions before you meet them.
    Math questions, heheheh.\"
    """)
    print(f"{name}:\"That's great, I love Maths!\"")
    print("Bat: \"Cool cool.\"")
    first_question(var)

def first_question(var):
    print("Bat: \"So the first question is: solve 9 * 3 + 10 / 5 - 5\"")
    answer = input(">>>>> ")

    if answer == "24" or answer == "i hate math":
        print("Bat: \"Good job!\"")
        second_question(var)
    else:
        print("Bat: \"Nope! Try again\"")
        first_question(var) #doesn't have to be 'answer', can simply pass 'var' as argument!!

def second_question(var):
    print("Bat: \"Ok, second question: is the following statement True or False?\"")
    print("\n1 == 1 and (not(True or \'a\' == \'b\') or (23 == 24 and False))\n")
    mansw = input("True or False? \n>>>>> ")

    if mansw == "True" or mansw == "t":
        print()
        again = input("Bat: \"Sure ain't! Try again? yes or no\"\n>>>>> ")

        if again == "yes" or again == "y":
            second_question(var)
        else:
            print("Bat: \"OK, back to the Antichamber with you!!\"")
            antichamber(var)

    elif mansw == "False" or mansw == "f":
        print("Bat: \"Yusss, correct!\"")
        win(var)
    else:
        print("Bat: \"Huh? You speak so quitely, try again.\"")
        second_question(var)

def win(var):
        print("Dude: \"You win! You catch the Melmetal pokmon and find a sweet NFT!\"")
        input("[hit return to see the NFT]")
        import antigravity

# kick it all off!
antichamber(vars)


# more fun things to add:
# multiple pathways to the right place! "Do you want to go this way?" doesn't always lead the wrong way!
# must get it wrong and then go back to the same place and do it a second time to get it right!
# spiders fail multiple times before not scared of spiders??
# recall number for password at end: number of torches etc
# add in fighting? or some accual system? later? other game?
# taking multiple variables from input()
# https://towardsdatascience.com/a-complete-guide-to-user-input-in-python-727561fc16e1
# at the bottom
