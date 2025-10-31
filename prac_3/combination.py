def fact(x):
    r = 1
    for i in range(2, x+1):
        r *= i
    return r

def comb():
    try:
        n = int(input("jumlah total objek (n): "))
        r = int(input("jumlah objek dipilih (r): "))
    except ValueError:
        print("invalid.")
        return

    if r > n or n < 0 or r < 0:
        print("invalid.")
        return

    c = fact(n) // (fact(r) * fact(n - r))
    print(f"\nC({n}, {r}) = {c}")

    from itertools import combinations
    huruf = [chr(65 + i) for i in range(n)]
    hasil = list(combinations(huruf, r))
    print("\nKombinasi huruf:")
    for h in hasil:
        print(h)

while True:
    print("=== COMBINATION PROGRAM ===")
    print("1. Hitung kombinasi")
    print("2. Quit")
    ch = input("Choose bet. 1-2: ")

    if ch == "1":
        comb()
    elif ch == "2":
        print("finished.")
        break
    else:
        print("invalid.")

    re = input("\nrestart? (y/n): ")
    if re.lower() != "y":
        print("finished.")
        break