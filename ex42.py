class Climb(object):

    def __init__(self, name, grade, stars, pitches):
        self.name = name
        self.grade = grade
        self.stars = stars
        self.pitches = pitches
    
    def output(self, thingy):
        self.thingy = thingy
        print(thingy)



yellow_spur = Climb("yellow spur", "5.9", "****", "6 pitches")
print("The Yellow Spur is ", yellow_spur.grade, "and is a", yellow_spur.stars, "star route.")


naked_edge = {
    'name': 'The Naked Edge', 
    'grade': '5.11b', 
    'stars': '****', 
    'pitches': 'five pitches'
}

class RouteReader(object):

    def __init__(self):
        pass

    def read(self, route):
        self.route = route
        print(route)
    
    def just_pitches(self, pitches):
        self.pitches = pitches
        print(pitches["pitches"])

obj = RouteReader()
print(obj.read(naked_edge))
print(obj.just_pitches(naked_edge))


# the_edge = Climb(naked_edge[0], naked_edge[1], naked_edge[2], naked_edge[3], naked_edge[4])
# print(the_edge)



# # class Animal is-an object
# class Animal(object):
#     pass

# # class Dog is-an Animal
# class Dog(Animal):

#     def __init__(self, name):
#         # class Dog has-an attribute __init__ 
#         self.name = name

# # class Cat is-an Animal
# class Cat(Animal):

#     def __init__(self, name):
#         # class Cat has-a __init_ that takes self and name parameters
#         self.name = name

# # class Person is-an object
# class Person(object):

#     def __init__(self, name):
#         # class Person has a __init__ and also an attribute name
#         self.name= name

#         # Person has-a pet of some kind
#         self.pet = None

# # class Employee is-a Person
# class Employee(Person):

#     def __init__(self, name, salary):
#         # hmm, it's taking the class that it's in, Employee, and calling the __init__ using the name parameter
#         super(Employee, self).__init__(name)
#         # attribute
#         self.salary = salary

# # class Fish is-an object 
# class Fish(object):
#     pass

# # class Salmon is a Fish 
# class Salmon(Fish):
#     pass

# # class Halibut is a Fish
# class Halibut(Fish):
#     pass


# # rover is a Dog
# rover = Dog("rover")

# # satan is a Cat
# satan = Cat("satan")

# # Mary is a person
# mary = Person("Mary")

# # mary has a pet satan who is a Cat
# mary.pet = satan

# # frank is-a Employee with attributes for name and salary
# frank = Employee("Frank", 120000)

# # frank has a pet that is a rover
# frank.pet = rover

# # flipper is a Fish 
# flipper = Fish()

# # a crouse is a Salmon
# crouse = Salmon()

# #harry is a Halibut
# harry = Halibut()