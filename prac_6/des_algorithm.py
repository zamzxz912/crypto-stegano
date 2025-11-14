import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

PC_1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC_2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

SBOX = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def str_to_bits(s: str) -> str:
    return ''.join(format(b, '08b') for b in s.encode('utf-8', errors='ignore'))

def bits_to_hex(bstr: str) -> str:
    if not bstr:
        return ''
    hex_len = (len(bstr) + 3) // 4
    return format(int(bstr, 2), '0{}X'.format(hex_len))

def permute(bits: str, table: list) -> str:
    return ''.join(bits[i-1] for i in table)

def left_shift(bits: str, n: int) -> str:
    return bits[n:] + bits[:n]

def xor_bits(a: str, b: str) -> str:
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def sbox_substitute(bits48: str) -> str:
    out = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = SBOX[i][row][col]
        out.append(format(val, '04b'))
    return ''.join(out)

def generate_subkeys(key8: str):
    if len(key8) < 8:
        key8 = key8 + '\x00'*(8-len(key8))
    elif len(key8) > 8:
        key8 = key8[:8]
    key_bits = str_to_bits(key8)  # 64 bits
    key56 = permute(key_bits, PC_1)
    C = key56[:28]
    D = key56[28:]
    C0, D0 = C, D
    subkeys = []
    C_vals = [C0]
    D_vals = [D0]
    for s in SHIFTS:
        C = left_shift(C, s)
        D = left_shift(D, s)
        C_vals.append(C)
        D_vals.append(D)
        sub = permute(C + D, PC_2)
        subkeys.append(sub)
    return {
        'C0': C0, 'D0': D0, 'C_vals': C_vals, 'D_vals': D_vals, 'subkeys': subkeys
    }

def des_encrypt_block(block64: str, subkeys: list) -> str:
    ip = permute(block64, IP)
    L = ip[:32]
    R = ip[32:]
    for i in range(16):
        expanded = permute(R, E)
        x = xor_bits(expanded, subkeys[i])
        s_out = sbox_substitute(x)
        p_out = permute(s_out, P)
        newR = xor_bits(L, p_out)
        L = R
        R = newR
    preoutput = R + L
    cipher64 = permute(preoutput, FP)
    return cipher64

def pkcs7_pad(data_bytes: bytes, block_size=8) -> bytes:
    pad_len = block_size - (len(data_bytes) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data_bytes + bytes([pad_len])*pad_len

def des_encrypt(plaintext: str, key: str):
    ks = generate_subkeys(key)
    subkeys = ks['subkeys']
    C0 = ks['C0']; D0 = ks['D0']
    p_bytes = plaintext.encode('utf-8', errors='ignore')
    p_padded = pkcs7_pad(p_bytes, 8)
    blocks = []
    all_cipher_bits = ''
    for i in range(0, len(p_padded), 8):
        block = p_padded[i:i+8]
        block_bits = ''.join(format(b,'08b') for b in block)
        cipher64 = des_encrypt_block(block_bits, subkeys)
        all_cipher_bits += cipher64
        blocks.append({
            'index': i//8 + 1,
            'plain_bits': block_bits,
            'cipher_bits': cipher64,
            'cipher_hex': bits_to_hex(cipher64)
        })
    result = {
        'C0': C0, 'D0': D0, 'C_vals': ks['C_vals'], 'D_vals': ks['D_vals'],
        'subkeys': subkeys, 'blocks': blocks, 'cipher_all': all_cipher_bits
    }
    return result

class DESGui:
    def __init__(self, root):
        self.root = root
        root.title("DES Encryptor")
        root.geometry("1150x800")
        root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        header = ttk.Label(root, text="DES Encryptor (DES-64)", font=("Segoe UI", 16, "bold"))
        header.pack(pady=8)

        frm_inputs = ttk.Frame(root, padding=8)
        frm_inputs.pack(fill='x')

        ttk.Label(frm_inputs, text="Plaintext:").grid(row=0, column=0, sticky='w')
        self.txt_plain = tk.Text(frm_inputs, height=3, width=70, font=("Consolas", 11))
        self.txt_plain.grid(row=0, column=1, padx=6)

        ttk.Label(frm_inputs, text="Key (max 8 chars):").grid(row=1, column=0, sticky='w', pady=6)
        self.ent_key = ttk.Entry(frm_inputs, width=20, font=("Consolas", 11))
        self.ent_key.grid(row=1, column=1, sticky='w', padx=6)

        btn_frame = ttk.Frame(frm_inputs)
        btn_frame.grid(row=1, column=2, padx=6)
        self.btn_encrypt = ttk.Button(btn_frame, text="ENCRYPT", command=self.on_encrypt)
        self.btn_encrypt.pack()

        sep = ttk.Separator(root, orient='horizontal')
        sep.pack(fill='x', pady=8)

        frame_out = ttk.Frame(root)
        frame_out.pack(fill='both', expand=True, padx=8)

        left = ttk.Frame(frame_out)
        left.grid(row=0, column=0, sticky='ns', padx=6)

        ttk.Label(left, text="C0 (28 bits):", font=("Segoe UI", 10, "bold")).pack(anchor='w')
        self.txt_c0 = tk.Text(left, width=44, height=2, font=("Consolas", 10))
        self.txt_c0.pack(pady=4)
        self.txt_c0.configure(state='disabled')

        ttk.Label(left, text="D0 (28 bits):", font=("Segoe UI", 10, "bold")).pack(anchor='w')
        self.txt_d0 = tk.Text(left, width=44, height=2, font=("Consolas", 10))
        self.txt_d0.pack(pady=4)
        self.txt_d0.configure(state='disabled')

        ttk.Label(left, text="Rounds (C1..C16, D1..D16, K1..K16):", font=("Segoe UI", 10, "bold")).pack(anchor='w', pady=(6,0))
        self.txt_rounds = scrolledtext.ScrolledText(left, width=44, height=22, font=("Consolas", 10))
        self.txt_rounds.pack(pady=4)
        self.txt_rounds.configure(state='disabled')

        right = ttk.Frame(frame_out)
        right.grid(row=0, column=1, sticky='ns', padx=6)

        ttk.Label(right, text="Ciphertext (Binary):", font=("Segoe UI", 10, "bold")).pack(anchor='w')
        self.txt_cipher_bin = scrolledtext.ScrolledText(right, width=64, height=12, font=("Consolas", 10))
        self.txt_cipher_bin.pack(pady=4)
        self.txt_cipher_bin.configure(state='disabled')

        ttk.Label(right, text="Ciphertext (Hex):", font=("Segoe UI", 10, "bold")).pack(anchor='w', pady=(6,0))
        self.txt_cipher_hex = scrolledtext.ScrolledText(right, width=64, height=4, font=("Consolas", 10))
        self.txt_cipher_hex.pack(pady=4)
        self.txt_cipher_hex.configure(state='disabled')

        ttk.Label(right, text="Ciphertext (ASCII):", font=("Segoe UI", 10, "bold")).pack(anchor='w')
        self.txt_cipher_ascii = scrolledtext.ScrolledText(right, width=64, height=4, font=("Consolas", 10))
        self.txt_cipher_ascii.pack(pady=4)
        self.txt_cipher_ascii.configure(state='disabled')

        ttk.Label(right, text="Per-block details:", font=("Segoe UI", 10, "bold")).pack(anchor='w', pady=(6,0))
        self.txt_blocks = scrolledtext.ScrolledText(right, width=64, height=8, font=("Consolas", 10))
        self.txt_blocks.pack(pady=4)
        self.txt_blocks.configure(state='disabled')

        self.lbl_status = ttk.Label(root, text="Ready", foreground="green")
        self.lbl_status.pack(pady=6)

    def on_encrypt(self):
        plain = self.txt_plain.get("1.0", "end-1c")
        key = self.ent_key.get()
        if plain.strip() == "":
            messagebox.showwarning("Empty plaintext", "Please enter plaintext to encrypt.")
            return
        if key is None:
            key = ""
        if len(key) > 8:
            messagebox.showinfo("Key truncated", "Key longer than 8 chars — will be truncated to 8 chars.")
            key = key[:8]

        try:
            result = des_encrypt(plain, key)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")
            return

        def group_bits_space(s: str, n=7):
            return ' '.join(s[i:i+n] for i in range(0, len(s), n))

        def format_k_bits_commas(s: str, per_line=24):
            bits = [c for c in s]
            parts = []
            for i in range(0, len(bits), per_line):
                chunk = bits[i:i+per_line]
                parts.append(', '.join(chunk))
            return ',\n'.join(parts)

        self.txt_c0.configure(state='normal'); self.txt_c0.delete('1.0', tk.END)
        self.txt_c0.insert(tk.END, group_bits_space(result['C0'], 7))
        self.txt_c0.configure(state='disabled')

        self.txt_d0.configure(state='normal'); self.txt_d0.delete('1.0', tk.END)
        self.txt_d0.insert(tk.END, group_bits_space(result['D0'], 7))
        self.txt_d0.configure(state='disabled')

        self.txt_rounds.configure(state='normal'); self.txt_rounds.delete('1.0', tk.END)
        C_vals = result.get('C_vals', [])
        D_vals = result.get('D_vals', [])
        subkeys = result.get('subkeys', [])
        for i in range(1, 17):
            Ci = C_vals[i] if i < len(C_vals) else ''
            Di = D_vals[i] if i < len(D_vals) else ''
            Ki = subkeys[i-1] if i-1 < len(subkeys) else ''
            c_form = '[' + ' '.join(Ci) + ']'
            d_form = '[' + ' '.join(Di) + ']'
            if Ki:
                k_commas = '[{}]'.format(format_k_bits_commas(Ki, per_line=24))
            else:
                k_commas = '[]'
            self.txt_rounds.insert(tk.END, f"C{i} = {c_form}\n")
            self.txt_rounds.insert(tk.END, f"D{i} = {d_form}\n")
            self.txt_rounds.insert(tk.END, f"K{i} = {k_commas}\n\n")
        self.txt_rounds.configure(state='disabled')

        full_bin = result['cipher_all']
        full_hex = bits_to_hex(full_bin)
        bin_grouped = ' '.join(full_bin[i:i+8] for i in range(0, len(full_bin), 8))
        self.txt_cipher_bin.configure(state='normal'); self.txt_cipher_bin.delete('1.0', tk.END)
        self.txt_cipher_bin.insert(tk.END, bin_grouped)
        self.txt_cipher_bin.configure(state='disabled')

        if len(full_hex) % 2 == 1:
            full_hex = '0' + full_hex
        hex_grouped = ' '.join(full_hex[i:i+2] for i in range(0, len(full_hex), 2))
        self.txt_cipher_hex.configure(state='normal'); self.txt_cipher_hex.delete('1.0', tk.END)
        self.txt_cipher_hex.insert(tk.END, hex_grouped)
        self.txt_cipher_hex.configure(state='disabled')

        ascii_text = ""
        for i in range(0, len(full_bin), 8):
            byte = full_bin[i:i + 8]
            if len(byte) == 8:
                ascii_text += chr(int(byte, 2))

        self.txt_cipher_ascii.configure(state='normal')
        self.txt_cipher_ascii.delete('1.0', tk.END)
        self.txt_cipher_ascii.insert(tk.END, ascii_text)
        self.txt_cipher_ascii.configure(state='disabled')

        self.txt_blocks.configure(state='normal'); self.txt_blocks.delete('1.0', tk.END)
        for b in result['blocks']:
            plain_g = ' '.join(b['plain_bits'][i:i+8] for i in range(0, len(b['plain_bits']), 8))
            cipher_g = ' '.join(b['cipher_bits'][i:i+8] for i in range(0, len(b['cipher_bits']), 8))
            self.txt_blocks.insert(tk.END, f"Block {b['index']}:\n")
            self.txt_blocks.insert(tk.END, f"  Plain (bin): {plain_g}\n")
            self.txt_blocks.insert(tk.END, f"  Cipher(bin): {cipher_g}\n")
            hx = b['cipher_hex']
            if len(hx) % 2 == 1: hx = '0' + hx
            self.txt_blocks.insert(tk.END, f"  Cipher(hex): {' '.join(hx[i:i+2] for i in range(0,len(hx),2))}\n\n")
        self.txt_blocks.configure(state='disabled')

        self.lbl_status.config(text=f"Encrypted {len(result['blocks'])} block(s). (PKCS#7 padding applied if needed)")

def main():
    root = tk.Tk()
    app = DESGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
