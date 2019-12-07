import sys

def main():
    planets = {}
    for line in sys.stdin:
        print(line)
        (parent, planet) = read_orbit(line)
        planets[planet] = parent

    print(planets)

    #print(f"H: {count_orbits('H', planets)}")
    #print(f"L: {count_orbits('L', planets)}")

    total = 0
    for planet in planets:
        total = total + count_orbits(planet, planets)

    print(total)
    

def read_orbit(line):
    return  line.rstrip().split(')')


def count_orbits(planet, planets):
    if planet == 'COM':
        return 0;

    parent = planets[planet]

    return 1 + count_orbits(parent, planets)


if __name__ == '__main__':
    main()

