age_input = input("Enter your age:")
print(type(age_input))

#TYPE_ERROR: print(age_input + 1)

age = int(age_input)
print(type(age))

print(age + 1)   #works now that it's an int