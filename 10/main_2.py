import copy
import math


def main():
    # asteroids = [line.rstrip() for line in sys.stdin]
    asteroids = [line.rstrip() for line in open('input')]

    asteroid_posns = set()

    letters = dict()
    for y, line in enumerate(asteroids):
        for x, point in enumerate(line):
            if point != '#':
                continue

            asteroid_posns.add((x, y))
            letters[(x, y)] = chr(x * y + x + 97)

    #print(asteroid_posns)

    for y, line in enumerate(asteroids):
        s = ''
        for x, point in enumerate(line):
            if point == '#':
                s = s + str(letters[(x, y)])
            else:
                s = s + '.'

        #print(s)

    soln = dict()
    for base in [(0, 0)]:
        posns = set(map(lambda p: (p[0] - base[0], p[1] - base[1]), copy.copy(asteroid_posns)))
        #print(posns)
        max_x = max(posns, key=lambda p: p[0])[0]
        max_y = max(posns, key=lambda p: p[1])[1]
        min_x = min(posns, key=lambda p: p[0])[0]
        min_y = min(posns, key=lambda p: p[1])[1]

        in_view = set()
        # quadrant 1
        y = max_y
        possible = set(filter(lambda i: i[0] >= 0 and i[1] >= 0, posns)).difference({(0, 0)})
        for x in range(0, max_x + 1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        x = max_x
        possible = set(filter(lambda i: i[0] >= 0 and i[1] >= 0, posns)).difference({(0, 0)})
        for y in range(max_y - 1, -1, -1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        # quadrant 2
        x = max_x
        possible = set(filter(lambda i: i[0] >= 0 and i[1] <= 0, posns)).difference({(0, 0)})
        for y in range(0, min_y - 1, -1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        y = min_y
        possible = set(filter(lambda i: i[0] >= 0 and i[1] <= 0, posns)).difference({(0, 0)})
        for x in range(max_x, -1, -1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        # quadrant 3
        y = min_y
        possible = set(filter(lambda i: i[0] <= 0 and i[1] <= 0, posns)).difference({(0, 0)})
        for x in range(0, min_x - 1, -1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        x = min_x
        possible = set(filter(lambda i: i[0] <= 0 and i[1] <= 0, posns)).difference({(0, 0)})
        for y in range(min_y, 1, -1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        # quadrant 4
        x = min_x
        possible = set(filter(lambda i: i[0] <= 0 and i[1] > 0, posns)).difference({(0, 0)})
        for y in range(0, max_y + 1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        y = max_y
        possible = set(filter(lambda i: i[0] < 0 and i[1] >= 0, posns)).difference({(0, 0)})
        for x in range(min_x, 1, 1):
            for i in possible:
                if vec_divide(i, (x, y)):
                    in_view.add(i)
                    break
            print((x, y))

        #print(f"{base}: {len(in_view)}")
        #print(in_view)
        soln[base] = len(in_view)


    soln = dict()
    for base in asteroid_posns:
        in_view = []
        possible = asteroid_posns.difference({base})
        for asteroid in possible:
            if not is_blocked(base, in_view, asteroid):
                in_view.append(asteroid)

        #print(in_view)
        #print(f"In view for {base}: {len(in_view)}")
        soln[base] = len(in_view)

    # print(soln)

    for y, line in enumerate(asteroids):
        s = ''
        for x, point in enumerate(line):
            if point == '#':
                s = s + str(soln[(x, y)])
            else:
                s = s + '.'

        print(s)

    print(f"Best asteroid: {max(soln.values())}")


def is_blocked(base, in_view, asteroid):
    for i in in_view:
        theta = get_angle(base, asteroid, i)
        if theta == 0:
            return True

    return False


def vec_divide(a, b):
    a_new = a[0] * b[1], a[1] * b[1]
    b_new = b[0] * a[1], b[1] * a[1]
    return a == b


def get_angle(p1, p2, p3):
    return math.atan2(p3[1] - p1[1], p3[0] - p1[0]) - math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def between(left, middle, right):
    return middle[0] in range(min(left[0], right[0]), max(left[0], right[0]) + 1) and middle[1] in range(min(left[1], right[1]), max(left[1], right[1]) + 1)


def map_to_letters(letters, l, base):
    return list(map(lambda p: letters[(p[0] + base[0], p[1] + base[1])], l))

if __name__ == '__main__':
    main()

