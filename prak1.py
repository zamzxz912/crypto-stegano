def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
print(f"Hasil penjumlahan: {tambah(angka1, angka2)}")
print(f"Hasil pengurangan: {kurang(angka1, angka2)}")
print(f"Hasil perkalian: {kali(angka1, angka2)}")
print(f"Hasil pembagian: {bagi(angka1, angka2)}")