import copy


class Moon:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        self.id = id

    def __repr__(self):
        return f"pos=<x={self.x}, y={self.y}, z={self.z}> vel=<x={self.vel_x}, y={self.vel_y}, z={self.vel_z}>"


def energy_for_moon(moon: Moon):
    return (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z))


def main():
    def map_to_posn(x):
        return tuple(map(lambda p: int(p[2:]), x.rstrip()[1:-1].split(', ')))

    moons = list()

    for i, m in enumerate(list(map(map_to_posn, open('input')))):
        moons.append(Moon(m[0], m[1], m[2], i))

    for i in range(0, 1000):
        if i % 10 == 0:
            print(f"Step: {i}")
            for moon in moons:
                print(moon)
            energy = sum([energy_for_moon(m) for m in moons])
            print(f"Energy energy: {energy}")

        updated_moons = dict()
        for moon in moons:
            updated_moons[moon] = copy.deepcopy(moon)

        # apply gravity
        for moon in moons:
            for other_moon in moons:
                if moon == other_moon:
                    continue

                if other_moon.x < moon.x:
                    updated_moons[other_moon].vel_x += 1
                elif other_moon.x > moon.x:
                    updated_moons[other_moon].vel_x -= 1

                if other_moon.y < moon.y:
                    updated_moons[other_moon].vel_y += 1
                elif other_moon.y > moon.y:
                    updated_moons[other_moon].vel_y -= 1

                if other_moon.z < moon.z:
                    updated_moons[other_moon].vel_z += 1
                elif other_moon.z > moon.z:
                    updated_moons[other_moon].vel_z -= 1

        # apply velocity
        for old_moon in updated_moons:
            updated_moons[old_moon].x += updated_moons[old_moon].vel_x
            updated_moons[old_moon].y += updated_moons[old_moon].vel_y
            updated_moons[old_moon].z += updated_moons[old_moon].vel_z

        for i in moons:
            m = updated_moons[i]
            m.vel_x = m.x - i.x
            m.vel_y = m.y - i.y
            m.vel_z = m.z - i.z

        moons = list(updated_moons.values())
        moons.sort(key=lambda x: x.id)

    print(f"Total energy: {sum([energy_for_moon(m) for m in moons])}")


if __name__ == '__main__':
    main()
