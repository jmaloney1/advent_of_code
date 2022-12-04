def get_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


if __name__ == '__main__':
    with open('input') as f:
        fully_containing = 0
        for line in f:
            section_1, section_2 = line.strip().split(',')[:2]
            section_1 = tuple(map(int, section_1.split('-')))
            section_2 = tuple(map(int, section_2.split('-')))
            print(section_1)
            print(section_2)

            if section_1[0] <= section_2[0] and section_1[1] >= section_2[1]:
                fully_containing += 1
            elif section_1[0] >= section_2[0] and section_1[1] <= section_2[1]:
                fully_containing += 1

    print(fully_containing)
