import tkinter as tk
from tkinter import ttk, messagebox

# ===============================
# CLASS VigenereCipher (PBO)
# ===============================
class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _format_text(self, text):
        return ''.join(filter(str.isalpha, text)).upper()

    def _generate_key(self, text):
        key = self.key
        key = key.upper()
        if len(key) < len(text):
            key = (key * (len(text) // len(key) + 1))[:len(text)]
        return key

    def encrypt(self, plaintext):
        plaintext = self._format_text(plaintext)
        key = self._generate_key(plaintext)
        ciphertext = ""
        proses = []

        for p, k in zip(plaintext, key):
            enc = chr(((ord(p) - 65 + (ord(k) - 65)) % 26) + 65)
            ciphertext += enc
            proses.append(f"{p} + {k} = {enc}")

        return ciphertext, "\n".join(proses)

    def decrypt(self, ciphertext):
        ciphertext = self._format_text(ciphertext)
        key = self._generate_key(ciphertext)
        plaintext = ""
        proses = []

        for c, k in zip(ciphertext, key):
            dec = chr(((ord(c) - 65 - (ord(k) - 65)) % 26) + 65)
            plaintext += dec
            proses.append(f"{c} - {k} = {dec}")

        return plaintext, "\n".join(proses)


# ===============================
# CLASS GUI
# ===============================
class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Vigenère Cipher Encryption & Decryption")
        self.root.geometry("650x600")
        self.root.configure(bg="#e9f0f5")

        title = tk.Label(root, text="🔐 VIGENÈRE CIPHER TOOL",
                         font=("Poppins", 18, "bold"), bg="#e9f0f5", fg="#2b4c7e")
        title.pack(pady=10)

        # Frame Input
        frame_input = tk.Frame(root, bg="#ffffff", padx=10, pady=10, relief="groove", bd=2)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Masukkan Teks:", bg="#ffffff", font=("Poppins", 11)).grid(row=0, column=0, sticky="w")
        self.text_entry = tk.Entry(frame_input, width=50, font=("Poppins", 11))
        self.text_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_input, text="Masukkan Kunci:", bg="#ffffff", font=("Poppins", 11)).grid(row=1, column=0, sticky="w")
        self.key_entry = tk.Entry(frame_input, width=50, font=("Poppins", 11))
        self.key_entry.grid(row=1, column=1, padx=10, pady=5)

        # Tombol
        frame_button = tk.Frame(root, bg="#e9f0f5")
        frame_button.pack(pady=5)
        ttk.Button(frame_button, text="🔒 Enkripsi", command=self.encrypt_text).grid(row=0, column=0, padx=10)
        ttk.Button(frame_button, text="🔓 Dekripsi", command=self.decrypt_text).grid(row=0, column=1, padx=10)

        # Hasil
        frame_output = tk.Frame(root, bg="#ffffff", padx=10, pady=10, relief="ridge", bd=2)
        frame_output.pack(pady=10, fill="both", expand=True)

        tk.Label(frame_output, text="Hasil:", bg="#ffffff", font=("Poppins", 11, "bold")).pack(anchor="w")
        self.output_text = tk.Text(frame_output, height=4, font=("Consolas", 11), wrap="word")
        self.output_text.pack(fill="x", pady=5)

        tk.Label(frame_output, text="Proses Detail:", bg="#ffffff", font=("Poppins", 11, "bold")).pack(anchor="w")
        self.process_text = tk.Text(frame_output, height=15, font=("Consolas", 10), wrap="word", fg="#333")
        self.process_text.pack(fill="both", expand=True, pady=5)

    def encrypt_text(self):
        text = self.text_entry.get()
        key = self.key_entry.get()

        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci harus diisi!")
            return

        cipher = VigenereCipher(key)
        ciphertext, proses = cipher.encrypt(text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, ciphertext)
        self.process_text.delete("1.0", tk.END)
        self.process_text.insert(tk.END, proses)

    def decrypt_text(self):
        text = self.text_entry.get()
        key = self.key_entry.get()

        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci harus diisi!")
            return

        cipher = VigenereCipher(key)
        plaintext, proses = cipher.decrypt(text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, plaintext)
        self.process_text.delete("1.0", tk.END)
        self.process_text.insert(tk.END, proses)


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()
