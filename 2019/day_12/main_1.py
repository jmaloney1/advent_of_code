import copy

from day_11.IntCode import IntCode, compute


def main():
    int_code = list(map(int, open('input').readline().split(',')))
    # int_code = list(map(int, sys.stdin.readline().split(',')))

    hull = set()
    painted_once = set()
    robot_posn = (0, 0)
    robot_dir = '^'
    print_hull(hull, robot_dir, robot_posn)

    inp = []
    code = IntCode(copy.copy(int_code), inp)
    while code.position >= 0:
        inp.append((0, 1)[robot_posn in hull])

        colour = compute(code, debug=False)
        if code.position < 0:
            break

        turn = compute(code, debug=False)
        if code.position < 0:
            break

        if colour == 1:
            hull.add(robot_posn)
            painted_once.add(robot_posn)
        elif robot_posn in hull:
            hull.remove(robot_posn)
            painted_once.add(robot_posn)

        if robot_dir == '^':
            if turn == 0:
                robot_dir = '<'
                robot_posn = (robot_posn[0] - 1, robot_posn[1])
            else:
                robot_dir = '>'
                robot_posn = (robot_posn[0] + 1, robot_posn[1])
        elif robot_dir == '>':
            if turn == 0:
                robot_dir = '^'
                robot_posn = (robot_posn[0], robot_posn[1] + 1)
            else:
                robot_dir = 'V'
                robot_posn = (robot_posn[0], robot_posn[1] - 1)
        elif robot_dir == 'V':
            if turn == 0:
                robot_dir = '>'
                robot_posn = (robot_posn[0] + 1, robot_posn[1])
            else:
                robot_dir = '<'
                robot_posn = (robot_posn[0] - 1, robot_posn[1])
        elif robot_dir == '<':
            if turn == 0:
                robot_dir = 'V'
                robot_posn = (robot_posn[0], robot_posn[1] - 1)
            else:
                robot_dir = '^'
                robot_posn = (robot_posn[0], robot_posn[1] + 1)

        print_hull(hull, robot_dir, robot_posn)

    print(len(painted_once))


def print_hull(hull, robot_dir, robot_posn):
    if len(hull) == 0:
        min_y = -2
        max_y = 2
        min_x = -2
        max_x = 2
    else:
        min_y = min(hull, key=lambda x: x[1])[1]
        max_y = max(hull, key=lambda x: x[1])[1]
        min_x = min(hull, key=lambda x: x[0])[0]
        max_x = max(hull, key=lambda x: x[0])[0]
    print('-------------------')
    for y in range(max_y, min_y - 1, -1):
        s = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in hull:
                if (x, y) in hull:
                    s = s + '#'
            elif (x, y) == robot_posn:
                s = s + robot_dir
            else:
                s = s + ' '
        print(s)
    print('-------------------')


if __name__ == '__main__':
    main()
