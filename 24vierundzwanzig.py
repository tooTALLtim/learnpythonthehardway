print("Let's practice everything")
print('You\'d need to know \'bout escapes using \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""

print("-" * 10)
print(poem)
print("-" * 10)


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def bean_counter(placeholder0):
    placeholder1 = placeholder0 * 500
    placeholder2 = placeholder1 / 1000
    placeholder3 = placeholder2 / 100
    return placeholder1, placeholder2, placeholder3


start_point = 10000
print("I'm starting off with 10,000 beans.")
beans, jars, crates = bean_counter(start_point)

#this might be my favourite way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"I have {beans} beans, {jars} jars, and {crates} crates.")

your_beans = int(input("How many beans do you have? Whole numbers only, please: "))

formula = bean_counter(your_beans)
#this is an easier way to to apply a list to format a string!!
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


# print("Let's practice everything")
# print('You\'d need to know \'bout escapes using \\ that do:')
# print('\n newlines and \t tabs.')

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires and explanation
# \n\twhere there is none.
# """

# print("-" * 10)
# print(poem)
# print("-" * 10)


# five = 10 - 2 + 3 - 6
# print(f"This should be five: {five}")

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates


# start_point = 10000
# beans, jars, crates = secret_formula(start_point)

# #this might be my favourite way to format a string
# print("With a starting point of: {}".format(start_point))
# #it's just like with an f"" string
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# start_point = start_point / 10

# print("We can also do that this way:")
# formula = secret_formula(start_point)
# #this is an easy way to to apply a list to format a string
# print("We'd have {} beans, {} jars, and {} crates.".format(*formula))