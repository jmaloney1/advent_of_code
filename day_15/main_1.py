import copy
import enum
import random

from day_13.IntCode import IntCode, compute


class Direction(enum.IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


def main():
    int_code = list(map(int, open('input').readline().split(',')))

    next_move = None
    inp = [1]

    def get_input():
        nonlocal next_move
        next_move = inp.pop(0)
        return next_move

    area = dict()
    code = IntCode(copy.copy(int_code), get_input)
    posn = (0, 0)
    while code.position >= 0:
        status = compute(code)
        choices = [Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST]
        if status == 0:
            if next_move == Direction.NORTH:
                area[(posn[0] + 1, posn[1])] = '#'
            elif next_move == Direction.SOUTH:
                area[(posn[0] - 1, posn[1])] = '#'
            elif next_move == Direction.WEST:
                area[(posn[0], posn[1] + 1)] = '#'
            elif next_move == Direction.EAST:
                area[(posn[0], posn[1] - 1)] = '#'

            if (posn[0] + 1, posn[1]) in area and area[(posn[0] + 1, posn[1])] == '#':
                choices.remove(Direction.NORTH)
            elif (posn[0] - 1, posn[1]) in area and area[(posn[0] - 1, posn[1])] == '#':
                choices.remove(Direction.SOUTH)
            elif (posn[0], posn[1] + 1) in area and area[(posn[0], posn[1] + 1)] == '#':
                choices.remove(Direction.WEST)
            elif (posn[0], posn[1] - 1) in area and area[(posn[0], posn[1] - 1)] == '#':
                choices.remove(Direction.EAST)

            inp.append(random.choice(choices))

        elif status == 1:
            area[posn] = '.'
            if next_move == Direction.NORTH:
                posn = (posn[0] + 1, posn[1])
            elif next_move == Direction.SOUTH:
                posn = (posn[0] - 1, posn[1])
            elif next_move == Direction.WEST:
                posn = (posn[0], posn[1] + 1)
            elif next_move == Direction.EAST:
                posn = (posn[0], posn[1] - 1)

            if (posn[0] + 1, posn[1]) in area and area[(posn[0] + 1, posn[1])] == '#':
                choices.remove(Direction.NORTH)
            elif (posn[0] - 1, posn[1]) in area and area[(posn[0] - 1, posn[1])] == '#':
                choices.remove(Direction.SOUTH)
            elif (posn[0], posn[1] + 1) in area and area[(posn[0], posn[1] + 1)] == '#':
                choices.remove(Direction.WEST)
            elif (posn[0], posn[1] - 1) in area and area[(posn[0], posn[1] - 1)] == '#':
                choices.remove(Direction.EAST)

            inp.append(random.choice(choices))

        elif status == 2:
            area[posn] = '.'
            if next_move == Direction.NORTH:
                posn = (posn[0] + 1, posn[1])
            elif next_move == Direction.SOUTH:
                posn = (posn[0] - 1, posn[1])
            elif next_move == Direction.WEST:
                posn = (posn[0], posn[1] + 1)
            elif next_move == Direction.EAST:
                posn = (posn[0], posn[1] - 1)

            area[posn] = 'O'
            break

        print_area(area, posn)

    print('Completed')
    print_area(area, (0, 0))


def print_area(area, posn):
    if len(area) == 0:
        return

    min_x = min(list(map(lambda x: x[0], area)))
    max_x = max(list(map(lambda x: x[0], area)))
    min_y = min(list(map(lambda x: x[1], area)))
    max_y = max(list(map(lambda x: x[1], area)))

    oxygen = None
    print('---------------------')
    for y in range(min_y, max_y + 1):
        s = ''
        for x in range(min_x, max_x + 1):
            if (x, y) == posn:
                s = s + 'D'
            elif (x, y) in area:
                if area[(x, y)] == 'O':
                    oxygen = (x, y)
                s = s + area[(x, y)]
            else:
                s = s + ' '
        print(s)
    print('---------------------')

    print(oxygen)


if __name__ == '__main__':
    main()
