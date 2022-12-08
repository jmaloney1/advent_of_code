import util
import numpy as np


def check_tree(canopy, x, y):
    tree = canopy[y, x]
    # from top
    top = canopy.T[x, :y].tolist()
    # from bottom
    bottom = list(reversed(canopy.T[x, (y+1):]))
    # from left
    left = canopy[y, :x].tolist()
    # from right
    right = list(reversed(canopy[y, (x+1):]))

    for l in [top, bottom, left, right]:
        print(l)
        if len(list(filter(lambda t: tree <= t, l))) == 0:
            return True
    return False


if __name__ == '__main__':
    canopy = []
    for line in util.read_input('input'):
        canopy += [(list(map(int, line.strip())))]

    matrix = np.array(canopy)
    print(matrix)

    visible_count = 0
    for y in range(len(canopy[0])):
        for x in range(len(canopy)):
            visible = check_tree(matrix, x, y)
            if visible:
                visible_count += 1
                print(f"{(x, y)}")

    print(visible_count)
