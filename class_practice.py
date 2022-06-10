"""Playing around with modifying variables and dictionaries in classes"""

class Car(object):

    specs = {
        'tires': 'OEM',
        'engine': 'OEM',
        'color': 'OEM'
    }

    model = None

coche = Car()
print(coche.specs['tires'])
coche.specs['tires'] = 'snow tires'
print(coche.specs['tires'])

class Choose_Car(Car):

    def modify_dict(self):
        print("choosey")
        print("currently the car's color is:", Car.specs['color'])
        Car.specs['color'] = input("what color do you want?\n>>> ")
        print("sweet, now your car is:", Car.specs['color'])
    
    def var(self):
        print("Currently the car model is:", Car.model)
        Car.model = input("Oh, and what model is your dream car?\n>>>")
        print(f"Ok, now the car model is {Car.model}")


my_car = Choose_Car()
my_car.modify_dict()
my_car.var()
print(Car.specs['color'])
print(Car.model)

class Leaf(object):

    leaf = "default"


class Flower(object):

    flower = "default"


class Plant(Leaf, Flower):

    def __init__(self, leaf, flower):
        self.leaf = leaf
        self.flower = flower

daffodil = Plant('round', 'yellow')
print(daffodil.leaf)
print(daffodil.flower)

the_leaf = Leaf()
print(the_leaf.leaf)