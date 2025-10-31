def mk_rules():
    rule = {}
    print("enter the substitution rule (type 'done' to finish)")
    while True:
        r = input("rule: ").strip().upper()
        if r == "DONE":
            break
        if "=" not in r or len(r) != 3:
            print("invalid.")
            continue
        k, v = r.split("=")
        if not (k.isalpha() and v.isalpha()):
            print("no number.")
            continue
        rule[k] = v
    return rule

def sub_cip(p, a):
    c = ""
    for chx in p.upper():
        if chx in a:
            c += a[chx]
        else:
            c += chx
    return c

def run():
    p = input("input plaintext: ").upper()
    a = mk_rules()
    print("\n=== RESULT ===")
    for k, v in a.items():
        print(f"{k} → {v}")
    c = sub_cip(p, a)
    print(f"\nPlaintext : {p}")
    print(f"Ciphertext: {c}")

while True:
    print("=== SUBSTITUSI CIPHER ===")
    print("1. Enkripsi")
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
