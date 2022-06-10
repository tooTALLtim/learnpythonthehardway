"Playing with dictionaries"

spells = {
    'Accio': 'Summon an object',
    'Mobilicorpus': 'Levitate and move bodies',
    'Impedimenta': 'Slows or stops target',
    'Relashio': 'Forces target to release its grip',
    'Sectumsempra': 'To slash or cut with invisible sword'
}

def read_spells():
    print("Here's a list of the spells we have:")
    for name, description in list(spells.items()):
        print(f"The spell {name} will do the action: {description}.")

def Spellcasting():
    request = input("Which spell would you like to cast?\n>>>>> ")
    if request == 'Sectumsempra':
        raise Exception("Oh, that's a bad one, don't use that one.")
    elif request in spells:
        print("Ah, found it here, casting!")
        print("Effect:", spells[request])
    else:
        print("Sorry, I can't find that spell...")
        Spellcasting()


def add_spell():
    print("Now let's add a spell to the dictionary.")
    spell_name = input("What's the name of your spell?\n>>>>> ")
    spell_description = input("And what does your spell do?\n>>>>> ")
    print("Cool! Adding that to the dictionary...")
    spells[spell_name] = spell_description
    print("The new list of spells are")
    read_spells()

read_spells()
Spellcasting()
add_spell()

nested_dict = {
    1: 'forces',
    2: 'poop',
    3: {'eins': 'mutter', 'zwei': 'poop'}
}

print(nested_dict)
print(nested_dict[1])
print(nested_dict[3]['zwei'])


# # create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

# # create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Fransisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# # print out some cities
# print("-" * 10)
# print(cities['NY'], " is in New York.")
# print(cities['OR'], " is in Oregon.")

# # print some states
# print("-" * 10)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abbreviation is: ", states['Florida'])

# # do it by using the states then cities dictionary
# print("-" * 10)
# print("In the state of Michigan you'll find the city ", cities[states['Michigan']])
# print("And in the state of Florida you'll find the city ", cities[states['Florida']])

# # print every state abbreviation
# print("-" * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated {abbrev}")

# # print every city in state
# print("-" * 10)
# for abbrev, city in list(cities.items()):
#     print(f"{abbrev} has the city {city}")

# # now do both at the same time
# print("-" * 10)
# for state, abbrev in list(states.items()):
#     print(f"The state {state} is abbreviated as {abbrev}")
#     print(f"And has a city in it named {cities[abbrev]}.")

# print("-" * 10)
# # safely get an abbreviation by a state that might not be there
# state = states.get('Texas')

# if not state:
#     print("Sorry, no Texas.")

# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print(f"The city for the state \'TX\' is: {city}")