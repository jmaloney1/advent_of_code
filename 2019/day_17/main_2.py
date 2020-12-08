import copy
import enum
import itertools
import re

from day_13.IntCode import IntCode, compute


class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def main():
    code = [int(d) for d in open('input').readline().rstrip().split(',')]
    int_code = IntCode(copy.copy(code), lambda: 0)

    # print and save scaffolding
    view = set()
    posn = (0, 0)
    starting_posn = None
    while True:
        c = chr(compute(int_code))

        if int_code.position < 0:
            break

        print(c, end='')
        if c == '\n':
            posn = (0, posn[1] + 1)
        else:
            if c != '.':
                if c != '#':
                    starting_posn = posn
                view.add(posn)
            posn = (posn[0] + 1, posn[1])

    def has_intersection(posn: tuple) -> bool:
        north_in_view = (posn[0], posn[1] + 1) in view
        south_in_view = (posn[0], posn[1] - 1) in view
        west_in_view = (posn[0] - 1, posn[1]) in view
        east_in_view = (posn[0] + 1, posn[1]) in view
        return north_in_view and south_in_view and west_in_view and east_in_view

    intersections = set(filter(has_intersection, view))

    print_view(view, intersections, starting_posn)

    alignment = sum(map(lambda t: t[0] * t[1], intersections))
    print(f"Sum of alignment parameters: {alignment}")

    pattern = generate(view, starting_posn)

    single_pattern = []
    for p in pattern:
        m = re.search(r"[A-Z]", str(p))
        if m:
            single_pattern.append(p)
        else:
            single_pattern.append(str(chr(ord('a') + p)))


    print(convert_back(single_pattern))

    pat = pattern_to_str(single_pattern)
    print(pat)

    best_split = None
    saved = 0
    for i in range(1, 7):
        p = pat[:i]
        p_temp = pat.split(pattern_to_str(p))
        if len(p_temp) * len(p) > saved:
            best_split = p

    pat = 'A'.join(pat.split(pattern_to_str(best_split)))
    print(pattern_to_str(convert_back(pat)))
    movement_function_a = list(map(ord, ','.join(best_split) + '\n'))
    print(f"A: {convert_back(best_split)}")

    best_split = None
    saved = 0
    for i in range(2, 8):
        p = pat[1:i]
        p_temp = pat.split(pattern_to_str(p))
        if len(p_temp) * len(p) > saved:
            best_split = p

        print(p_temp)

    pat = 'B'.join(pat.split(pattern_to_str(best_split)))
    print(pattern_to_str(convert_back(pat)))
    movement_function_b = list(map(ord, ','.join(best_split) + '\n'))
    print(f"B: {convert_back(best_split)}")

    code[0] = 2
    main_routine = list(map(ord, 'A,A,A,A,A,A,A,A,A,A\n'))
    #movement_function_a = list(map(ord, 'R,1,1,1,1,1\n'))
    #movement_function_b = list(map(ord, 'R,1,1,1,1,1\n'))
    movement_function_c = list(map(ord, 'R,1,1,1,1,1\n'))
    video_feed = list(map(ord, 'y\n'))

    inp = main_routine + movement_function_a + movement_function_b + movement_function_c + video_feed

    def get_input():
        return inp.pop(0)

    int_code = IntCode(copy.copy(code), get_input)

    while True:
        c = chr(compute(int_code))

        if int_code.position < 0:
            break

        print(c, end='')


def convert_back(p):
    r = []
    for i in p:
        if i.isalpha() and i.isupper():
            r.append(i)
        else:
            r.append(ord(i) - ord('a'))

    return r


def pattern_to_str(p):
    return ''.join(list(map(str, p)))


def generate(view: set, posn):

    out = []
    posn = posn
    direction = Direction.NORTH
    while True:
        r, direction, posn = generate_simple(view, posn, direction)
        if r == -1:
            break
        out = out + r

    print(out)

    return out


def generate_simple(view: set, posn, direction: Direction):
    dir_posns = {
        Direction.NORTH: (posn[0], posn[1] - 1),
        Direction.SOUTH: (posn[0], posn[1] + 1),
        Direction.WEST: (posn[0] - 1, posn[1]),
        Direction.EAST: (posn[0] + 1, posn[1])
    }

    left = Direction((direction - 1) % 4)
    right = Direction((direction + 1) % 4)

    direction = None
    out = []
    if dir_posns[right] in view:
        out.append('R')
        direction = right
    elif dir_posns[left] in view:
        out.append('L')
        direction = left
    else:
        return -1, None, None

    def generate_distance():
        for i in itertools.count(start=1):
            if direction == Direction.NORTH and (posn[0], posn[1] - (i + 1)) not in view:
                out.append(i)
                return posn[0], posn[1] - i
            elif direction == Direction.SOUTH and (posn[0], posn[1] + (i + 1)) not in view:
                out.append(i)
                return posn[0], posn[1] + i
            elif direction == Direction.WEST and (posn[0] - (i + 1), posn[1]) not in view:
                out.append(i)
                return posn[0] - i, posn[1]
            elif direction == Direction.EAST and (posn[0] + (i + 1), posn[1]) not in view:
                out.append(i)
                return posn[0] + i, posn[1]

    return out, direction, generate_distance()


def print_view(view: set, intersections: set, posn):
    max_x = max(map(lambda t: t[0], view))
    max_y = max(map(lambda t: t[1], view))

    print('------------------------------------')
    for y in range(max_y + 1):
        s = ''
        for x in range(max_x + 1):
            if (x, y) == posn:
                s = s + '@'
            elif (x, y) in intersections:
                s = s + 'O'
            elif (x, y) in view:
                s = s + '#'
            else:
                s = s + ' '
        print(s)
    print('------------------------------------')


if __name__ == '__main__':
    main()
