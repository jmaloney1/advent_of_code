import numpy as np

import util


def search(heightmap, cur, path):
    cur_val = heightmap[cur]
    if cur_val == ord('E'):
        return path

    adj = []
    if cur[1] + 1 < heightmap.shape[1]:
        adj.append((cur[0], cur[1] + 1))

    if cur[1] > 0:
        adj.append((cur[0], cur[1] - 1))

    if cur[0] > 0:
        adj.append((cur[0] - 1, cur[1]))

    if cur[0] + 1 < heightmap.shape[0]:
        adj.append((cur[0] + 1, cur[1]))

    print(adj)
    paths = []
    for a in adj:
        e = heightmap[a]
        is_reachable = 0 <= e - cur_val <= 1
        is_starting_posn = cur_val == ord('S')
        is_new_posn = not (a in path)
        if (is_reachable or is_starting_posn) and is_new_posn:
            paths.append(search(heightmap, a, path + [a]))

    return min(filter(lambda p: not (p is None), paths), key=len, default=None)


if __name__ == '__main__':
    heightmap_raw = []
    for line in util.read_input('test_input_1'):
        heightmap_raw += [(list(map(ord, line.strip())))]

    heightmap = np.array(heightmap_raw)
    print(heightmap)

    start_position = np.where(heightmap == ord('S'))
    start_position = start_position[1][0], start_position[0][0]

    print(start_position)
    visible_count = 0

    print(search(heightmap, start_position, []))
    # for y in range(len(canopy[0])):
    #     for x in range(len(canopy)):
    #         visible = check_tree(matrix, x, y)
    #         if visible:
    #             visible_count += 1
    #             print(f"{(x, y)}")
    #
    # print(visible_count)
