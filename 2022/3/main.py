import math


def get_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


if __name__ == '__main__':
    with open('input') as f:
        total = 0
        for line in f:
            line = line.strip()
            half = math.floor(len(line) / 2)
            p1 = set(line[:half])
            p2 = set(line[half:])
            p_int = p1.intersection(p2)
            values = sum(map(get_priority, p_int))
            print(values)
            total += values

        print(total)
