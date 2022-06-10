# first way
a = "left side"
b = "right side"
print(a + b)
print(a, b)


# second way
c = "chocolate"
print(f"What do you like to eat? {c}")


#third way
d = 10000
e = f"How many chocolate bars? {d}"
print(e)


#fourth way
statement = "There is no path to Happiness, {}"
answer = "Happiness is the Path."
print(statement.format(answer))