from validators import get_int, get_float, highest_lowest

CATEGORIES = ("Food", "Travel", "Utilities", "Stationery", "Other")


def add_expense(expenses):
    description = input("Description: ").strip()

    amount = get_float(
        "Amount: ",
        0.01
    )

    print("\nCategories")
    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")

    choice = get_int(
        "Category: ",
        1,
        len(CATEGORIES)
    )

    category = CATEGORIES[choice - 1]

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

    print("Expense saved successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expense records available.")
        return

    print("\n---------------- EXPENSES ----------------")
    print(f"{'Description':<20}{'Category':<15}{'Amount':>12}")
    print("-" * 47)

    for expense in expenses:
        print(
            f"{expense['description']:<20}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:>10.2f}"
        )


def expense_summary(expenses):
    if not expenses:
        print("No expense records available.")
        return

    total = 0
    amounts = []

    category_totals = {
        category: 0
        for category in CATEGORIES
    }

    for expense in expenses:
        amount = expense["amount"]

        total += amount
        amounts.append(amount)

        category_totals[expense["category"]] += amount

    highest, lowest = highest_lowest(amounts)

    print("\n------------- EXPENSE SUMMARY -------------")

    for category in CATEGORIES:
        print(
            f"{category:<15}: "
            f"₹{category_totals[category]:.2f}"
        )

    print("-" * 42)
    print(f"{'Grand Total':<15}: ₹{total:.2f}")
    print(f"Highest Expense : ₹{highest:.2f}")
    print(f"Lowest Expense  : ₹{lowest:.2f}")


def expense_menu(expenses):
    while True:
        print("\n--- EXPENSE MANAGEMENT ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Summary")
        print("4. Back")

        choice = get_int("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            add_expense(expenses)

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            expense_summary(expenses)

        else:
            break