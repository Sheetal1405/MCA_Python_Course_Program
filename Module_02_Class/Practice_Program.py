# Create a class name Smart Calculator with 4 versions of fuctions name calculate(). We will create a class with one method only.
# Method 1 with 1 argument and find square of number
# Method 2 with 2 arguments and addition of 2 numbers
# Method 3 with 3 arguments and multiplication of 3 numbers
# Method 4 with 4 arguents and find average of 4 numbers

class SmartCalculator:

    def calculate(self, a, b = None, c = None, d = None):

        if b is None:
            return a*a

        elif c is None:
            return a+b

        elif d is None:
            return a*b*c

        else:
            return (a+b+c+d)/4

#Creating an object
calc = SmartCalculator()
#Calling the method with different numbers of arguments
print(calc.calculate(10))
print(calc.calculate(20, 40))
print(calc.calculate(3, 5, 4))
print(calc.calculate(14, 16, 18 ,20))