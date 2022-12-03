def get_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


if __name__ == '__main__':
    with open('input') as f:
        total = 0
        f_iter = iter(f)
        while True:
            try:
                line_1 = set(next(f_iter).strip())
                line_2 = set(next(f_iter).strip())
                line_3 = set(next(f_iter).strip())
                badge = line_1.intersection(line_2).intersection(line_3)
                print(badge)
                total += get_priority(badge.pop())

            except StopIteration:
                break

        print(total)
