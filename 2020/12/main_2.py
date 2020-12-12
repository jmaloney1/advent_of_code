import copy
import itertools


def print_state(round, state):
    print(f"--------{round}-----------")
    for line in state:
        print(''.join(line))


def check_direction(x, y, delta_x, delta_y, old_state):
    for delta in itertools.count(1):
        x_1 = x + (delta_x * delta)
        y_1 = y + (delta_y * delta)
        if 0 <= x_1 < len(old_state[0]) and 0 <= y_1 < len(old_state):
            if old_state[y_1][x_1] == '#':
                return True
            elif old_state[y_1][x_1] == 'L':
                return False
        else:
            return False

    return False


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [list(line.strip()) for line in input]

    old_state = input_list
    print_state(0, old_state)

    for round in itertools.count(1):
        new_state = []
        for line in old_state:
            new_state.append(copy.deepcopy(line))

        for y, line in enumerate(old_state):
            for x, posn in enumerate(line):
                if posn == 'L':
                    occupied_count = 0
                    for (delta_x, delta_y) in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                        if check_direction(x, y, delta_x, delta_y, old_state):
                            occupied_count += 1

                    if occupied_count == 0:
                        new_state[y][x] = '#'

                elif posn == '#':
                    occupied_count = 0
                    for (delta_x, delta_y) in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                        if check_direction(x, y, delta_x, delta_y, old_state):
                            occupied_count += 1

                    if occupied_count >= 5:
                        new_state[y][x] = 'L'


        print_state(round, new_state)
        same = True
        for y, line in enumerate(new_state):
            for x, posn in enumerate(line):
                if old_state[y][x] != posn:
                    old_state = copy.deepcopy(new_state)
                    same = False

        if same:
            count = 0
            for line in new_state:
                count += line.count('#')
            print(count)
            break


