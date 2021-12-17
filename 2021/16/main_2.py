import operator
from functools import reduce


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
    i, header_version, type_id = read_header(i, packets)
    print(f"version: {header_version} type_id: {type_id}")
    number = None
    if type_id == 4:
        number, i = read_number(i, packets)
    else:
        length_id = packets[i]
        i += 1
        numbers = []
        if length_id == 0:
            num_bits = bit_str_to_int(packets[i:i + 15])
            i += 15
            start_i = i
            while i < start_i + num_bits:
                number, i = read_packet(i, packets)
                numbers.append(number)
        elif length_id == 1:
            num_packets = bit_str_to_int(packets[i:i + 11])
            i += 11
            for s in range(num_packets):
                number, i = read_packet(i, packets)
                numbers.append(number)

        if type_id == 0:
            number = sum(numbers)
        elif type_id == 1:
            number = reduce(operator.mul, numbers)
        elif type_id == 2:
            number = min(numbers)
        elif type_id == 3:
            number = max(numbers)
        elif type_id == 5:
            number = (0, 1)[numbers[0] > numbers[1]]
        elif type_id == 6:
            number = (0, 1)[numbers[0] < numbers[1]]
        elif type_id == 7:
            number = (0, 1)[numbers[0] == numbers[1]]

    return number, i


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
        number, i = read_packet(0, packets)

        print(number)
