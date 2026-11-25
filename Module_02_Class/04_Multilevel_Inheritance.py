class Animal:
    name = " "

    def eat(self):
        print("I can eat")

class Dog(Animal):

    def display(self):
        #Access name attribute of superclass using self
        print("My name is ", self.name)

class Breed(Dog):
    def prints(self):
        print("This is the breed part")

ob1 = Breed()
ob2 = Dog()
ob2.name = "Guddu"
ob1.prints()
ob2.display()

# create an object of the subclass
labrador = Dog()

#access superclass attribute and method
labrador.name = "Rocky"
labrador.eat()

#call subclass method
labrador.display()

gs = Dog()
gs.name = "Gold"
gs.eat()
gs.display()