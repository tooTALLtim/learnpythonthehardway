

def naming(var):
    print(f"Dude: \"Hmmm, \'{var}\' sure is an odd name, never heard that one before.\"")
    var = list(var)
    var = var[:3]
    var = ''.join([str(item) for item in var])
    print(f"Dude: \"I'll just call you \'{var}\' for short since we're now friends.\"")

naming(input("Dude: \"And adventurer, what should I call you?\"\n>>>>> "))



# def split(var):
#     return list(var)

# full_name = input("Dude: \"And adventurer, what should I call you?\"\n>>>>> ")
# broken_name = split(full_name)
# print("Hmmm, {} is sure an odd name, never heard that before.".format(broken_name))

# print("Let's shorten that down to the first three letters: ")

# nickname = broken_name[:3]
# name = ''.join([str(item) for item in nickname])
# print(f"Ah, {name}, that sounds a lot better!")