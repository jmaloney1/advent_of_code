if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [(line.strip()[0], int(line.strip()[1:])) for line in input]

    direction_order = ['N', 'E', 'S', 'W']
    direction = 1
    posn = 0, 0
    for instruction in input_list:
        print(direction_order[direction], posn)
        print(instruction)
        if instruction[0] in ['L', 'R']:
            rot = (1, -1)[instruction[0] == 'L']
            direction = (int(instruction[1] / (rot * 90)) + direction) % len(direction_order)
        elif instruction[0] == 'F':
            if direction_order[direction] in ['N', 'S']:
                d = (1, -1)[direction_order[direction] == 'S']
                posn = posn[0], posn[1] + instruction[1] * d
            elif direction_order[direction] in ['E', 'W']:
                d = (1, -1)[direction_order[direction] == 'W']
                posn = posn[0] + instruction[1] * d, posn[1]
        elif instruction[0] in direction_order:
            if instruction[0] in ['N', 'S']:
                d = (1, -1)[instruction[0] == 'S']
                posn = posn[0], posn[1] + instruction[1] * d
            elif instruction[0] in ['E', 'W']:
                d = (1, -1)[instruction[0] == 'W']
                posn = posn[0] + instruction[1] * d, posn[1]

    print(direction_order[direction], posn)
    print(abs(posn[0]) + abs(posn[1]))
