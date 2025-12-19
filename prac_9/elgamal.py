import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTextEdit,
                             QGroupBox, QFormLayout)


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


def power(a, b, m):
    return pow(a, b, m)


class ElGamalApp(QWidget):
    def __init__(self):
        super().__init__()

        self.p_input = QLineEdit()
        self.g_input = QLineEdit()
        self.x_input = QLineEdit()
        self.btn_gen = QPushButton("Generate Kunci Publik (y)")

        self.msg_input = QLineEdit()
        self.k_input = QLineEdit()
        self.btn_enc = QPushButton("Enkripsi")
        self.btn_dec = QPushButton("Dekripsi")

        self.btn_clear_all = QPushButton("Reset Semua Data")
        self.log_output = QTextEdit()

        self.current_y = None
        self.encrypted_pairs = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ElGamal Algorithm')
        self.setMinimumSize(1100, 800)

        self.setStyleSheet("""
            QWidget { background-color: #0f172a; color: #f1f5f9; font-family: 'Inter', sans-serif; }
            QGroupBox { font-weight: bold; border: 2px solid #1e293b; border-radius: 10px; margin-top: 20px; padding: 20px; font-size: 16px; color: #38bdf8; }
            QLabel { color: #94a3b8; font-size: 16px; }
            QLineEdit { background-color: #1e293b; border: 1px solid #334155; padding: 12px; border-radius: 6px; color: #ffffff; font-size: 16px; }
            QPushButton { background-color: #1d4ed8; border: none; padding: 15px; border-radius: 6px; font-weight: bold; color: white; font-size: 15px; }
            QPushButton:hover { background-color: #2563eb; }
            QTextEdit { background-color: #020617; border: 2px solid #1d4ed8; border-radius: 10px; padding: 20px; color: #38bdf8; font-family: 'Consolas', monospace; font-size: 18px; }
        """)

        main_layout = QHBoxLayout()
        left_panel = QVBoxLayout()

        group_key = QGroupBox("Konfigurasi Kunci")
        form_key = QFormLayout()
        form_key.addRow("Bilangan Prima (p):", self.p_input)
        form_key.addRow("Generator (g):", self.g_input)
        form_key.addRow("Kunci Privat (x):", self.x_input)

        getattr(self.btn_gen.clicked, 'connect')(self.handle_gen)

        v_key = QVBoxLayout()
        v_key.addLayout(form_key)
        v_key.addWidget(self.btn_gen)
        group_key.setLayout(v_key)

        group_proc = QGroupBox("Proses Enkripsi dan Dekripsi")
        form_proc = QFormLayout()
        form_proc.addRow("Input Teks:", self.msg_input)
        form_proc.addRow("Nilai Acak (k):", self.k_input)

        getattr(self.btn_enc.clicked, 'connect')(self.handle_enc)
        getattr(self.btn_dec.clicked, 'connect')(self.handle_dec)

        h_btn = QHBoxLayout()
        h_btn.addWidget(self.btn_enc)
        h_btn.addWidget(self.btn_dec)

        v_proc = QVBoxLayout()
        v_proc.addLayout(form_proc)
        v_proc.addLayout(h_btn)
        group_proc.setLayout(v_proc)

        self.btn_clear_all.setStyleSheet("background-color: #475569; padding: 12px;")
        getattr(self.btn_clear_all.clicked, 'connect')(self.clear_all)

        left_panel.addWidget(group_key)
        left_panel.addWidget(group_proc)
        left_panel.addWidget(self.btn_clear_all)
        left_panel.addStretch()

        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("LOG PERHITUNGAN DAN DATA OUTPUT"))
        self.log_output.setReadOnly(True)
        right_panel.addWidget(self.log_output)

        container_left = QWidget()
        container_left.setLayout(left_panel)
        container_left.setFixedWidth(420)

        main_layout.addWidget(container_left)
        main_layout.addLayout(right_panel)
        self.setLayout(main_layout)

    def log(self, text):
        self.log_output.append(text)

    def clear_all(self):
        self.p_input.clear()
        self.g_input.clear()
        self.x_input.clear()
        self.msg_input.clear()
        self.k_input.clear()
        self.log_output.clear()
        self.current_y = None
        self.encrypted_pairs = []

    def handle_gen(self):
        try:
            p = int(self.p_input.text() or 0)
            g = int(self.g_input.text() or 0)
            x = int(self.x_input.text() or 0)

            if not is_prime(p):
                self.log("<span style='color: #f87171;'>[Kesalahan] p bukan prima.</span>")
                return

            self.current_y = power(g, x, p)
            self.log("<b>[LANGKAH 1: GENERASI KUNCI]</b>")
            self.log(f"y = {g}^{x} mod {p} = <b>{self.current_y}</b>")
            self.log("-" * 60)
        except ValueError:
            self.log("<span style='color: #f87171;'>[Kesalahan] p, g, x harus angka.</span>")

    def handle_enc(self):
        if self.current_y is None:
            self.log("<span style='color: #f87171;'>[Kesalahan] Hitung kunci y dulu.</span>")
            return

        text = self.msg_input.text()
        try:
            p = int(self.p_input.text())
            g = int(self.g_input.text())
            y = self.current_y
            k = int(self.k_input.text() or 0)

            self.encrypted_pairs = []
            self.log("<b>[LANGKAH 2: PROSES ENKRIPSI]</b>")
            self.log(f"{'Char':<8} | {'ASCII':<10} | {'c1':<15} | {'c2':<15}")
            self.log("=" * 60)

            for char in text:
                m = ord(char)
                c1 = power(g, k, p)
                c2 = (m * power(y, k, p)) % p
                self.encrypted_pairs.append((c1, c2))
                self.log(f"{char:<8} | {m:<10} | {c1:<15} | {c2:<15}")

            self.log("-" * 60)
        except ValueError:
            self.log("<span style='color: #f87171;'>[Kesalahan] Nilai k harus angka.</span>")

    def handle_dec(self):
        if not self.encrypted_pairs:
            self.log("<span style='color: #f87171;'>[Kesalahan] Tidak ada ciphertext.</span>")
            return

        try:
            p = int(self.p_input.text())
            x = int(self.x_input.text())

            self.log("<b>[LANGKAH 3: PROSES DEKRIPSI]</b>")
            self.log(f"{'c1':<10} | {'c2':<10} | {'Secret':<12} | {'Char':<6}")
            self.log("=" * 60)

            final_chars = []
            for c1, c2 in self.encrypted_pairs:
                s = power(c1, x, p)
                m = (c2 * power(s, p - 2, p)) % p
                final_chars.append(chr(m))
                self.log(f"{c1:<10} | {c2:<10} | {s:<12} | {chr(m):<6}")

            res = "".join(final_chars)
            self.log("-" * 60)
            self.log(f"HASIL AKHIR: <b style='font-size: 22px;'>{res}</b>")
        except Exception as e:
            self.log(f"[Kesalahan] {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ElGamalApp()
    ex.show()
    sys.exit(app.exec_())