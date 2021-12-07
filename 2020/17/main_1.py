from collections import defaultdict


def print_grid(grid, d):
    for z in range(d):
        print(f"z={z - (d//2)}")
        for y in range(d):
            for x in range(d):
                c = grid[x, y, z]
                if c:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')


def count_neighbours(grid, x, y, z):
    count = 0
    for z_i in range(z - 1, z + 2):
        for y_i in range(y - 1, y + 2):
            for x_i in range(x - 1, x + 2):
                n = z_i, y_i, z_i
                if (x, y, z) == n:
                    continue
                elif grid[n]:
                    count += 1

    return count


if __name__ == '__main__':
    with open('test_1', 'r') as input:
        input_list = [line.strip() for line in input]

    print(input_list)

    d = len(input_list)

    grid = defaultdict(lambda: False)

    for y, line in enumerate(input_list):
        for x, c in enumerate(line):
            if c == '#':
                grid[(x, y, 1)] = True

    print_grid(grid, d)

    for i in range(6):
        old_grid = grid.copy()
        grid = defaultdict(lambda: False)

        for z in range(d):
            for y in range(d):
                for x in range(d):
                    active = old_grid[(x, y, z)]
                    if active:
                        if count_neighbours(old_grid, x, y, z) in (2, 3):
                            grid[(x, y, z)] = True
                    else:
                        if count_neighbours(old_grid, x, y, z) == 3:
                            grid[(x, y, z)] = True

        print(f"After {i + 1} cycles:")
        print_grid(grid, 3)
