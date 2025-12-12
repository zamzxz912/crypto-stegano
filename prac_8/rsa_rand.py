import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTextEdit, QGroupBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

APP_BG = "#000000"
INPUT_BG = "#1e1e1e"
TEXT_COLOR = "#ECEFF4"
ACCENT_COLOR = "#794c74"
ACCENT_HOVER = "#B48EAD"
SUCCESS_COLOR = "#A3BE8C"
HIGHLIGHT_COLOR = "#B48EAD"

BASE_STYLE = f"""
    QWidget {{
        background-color: {APP_BG};
        color: {TEXT_COLOR};
        font-family: 'Century Gothic';
    }}
    QGroupBox {{
        color: {TEXT_COLOR};
        border: 2px solid {ACCENT_COLOR};
        border-radius: 8px;
        padding-top: 20px;
        margin-top: 10px;
        font-size: 14pt;
        font-weight: bold;
    }}
    QLabel {{
        color: {TEXT_COLOR};
        font-size: 14pt;
    }}
    QLineEdit {{
        background-color: {INPUT_BG};
        color: {TEXT_COLOR};
        border: 1px solid {ACCENT_COLOR};
        border-radius: 8px;
        padding: 8px;
        font-size: 14pt;
    }}
    QTextEdit {{
        background-color: {INPUT_BG};
        color: {SUCCESS_COLOR};
        border: 1px solid {ACCENT_COLOR};
        border-radius: 8px;
        padding: 10px;
        font-size: 11pt;
    }}
"""

GENERATE_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: #BF616A;
        color: {TEXT_COLOR}; 
        padding: 12px;
        border: none;
        border-radius: 8px;
        font-size: 14pt;
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: #D08770;
    }}
    QPushButton:pressed {{
        background-color: #B48EAD; 
    }}
"""

PROCESS_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {ACCENT_COLOR};
        color: {TEXT_COLOR};
        padding: 12px;
        border: none;
        border-radius: 8px;
        font-size: 14pt;
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {ACCENT_HOVER};
        color: {APP_BG};
    }}
    QPushButton:pressed {{
        background-color: {ACCENT_COLOR};
        color: {TEXT_COLOR};
    }}
"""

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def get_random_prime(min_val, max_val):
    primes = [n for n in range(min_val, max_val + 1) if is_prime(n)]
    if not primes: raise Exception("Tidak ada bilangan prima")
    return random.choice(primes)

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y

def mod_inverse_with_steps(a, m):
    debug_steps = [f"1. Mencari GCD({a}, {m}) menggunakan Algoritma Euclidean:"]
    r0, r1 = m, a
    while r1 != 0:
        q = r0 // r1
        r2 = r0 % r1
        debug_steps.append(f"   {r0} = {q} * {r1} + {r2}")
        r0, r1 = r1, r2
    g = r0
    if g != 1: raise Exception(f"GCD({a}, {m}) = {g}. Invers modular tidak ada.")
    debug_steps.append(f"   GCD({a}, {m}) = 1. Invers modular ada.")
    g, x, y = extended_gcd(a, m)
    d = x % m
    if d < 0: d += m
    debug_steps.append(f"\n2. Menggunakan Extended Euclidean Algorithm untuk d: {d}")
    debug_steps.append(f"   Pengujian: ({d} * {a}) mod {m} = {(d * a) % m}")
    return d, "\n".join(debug_steps)

def modular_pow(base, exponent, modulus):
    return pow(base, exponent, modulus)

class RSARand(QWidget):
    def __init__(self):
        super().__init__()
        self.p = self.q = self.e = self.n = self.phi_n = self.d = 0

        self.key_layout = QHBoxLayout()
        self.plaintext_input = QLineEdit()
        self.generate_button = QPushButton()
        self.process_button = QPushButton()
        self.debug_output = QTextEdit()

        self.setWindowTitle("RSA Random")
        self.setGeometry(100, 100, 950, 800)
        self.setStyleSheet(BASE_STYLE)
        self.setup_ui()
        self.generate_keys()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        key_group = QGroupBox("Kunci RSA yang Dihasilkan")
        key_group.setLayout(self.key_layout)
        main_layout.addWidget(key_group)

        pt_input_layout = QHBoxLayout()
        pt_label = QLabel("Plaintext (Teks):")
        self.plaintext_input.setPlaceholderText("Masukkan teks untuk dienkripsi (e.g., UJICOBA)")
        pt_input_layout.addWidget(pt_label)
        pt_input_layout.addWidget(self.plaintext_input)
        main_layout.addLayout(pt_input_layout)

        button_layout = QHBoxLayout()
        self.generate_button.setText("Generate Kunci Baru")
        self.generate_button.setStyleSheet(GENERATE_BUTTON_STYLE)
        self.generate_button.clicked.connect(self.generate_keys)  # type: ignore

        self.process_button.setText("Proses Enkripsi & Dekripsi")
        self.process_button.setStyleSheet(PROCESS_BUTTON_STYLE)
        self.process_button.clicked.connect(self.process_rsa)  # type: ignore

        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.process_button)
        main_layout.addLayout(button_layout)

        output_group = QGroupBox("Langkah-Langkah Perhitungan dan Hasil Akhir")
        output_layout = QVBoxLayout()
        output_layout.addWidget(self.debug_output)
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        self.setLayout(main_layout)

    def update_key_display(self):
        for i in reversed(range(self.key_layout.count())):
            item = self.key_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)

        params = [("p", self.p), ("q", self.q), ("e", self.e),
                  ("n", self.n), ("phi(n)", self.phi_n), ("d", self.d)]

        for name, value in params:
            label = QLabel(f"{name.upper()}: {value}")
            label.setFont(QFont("Century Gothic", 12, QFont.Bold))
            if name in ['p', 'q', 'e', 'd']:
                label.setStyleSheet(f"color: {ACCENT_HOVER};")
            self.key_layout.addWidget(label, alignment=Qt.AlignCenter)

    def generate_keys(self):
        self.debug_output.clear()
        try:
            self.p = get_random_prime(50, 200)
            while True:
                self.q = get_random_prime(50, 200)
                if self.q != self.p: break
            self.n = self.p * self.q
            self.phi_n = (self.p - 1) * (self.q - 1)
            e_candidates = [num for num in range(2, self.phi_n) if gcd(num, self.phi_n) == 1]
            if not e_candidates: raise Exception("Tidak ada kandidat e yang valid.")
            self.e = random.choice(e_candidates)
            self.d, d_steps = mod_inverse_with_steps(self.e, self.phi_n)

            debug_text = f"--- Langkah-langkah Generate Kunci ---\n"
            debug_text += f"1. p = {self.p}, q = {self.q}\n2. n = {self.n}\n3. phi(n) = {self.phi_n}\n4. e = {self.e}\n"
            debug_text += f"   Kunci Publik (e, n) = ({self.e}, {self.n})\n\n"
            debug_text += f"5. Hitung Eksponen Privat d:\n   d * {self.e} = 1 (mod {self.phi_n})\n"
            debug_text += f"   Langkah-langkah Euclidean:\n{d_steps}\n"
            debug_text += f"   Kunci Privat (d, n) = ({self.d}, {self.n})\n"
            self.debug_output.setText(f"<pre>{debug_text}</pre>")
            self.update_key_display()

        except Exception as e:
            self.debug_output.setText(f"Error dalam perhitungan kunci: {e}")
            self.p = self.q = self.e = self.n = self.phi_n = self.d = 0
            self.update_key_display()

    def process_rsa(self):
        if self.n == 0 or self.d == 0:
            self.debug_output.append("\n!!! Mohon Generate Kunci RSA terlebih dahulu !!!")
            return
        plaintext_input = self.plaintext_input.text().strip()
        if not plaintext_input:
            self.debug_output.append("\n!!! Mohon masukkan Plaintext !!!")
            return

        debug_text = "\n\n--- Proses Enkripsi dan Dekripsi (Per Karakter) ---\n"

        try:
            plaintext_chars = list(plaintext_input)
            ciphertexts = []
            decrypted_chars = []

            for char in plaintext_chars:
                m = ord(char)
                c = modular_pow(m, self.e, self.n)
                m_decrypted = modular_pow(c, self.d, self.n)
                decrypted_char = chr(m_decrypted)

                ciphertexts.append(str(c))
                decrypted_chars.append(decrypted_char)

                debug_text += f"Karakter: '{char}' (m={m})\n"
                debug_text += f"Enkripsi (c = m^e mod n): {m}^{self.e} mod {self.n} = {c}\n"
                debug_text += f"Dekripsi (m = c^d mod n): {c}^{self.d} mod {self.n} = {m_decrypted} ('{decrypted_char}')\n"
                debug_text += "--------------------------------------\n"

            final_ciphertext = " ".join(ciphertexts)
            final_decrypted = "".join(decrypted_chars)

            debug_text_final = "\n\n======================================\n"
            debug_text_final += "FINAL CIPHERTEXT:\n"
            debug_text_final += f"<span style='color:{HIGHLIGHT_COLOR}; font-size:12pt; font-weight:bold;'>{final_ciphertext}</span>\n"
            debug_text_final += "--------------------------------------\n"
            debug_text_final += "FINAL DECRYPTED PLAINTEXT:\n"
            debug_text_final += f"<span style='color:{HIGHLIGHT_COLOR}; font-size:12pt; font-weight:bold;'>{final_decrypted}</span>\n"
            debug_text_final += "======================================\n"

            existing_text = self.debug_output.toPlainText()
            self.debug_output.setHtml(f"<pre>{existing_text}{debug_text}{debug_text_final}</pre>")

        except Exception as e:
            self.debug_output.append(f"\n!!! Terjadi kesalahan saat proses RSA: {e} !!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RSARand()
    window.show()
    sys.exit(app.exec_())