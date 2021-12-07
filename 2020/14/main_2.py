from collections import defaultdict


def expand_addr(mask, mem_addr):
    bin_str = str(bin(mem_addr))[2:].zfill(36)

    ret = ''
    for i in range(36):
        if mask[i] == '0':
            ret += bin_str[i]
        else:
            ret += mask[i]

    addrs_to_expand = [ret]
    while len(addrs_to_expand) > 0:
        addr = addrs_to_expand.pop()
        for i in range(36):
            if addr[i] == 'X':
                addrs_to_expand.append(addr[:i] + '0' + addr[i+1:])
                addrs_to_expand.append(addr[:i] + '1' + addr[i+1:])
                break

        if 'X' not in addr:
            yield int(addr, 2)


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
            for a in expand_addr(mask, addr):
                print(a)
                mem[a] = value

    print(sum(map(int, mem.values())))
