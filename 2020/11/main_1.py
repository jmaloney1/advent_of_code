import copy
import itertools


def print_state(round, state):
    print(f"--------{round}-----------")
    for line in state:
        print(''.join(line))

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
                    for i in range(max(0, y-1), min(len(old_state), y+2)):
                        occupied_count += old_state[i][max(0, x-1):min(len(line), x+2)].count('#')

                    if occupied_count == 0:
                        new_state[y][x] = '#'

                elif posn == '#':
                    occupied_count = -1
                    for i in range(max(0, y-1), min(len(old_state), y+2)):
                        occupied_count += old_state[i][max(0, x-1):min(len(line), x+2)].count('#')

                    if occupied_count >= 4:
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
