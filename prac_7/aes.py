import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


SBOX = [
    0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
    0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
    0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
    0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
    0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
    0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
    0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
    0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
    0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
    0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
    0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
    0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
    0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
    0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
    0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
    0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]


def text_to_hex(t):
    return [format(ord(c), "02X") for c in t]


def to_matrix(hex_list):
    mat = [[0] * 4 for _ in range(4)]
    for i in range(16):
        r = i // 4
        c = i % 4
        mat[r][c] = int(hex_list[i], 16)
    return mat


def mat_hex(mat):
    return "\n".join(" ".join(f"{x:02X}" for x in row) for row in mat)


def xor(a, b):
    return [[a[r][c] ^ b[r][c] for c in range(4)] for r in range(4)]


def subbytes(state):
    return [[SBOX[x] for x in row] for row in state]


def shiftrows(state):
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]


def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1) & 0xFF


def mixcolumns(state):
    out = [[0] * 4 for _ in range(4)]
    for c in range(4):
        a = [state[r][c] for r in range(4)]
        out[0][c] = xtime(a[0]) ^ a[3] ^ a[2] ^ xtime(a[1]) ^ a[1]
        out[1][c] = xtime(a[1]) ^ a[0] ^ a[3] ^ xtime(a[2]) ^ a[2]
        out[2][c] = xtime(a[2]) ^ a[1] ^ a[0] ^ xtime(a[3]) ^ a[3]
        out[3][c] = xtime(a[3]) ^ a[2] ^ a[1] ^ xtime(a[0]) ^ a[0]
    return out


def key_expansion(key_mat):
    words = []
    for c in range(4):
        words.append([key_mat[r][c] for r in range(4)])

    for i in range(4, 44):
        temp = words[i - 1][:]
        if i % 4 == 0:
            temp = temp[1:] + temp[:1]
            temp = [SBOX[x] for x in temp]
            temp[0] ^= RCON[(i // 4) - 1]
        words.append([temp[j] ^ words[i - 4][j] for j in range(4)])

    keys = []
    for r in range(11):
        m = [[0] * 4 for _ in range(4)]
        for c in range(4):
            for row in range(4):
                m[row][c] = words[r * 4 + c][row]
        keys.append(m)

    return keys

class AESWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AES-128")
        self.resize(950, 720)

        root = QVBoxLayout()
        root.setContentsMargins(25, 25, 25, 25)
        root.setSpacing(20)

        header = QLabel("AES-128 Encryption")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Segoe UI", 22, QFont.Bold))

        header.setStyleSheet("""
            QLabel {
                padding: 20px;
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.06);
                color: black;
                border: 1px solid rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(12px);
            }
        """)
        root.addWidget(header)

        card = QWidget()
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(15)

        card.setStyleSheet("""
            QWidget {
                background: #111111;
                border-radius: 18px;
                border: 1px solid #222;
            }
        """)

        font_label = QFont("Segoe UI", 12, QFont.Bold)
        font_input = QFont("Consolas", 14)

        lbl_pt = QLabel("Plaintext (16 chars)")
        lbl_pt.setFont(font_label)
        lbl_pt.setStyleSheet("color: #d9d9d9;")
        card_layout.addWidget(lbl_pt)

        self.pt = QLineEdit()
        self.pt.setFont(font_input)
        self.pt.setStyleSheet("""
            QLineEdit {
                background: #1a1a1a;
                color: #e8e8e8;
                padding: 10px 12px;
                border-radius: 10px;
                border: 1px solid #333;
            }
            QLineEdit:focus {
                border: 1px solid #b892ff;
            }
        """)
        card_layout.addWidget(self.pt)

        lbl_ck = QLabel("Cipher Key (16 chars)")
        lbl_ck.setFont(font_label)
        lbl_ck.setStyleSheet("color: #d9d9d9;")
        card_layout.addWidget(lbl_ck)

        self.ck = QLineEdit()
        self.ck.setFont(font_input)
        self.ck.setStyleSheet("""
            QLineEdit {
                background: #1a1a1a;
                color: #e8e8e8;
                padding: 10px 12px;
                border-radius: 10px;
                border: 1px solid #333;
            }
            QLineEdit:focus {
                border: 1px solid #b892ff;
            }
        """)
        card_layout.addWidget(self.ck)

        btn_row = QHBoxLayout()

        button_style = """
            QPushButton {
                background-color: #b892ff;
                padding: 12px;
                border-radius: 10px;
                font-size: 14px;
                color: black;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c7a7ff;
            }
        """

        btn_key: QPushButton = QPushButton("Generate Keys")
        btn_key.setStyleSheet(button_style)
        btn_key.clicked.connect(self.generate_keys)

        btn_enc: QPushButton = QPushButton("Encrypt AES")
        btn_enc.setStyleSheet(button_style)
        btn_enc.clicked.connect(self.encrypt)

        btn_row.addWidget(btn_key)
        btn_row.addWidget(btn_enc)
        card_layout.addLayout(btn_row)

        self.out = QTextEdit()
        self.out.setFont(QFont("Consolas", 14))
        self.out.setStyleSheet("""
            QTextEdit {
                background: #0d0d0d;
                color: #92f5d9;
                padding: 15px;
                border-radius: 14px;
                border: 1px solid #222;
            }
        """)
        card_layout.addWidget(self.out)

        root.addWidget(card)
        self.setLayout(root)

        self.round_keys = None

    def generate_keys(self):
        pt = self.pt.text()
        ck = self.ck.text()

        if len(pt) != 16 or len(ck) != 16:
            QMessageBox.critical(self, "Error", "HARUS 16 karakter!")
            return

        key0 = to_matrix(text_to_hex(ck))
        self.round_keys = key_expansion(key0)

        self.out.clear()
        self.out.append("=== KEY EXPANSION K0–K10 ===")
        for i, k in enumerate(self.round_keys):
            self.out.append(f"\nK{i}:\n{mat_hex(k)}")

    def encrypt(self):
        if self.round_keys is None:
            QMessageBox.warning(self, "Info", "Generate key dulu bro!")
            return

        pt = self.pt.text()
        ck = self.ck.text()

        if len(pt) != 16 or len(ck) != 16:
            QMessageBox.critical(self, "Error", "HARUS 16 karakter!")
            return

        self.out.clear()

        state = to_matrix(text_to_hex(pt))
        key0 = to_matrix(text_to_hex(ck))

        state = xor(state, key0)
        self.out.append("=== XOR ROUND 0 ===\n" + mat_hex(state) + "\n")

        for r in range(1, 10):
            self.out.append(f"===== ROUND {r} =====")
            state = subbytes(state); self.out.append("\nSubBytes:\n" + mat_hex(state))
            state = shiftrows(state); self.out.append("\nShiftRows:\n" + mat_hex(state))
            state = mixcolumns(state); self.out.append("\nMixColumns:\n" + mat_hex(state))
            state = xor(state, self.round_keys[r]); self.out.append("\nAddRoundKey:\n" + mat_hex(state))

        self.out.append("\n===== ROUND 10 =====")
        state = subbytes(state); self.out.append("\nSubBytes:\n" + mat_hex(state))
        state = shiftrows(state); self.out.append("\nShiftRows:\n" + mat_hex(state))
        state = xor(state, self.round_keys[10]); self.out.append("\nAddRoundKey:\n" + mat_hex(state))

        cipher = "".join(f"{state[r][c]:02X}" for r in range(4) for c in range(4))
        self.out.append("\n=== FINAL CIPHERTEXT ===\n" + cipher)

app = QApplication(sys.argv)
win = AESWindow()
win.show()
sys.exit(app.exec_())
