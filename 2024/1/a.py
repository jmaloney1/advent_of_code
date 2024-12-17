def main():
    with open("1/input/input") as f:
        lines = f.readlines()

    columns = [], []
    for line in lines:
        line = line.strip().split()
        columns[0].append(int(line[0]))
        columns[1].append(int(line[1]))

    print(columns)

    columns[0].sort()
    columns[1].sort()

    print(columns)

    sum = 0
    for x, y in zip(columns[0], columns[1]):
        sum += abs(y - x)

    print(sum)

if __name__ == "__main__":
    main()