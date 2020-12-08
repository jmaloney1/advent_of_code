def main():
    inp = open('input').readline().rstrip()

    digits_1 = [int(i) for i in str(inp)]

    digits = digits_1 * 10000
    offset = int(''.join(list(map(str, digits[:7]))))

    col = digits
    for i in range(0, 100):
        col = compute_phase(col)
        print(f"After phase {i + 1}: {col}")

    print(f"Offset: {offset}")
    print(col[offset:offset + 8])


def compute_phase(inp):
    r = list()
    r.append(inp[-1])
    for i in range(1, len(inp)):
        x = abs((inp[-i - 1] + r[i - 1]) % 10)
        r.append(x)

    r.reverse()
    return r


if __name__ == '__main__':
    main()
