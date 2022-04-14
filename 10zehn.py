# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split \non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """

# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

print("Here's a backslash \\")
print("Here's a \' single and duoble \" quote")

print("\nWhat the hells is ASCII bell? '\\a' \a It's right here.")
print("Oh, bell makes a noise! Was used to tell of incoming messages.")
print("Think of it as \'audible\' or \"alert\".")

print("\nOk let's mess with \'\\b' backspace.")
print("Will backspace remove a character? 012\b345.")
print("Yep! I put it between the '2' and '3' and it removed the '2'.")

print("\nOk, time for a form feed '\\f', whatdaya say? Before\f After ")
print("""
    What did that do? Oooh, interesting. It printed the text
    on a new line, but it printed it in the same position
    as if the page break

""")

print("\nOnto line feed '\\n'.")
print("I \ncan \nput \nthese \non \ntheir \nown \nlines!")

print("\nNext up, Unicode named character in the database.")
print("That looks like this \'\\N{name}\'")
print("Let's try 'LEFT CURLY BRACKET' \n\N{LEFT CURLY BRACKET}")

print("\nIs a carriage return '\\r' right there.")
print("Does it split \r this sentence?")
print("\rHmm, just deleted everything in front of it.")
print("Let's figure out what this really does later.")

print("\n\tThis is a horizontal tab '\\t'.")
print("\t\t\t'\\t\\t\\t'Does this tab three times? Sure does!")
print("(\t*3)How about '\\t*3'? Nope, that doesn't work.")
print("\vAnd this is a vertical tab! '\\v'")
print("That vertical tab just looks like a line feed (new line).")

print("\nThat's good for now :D")