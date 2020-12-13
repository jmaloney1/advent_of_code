if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [(line.strip()[0], int(line.strip()[1:])) for line in input]

    direction_order = ['N', 'E', 'S', 'W']
    direction = 1
    waypoint = 10, 1
    posn = 0, 0
    for instruction in input_list:
        print(f"{direction_order[direction]} posn: {posn} waypoint: {waypoint}")
        print(instruction)
        if instruction[0] in ['L', 'R']:
            rot = instruction[1] % 360
            if instruction[0] == 'L':
                rot = 360 - rot
            num_rot = int(rot / 90)
            new_direction = (direction + num_rot) % len(direction_order)
            # 90 clockwise
            if num_rot == 1:
                waypoint = waypoint[1], -waypoint[0]
            # 180 clockwise
            elif num_rot == 2:
                waypoint = -waypoint[0], -waypoint[1]
            # 270 clockwise
            elif num_rot == 3:
                waypoint = -waypoint[1], waypoint[0]

            direction = new_direction

        elif instruction[0] == 'F':
            posn = posn[0] + instruction[1] * waypoint[0], posn[1] + instruction[1] * waypoint[1]
        elif instruction[0] in direction_order:
            if instruction[0] in ['N', 'S']:
                d = (1, -1)[instruction[0] == 'S']
                waypoint = waypoint[0], waypoint[1] + instruction[1] * d
            elif instruction[0] in ['E', 'W']:
                d = (1, -1)[instruction[0] == 'W']
                waypoint = waypoint[0] + instruction[1] * d, waypoint[1]

    print(direction_order[direction], posn)
    print(abs(posn[0]) + abs(posn[1]))
