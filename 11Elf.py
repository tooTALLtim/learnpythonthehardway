# print("What's your name?", end=' ')
# name = input()
# print(f"\nOh, heya {name}! \nNice to meet you.")

# print("\nHow many pitches do you want to climb today?", end=" ")
# pitches = input()
# print(f"\nOh that's cool, climbing {pitches} today sounds reasonable")

# print("\nWie is das Wetter heute?", end=" ")
# Wetter = input()
# print("Moment, ist {Wetter} heute?")
# print(f"""
# \n\nI hope that you, {name}, can climb {pitches} pitches 
# today in {Wetter} weather!\n\n""")


#print("What's your name?", end=" ")
#name = input()

#a different way to do the above: put the string in the input!
name = input("What's your name? ")
print("\n\tOh, heya {}! \n\tNice to meet you.".format(name))

print("\nHow many pitches do you want to climb today?", end=" ")
print("Oh, and please only type in an integer or I'll break.", end=" ")
pitches = int(input())
print("\n\tOh that's cool, climbing {} pitches today sounds *totally* reasonable".format(pitches))

print("\nWie is das Wetter heute?", end=" ")
Wetter = input()
print("\n\tMoment, ist {} heute?".format(Wetter))

print("""
\n\n\tI hope that you, {}, can climb {} pitches
\ttoday in {} weather!\n\n""".format(name, pitches, Wetter))