import tkinter as tk
from tkinter import messagebox, simpledialog

def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else None

def jalankan_kalkulator1():
    try:
        a = float(simpledialog.askstring("Input", "Masukkan angka pertama:"))
        b = float(simpledialog.askstring("Input", "Masukkan angka kedua:"))
        hasil = (
            f"Penjumlahan: {tambah(a, b)}\n"
            f"Pengurangan: {kurang(a, b)}\n"
            f"Perkalian  : {kali(a, b)}\n"
            f"Pembagian  : {bagi(a, b) if b != 0 else 'Error: Bagi 0'}"
        )
        messagebox.showinfo("Hasil Kalkulator 1", hasil)
    except:
        messagebox.showerror("Error", "Input tidak valid.")

def jalankan_kalkulator2():
    try:
        a = float(simpledialog.askstring("Input", "Masukkan angka pertama:"))
        b = float(simpledialog.askstring("Input", "Masukkan angka kedua:"))
        op = simpledialog.askstring("Input", "Masukkan operator (+, -, *, /):")

        if op == '+':
            hasil = a + b
        elif op == '-':
            hasil = a - b
        elif op == '*':
            hasil = a * b
        elif op == '/':
            if b == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diizinkan.")
                return
            hasil = a / b
        else:
            messagebox.showerror("Error", "Operator tidak valid.")
            return

        messagebox.showinfo("Hasil Kalkulator 2", f"Hasil: {hasil}")
    except:
        messagebox.showerror("Error", "Input tidak valid.")

def final_sc(sikap, tugas, uts, uas):
    bobot = {"sikap": 0.1, "tugas": 0.3, "uts": 0.25, "uas": 0.35}
    tot_nilai = sikap*bobot["sikap"] + tugas*bobot["tugas"] + uts*bobot["uts"] + uas*bobot["uas"]

    if 81 <= tot_nilai <= 100:
        n_huruf, nilai_bobot = "A", 4
    elif 76 <= tot_nilai <= 80:
        n_huruf, nilai_bobot = "B+", 3.5
    elif 71 <= tot_nilai <= 75:
        n_huruf, nilai_bobot = "B", 3
    elif 66 <= tot_nilai <= 70:
        n_huruf, nilai_bobot = "C+", 2.5
    elif 56 <= tot_nilai <= 65:
        n_huruf, nilai_bobot = "C", 2
    elif 46 <= tot_nilai <= 55:
        n_huruf, nilai_bobot = "D", 1
    else:
        n_huruf, nilai_bobot = "E", 0

    ket = "Lulus" if tot_nilai >= 56 else "Tidak Lulus"
    return tot_nilai, n_huruf, nilai_bobot, ket

def jalankan_form_nilai():
    win = tk.Toplevel(root)
    win.title("Hitung Nilai Akhir")

    frame = tk.Frame(win, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Nilai Sikap:").grid(row=0, column=0, sticky="e")
    entry_sikap = tk.Entry(frame)
    entry_sikap.grid(row=0, column=1)

    tk.Label(frame, text="Nilai Tugas:").grid(row=1, column=0, sticky="e")
    entry_tugas = tk.Entry(frame)
    entry_tugas.grid(row=1, column=1)

    tk.Label(frame, text="Nilai UTS:").grid(row=2, column=0, sticky="e")
    entry_uts = tk.Entry(frame)
    entry_uts.grid(row=2, column=1)

    tk.Label(frame, text="Nilai UAS:").grid(row=3, column=0, sticky="e")
    entry_uas = tk.Entry(frame)
    entry_uas.grid(row=3, column=1)

    lbl_hasil = tk.Label(frame, text="", font=("Arial", 10), justify="left")
    lbl_hasil.grid(row=5, column=0, columnspan=2)

    def hitung():
        try:
            s = float(entry_sikap.get())
            t = float(entry_tugas.get())
            u = float(entry_uts.get())
            a = float(entry_uas.get())
            for n in (s, t, u, a):
                if not (0 <= n <= 100):
                    raise ValueError
            tot, huruf, bobot, ket = final_sc(s, t, u, a)
            lbl_hasil.config(text=f"Total: {tot:.2f}\nNilai Akhir: {huruf} (Bobot {bobot})\nKeterangan: {ket}")
        except:
            messagebox.showerror("Error", "Input nilai harus angka 0-100")

    tk.Button(frame, text="Hitung", command=hitung).grid(row=4, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Program Multi-Menu")

menubar = tk.Menu(root)

menu_kalkulator = tk.Menu(menubar, tearoff=0)
menu_kalkulator.add_command(label="Kalkulator 1 (Operasi Lengkap)", command=jalankan_kalkulator1)
menu_kalkulator.add_command(label="Kalkulator 2 (Dengan Operator)", command=jalankan_kalkulator2)
menubar.add_cascade(label="Kalkulator", menu=menu_kalkulator)

menu_nilai = tk.Menu(menubar, tearoff=0)
menu_nilai.add_command(label="Form Hitung Nilai Akhir", command=jalankan_form_nilai)
menubar.add_cascade(label="Nilai", menu=menu_nilai)

menu_exit = tk.Menu(menubar, tearoff=0)
menu_exit.add_command(label="Keluar", command=root.quit)
menubar.add_cascade(label="Exit", menu=menu_exit)

root.config(menu=menubar)
tk.Label(root, text="Silakan pilih menu di atas", font=("Arial", 12, "bold"), pady=50).pack()

root.mainloop()
