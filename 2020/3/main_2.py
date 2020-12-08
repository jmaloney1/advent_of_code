def check_slope(delta_x, delta_y, input_list):
    posn = 0
    max_length = len(input_list[0])
    trees = 0
    for i, line in enumerate(input_list):
        if i % delta_y != 0:
            # print(f"{line}")
            continue

        c = "O"
        if line[posn] == "#":
            trees = trees + 1
            c = "X"

        # print(f"{line[:posn]}{c}{line[posn + 1:]}")

        posn = (posn + delta_x) % max_length
    # print(trees)

    return trees


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    result = 1

    v = check_slope(1, 1, input_list)
    print(v)
    result = result * v

    v = check_slope(3, 1, input_list)
    print(v)
    result = result * v

    v = check_slope(5, 1, input_list)
    print(v)
    result = result * v

    v = check_slope(7, 1, input_list)
    print(v)
    result = result * v

    v = check_slope(1, 2, input_list)
    print(v)
    result = result * v

    print(result)
