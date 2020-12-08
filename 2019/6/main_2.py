import sys

def main():
    planets = {}
    for line in sys.stdin:
        print(line)
        (parent, planet) = read_orbit(line)
        planets[planet] = parent

    print(planets)

    route_1 = get_route('YOU', planets)
    route_2 = get_route('SAN', planets)

    print(route_1)
    print(route_2)

    last_same = None
    for i, j in zip(route_1.copy(), route_2.copy()):
        if i == j:
            last_same = route_1.pop(0)
            route_2.pop(0)
        else:
            break

    print(last_same)
    print(route_1)
    print(route_2)

    print(f"Transfers to Santa: {1 + len(route_1) - 2 + len(route_2) - 1}")


def read_orbit(line):
    return  line.rstrip().split(')')


def get_route(planet, planets):
    if planet == 'COM':
        return ['COM']

    parent = planets[planet]

    route = get_route(parent, planets)
    route.append(planet)
    return route


if __name__ == '__main__':
    main()

