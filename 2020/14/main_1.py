from collections import defaultdict


def value_to_write(mask, value):
    bin_str = str(bin(value))[2:].zfill(36)

    ret = ''
    for i in range(36):
        if mask[i] != 'X':
            ret += mask[i]
        else:
            ret += bin_str[i]

    return ret


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    mask = 'X' * 36
    mem = defaultdict(lambda: ''.zfill(36))
    for line in input_list:
        op, _, value = line.partition(' = ')
        if op == 'mask':
            mask = value
        else:
            addr = int(op[4:-1])
            mem[addr] = value_to_write(mask, int(value))

    print(sum([int(mem[m], 2) for m in mem]))
