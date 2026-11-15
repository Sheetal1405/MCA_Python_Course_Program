#Complete this grade assigner
marks = int(input("Marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
     grade = "C"
elif marks >= 60:
     grade = "D"
else:
    grade = "F"

print("Grade: ", grade)

#Test: marks=95 -> A, marks = 75-> B, marks = 50 -> F
