import os

def binary():
    b = input("input b: ")
    try:
        d = int(b, 2)
    except ValueError:
        print("input tidak valid (harus biner).")
        return
    hd = hex(d)[2:].upper()
    o = oct(d)[2:]

    print("desimal:", d)
    print("hexadesimal:", hd)
    print("oktal:", o)

def octal():
    o = input("input o: ")
    try:
        d = int(o, 8)
    except ValueError:
        print("input tidak valid (harus oktal).")
        return
    b = bin(d)[2:]
    hd = hex(d)[2:].upper()

    print("desimal:", d)
    print("biner:", b)
    print("hexadesimal:", hd)

def hexadecimal():
    hd = input("input hex: ")
    try:
        d = int(hd, 16)
    except ValueError:
        print("input tidak valid (harus hex).")
        return
    b = bin(d)[2:]
    o = oct(d)[2:]

    print("desimal:", d)
    print("biner:", b)
    print("oktal:", o)

while True:
    print("=== NUMERIC CONVERTION ===")
    print("1. Biner --> Desimal, Hexadesimal & Oktal")
    print("2. Oktal --> Desimal, Biner & Hexadesimal")
    print("3. Hexadesimal --> Desimal, Biner & Oktal")
    print("4. Quit")
    ch = input("Choose bet. 1-4: ")

    if ch == "1":
        binary()

    elif ch == "2":
        octal()

    elif ch == "3":
        hexadecimal()

    elif ch == "4":
        print("finished.")
        break

    else:
        print("invalid.")

    ulang = input("\nrestart? (y/n): ")
    if ulang.lower() != "y":
        print("finished.")
        break
