def print_paper(coords):
    max_x = max(map(lambda c: c[0], coords))
    max_y = max(map(lambda c: c[1], coords))
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')


def fold_paper(coords, fold):
    if fold[0] == 'y':
        def map_coord(c):
            if c[1] < fold[1]:
                return c
            else:
                return c[0], fold[1] * 2 - c[1]
        return set(map(lambda c: map_coord(c), coords))
    else:
        def map_coord(c):
            if c[0] < fold[1]:
                return c
            else:
                return fold[1] * 2 - c[0], c[1]
        return set(map(lambda c: map_coord(c), coords))


if __name__ == '__main__':
    coords = set()
    folds = []
    with open('input') as f:
        read_folds = False
        for line in f:
            if line == '\n':
                read_folds = True
            elif read_folds:
                fold_raw = line.strip().replace('fold along ', '').split('=')[:2]
                folds.append((fold_raw[0], int(fold_raw[1])))
            else:
                coord = tuple(map(int, line.strip().split(',')[:2]))
                coords.add(coord)

    print(coords)
    print(folds)

    # print_paper(coords)
    coords = fold_paper(coords, folds[0])

    for f in folds:
        coords = fold_paper(coords, f)

    print("After folds")
    print_paper(coords)
