import math
import sys


def main():
    #asteroids = [line.rstrip() for line in sys.stdin]
    asteroids = [line.rstrip() for line in open('input')]

    asteroid_posns = set()

    for y, line in enumerate(asteroids):
        for x, point in enumerate(line):
            if point != '#':
                continue

            asteroid_posns.add((x, y))

    #print(asteroid_posns)

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

    #print(soln)

    for y, line in enumerate(asteroids):
        s = ''
        for x, point in enumerate(line):
            if point == '#':
                s = s + str(soln[(x, y)])
            else:
                s = s + '.'

        print(s)

    print(f"Best asteroid: {max(soln.values())}")
    print(f"{soln}")


def is_blocked(base, in_view, asteroid):
    for i in in_view:
        theta = get_angle(base, asteroid, i)
        if theta == 0:
            return True

    return False


def get_angle(p1, p2, p3):
    return math.atan2(p3[1] - p1[1], p3[0] - p1[0]) - math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def between(left, middle, right):
    return middle[0] in range(min(left[0], right[0]), max(left[0], right[0]) + 1) and middle[1] in range(min(left[1], right[1]), max(left[1], right[1]) + 1)


if __name__ == '__main__':
    main()

