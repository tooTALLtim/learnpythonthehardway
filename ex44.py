class Parent(object):

    def override(self):
        print("Parent override!")
    
    def implicit(self):
        print("Parent implicit!")

    def altered(self):
        print("Parent altered!")
    

class Child(Parent):

    def override(self):
        print("Child override!")
    
    def altered(self):
        print("Child before LSD")
        super(Child, self).altered()
        print("Child after LSD")

mom = Parent()
daughter = Child()

mom.implicit()
daughter.implicit()

mom.override()
daughter.override()

mom.altered()
daughter.altered()
