from sys import argv
script, input_file = argv

def print_all(placeholder):
    print("Engage function 'print_all' using file = ", placeholder)
    print(placeholder.read())
    print("Ending 'print_all' sequence of file = ", placeholder)

def rewind(placeholder):
    print("\nNow let's rewind, much like the olden days when they used tapes!")
    placeholder.seek(0)
    print("<<<<<<rewound tape>>>>>>\n")

def print_a_line(line_count, placeholder):
    print(line_count, placeholder.readline())


current_file = open(input_file)


print_all(current_file)

rewind(current_file)

print("Now let's print just three lines:\n")
current_line = 1
# this will print the first line in the file
print_a_line(current_line, current_file)

# the symbols '+=' are a contraction! it is 'x = x + y' shortened into 'x += y'
current_line += 1
# this will print the second line because THAT'S WHERE THE POINTER IS!
print_a_line(current_line, current_file)

current_line += 1
# same as above, it'll print line 3 only because that's where the pointer is
# the 'curent_line' variable has NO EFFECT on what line is being printed
# it just happens to be where the pointer stops
print_a_line(current_line, current_file)

print("\nThat's all, folks!\n")