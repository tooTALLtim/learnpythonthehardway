def add(a, b):
    print(f"Adding {a} and {b}.")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} from {b}.")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}.")
    return a * b

def divide(a, b):
    print(f"Dividing {a} from {b}.")
    return a / b

print("Lets play with some numbers!")
result = ("That returns >>>")

chocolate = int(input("How much chocolate do you want to eat? Numbers only please >>> "))
flowers = int(input("How many flowers are on the table? Numbers only please >>> "))

print("Now we add chocolate and flowers together.")
print(result, add(chocolate, flowers))



# original lesson
# def add(a, b):
#     print(f"Adding {a} and {b}.")
#     return a + b

# def subtract(a, b):
#     print(f"Subtracting {a} from {b}.")
#     return a - b

# def multiply(a, b):
#     print(f"Multiplying {a} and {b}.")
#     return a * b

# def divide(a, b):
#     print(f"Dividing {a} from {b}.")
#     return a / b

# print("Lets play with some numbers!")
# result = ("That returns >>>")

# age = add(30, 9)
# print(result, age)

# height = subtract(200, 2)
# print(result, height)

# weight = multiply(90, 2)
# print(result, weight)

# iq = divide(51, 3)
# print(result, iq)

# print("Here's some extra credit for funsies.")

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print("That becomes", what, "I should be able to do this by hand.")