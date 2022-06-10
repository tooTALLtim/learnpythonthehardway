def is_a_number(x):
    try:
        int(x) == True
        print("That's an integer!")
    except ValueError:
        print("That ain't an integer! Try again...")

x = input("Bat: \"Ok, gimme an integer, no decimal points\"\n>>>>> ")
is_a_number(x)