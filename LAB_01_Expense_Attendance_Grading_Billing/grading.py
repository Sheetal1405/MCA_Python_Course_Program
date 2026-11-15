from validators import get_float, get_int, get_name, highest_lowest

SUBJECTS = ("Python", "DBMS", "DSA", "AI", "ML")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"


def calculate_result(marks):
    for mark in marks:
        if mark < 35:
            return "FAIL"

    return "PASS"


def add_student_marks(students):
    roll_no = input("Registration/Roll No.: ").strip()

    if not roll_no:
        print("Roll No. cannot be empty.")
        return

    if roll_no in students:
        print("Roll No. already exists.")
        return

    name = get_name("Student Name: ")

    print("\nEnter marks for:")

    # map() is used for input as required
    while True:
        try:
            marks = list(
                map(float, input(
                    "Python DBMS DSA AI ML: "
                ).split())
            )

            if len(marks) != len(SUBJECTS):
                raise ValueError

            valid = True

            for mark in marks:
                if mark < 0 or mark > 100:
                    valid = False
                    break

            if not valid:
                raise ValueError

            break

        except ValueError:
            print("Enter exactly 5 marks between 0 and 100.")

    subject_marks = dict(
        zip(SUBJECTS, marks)
    )

    total = 0

    for mark in marks:
        total += mark

    average = total / len(SUBJECTS)
    percentage = average

    result = calculate_result(marks)

    if result == "FAIL":
        final_grade = "F"
    else:
        final_grade = calculate_grade(percentage)

    students[roll_no] = {
        "name": name,
        "marks": subject_marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": final_grade,
        "result": result
    }

    highest, lowest = highest_lowest(marks)

    print("\nStudent marks saved successfully!")
    print(f"Roll No.             : {roll_no}")
    print(f"Name                 : {name}")
    print(f"Total                : {total:.2f}/500")
    print(f"Average              : {average:.2f}")
    print(f"Percentage           : {percentage:.2f}%")
    print(f"Grade                : {final_grade}")
    print(f"Result               : {result}")
    print(f"Highest Subject Mark : {highest:.2f}")
    print(f"Lowest Subject Mark  : {lowest:.2f}")


def generate_report_card(students):
    if not students:
        print("No student records available.")
        return

    roll_no = input("Enter Registration/Roll No.: ").strip()

    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]

    print("\n============ REPORT CARD ============")
    print(f"Roll No. : {roll_no}")
    print(f"Student  : {student['name']}")
    print("-------------------------------------")
    print(f"{'Subject':<15}{'Marks':>8}")
    print("-------------------------------------")

    for subject, mark in student["marks"].items():
        print(f"{subject:<15}{mark:>8.2f}")

    print("-------------------------------------")

    marks = list(student["marks"].values())
    highest, lowest = highest_lowest(marks)

    print(f"Total       : {student['total']:.2f} / 500")
    print(f"Average     : {student['average']:.2f}")
    print(f"Percentage  : {student['percentage']:.2f}%")
    print(f"Grade       : {student['grade']}")
    print(f"Result      : {student['result']}")
    print(f"Highest Mark: {highest:.2f}")
    print(f"Lowest Mark : {lowest:.2f}")
    print("=====================================")


def class_summary(students):
    if not students:
        print("No student records available.")
        return

    percentages = []
    total_percentage = 0
    pass_count = 0
    fail_count = 0

    topper_roll = ""
    topper_name = ""
    topper_percentage = -1

    print("\n------------- CLASS SUMMARY -------------")

    print(
        f"{'Roll No.':<12}"
        f"{'Name':<20}"
        f"{'Percentage':<15}"
        f"{'Grade':<8}"
        f"{'Result'}"
    )

    print("-" * 70)

    for roll_no, student in students.items():

        print(
            f"{roll_no:<12}"
            f"{student['name']:<20}"
            f"{student['percentage']:.2f}%"
            f"{'':<9}"
            f"{student['grade']:<8}"
            f"{student['result']}"
        )

        percentages.append(student["percentage"])
        total_percentage += student["percentage"]

        if student["result"] == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        if student["percentage"] > topper_percentage:
            topper_percentage = student["percentage"]
            topper_roll = roll_no
            topper_name = student["name"]

    highest, lowest = highest_lowest(percentages)

    class_average = total_percentage / len(students)

    print("\nClass Average : {:.2f}%".format(class_average))
    print(f"Highest       : {highest:.2f}%")
    print(f"Lowest        : {lowest:.2f}%")
    print(
        f"Topper        : {topper_name} "
        f"({topper_roll}) - {topper_percentage:.2f}%"
    )
    print(f"Pass Count    : {pass_count}")
    print(f"Fail Count    : {fail_count}")


def grading_menu(students):
    while True:
        print("\n--- GRADING SYSTEM ---")
        print("1. Add Student Marks")
        print("2. Student Report Card")
        print("3. Class Summary")
        print("4. Back")

        choice = get_int("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            add_student_marks(students)

        elif choice == 2:
            generate_report_card(students)

        elif choice == 3:
            class_summary(students)

        else:
            break