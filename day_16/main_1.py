import itertools

import numpy as np


def main():
    inp = int(open('input').readline().rstrip())

    digits = [int(i) for i in str(inp)]
    size = len(digits)

    original_pattern = [0, 1, 0, -1]

    pattern_matrix = np.zeros([0, size])
    for y in range(0, size):
        pattern = np.repeat(original_pattern, y + 1)
        pattern = np.roll(pattern, -1)

        x = 0
        row = []
        for i in itertools.cycle(pattern):
            if x >= size:
                break
            row.append(i)
            x += 1
        pattern_matrix = np.append(pattern_matrix, [row], axis=0)

    print(pattern_matrix)

    col = np.array([digits]).T
    for i in range(0, 100):
        r = compute_phase(pattern_matrix, col)
        print(f"After phase {i + 1}: {r.T[:, :8]}")
        col = r


def compute_phase(pattern_matrix, col):
    r = np.matmul(pattern_matrix, col)
    r = np.absolute(r)
    for cell in np.nditer(r, op_flags=['readwrite']):
        cell[...] = cell % 10
    return r


if __name__ == '__main__':
    main()
