if __name__ == '__main__':
    with open('input') as f:
        count = 0
        cals = []
        for line in f:
            if str(line) == '\n':
                cals.append(count)
                count = 0
            else:
                count += int(line)

    print(max(cals))
