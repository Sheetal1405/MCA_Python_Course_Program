from validators import get_int
from expenses import expense_menu
from attendance import attendance_menu
from grading import grading_menu
from billing import billing_menu
from reports import reports


def display_menu():
    print("\n" + "=" * 55)
    print("INTEGRATED EXPENSE | ATTENDANCE | GRADING | BILLING")
    print("=" * 55)

    print("Name    : Sheetal")
    print("Class   : MCA AI & ML")
    print("Roll No.: 2601940062")

    print("-" * 55)
    print("1. Expense Management")
    print("2. Attendance Management")
    print("3. Grading System")
    print("4. Billing System")
    print("5. View Reports")
    print("6. Exit")
    print("-" * 55)


def main():
    expenses = []
    attendance = {}
    students = {}
    bills = []

    while True:
        display_menu()

        choice = get_int(
            "Enter your choice (1-6): ",
            1,
            6
        )

        if choice == 1:
            expense_menu(expenses)

        elif choice == 2:
            attendance_menu(attendance)

        elif choice == 3:
            grading_menu(students)

        elif choice == 4:
            billing_menu(bills)

        elif choice == 5:
            reports(
                expenses,
                attendance,
                students,
                bills
            )

        else:
            print("\nThank you for using the system. Goodbye!")
            break


try:
    main()

except KeyboardInterrupt:
    print("\n\nProgram stopped safely.")

finally:
    print("Program execution completed.")