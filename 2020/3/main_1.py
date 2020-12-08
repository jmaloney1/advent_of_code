if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    posn = 0
    max_length = len(input_list[0])
    trees = 0
    for i, line in enumerate(input_list):
        c = "O"
        if line[posn] == "#":
            trees = trees + 1
            c = "X"

        print(f"{line[:posn]}{c}{line[posn+1:]}")

        posn = (posn + 3) % max_length

    print(trees)
