# from sys import argv
# script, first, second, third = argv

# print("The script is called: ", script)
# print("The first variable is called: ", first)
# print("The second variable I see is: ", second)
# print("And finally, the third one I got is: ", third)


# from sys import argv
# filename, codeword01, codeword02 = argv

# print(f"Hello World! The name of the code I'm running is >>> {filename}")
# print("The first codeword you entered is >>> {}".format(codeword01))
# print((f"The second codeword you entered is >>> {codeword02}"))
# print("That's all for now, thanks to >>> {}".format(filename))


from sys import argv
fn, ui1, ui2, ui3, ui4 = argv

print("Heya fellow human! I'm running the program \n\t>>> {}".format(fn))
print(f"\nThat's pretty neat, huh? Ok, the first thing you typed was\n\t>>> {ui1}")
print("\nDon't know why you wanted me to know {}, but ok. Second thing was \n\t>>> {}".format(ui1, ui2))
print(f"\nOh really, gotcha! The third and fourth things you typed were \n\t>>> {ui3} \n\t>>> {ui4}")
print(f"""\n\n
    Great! So we're running program
    >>> {fn}
    and the inputs you gave me were:
    >>> {ui1}
    >>> {ui2}
    >>> {ui3}
    >>> {ui4}
""")

finalanswer = input("And of the four things you typed, what was your favourite? >>> ")
print(f"Really, did you even type {finalanswer} in last time?!?!? You goof :P")