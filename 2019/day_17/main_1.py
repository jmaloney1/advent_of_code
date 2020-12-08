from day_13.IntCode import IntCode, compute


def main():
    code = [int(d) for d in open('input').readline().rstrip().split(',')]
    int_code = IntCode(code, lambda: 0)

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


def print_view(view: set, intersections: set, posn):
    max_x = max(map(lambda t: t[0], view))
    max_y = max(map(lambda t: t[1], view))

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


if __name__ == '__main__':
    main()
