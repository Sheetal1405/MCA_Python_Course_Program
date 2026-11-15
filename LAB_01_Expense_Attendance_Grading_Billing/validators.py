def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = eval(input(prompt))

            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError

            if min_val is not None and value < min_val:
                raise ValueError

            if max_val is not None and value > max_val:
                raise ValueError

            return value

        except (ValueError, SyntaxError, NameError, TypeError):
            print("Invalid input. Enter a valid whole number.")


def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = eval(input(prompt))

            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError

            value = float(value)

            if min_val is not None and value < min_val:
                raise ValueError

            if max_val is not None and value > max_val:
                raise ValueError

            return value

        except (ValueError, SyntaxError, NameError, TypeError):
            print("Invalid input. Enter a valid number.")


def get_name(prompt):
    while True:
        name = input(prompt).strip()

        if (
            2 <= len(name) <= 40
            and all(c.isalpha() or c.isspace() for c in name)
        ):
            return name

        print("Name must contain 2-40 letters.")


def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip()

        if choice in options:
            return choice

        print("Choose a valid option.")


def highest_lowest(values):
    highest = values[0]
    lowest = values[0]

    for value in values:
        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

    return highest, lowest