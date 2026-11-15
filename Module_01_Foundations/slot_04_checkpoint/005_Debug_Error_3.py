#BROKEN - runs without crashing, but gives the WRONG answer
Math = int(input("Math Marks: "))
English = int(input("English Marks: "))
Science = int(input("Science Marks: "))
Average = (Math + English) / 3 #Wrong! Should include Science
print(Average)

#FIXED
Average = (Math+English+Science)/3
print(Average)