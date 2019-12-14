import copy
import itertools
import math


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
        return f"id={self.id} pos=<x={self.x}, y={self.y}, z={self.z}> vel=<x={self.vel_x}, y={self.vel_y}, z={self.vel_z}>"


def find_cycle_x(moons):
    starting_posns = {
        moons[0].id, (moons[0].x, moons[0].vel_x),
        moons[1].id, (moons[1].x, moons[1].vel_x),
        moons[2].id, (moons[2].x, moons[2].vel_x),
        moons[3].id, (moons[3].x, moons[3].vel_x)
    }

    moon_state = None
    for i in itertools.count():
        if starting_posns == moon_state:
            print(f"History Repeats itself! epoch: {i}")
            return i

        # if True:
        #     print(f"Step: {i}")
        #     for moon in moons:
        #         print(moon.x)

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

        # apply velocity
        for old_moon in updated_moons:
            updated_moons[old_moon].x += updated_moons[old_moon].vel_x

        for i in moons:
            m = updated_moons[i]
            m.vel_x = m.x - i.x

        moons = list(updated_moons.values())
        moons.sort(key=lambda x: x.id)

        moon_state = {
            moons[0].id, (moons[0].x, moons[0].vel_x),
            moons[1].id, (moons[1].x, moons[1].vel_x),
            moons[2].id, (moons[2].x, moons[2].vel_x),
            moons[3].id, (moons[3].x, moons[3].vel_x)
        }


def find_cycle_y(moons):
    starting_posns = {
        moons[0].id, (moons[0].y, moons[0].vel_y),
        moons[1].id, (moons[1].y, moons[1].vel_y),
        moons[2].id, (moons[2].y, moons[2].vel_y),
        moons[3].id, (moons[3].y, moons[3].vel_y)
    }

    moon_state = None
    for i in itertools.count():
        if starting_posns == moon_state:
            print(f"History Repeats itself! epoch: {i}")
            return i

        # if True:
        #     print(f"Step: {i}")
        #     for moon in moons:
        #         print(moon.x)

        updated_moons = dict()
        for moon in moons:
            updated_moons[moon] = copy.deepcopy(moon)

        # apply gravity
        for moon in moons:
            for other_moon in moons:
                if moon == other_moon:
                    continue

                if other_moon.y < moon.y:
                    updated_moons[other_moon].vel_y += 1
                elif other_moon.y > moon.y:
                    updated_moons[other_moon].vel_y -= 1

        # apply velocity
        for old_moon in updated_moons:
            updated_moons[old_moon].y += updated_moons[old_moon].vel_y

        for i in moons:
            m = updated_moons[i]
            m.vel_y = m.y - i.y

        moons = list(updated_moons.values())
        moons.sort(key=lambda x: x.id)

        moon_state = {
            moons[0].id, (moons[0].y, moons[0].vel_y),
            moons[1].id, (moons[1].y, moons[1].vel_y),
            moons[2].id, (moons[2].y, moons[2].vel_y),
            moons[3].id, (moons[3].y, moons[3].vel_y)
        }


def find_cycle_z(moons):
    starting_posns = {
        moons[0].id, (moons[0].z, moons[0].vel_z),
        moons[1].id, (moons[1].z, moons[1].vel_z),
        moons[2].id, (moons[2].z, moons[2].vel_z),
        moons[3].id, (moons[3].z, moons[3].vel_z)
    }

    moon_state = None
    for i in itertools.count():
        if starting_posns == moon_state:
            print(f"History Repeats itself! epoch: {i}")
            return i

        # if True:
        #     print(f"Step: {i}")
        #     for moon in moons:
        #         print(moon.x)

        updated_moons = dict()
        for moon in moons:
            updated_moons[moon] = copy.deepcopy(moon)

        # apply gravity
        for moon in moons:
            for other_moon in moons:
                if moon == other_moon:
                    continue

                if other_moon.z < moon.z:
                    updated_moons[other_moon].vel_z += 1
                elif other_moon.z > moon.z:
                    updated_moons[other_moon].vel_z -= 1

        # apply velocity
        for old_moon in updated_moons:
            updated_moons[old_moon].z += updated_moons[old_moon].vel_z

        for i in moons:
            m = updated_moons[i]
            m.vel_z = m.z - i.z

        moons = list(updated_moons.values())
        moons.sort(key=lambda x: x.id)

        moon_state = {
            moons[0].id, (moons[0].z, moons[0].vel_z),
            moons[1].id, (moons[1].z, moons[1].vel_z),
            moons[2].id, (moons[2].z, moons[2].vel_z),
            moons[3].id, (moons[3].z, moons[3].vel_z)
        }


def lcm(x, y):
    return x * y // math.gcd(x, y)


def main():
    def map_to_posn(x):
        return tuple(map(lambda p: int(p[2:]), x.rstrip()[1:-1].split(', ')))

    moons = list()

    for i, m in enumerate(list(map(map_to_posn, open('input')))):
        moons.append(Moon(m[0], m[1], m[2], i))

    x_cycle = find_cycle_x(copy.deepcopy(moons))
    y_cycle = find_cycle_y(copy.deepcopy(moons))
    z_cycle = find_cycle_z(copy.deepcopy(moons))

    x_y = lcm(x_cycle, y_cycle)
    print(lcm(x_y, z_cycle))

    # for i in range(0, 3000):
    #     if i in existing_set:
    #         print(f"History Repeats itself! epoch: {i}")
    #         break
    #
    #     existing_set.add(str_rep)
    #
    #     if i % 10 == 0:
    #         print(f"Step: {i}")
    #         for moon in moons:
    #             print(moon)
    #
    #     updated_moons = dict()
    #     for moon in moons:
    #         updated_moons[moon] = copy.deepcopy(moon)
    #
    #     # apply gravity
    #     for moon in moons:
    #         for other_moon in moons:
    #             if moon == other_moon:
    #                 continue
    #
    #             if other_moon.x < moon.x:
    #                 updated_moons[other_moon].vel_x += 1
    #             elif other_moon.x > moon.x:
    #                 updated_moons[other_moon].vel_x -= 1
    #
    #             if other_moon.y < moon.y:
    #                 updated_moons[other_moon].vel_y += 1
    #             elif other_moon.y > moon.y:
    #                 updated_moons[other_moon].vel_y -= 1
    #
    #             if other_moon.z < moon.z:
    #                 updated_moons[other_moon].vel_z += 1
    #             elif other_moon.z > moon.z:
    #                 updated_moons[other_moon].vel_z -= 1
    #
    #     # apply velocity
    #     for old_moon in updated_moons:
    #         updated_moons[old_moon].x += updated_moons[old_moon].vel_x
    #         updated_moons[old_moon].y += updated_moons[old_moon].vel_y
    #         updated_moons[old_moon].z += updated_moons[old_moon].vel_z
    #
    #     for i in moons:
    #         m = updated_moons[i]
    #         m.vel_x = m.x - i.x
    #         m.vel_y = m.y - i.y
    #         m.vel_z = m.z - i.z
    #
    #     moons = list(updated_moons.values())
    #     moons.sort(key=lambda x: x.id)


if __name__ == '__main__':
    main()
