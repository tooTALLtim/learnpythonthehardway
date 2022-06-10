siblings = ['sarah', 'rebecca', 'zach']
# for each element (let's call it i) in siblings:
# could better say: for each element in 'siblings' assign them to 'i'
for i in siblings: 
    print(f"Tim\'s siblings are: {i}")
    print()

print("What does Tim like to do?")
likes = ['climbing', 'Jasmyn', 'chocolate', 42, 'MTB', 'pooping', 'sunshine']
for i in likes:
    print(i, end=' ')
print()

# the range function doesn't like things that aren't integers, the below doesn't work
print("OK, what are Tim's top three favourite things?")
print(likes[0])
print(likes[1])
print(likes[2])
print()

print("Let's do some simple counting!")
for i in range (10):
    print(i, end='')
print()
print("""Notice how that started at zero when I didn't specify a starting point
and only printed out ten integers when given a range of \'10\'.
""")

print("Let's count from 14 to 88 by 4\'s:")
for i in range(14, 88, 4):
    print(i, end=' ')
print()

print("can we count by less than an integer?")
for i in range(40, 100, 5):
    print(i)
print("Hell no!")

elements = []
print(f"Let's start with an empty list: {elements}.")
print("And use the append function to add things to it.")
for i in range (0, 6):
    print(f"Adding {i} to the list.")
    # append is a function lists understand
    elements.append(i)
print(f"And now the list containts: {elements}")

print("And for a finale, let's add two lists together!")
print(f"Here's how the list \'siblings\' begins: {siblings}")
siblings.append(likes)
siblings.append(elements)
print("And here it is now!", siblings)


# lpthw exercise
# the_count = [1, 2, 3, 4, 5]
# fruits = ["apples", "oranges", "pears", "apricots"]
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print(f"This is the count {number}")

# # same a above
# for fruits in fruits:
#     print(f"A fruit of type: {fruits}")

# # can also go through mixed lists
# for i in change:
#     print(f"I got {i}")

# # we can also build lists, let's start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range (0, 6):
#     print(f"Adding {i} to the list.")
#     # append is a function lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print(f"Element was: {i}")


# Geek to Geek practice
# for i in range (0, 10):
#     print(i, end=" ")
# print()

# l = [10, 20, 30, 40, 50]
# for i in range(len(l)):
#     print(l[i], end=" ")
# print()

# # will print out even numbers between 8 and 15
# for i in range(8, 15, 2):
#         print(i)