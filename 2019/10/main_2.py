import math


def main():
    # asteroids = [line.rstrip() for line in sys.stdin]
    asteroids = [line.rstrip() for line in open('input')]

    asteroid_posns = set()

    for y, line in enumerate(asteroids):
        for x, point in enumerate(line):
            if point != '#':
                continue

            asteroid_posns.add((x, y))

    slopes = list()
    for base in [(31, 20)]:
    # for base in [(day_11, 13)]:
    # for base in [(8, 3)]:
        possible = asteroid_posns.difference({base})
        for asteroid in possible:
            offset = (asteroid[0] - base[0], asteroid[1] - base[1])
            dist = math.sqrt(pow(offset[0], 2) + pow(offset[1], 2))
            slopes.append((-get_angle((0, 0), offset, (0, -1)) % (2 * math.pi), dist, asteroid))

    print(slopes)
    slopes.sort(key=lambda x: x[1])
    slopes.sort(key=lambda x: x[0])

    previous_angle = None
    i = 0
    destroyed = []
    while len(destroyed) < 200:
    #while len(destroyed) < 9:
        if i >= len(slopes):
            i = 0

        s = slopes[i]
        if s[0] != previous_angle:
            slopes.pop(i)
            destroyed.append(s[2])
            print(f"Destroyed {len(destroyed)}: {s}")

            for y, line in enumerate(asteroids):
                st = ''
                for x, point in enumerate(line):
                    if point == '#':
                       if (x, y) in destroyed:
                           st = st + str(destroyed.index((x, y)) + 1)
                       else:
                           st = st + '#'
                    else:
                        st = st + '.'
                print(st)

            previous_angle = s[0]
        else:
            i = i + 1


def get_angle(p1, p2, p3):
    return math.atan2(p3[1] - p1[1], p3[0] - p1[0]) - math.atan2(p2[1] - p1[1], p2[0] - p1[0])


if __name__ == '__main__':
    main()

