
# get input file
while True:
    file_in = input('Input file: ')
    if not file_in:
        file_in = 'iof/f_test.bin'
    try:
        with open(file_in, 'r') as ftest:
            break
    except FileNotFoundError:
        print('Can not find the file, try again, pls.')

# trans bytes to binary
new_byte_list = []
with open(file_in, 'rb') as fi:
    rd_n = 0
    while True:
        rd_1B = fi.read(1)
        if not rd_1B:
            print(f'Read Done. {rd_n}B.')
            break
        rd_n = rd_n + 1
        int_1B = int(rd_1B.hex(), 16)
        # print('byte{:0>2d}: 0x{:0>2X}'.format(rd_n, int_1B))
        # separate 4bit|4bit
        byte_h4bit = (int_1B >> 4) &0x0f
        byte_l4bit = int_1B &0x0f
        # 0biqiq --> 0biq00_iq00
        bh_x1B = ((byte_h4bit << 4) ^(byte_h4bit << 2)) &0b11001100
        bl_x1B = ((byte_l4bit << 4) ^(byte_l4bit << 2)) &0b11001100
        print('byte{:0>2d}: 0x{:0>2x}\n{:0>4b}_{:0>4b} --> {:0>8b}_{:0>8b}'\
            .format(rd_n, int_1B, byte_h4bit, byte_l4bit, bh_x1B, bl_x1B))
        new_byte_list.append(bh_x1B)
        new_byte_list.append(bl_x1B)

# write in file
for c in reversed(range(len(file_in))):
    if file_in[c] == '.':
        file_out = file_in[:c] + '_iq00' + file_in[c:]

with open(file_out, 'wb') as fo:
    for new_byte in new_byte_list:
        fo.write(bytes([new_byte]))
    len_nbl = len(new_byte_list)
    print(f'Write Done. {len_nbl}B. Output file: {file_out}')

print('E N D\n')
