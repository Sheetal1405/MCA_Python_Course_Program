#Create 5 variables and print each with its type
my_name = input("Enter your name:")
my_age = int(input("Enter your age:"))
my_city = input("Enter your city:")
my_height = input("Enter your height:")
is_employed = bool(input("Enter your Employment status:"))  #False

print(my_name, my_age, my_city,my_height, is_employed)
print(type(my_name), type(my_age), type(my_city), type(my_height) , type(is_employed))