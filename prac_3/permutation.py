import itertools

def full_perm():
    d = input("input data (pisah spasi): ").split()
    if not d:
        print("data kosong.")
        return

    p = list(itertools.permutations(d))
    print("\n=== HASIL PERMUTASI MENYELURUH ===")
    for x in p:
        print(x)
    print("jumlah:", len(p))

def partial_perm():
    d = input("input data (pisah spasi): ").split()
    if not d:
        print("data kosong.")
        return
    try:
        k = int(input("panjang permutasi (k): "))
    except ValueError:
        print("input k harus berupa angka.")
        return

    if k < 1 or k > len(d):
        print("k harus antara 1 dan jumlah elemen data.")
        return

    p = list(itertools.permutations(d, k))
    print("\n=== HASIL PERMUTASI SEBAGIAN ===")
    for x in p:
        print(x)
    print("jumlah:", len(p))

def circular_perm():
    d = input("input data (pisah spasi): ").split()
    if len(d) <= 1:
        print("minimal 2 elemen.")
        return

    first = d[0]
    sub = list(itertools.permutations(d[1:]))
    p = [[first] + list(s) for s in sub]

    print("\n=== HASIL PERMUTASI KELILING ===")
    for x in p:
        print(x)
    print("jumlah:", len(p))

def grouped_perm():
    try:
        n = int(input("jumlah grup: "))
    except ValueError:
        print("input harus berupa angka.")
        return

    if n < 1:
        print("jumlah grup minimal 1.")
        return

    g = []
    for i in range(n):
        el = input(f"elemen grup-{i+1} (pisah spasi): ").split()
        if not el:
            print("grup tidak boleh kosong.")
            return
        g.append(el)

    hasil = [[]]
    for group in g:
        baru = []
        for h in hasil:
            for p in itertools.permutations(group):
                baru.append(h + list(p))
        hasil = baru

    print("\n=== HASIL PERMUTASI BERKELOMPOK ===")
    for x in hasil:
        print(x)
    print("jumlah:", len(hasil))

while True:
    print("=== PERMUTATION PROGRAM ===")
    print("1. Permutasi Menyeluruh")
    print("2. Permutasi Sebagian")
    print("3. Permutasi Keliling")
    print("4. Permutasi Berkelompok")
    print("5. Quit")
    ch = input("Choose bet. 1-5: ")

    if ch == "1":
        full_perm()
    elif ch == "2":

        partial_perm()
    elif ch == "3":
        circular_perm()
    elif ch == "4":
        grouped_perm()
    elif ch == "5":
        print("finished.")
        break
    else:
        print("invalid.")

    re = input("\nrestart? (y/n): ")
    if re.lower() != "y":
        print("finished.")
        break