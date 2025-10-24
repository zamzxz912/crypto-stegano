print("=== PROGRAM TEORI STRING INTERAKTIF ===\n")

while True:
    text = input("input teks: ")
    print(f"\nTeks yang dimasukkan: '{text}'\n")

    print("Pilih operasi yang ingin dilakukan:")
    print("1. slicing")
    print("2. looping")
    print("3. indeks")
    print("4. simetri & substring")
    print("5. manipulasi")

    choice = input("\nMasukkan choice (1-5): ")

    print("\n=== HASIL ===")

    if choice == '1':
        print(f"text[:5]  → {text[:5]}  (karakter dari indeks 0 sampai 4)")
        print(f"text[-5:] → {text[-5:]} (5 huruf terakhir)")
        print(f"text[2:8] → {text[2:8]} (karakter dari indeks 2 sampai 7)")

    elif choice == '2':
        print("Menampilkan setiap karakter:")
        for huruf in text:
            print(huruf, end=" ")
        print()

    elif choice == '3':
        if len(text) > 0:
            print(f"Karakter pertama (text[0]) = {text[0]}")
            print(f"Karakter terakhir (text[-1]) = {text[-1]}")
            if len(text) > 4:
                print(f"Karakter ke-5 (text[4]) = {text[4]}")
        else:
            print("String kosong, tidak bisa diindeks.")

    elif choice == '4':
        panjang = len(text)
        if panjang > 0:
            tengah = panjang // 2
            kiri = tengah - 3 if tengah - 3 >= 0 else 0
            kanan = tengah + 3 if tengah + 3 <= panjang else panjang
            simetri = text[kiri:kanan]
            print(f"Panjang string: {panjang}")
            print(f"Titik tengah: {tengah}")
            print(f"Bagian simetris di tengah: '{simetri}'")
        else:
            print("String kosong, tidak ada bagian simetris.")

    elif choice == '5':
        print(f"Teks huruf besar: {text.upper()}")
        print(f"Teks huruf kecil: {text.lower()}")
        print(f"Teks dibalik: {text[::-1]}")
        print(f"Jumlah huruf 'a': {text.count('a')}")
        kata_lama = input("\nKata yang ingin diganti: ")
        kata_baru = input("Ganti menjadi: ")
        print(f"Hasil replace: {text.replace(kata_lama, kata_baru)}")
        print(f"Apakah diawali huruf 'P'? → {text.startswith('P')}")
        print(f"Apakah diakhiri huruf 'n'? → {text.endswith('n')}")

    else:
        print("Pilihan tidak valid.")

    ulang = input("\nrestart? (y/n): ").upper()
    if ulang != 'Y':
        print("\nfinished.")
        break

    print("\n" + "="*40 + "\n")
