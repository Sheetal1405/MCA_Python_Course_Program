#Single Inheritance
class Animal:
    name = " "

    def eat(self):
        print("I can eat")

class Dog(Animal):

    def display(self):
        #Access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

#access superclass attribute and method
labrador.name = "Rocky"
labrador.eat()

#call subclass method
labrador.display()

gs = Animal()
gs.name = "Gold"
gs.eat()
#gs.display()