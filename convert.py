def conv_hex(inp_hex):
    return [int(b, 16) for b in inp_hex.split()]

def xor_arr(hex_arr):
    if not hex_arr:
        return []
    pjg = len(hex_arr[0])
    xor_hsl = []
    for idx in range(pjg):
        val = hex_arr[0][idx]
        for j in range(1, len(hex_arr)):
            val ^= hex_arr[j][idx]
        xor_hsl.append(val)
    return xor_hsl

num_blocks = int(input("block total: "))
all_blocks = []
for block_idx in range(num_blocks):
    user_hex = input("block %d: " % (block_idx + 1))
    all_blocks.append(conv_hex(user_hex))

fin_res = xor_arr(all_blocks)

print("result_hex:", " ".join("{:02X}".format(b) for b in fin_res))
print("result_ascii:", "".join(chr(b) if 32 <= b <= 126 else "." for b in fin_res))