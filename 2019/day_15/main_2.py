distance_map = dict()
full_map = dict()


def dfs(visited: dict, posn, count):
    visited[posn] = True
    # we hit a wall
    if full_map[posn] == '#':
        return

    full_map[posn] = '*'

    print_area(full_map)

    if posn not in distance_map or count < distance_map[posn]:
        distance_map[posn] = count

    adj = [
        (posn[0] + 1, posn[1]),
        (posn[0] - 1, posn[1]),
        (posn[0], posn[1] + 1),
        (posn[0], posn[1] - 1)
    ]
    for a in adj:
        if a not in visited:
            dfs(visited, a, 1 + count)


def main():
    char_map = list([line.rstrip() for line in open('full_map')])

    oxygen = None
    for y, line in enumerate(char_map):
        for x, char in enumerate(line):
            full_map[(x, y)] = char
            if char == 'O':
                oxygen = (x, y)

    dfs({}, oxygen, 0)

    print(distance_map)

    print(max(distance_map.values()))


def print_area(area):
    if len(area) == 0:
        return

    min_x = min(list(map(lambda x: x[0], area)))
    max_x = max(list(map(lambda x: x[0], area)))
    min_y = min(list(map(lambda x: x[1], area)))
    max_y = max(list(map(lambda x: x[1], area)))

    print('---------------------')
    for y in range(min_y, max_y + 1):
        s = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in area:
                s = s + str(area[(x, y)])
            else:
                s = s + ' '
        print(s)
    print('---------------------')


if __name__ == '__main__':
    main()
