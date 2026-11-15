from validators import get_float, get_int, get_name, highest_lowest


TAX_RATE = 18


def calculate_discount(subtotal):
    if subtotal < 1000:
        return 0
    elif subtotal < 5000:
        return 5
    elif subtotal < 10000:
        return 10
    else:
        return 15


def calculate_tax(taxable_amount):
    return taxable_amount * TAX_RATE / 100


def generate_invoice(bills):
    customer = get_name("Customer Name: ")

    items = []

    while True:
        data = input(
            "Item, Unit Price, Quantity (type done to finish): "
        ).strip()

        if data.lower() == "done":
            break

        try:
            # map() is used to split and clean input
            item, price, quantity = map(
                str.strip,
                data.split(",")
            )

            # eval() is used as required
            price = eval(price)
            quantity = eval(quantity)

            if (
                isinstance(price, bool)
                or not isinstance(price, (int, float))
                or price <= 0
            ):
                raise ValueError

            if (
                isinstance(quantity, bool)
                or not isinstance(quantity, int)
                or quantity < 1
            ):
                raise ValueError

            line_total = price * quantity

            items.append({
                "name": item,
                "price": float(price),
                "quantity": quantity,
                "total": line_total
            })

        except (ValueError, SyntaxError, NameError, TypeError):
            print("Example: Notebook, 45.00, 10")

    if not items:
        print("No items added.")
        return

    subtotal = 0
    item_totals = []

    for item in items:
        subtotal += item["total"]
        item_totals.append(item["total"])

    discount_rate = calculate_discount(subtotal)

    discount_amount = (
        subtotal * discount_rate / 100
    )

    taxable_amount = subtotal - discount_amount

    tax_amount = calculate_tax(taxable_amount)

    grand_total = taxable_amount + tax_amount

    highest, lowest = highest_lowest(item_totals)

    bill_no = f"B-{len(bills) + 1:04d}"

    bill = {
        "bill_no": bill_no,
        "customer": customer,
        "items": items,
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "taxable_amount": taxable_amount,
        "tax_amount": tax_amount,
        "grand_total": grand_total
    }

    bills.append(bill)

    print("\n================ INVOICE ================")
    print(f"Bill No.  : {bill_no}")
    print(f"Customer  : {customer}")
    print("-----------------------------------------")
    print(
        f"{'Item':<18}"
        f"{'Price':>10}"
        f"{'Qty':>6}"
        f"{'Total':>12}"
    )
    print("-----------------------------------------")

    for item in items:
        print(
            f"{item['name']:<18}"
            f"₹{item['price']:>8.2f}"
            f"{item['quantity']:>6}"
            f"₹{item['total']:>10.2f}"
        )

    print("-----------------------------------------")
    print(f"Subtotal          : ₹{subtotal:.2f}")
    print(
        f"Discount ({discount_rate}%)"
        f"       : -₹{discount_amount:.2f}"
    )
    print(f"Taxable Amount    : ₹{taxable_amount:.2f}")
    print(f"Tax (18%)         : ₹{tax_amount:.2f}")
    print(f"GRAND TOTAL       : ₹{grand_total:.2f}")
    print(f"Highest Item      : ₹{highest:.2f}")
    print(f"Lowest Item       : ₹{lowest:.2f}")
    print("=========================================")
    print("Thank you for your purchase!")


def view_last_bill(bills):
    if not bills:
        print("No billing records available.")
        return

    bill = bills[-1]

    print("\n--------------- LAST BILL ---------------")
    print(f"Bill No. : {bill['bill_no']}")
    print(f"Customer : {bill['customer']}")

    for item in bill["items"]:
        print(
            f"{item['name']:<18}"
            f"₹{item['price']:>8.2f}"
            f"{item['quantity']:>6}"
            f"₹{item['total']:>10.2f}"
        )

    print(f"\nSubtotal       : ₹{bill['subtotal']:.2f}")
    print(
        f"Discount       : ₹{bill['discount_amount']:.2f}"
    )
    print(
        f"Taxable Amount : ₹{bill['taxable_amount']:.2f}"
    )
    print(f"Tax            : ₹{bill['tax_amount']:.2f}")
    print(f"Grand Total    : ₹{bill['grand_total']:.2f}")


def billing_summary(bills):
    if not bills:
        print("No billing records available.")
        return

    totals = []
    total_sales = 0

    for bill in bills:
        totals.append(bill["grand_total"])
        total_sales += bill["grand_total"]

    highest, lowest = highest_lowest(totals)

    print("\n------------- BILLING SUMMARY -------------")
    print(f"Total Bills  : {len(bills)}")
    print(f"Total Sales  : ₹{total_sales:.2f}")
    print(
        f"Average Bill : ₹{total_sales / len(bills):.2f}"
    )
    print(f"Highest Bill : ₹{highest:.2f}")
    print(f"Lowest Bill  : ₹{lowest:.2f}")


def billing_menu(bills):
    while True:
        print("\n--- BILLING SYSTEM ---")
        print("1. Create Bill")
        print("2. View Last Bill")
        print("3. Billing Summary")
        print("4. Back")

        choice = get_int("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            generate_invoice(bills)

        elif choice == 2:
            view_last_bill(bills)

        elif choice == 3:
            billing_summary(bills)

        else:
            break