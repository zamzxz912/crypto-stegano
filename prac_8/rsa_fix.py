import sys
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
    }}
"""

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1: raise Exception('Invers modular tidak ada')
    return x % m

def modular_pow(base, exponent, modulus):
    return pow(base, exponent, modulus)

class RSAFix(QWidget):
    def __init__(self):
        super().__init__()
        self.p = 29 
        self.q = 13
        self.e = 5
        self.n = 0
        self.phi_n = 0
        self.d = 0

        self.plaintext_input = QLineEdit()
        self.process_button = QPushButton()
        self.debug_output = QTextEdit()

        self.setWindowTitle("RSA Fix")
        self.setGeometry(100, 100, 950, 750)
        self.setStyleSheet(BASE_STYLE)
        self.setup_ui()
        self.calculate_keys()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        input_group = QGroupBox("Parameter RSA Tetap")
        input_layout = QHBoxLayout()

        fixed_params = (f"p: {self.p}", f"q: {self.q}", f"e: {self.e}")
        for param in fixed_params:
            label = QLabel(param)
            label.setFont(QFont("Century Gothic", 16, QFont.ExtraBold))
            label.setStyleSheet(f"color: {ACCENT_HOVER};")
            input_layout.addWidget(label, alignment=Qt.AlignCenter)

        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        pt_input_layout = QHBoxLayout()
        pt_label = QLabel("Plaintext (Teks/Angka):")
        self.plaintext_input.setPlaceholderText("Masukkan teks atau angka untuk dienkripsi")
        pt_input_layout.addWidget(pt_label)
        pt_input_layout.addWidget(self.plaintext_input)
        main_layout.addLayout(pt_input_layout)

        self.process_button.setText("Proses Enkripsi & Dekripsi")
        self.process_button.setStyleSheet(PROCESS_BUTTON_STYLE)
        self.process_button.clicked.connect(self.process_rsa)  # type: ignore
        main_layout.addWidget(self.process_button)

        output_group = QGroupBox("Langkah Perhitungan dan Hasil Akhir")
        output_layout = QVBoxLayout()

        output_layout.addWidget(self.debug_output)

        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        self.setLayout(main_layout)

    def calculate_keys(self):
        try:
            self.n = self.p * self.q
            self.phi_n = (self.p - 1) * (self.q - 1)
            if gcd(self.e, self.phi_n) != 1:
                raise ValueError("e harus relatif prima terhadap phi(n)")
            self.d = mod_inverse(self.e, self.phi_n)
        except Exception as e:
            self.debug_output.setText(f"Error dalam perhitungan kunci: {e}")
            self.n = self.phi_n = self.d = 0

    def process_rsa(self):
        self.debug_output.clear()
        if self.n == 0 or self.d == 0:
            self.debug_output.setText("Kunci RSA belum dihitung dengan benar. Coba jalankan ulang.")
            return

        plaintext_input = self.plaintext_input.text().strip()
        if not plaintext_input:
            self.debug_output.setText("Mohon masukkan Plaintext.")
            return

        try:
            plaintext_chars = list(plaintext_input)

            debug_text = f"--- Kunci RSA Tergenerate ---\n"
            debug_text += f"Kunci Publik (e, n) = ({self.e}, {self.n})\n"
            debug_text += f"Kunci Privat (d, n) = ({self.d}, {self.n})\n\n"
            debug_text += "--- Proses Enkripsi dan Dekripsi (Per Karakter) ---\n"

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
                debug_text += f"Enkripsi: {m}^{self.e} mod {self.n} = {c}\n"
                debug_text += f"Dekripsi: {c}^{self.d} mod {self.n} = {m_decrypted} ('{decrypted_char}')\n"
                debug_text += "--------------------------------------\n"

            final_ciphertext = " ".join(ciphertexts)
            final_decrypted = "".join(decrypted_chars)

            debug_text += "\n\n======================================\n"
            debug_text += "FINAL CIPHERTEXT:\n"
            debug_text += f"<span style='color:{HIGHLIGHT_COLOR}; font-size:12pt; font-weight:bold;'>{final_ciphertext}</span>\n"
            debug_text += "--------------------------------------\n"
            debug_text += "FINAL DECRYPTED PLAINTEXT:\n"
            debug_text += f"<span style='color:{HIGHLIGHT_COLOR}; font-size:12pt; font-weight:bold;'>{final_decrypted}</span>\n"
            debug_text += "======================================\n"

            self.debug_output.setHtml(f"<pre>{debug_text}</pre>")

        except Exception as e:
            self.debug_output.setText(f"Terjadi kesalahan saat proses RSA: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RSAFix()
    window.show()
    sys.exit(app.exec_())