"""
Welcome to Araketh! Gather all the Artifacts to unlock the Vault in the Anitchamber!!
"""

# this imports the XKCD antigravity comic
from cgi import FieldStorage
from pickletools import float8
from pydoc import plain
# this imports the time function so the header rolls down slowly
import time
# let's make those printed dictionaries look pretty!
import pprint
# need some random in our lives
import random
# better whitespace management when using """
from textwrap import dedent
# A nice way to exit the game.
from sys import exit

class Player(object):

    name = 'default'
    backpack = {10: "chewed up gum in a wrapper"}
    toolbelt = ['lint']
    maths_passed = False

    def contents_of_backpack(self):
        for item, writing in list(Player.backpack.items()):
            print(f"the {item} has \'{writing}\' written on it")
    
    def contents_of_toolbelt(self):
        for item in Player.toolbelt:
            print(f"Dude: \"You have a {item} in your toolbelt.\"")
    
    def naming(self):
        player_name = (input("Dude: \"And adventurer, what should I call you?\"\n>>>>> "))
        player_name = list(player_name)
        player_name = player_name[0:3]
        Player.name = ''.join([str(item) for item in player_name])
        print(f"Dude: \"I'll just call you \'{Player.name}\' for short since now we're friends.\"")

# have a dictionary that has several artifacts that get popped randomly as player finds them
class ArtifactsTools(object):

    artifact_dict = {
        'horn' : 'speak',
        'scroll' : 'friend',
        'goblet' : 'and',
        'necklace' : 'enter'
    }

    tools_list = ['prybar', 'can of WD40', 'knife']

    def __init__(self):
        self.player = Player()

    def reveal_artifact(self, key, value):
        ArtifactsTools.artifact_dict.pop(key, value)
        print(f"Dude: \"Sweet! You found a {key} with \'{value}\' written on it.")
        print("Dude: \"I'll toss that in your backpack...\"")
        self.player.backpack[key] = value

    def pop_tool(self):
        # pop a random tool out of the tools_list for the Player to use later
        tool = ArtifactsTools.tools_list.pop(random.randrange(len(ArtifactsTools.tools_list)))
        print(dedent(f"""
        Dude: \"Woah {self.player.name}, it's a {tool}. I bet you'll find that useful later!
        I'll put it in your toolbelt for you...there, stowed away.\"
        """))
        self.player.toolbelt.append(tool)
        print("Dude: \"By the way, here's what's in your toolbelt:")
        print(self.player.toolbelt)


# handles the headers for all the rooms
class RoomHeader(object):

    def cool_header(self, room_title):
        # give them that slow roll baby!
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print(room_title.center(50, "#")) #can't have a value lower than 40 or it breaks
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50)
        time.sleep(0.5)
        print("#" * 50, "\n\n")
        time.sleep(0.5)

class TestingTools(object):

    # More econimical way to test if input is an integer.
    def is_a_number(self, x):
        try:
            int(x) == True
            # print("That's an integer!") # testing 
            return True
        except ValueError:
            # print("That ain't an integer! Try again...") # testing 
            return False

class OpeningScene(object):

    room_title = " Entering the Dungeons of Araketh "

    def __init__(self):
        self.room_header = RoomHeader()
        self.player = Player()

    def enter(self):
        # self.room_header.cool_header(OpeningScene.room_title)
        print("Opening Scene!")
        intro1 = (dedent("""\n
        Dude: \"Ok then, and hello! I'm your friendly guide \'Dude\' to the Dungeons of Araketh!
        No need to worry, no matter what dangers we encounter
        I won't be in the slightest trouble as I'm just a faerie"""))
        intro2 = (dedent("""
        You, however, will be in grave danger of grevious harm.
        Don't mess up and think fast so you'll come out with some treasure and a good story!\"
        """))
        print(intro1)
        #time.sleep(8)
        print(intro2)
        #time.sleep(5)
        self.player.naming()
        Engine.get_room(self, 'antichamber')


class Antichamber(object):

    room_title = " Entering the Antichamber "
    entered = False

    global safe_attempts
    safe_attempts = 0

    def __init__(self):
        self.room_header = RoomHeader()
        self.artifacts = ArtifactsTools()
        self.player = Player()

    def enter(self):
        # self.room_header.cool_header(Antichamber.room_title)
        print("Entered the Antichamber")
        if Antichamber.entered == False:
            Antichamber.first_entry(self)
        elif Antichamber.entered == True:
            Antichamber.second_entry(self)
        else:
            print('what broke?')

    def first_entry(self):
        Antichamber.entered = True
        print(dedent(f"""
        Dude: \"Well {self.player.name}, you are now in the Antichamber! Welcome, not many 
        adventurers have come this way in a while. There's much to check out but 
        you should totally look at this big safe built into the wall over there.
        There's a surprisingly modern-looking keypad on it, and I know that you could
        open it if you had the right password...not saying I tried to peek over the
        owner's shoulder while they typed in the code. Ouch.\"
        """))
        print(dedent(f"""
        Dude: \"So, {self.player.name}, I see three options for ways to explore:
        A dark and winding hallway on the left
        A creepy trapdoor in front of you
        Stairs winding their way up into the darkness\"
        """))
        # time.sleep(2)
        Antichamber.choose(self)
    
    def choose(self):
        choice = input("h for hallway\nt for trapdoor\ns for stairs\n>>>>> ")

        if choice == "h":
            print("[hallway chosen]")
            Engine.get_room(self, 'diningroom')
        elif choice == "t":
            print("[trapdoor chosen]")
            print("[you grab the large, steel ring and pull up the trapdoor]")
            print(dedent(f"""
            Dude: \"Yo {self.player.name}, what are you doing?!?!
            It's called a \'TRAPdoor\' for a reason!\"
            """))
            Engine.get_room(self, 'dungeon')
        elif choice == "s":
            Engine.get_room(self, 'collapsedstairwell')
        else:
            #time.sleep(2)
            print(f"""
            \nDude: \"Ooops, sorry {self.player.name}, I didn't quite hear you over the bats, 
            say that again? Please just type h for hallway, t for trapdoor, or s for stairs.\"
            """)
            Antichamber.choose(self)
    
    def second_entry(self):
        print(dedent("""
        Dude: \"Cool, now we're back in the Antichamber! What do you want to do now?
        You could try and enter the code in the safe's keypad,
        pull open that trapdoor, wall up those stairs winding their way
        up into the darkness, or walk down that hallway.\"
        """))
        choice = input("""
        c for code
        t for trapdoor
        s for stairs
        h for hallway
        >>>>> """)
        if choice == "c":
            print("[trying the safe's code]")
            Antichamber.safe_keypad(self, safe_attempts)
        elif choice == "t":
            print("[trapdoor chosen]")
            Engine.get_room(self, 'dungeon')
        elif choice == 's':
            Engine.get_room(self, 'collapsedstairwell')
        elif choice == "h":
            print("[hallway chosen]")
            Engine.get_room(self, 'diningroom')
        else:
            #time.sleep(2)
            print(dedent(f"""
            \nDude: \"Ooops, sorry {self.player.name}, those barking spiders are loud today,
            say that again? Please just type h for hallway, t for trapdoor, or s for stairs.\"
            """))
            Antichamber.second_entry(self)
    
    def safe_keypad(self, safe_attempts):
        
        print("starting attempts:", safe_attempts)

        print("""\nDude: \"Got enough of the password? Sweet! Type it in!
        If you can't get it correctly and are frustrated just type \'exit\' to 
        go back to the Antichamber. Or type \'quit\' if you're really over it.
        """)
        password = input(">>>>> ")

        if password == "speak friend and enter":
            self.room_header.cool_header(" YOU WON!!! ")
            print("Dude: \"You win! You catch the Melmetal pokmon and find a sweet NFT!\"")
            input("\n\t[hit return to see the NFT]")
            import antigravity
            exit
        elif password == "exit":
            print("\nDude: \"Cool, let's go back out there and explore some more to find the password.")
            Antichamber.second_entry(self)
        elif password == "quit":
            print(f"\nDude: \"Well it's been fun {self.player.name}, thanks for playing!")
            quit
        elif password != "speak friend and enter" and safe_attempts <= 3:
            print("\nDude: \"Well that doesn't work, try again")
            safe_attempts += 1
            print("after attempt", safe_attempts)
            Antichamber.safe_keypad(self, safe_attempts)
        elif password != "speak friend and enter" and safe_attempts == 4:
            print(dedent(f"""
            Dude: \"Hey {self.player.name}, ever read Lord of the Rings?
            You should channel your inner Gandalf, hint hint.\"
            """))
            safe_attempts += 1
            print("after attempt", safe_attempts)
            Antichamber.safe_keypad(self, safe_attempts)
        elif password != "speak friend and enter" and safe_attempts == 5:
            print(dedent("""
            \nDude: \"Hmmm, you're really having a tough go of this. 
            Hop back out to the Antichamber and let's look for more clues.
            """))
            Antichamber.second_entry(self)
        else:
            print("Dude: \"errrrr...FATAL ERROR!!!\"")
            quit


class CollapsedStairwell(object):

    room_title = " Climbing the Stairwell "

    entered = False

    def __init__(self):
        self.room_header = RoomHeader()
        self.artifactstools = ArtifactsTools()
        self.player = Player()
    
    def enter(self):
        if CollapsedStairwell.entered == False:
            CollapsedStairwell.first_entry(self)
        elif CollapsedStairwell.entered == True:
            CollapsedStairwell.second_entry(self)

    def first_entry(self):
        CollapsedStairwell.entered = True
        # self.room_header.cool_header(Hallway.room_title)
        print("\t[going up the very creaky stairs]\n")
        #time.sleep(3)
        print(f"Dude: \"Yo {self.player.name}, I don't think that...")
        print("""
        [*BOOOM* your feet punch through the floor and 
        you tumble into a pile of wood that was the stairwell!]
        """)
        #time.sleep(5)
        print(dedent(f"""
        Dude: \"Woooah! Hey {self.player.name}, are you ok?!?!?! Been a while since
        anyone took those stairs but I didn't think that was gonna happen. Hey, what's
        that under that piece of wood?\"
        """))
        self.artifactstools.pop_tool()
        print("\t[You kick through the stairwell rubble and fall back into the Antichamber]")
        Engine.get_room(self, 'antichamber')
    
    def second_entry(self):
        print(dedent(f"""
        Dude: \"Yeah, once again {self.player.name},
        I'm really sorry I took you up these stairs and
        they broke, my bad! Let's go back to the Antichamber
        and explore some more.
        """))
        Engine.get_room(self, 'antichamber')


class Dungeon(object):

    room_title = " Opening the Trapdoor "
    entered = False
    cell_looted = False
    box_looted = False

    def __init__(self):
        self.room_header = RoomHeader()
        self.artifactstools = ArtifactsTools()
        self.player = Player()

    def enter(self):
        print("Opening the Trapdoor")
        # self.room_header.cool_header(Hallway.room_title)
        if self.entered == False:
            Dungeon.first_entry(self)
        else:
            Dungeon.second_entry(self)
        
    def first_entry(self):
        Dungeon.entered = True
        print("""
        [you skid into a dark Dungeon.
        The floor is damp and you are thankful for plentiful torches 
        in sconces along the walls.
        """)
        print("""
        You look around and see a few things in the Dungeon:
        > a metal-barred cell with a sack in the corner
        > a wooden box up on a shelf
        > the stairs you fell down
        """)
        Dungeon.first_choice(self)
        
    def first_choice(self):
        choice = input("What do you want to do?\nc for cell\nb for box\ns for stairs\n>>>>> ")
        if choice == "c":
            return Dungeon.cell(self)
        elif choice == "b":
            return Dungeon.box(self)
        elif choice == "s":
            print("Dude: \"This place is creeping me out too, let's go back up")
            return Antichamber.enter(self)
        else:
            print(dedent(f"""
            \nDude: \"Ooops, sorry {self.player.name}, you get really quiet when you're scared,
            say that again?\"
            """))
            Dungeon.first_choice(self)
    
    def second_entry(self):
        print(dedent(f"""
        Dude: \"Cool {self.player.name}, we're back in the Dungeon!
        What do you want to do this time?\"
        """))
        Dungeon.second_choice(self)

    # don't want players mining the area if they figure out the box pops out a random tool
    # also don't want it to be boring
    def second_choice(self):
        print("[time for second choices]")
        if Dungeon.box_looted == True and Dungeon.cell_looted == True:
            print(dedent(f"""
            Dude: \"Hmm, looks like you looted the box and the cell
            {self.player.name}, not much more to do down here. 
            Let's go back up to the Anitchamber...\""
            """))
            time.sleep(2)
            Engine.get_room(self, 'antichamber')
        elif Dungeon.box_looted == True and Dungeon.cell_looted == False:
            print(dedent(f"""
            Dude: \"The shattered remains of that box are over there,
            but you haven't opened the cell yet. {self.player.name},
            want to give that a go, or head back up the stairs to the 
            Antichamber?\"
            """))
            choice = input("c for cell\ns for stairs\n>>>>> ")
            if choice == 'c':
                Dungeon.cell(self)
            elif choice == 's':
                print("Dude: \"Ok, going back up the stairs!\"")
                Engine.get_room(self, 'antichamber')
            else:
                print("what broke?")
                exit
        elif Dungeon.box_looted == False and Dungeon.cell_looted == True:
            print(dedent(f"""
            Dude: \"You got looted the cell but haven't messed with the 
            box yet, let's go check that out.\"
            """))
            time.sleep(2)
            Dungeon.box(self)
        elif Dungeon.box_looted == False and Dungeon.cell_looted == False:
            print(dedent(f"""
            Dude: \"So you're looking around the Dungeon again, {self.player.name},
            and the cell is proving difficult. Let's try and get that box open.\"
            """))
            time.sleep(2)
            Dungeon.box(self)
        else:
            print(dedent(f"""
            \nDude: \"Ooops, sorry {self.player.name}, you get really quiet when you're scared,
            say that again?\"
            """))
            Dungeon.second_choice(self)

    def cell(self):
        print(dedent("""
        Dude: \"Daaaang, that's a creepy cell! The door is slightly ajar, 
        I bet you could muscle that open if you tried. Give it a shove!\"
        """))
        print("""
        [You push and shove but can't slide the door open.
        The rust along the bottom of the door is substantial
        and is obviously keeping the door from moving]
        """)
        print(dedent(f"""
        \nDude: \"Wow, it's been a while since anyone opened that up.
        Do you have anything in your backpack that could loosen up that rust?
        Lemme get back there and see what's in there. Here we go: \"
        """))
        self.player.contents_of_toolbelt()
        if "can of WD40" in self.player.toolbelt:
            print("Dude: \"Hey, I bet this WD40 would help loosen up that door!\"")
            Dungeon.open_cell(self)
        else:
            print("\"Shoot, I bet some lubricant would do the trick. Let's find some!\"")
            Dungeon.second_entry(self)

    def open_cell(self):
        Dungeon.cell_looted = True

        print(dedent(f"""
        Dude: \"Sweet {self.player.name}, 
        spray that on the bottom of the door and give it a shoulder!\"
        """))
        print("""
        [you spray the lubricant along the bottom of the cell door
        and start pushing on the door. It doesn't move at first,
        but then the door reluctantly starts to move with a
        loud screeching noise until it's wide enough to enter
        the cell.]
        """)
        print("[you slip into the cell and find a small, velvet, bag with two items inside]")
        print("Dude: \"Cool, what'd you find?!?!\"")
        self.artifactstools.reveal_artifact('scroll', 'friend')
        self.artifactstools.reveal_artifact('glass', 'and')        
        print("Dude: \"Done. Here's what's in there:\"")
        self.player.contents_of_backpack()
        Dungeon.second_choice(self)

    def box(self):
        Dungeon.box_looted = True
        box_kicked = 0

        print(dedent(f"""
        Dude: \"That's a good size box, {self.player.name}, and it's nailed tight.
        But when you shake it around it sounds like something is in there.
        Maybe if you kick it a bunch it'll break open!
        """))
        while box_kicked < 5:
            kick = input("Dude: \"Kick it again!!\" [hit enter]")
            box_kicked += 1
        print("Dude: \"The box broke open! What's in there?\"")
        tool = self.artifactstools.tools_list.pop(random.randrange(len(self.artifactstools.tools_list)))
        print(f"Dude: \"Sweet, there was a {tool} in there! Put it in your toolbelt.")
        self.player.toolbelt.append(tool)
        self.player.contents_of_toolbelt()
        Dungeon.second_choice(self)


class DiningRoom(object):
    room_title = " Entering the Dining Room "
    entered = False
    maths_one_tries = 0
    maths_two_tries = 0
    maths_three_tries = 0
    maths_three_list_length = 0
    maths_three_list = []
    maths_passed = False

    def __init__(self):
        self.room_header = RoomHeader()
        self.artifacts_tools = ArtifactsTools()
        self.player = Player()
        self.testing_tools = TestingTools()

    def enter(self):
        # self.room_header.cool_header(Antichamber.room_title)
        print("Entered the Dining Room")
        if DiningRoom.entered == False:
            DiningRoom.first_entry(self)
        elif DiningRoom.entered == True and self.player.maths_passed == False:
            print("Bat: \"Welcome back! Read to tackle that math again? Alright!\"")
            DiningRoom.question_one(self)
        elif DiningRoom.entered == True and self.player.maths_passed == True:
            DiningRoom.second_entry(self)
        else:
            print("What broke")
            exit

    def first_entry(self):
        DiningRoom.entered = True
        print("[you enter the dimly lit room and look around while your eyes slowly adjust]")
        # time.sleep(4)
        print("""
        [You see a large banquet table, resplendent with fine crystal vessels,
        fine silver cutlery, and golden plates. It looks like the table was being
        set for a large meal for many guests, and was interrupted decades ago.
        Dust and cowbwebs cover everthing, and an eery stillness 
        permeates the Dining Room.]
        """)
        print(f"Dude: \"Yo {self.player.name}, I think you scared them all away, hah!\"")
        print("""
        [out of a dark corner of the ceiling, a small bat flies down and lands 
        on the table in front of you and Dude]
        """)
        print(f"Bat: \"Hey Dude, hey {self.player.name}.\"")
        print(f"{self.player.name}: \"How do you know my name?\"")
        print(f"\"Uhhh, Dude just said your name, {self.player.name}. I'm a bat, I have good ears.\"")
        print("""\
        \"I've been hanging out with just Dude for the longest time,
        and I was wondering...want to do some maths?
        I'm pretty psyched on maths.\"
        """)
        print(f"{self.player.name}:\"That's great, I love maths!\"")
        print("Bat: \"Cool cool.\"")
        DiningRoom.question_one(self)
    
    def second_entry(self):
        print("[The bat has flown away, but the creepy atmosphere remains]")
        DiningRoom.exit_choices(self)

    def question_one(self):
        print("Bat: \"So the first question is: solve 9 * 3 + 10 / 5 - 5\"")
        answer = input(">>>>> ")
        if answer == "24" or answer == "i hate math":
            print("Bat: \"Good job!\"")
            DiningRoom.question_two(self)
        elif DiningRoom.maths_one_tries <= 2:
            print("Bat: \"Nope! Try again\"")
            DiningRoom.maths_one_tries += 1
            DiningRoom.question_one(self)
        else:
            print("Bat: \"What?!? Let's try this all over again...\"")
            DiningRoom.maths_one_tries = 0
            DiningRoom.first_entry(self)
    
    def question_two(self):
        print("Bat: \"Ok, second question: is the following statement True or False?\"")
        print("\n1 == 1 and (not(True or \'a\' == \'b\') or (23 == 24 and False))\n")
        answer = input("t for True\nf for False\n>>>>> ")
        if answer == "False" or answer == "f":
            print("Bat: \"Yusss, correct! For our last question, let's make a list.\"")
            DiningRoom.make_list(self)
        elif DiningRoom.maths_two_tries <= 2:
            print("Bat: \"Sure ain't! Try again.\"")
            DiningRoom.maths_two_tries += 1
            DiningRoom.question_two(self)
        else:
            print(dedent(f"""Bat: \"Yep {self.player.name}, this one is tricky. 
            Brush up on your Boolean logic and come back another time.
            G'bye!\"
            """))
            DiningRoom.maths_two_tries = 0
            Engine.get_room(self, 'antichamber')
    
    # I can't quite get this to work without it repeating itself the 
    # same number of times as the 'except' is raised. So i broke it out into 
    # two functions (make_list and fill_list) and it works properly.
    def make_list(self):
        DiningRoom.maths_three_list_length = input("How long do you want our list to be?\ntype a number 1-6 >>> ")
        one_to_six = ['1', '2', '3', '4', '5', '6']
        if DiningRoom.maths_three_list_length in one_to_six:
            print(dedent("""
            Bat: \"yusss, you followed my directions. now let's fill that list up with numbers
            Whole numbers (integers) only, please.\"
            """))
            DiningRoom.maths_three_list_length = int(DiningRoom.maths_three_list_length)
            DiningRoom.fill_list(self)
        else:
            print("Bat \"That isn't a number 1-6, try again please!\"")
            DiningRoom.make_list(self)
    
    def fill_list(self):
        while DiningRoom.maths_three_list_length > 0:
            try:
                x = int(input("Bat: \"Ok, gimme an integer, no decimal points\"\n>>>>> "))
                DiningRoom.maths_three_list.append(x)
                DiningRoom.maths_three_list_length -= 1
            except ValueError:
                print("That ain't an integer! Try again...")
        DiningRoom.question_three(self)

    # this works but doesn't check if an integer is entered
    # def fill_list(self):
    #     while DiningRoom.maths_three_list_length > 0:
    #         x = int(input("any integer here >>> "))
    #         DiningRoom.maths_three_list.append(x)
    #         DiningRoom.maths_three_list_length -= 1
    #     print("Now we have a list that contains the integers:", DiningRoom.maths_three_list)
    #     print("Ok, let's do some math together with that list of integers!")
    #     DiningRoom.question_three(self)

    def question_three(self):
        bat_maths = {
            'length': (num_length := len(DiningRoom.maths_three_list)),
            'sum': (num_sum := sum(DiningRoom.maths_three_list)),
            'mean': num_sum / num_length,
        }
        print("to start tries are:", DiningRoom.maths_three_tries)
        print("Bat: \"To begin with, you gave me a list of", bat_maths['length'], "numbers\"")
        print("Bat: \"And the sum of those numbers is", bat_maths['sum'])
        print(dedent("""
        Bat: \"Your final question is: what is the mean (average) of those numbers?
        Please round to the nearest integer.\"
        """))
        
        # Did some troubleshooting and found out about how  
        # dictionary numbers are stored! These are floats.
        # print(b_maths["mean"])
        # print("stored in the dictionary this is a:") # float number
        # print(type((b_maths["mean"])))
        q_3_answer = round(bat_maths["mean"]) # the round function changes the float to an integer!
        # print("and after rounding it's a type:")
        # print(type(q_3_answer))
        print("CHEAT CODE The answer is:", q_3_answer)

        your_answer = input(">>>>> ")
        if self.testing_tools.is_a_number(your_answer) == True:
            if int(your_answer) == q_3_answer:
                print(f"{your_answer} is correct!")
                self.player.maths_passed = True
                print("yaaaaaa!")
                print("Bat: \"Here's a random tool, I hope you find it useful!\"")
                self.artifacts_tools.pop_tool()
                print(dedent(f"""
                {self.player.name}: \"Thanks Bat, that was fun to solving
                maths problems, and thanks for that tool!
                """))
                DiningRoom.exit_choices(self)
            elif your_answer != q_3_answer and DiningRoom.maths_three_tries <= 1:
                print(dedent("""
                Bat: \"Nope! Try again, and think about how to find the average.
                And remember to round down to the nearest even integer.
                """))
                DiningRoom.maths_three_tries += 1
                print("after attempt tries are now:", DiningRoom.maths_three_tries)
                DiningRoom.question_three(self)
            elif your_answer != q_3_answer and DiningRoom.maths_three_tries == 2:
                print(dedent(f"""
                Bat: \"Hey {self.player.name}, you've been crushing everything else, and 
                I hate to give such a strong mind a big clue, but how about
                you take the sum of the numbers and divide it by the list length.\" 
                """))
                DiningRoom.maths_three_tries += 1
                print("after attempt tries are now:", DiningRoom.maths_three_tries)
                DiningRoom.question_three(self)
            elif your_answer != q_3_answer and DiningRoom.maths_three_tries == 3:
                print(dedent(f"""
                Bat: \"So, {self.player.name}, you're cool and I want you to continue,
                so the answer is: {q_3_answer}\"
                """))
                DiningRoom.maths_three_tries += 1
                print("after attempt tries are now:", DiningRoom.maths_three_tries)
                DiningRoom.question_three(self)
            elif your_answer != q_3_answer and DiningRoom.maths_three_tries > 3:
                print(dedent(f"""
                Bat: \"YO {self.player.name}, JUST TYPE IN {q_3_answer}, PLEASE!\"
                """))
                DiningRoom.question_three(self)
            else:
                print("some error here, fix it Tim")
                exit
        elif (self.testing_tools.is_a_number(your_answer) == False 
                and DiningRoom.maths_three_tries <= 3):
            print("Bat: \"That isn't an integer! Try again.\"")
            DiningRoom.maths_three_tries += 1
            DiningRoom.question_three(self)
        elif (self.testing_tools.is_a_number(your_answer) == False 
                and DiningRoom.maths_three_tries > 3):
            print(dedent(f"""
            Bat: \"YO {self.player.name}, JUST TYPE IN {q_3_answer}, PLEASE!\"
            """))
            DiningRoom.question_three(self)
        else:
            print("something crazy went wrong")
            exit

    def exit_choices(self):
        print(dedent(f"""
        Dude: \"Sweet as! So {self.player.name}, there are
        a couple choices ahead of us: there's a boarded up
        doorway, another set of stairs...and they look
        pretty solid this time...and the hallway back to the Antichamber.
        """))
        exit
        choice = input("d for doorway\ns for stairs\nh for hallway\n>>>>> ")
        if choice == 'd':
            print(dedent(f"""
            Dude: \"Those boards over the doorway are on there tight!
            Do you have a tool you could use to remove them?
            Let's look at your toolbelt: {self.player.toolbelt}
            """))
            if 'prybar' in self.player.toolbelt:
                print(dedent(f"""
                Dude: \"Sweet! you have a prybar! 
                Use it to rip those boards out.\"
                """))
                print("""[you use the prybar to tear away the
                boards blocking the darkend doorway. As you 
                pull away the boards, you see inide the doorway
                and see nothing but blackness.\n
                With all the boards now removed, you are able to
                see into the doorway and see a slide just a few
                meters into the entrance]
                """)
                print(dedent(f"Dude: \"Woah, a slide, cool find {self.player.name}!\""))
                print(f"{self.player.name}: \"Rocking, let's do this!\"")
                Engine.get_room(self, 'dungeon')
            else:
                print(dedent(f"""
                Dude: \"Shoot! You don't have anything in your
                toolbelt to remove those boards over the doorway.
                Let's keep exploring to find the right tool!\"
                """))
                DiningRoom.exit_choices(self)
        elif choice == 's':
            print(dedent(f"""
            Dude: \"Thanks for trusting me more on the stairs this time, 
            {self.player.name}, these ones look way better than the last ones.\"
            """))
            Engine.get_room(self, 'aviary')
        elif choice == 'h':
            print(dedent(f"""
            Dude: \"Sounds good to me {self.player.name},
            let's go back to the Antichamber!\"
            """))
            Engine.get_room(self, 'antichamber')
        else:
            print("Dude: \"Are you kidding!?!? We can't go there, try again.\"")
            DiningRoom.exit_choices(self)



# gordian knot around eagle's leg
# need knife to cut free, can't untie
# get inscriptions inside bag
# leaving aviary: only once choice is slide back to Antichamber
# eagle is smarter, rounds numbers 'normally'
# import decimal
# from decimal import Decimal
# use it like so: Decimal('2.555').quantize(Decimal(1'1.00'))
# >>> '2.56'



class Aviary(object):
    room_title = " Entering the Aviary "
    entered = False

    def __init__(self):
        self.room_header = RoomHeader()
        self.artifacts_tools = ArtifactsTools()
        self.player = Player()

    def enter(self):
        print("Entered the Aviary")
        if self.entered == False:
            Aviary.first_entry(self)
        else:
            Aviary.second_entry(self)
            
    def first_entry(self):
        self.entered = True
        print("first entry into Aviary")

    def second_entry(self):
        pass


#Aviary.entered = True



















class Engine(object):

    rooms = {
        'opening': OpeningScene(),
        'antichamber': Antichamber(),
        'collapsedstairwell': CollapsedStairwell(),
        'dungeon': Dungeon(),
        'diningroom': DiningRoom(),
        'aviary': Aviary()
    }

    def get_room(self, room):
        self.room = room
        val = Engine.rooms.get(room)
        val.enter()
    

begin = Engine()
begin.get_room('opening')