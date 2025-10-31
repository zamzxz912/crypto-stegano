def sub_cip(p, a):
    c = ""
    for chx in p.upper():
        if chx in a:
            c += a[chx]
        else:
            c += chx
    return c

def trans_cip(p):
    pl = len(p) // 4
    parts = [p[i:i+pl] for i in range(0, len(p), pl)]
    c = ""
    for colx in range(4):
        for part in parts:
            if colx < len(part):
                c += part[colx]
    return c

def run():
    a = {'U':'N','N':'Y','I':'K','K':'I','A':'B'}
    p = input("input plaintext: ").upper()
    print(f"\nPlaintext : {p}")
    s = sub_cip(p, a)
    print(f"Cipher(Substitusi): {s}")
    t = trans_cip(s)
    print(f"Cipher(Substitusi+Transposisi): {t}")

while True:
    print("=== CIPHER COMBINATION ===")
    print("1. Enkripsi (Substitusi + Transposisi)")
    print("2. Quit")
    ch = input("Choose bet. 1-2: ")
    if ch == "1":
        run()
    elif ch == "2":
        print("finished.")
        break
    else:
        print("invalid.")

    re = input("\nrestart? (y/n): ")
    if re.lower() != "y":
        print("finished.")
        break