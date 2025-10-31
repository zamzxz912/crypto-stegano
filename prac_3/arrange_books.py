import itertools

def arrange_books():
    try:
        n = int(input("jumlah buku (n): "))
        r = int(input("jumlah bagian rak (r): "))
    except ValueError:
        print("invalid.")
        return

    books = [f"B{i+1}" for i in range(n)]
    perm = list(itertools.permutations(books, r))

    print(f"\njumlah cara: {len(perm)}")
    for p in perm:
        print(p)

while True:
    print("=== PERMUTATION PROGRAM ===")
    print("1. Susunan buku di rak")
    print("2. Quit")
    ch = input("Choose bet. 1-2: ")

    if ch == "1":
        arrange_books()
    elif ch == "2":
        print("finished.")
        break
    else:
        print("invalid.")

    re = input("\nrestart? (y/n): ")
    if re.lower() != "y":
        print("finished.")
        break