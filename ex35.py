from sys import exit

def gold_room():
    print("This room is full of gold, how much do you take?")

    choice = input(">>> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("geeze, learn to type a number...")

    if how_much < 50:
        print("Not too greedy, you win!!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear is happily eating some honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">>> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("Now you've pissed off the bear and they chew your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("What did you just say?!?!?")


def cthulhu_room():
    print("Here you meet the great and evil Cthulhu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">>> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("MMMM, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Too bad, try again!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which door do you take?")
    
    choice = input(">>> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("That wasn't a choice! You wander around and starve.")


start()