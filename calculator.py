print("==calculator==")


while True:
    a = float(input("nilai a: "))
    b = float(input("nilai b: "))
    op = ""

    print("\nmodel:")
    print("1. arithmetic")
    print("2. compare")

    model = input("choose (1/2): ")

    if model == '1':
        op = input("operator (+, -, *, /, %, **): ")

        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b if b != 0 else "error."
        elif op == '%':
            res = a % b if b != 0 else "error."
        elif op == '**':
            res = a ** b
        else:
            res = "invalid operator"

    elif model == '2':
        op = input("operator (==, !=, >, <, >=, <=): ")

        if op == '==':
            res = f"{a} sama dengan {b}" if a == b else f"{a} tidak sama dengan {b}"
        elif op == '!=':
            res = f"{a} tidak sama dengan {b}" if a != b else f"{a} sama dengan {b}"
        elif op == '>':
            res = f"{a} lebih besar dari {b}" if a > b else f"{a} tidak lebih besar dari {b}"
        elif op == '<':
            res = f"{a} lebih kecil dari {b}" if a < b else f"{a} tidak lebih kecil dari {b}"
        elif op == '>=':
            res = f"{a} lebih besar atau sama dengan {b}" if a >= b else f"{a} lebih kecil dari {b}"
        elif op == '<=':
            res = f"{a} lebih kecil atau sama dengan {b}" if a <= b else f"{a} lebih besar dari {b}"
        else:
            res = "invalid operator"
    else:
        res = "invalid mode"

    print(f"\n{a} {op} {b} = {res}")

    restart = input("\nrestart? (y/n): ").upper()
    if restart != 'Y':
        print("finished.")
        break
