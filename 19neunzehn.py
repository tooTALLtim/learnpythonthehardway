def chips_and_salsa(chip_bags, salsa_jars):
    print(f"I have {chip_bags} bags of chips!")
    print(f"I also have {salsa_jars} jars of salsa.")
    print("Boy howdy! Let's call up the friends!\nGames and snacks tonight!\n")

print("I can just give the arguments values directly in the parantheses like this:")
chips_and_salsa(30, 40)

print("Or I can define them as simple variables:")
chips_en_casa = 2
salsa_en_casa = 4
chips_and_salsa(chips_en_casa, salsa_en_casa)

print("I could ask you how many you have:")
usr_chips = input("How many bags of chips do you have? >>> ")
usr_salsa = input("And how many jars of salsa? >>> ")
chips_and_salsa(usr_chips, usr_salsa)

print("Oooh, let's add some maths. Tell me how many you have and I'll add it to the number I have en casa.")
print("Numbers only or I'll break!")
usr_chips = int(input("How many bags of chips do you have? >>> "))
usr_salsa = int(input("And how many jars of salsa? >>> "))
chips_and_salsa(usr_chips + chips_en_casa, usr_salsa + salsa_en_casa)