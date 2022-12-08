import util
import numpy as np


def check_tree(canopy, x, y):
    tree = canopy[y, x]
    # from top
    top = list(reversed(canopy.T[x, :y].tolist()))
    # from bottom
    bottom = (canopy.T[x, (y+1):])
    # from left
    left = list(reversed(canopy[y, :x].tolist()))
    # from right
    right = (canopy[y, (x+1):])

    scenic_score = 1
    for l in [top, bottom, left, right]:
        # print(l)
        score = next((i for i, v in enumerate(l) if tree <= v), len(l) - 1) + 1
        scenic_score *= score

    return scenic_score


if __name__ == '__main__':
    canopy = []
    for line in util.read_input('input'):
        canopy += [(list(map(int, line.strip())))]

    matrix = np.array(canopy)
    print(matrix)

    max_scenic_score = 0
    for y in range(len(canopy[0])):
        for x in range(len(canopy)):
            max_scenic_score = max(check_tree(matrix, x, y), max_scenic_score)

    print(max_scenic_score)
