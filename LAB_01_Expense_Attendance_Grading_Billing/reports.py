from validators import highest_lowest


def reports(expenses, attendance, students, bills):
    print("\n" + "=" * 55)
    print("                    REPORTS")
    print("=" * 55)

    # Expense Report
    print("\n--- EXPENSE REPORT ---")

    if expenses:
        amounts = []

        for expense in expenses:
            amounts.append(expense["amount"])

        total = 0

        for amount in amounts:
            total += amount

        highest, lowest = highest_lowest(amounts)

        print(f"Total Expense   : ₹{total:.2f}")
        print(f"Highest Expense : ₹{highest:.2f}")
        print(f"Lowest Expense  : ₹{lowest:.2f}")
    else:
        print("No expense records available.")

    # Attendance Report
    print("\n--- ATTENDANCE REPORT ---")

    if attendance:
        percentages = []

        for student in attendance.values():
            percentages.append(student["percentage"])

        highest, lowest = highest_lowest(percentages)

        print(f"Highest Attendance : {highest:.2f}%")
        print(f"Lowest Attendance  : {lowest:.2f}%")
    else:
        print("No attendance records available.")

    # Grading Report
    print("\n--- GRADING REPORT ---")

    if students:
        percentages = []

        for student in students.values():
            percentages.append(student["percentage"])

        highest, lowest = highest_lowest(percentages)

        print(f"Highest Percentage : {highest:.2f}%")
        print(f"Lowest Percentage  : {lowest:.2f}%")
    else:
        print("No grading records available.")

    # Billing Report
    print("\n--- BILLING REPORT ---")

    if bills:
        totals = []

        for bill in bills:
            totals.append(bill["grand_total"])

        highest, lowest = highest_lowest(totals)

        print(f"Highest Bill : ₹{highest:.2f}")
        print(f"Lowest Bill  : ₹{lowest:.2f}")
    else:
        print("No billing records available.")