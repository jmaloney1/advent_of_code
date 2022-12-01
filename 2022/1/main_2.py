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

    top_3 = sorted(cals, reverse=True)[:3]
    print(top_3)
    print(sum(top_3))
