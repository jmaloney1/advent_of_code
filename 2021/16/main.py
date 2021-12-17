def read_number(i, packets):
    num_str = ''
    while True:
        start_bit = packets[i]
        i += 1
        num_str += ''.join(map(str, packets[i:i + 4]))
        if start_bit == 0:
            return bit_str_to_int(num_str), i + 4

        i += 4


def bit_str_to_int(p):
    return int(''.join(map(str, p)), 2)


def read_header(i, packets):
    header_version = bit_str_to_int(packets[i:i + 3])
    i += 3
    type_id = bit_str_to_int(packets[i:i + 3])
    i += 3
    return i, header_version, type_id


def read_packet(i, packets):
    global version_total
    i, header_version, type_id = read_header(i, packets)
    version_total += header_version
    print(f"version: {header_version} type_id: {type_id}")
    if type_id == 4:
        number, i = read_number(i, packets)

    else:
        length_id = packets[i]
        i += 1
        if length_id == 0:
            num_bits = bit_str_to_int(packets[i:i + 15])
            i += 15
            start_i = i
            while i < start_i + num_bits:
                i = read_packet(i, packets)
        elif length_id == 1:
            num_packets = bit_str_to_int(packets[i:i + 11])
            i += 11
            for s in range(num_packets):
                i = read_packet(i, packets)

    return i


if __name__ == '__main__':
    with open('input') as f:
        l = f.readline().strip()
        packets = []
        for c in l:
            p = list(map(int, str(bin(int(c, 16)))[2:]))
            p = [0] * (4 - len(p)) + p
            packets += p

        print(packets)
        print(hex(int(''.join(map(str, packets)), 2)))
        i = 0

        version_total = 0
        read_packet(0, packets)

        print(version_total)
