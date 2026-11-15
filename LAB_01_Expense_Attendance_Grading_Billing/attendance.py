from validators import get_int, get_name, highest_lowest


def attendance_percentage(present, total):
    return (present / total) * 100


def attendance_status(percentage):
    if percentage >= 75:
        return "Eligible"
    elif percentage >= 60:
        return "Warning"
    else:
        return "Shortage"


def mark_attendance(attendance):
    roll_no = input("Registration/Roll No.: ").strip()

    if not roll_no:
        print("Roll No. cannot be empty.")
        return

    if roll_no in attendance:
        print("Roll No. already exists.")
        return

    name = get_name("Student Name: ")

    total_days = get_int(
        "Total Working Days: ",
        1
    )

    present_days = get_int(
        "Present Days: ",
        0,
        total_days
    )

    percentage = attendance_percentage(
        present_days,
        total_days
    )

    status = attendance_status(percentage)

    attendance[roll_no] = {
        "name": name,
        "total_days": total_days,
        "present_days": present_days,
        "percentage": percentage,
        "status": status
    }

    print("\nAttendance saved successfully!")
    print(f"Roll No.   : {roll_no}")
    print(f"Name       : {name}")
    print(f"Attendance : {percentage:.2f}%")
    print(f"Status     : {status}")


def attendance_summary(attendance):
    if not attendance:
        print("No attendance records available.")
        return

    percentages = []
    total_percentage = 0

    eligible = 0
    warning = 0
    shortage = 0

    print("\n------------- ATTENDANCE SUMMARY -------------")
    print(
        f"{'Roll No.':<12}"
        f"{'Name':<20}"
        f"{'Attendance':<15}"
        f"{'Status'}"
    )
    print("-" * 62)

    for roll_no, student in attendance.items():

        print(
            f"{roll_no:<12}"
            f"{student['name']:<20}"
            f"{student['percentage']:.2f}%"
            f"{'':<9}"
            f"{student['status']}"
        )

        percentages.append(student["percentage"])
        total_percentage += student["percentage"]

        if student["status"] == "Eligible":
            eligible += 1
        elif student["status"] == "Warning":
            warning += 1
        else:
            shortage += 1

    highest, lowest = highest_lowest(percentages)

    average = total_percentage / len(percentages)

    print("\nTotal Students     :", len(attendance))
    print(f"Average Attendance : {average:.2f}%")
    print(f"Highest Attendance : {highest:.2f}%")
    print(f"Lowest Attendance  : {lowest:.2f}%")
    print("Eligible            :", eligible)
    print("Warning             :", warning)
    print("Shortage            :", shortage)


def attendance_menu(attendance):
    while True:
        print("\n--- ATTENDANCE MANAGEMENT ---")
        print("1. Mark Attendance")
        print("2. Attendance Summary")
        print("3. Back")

        choice = get_int("Enter your choice (1-3): ", 1, 3)

        if choice == 1:
            mark_attendance(attendance)

        elif choice == 2:
            attendance_summary(attendance)

        else:
            break