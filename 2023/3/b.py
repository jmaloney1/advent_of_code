from functools import reduce

from util_2023 import read_input

if __name__ == '__main__':

    def check_hand(hand, required_cubes):
        required_cubes[hand[1]] = max(required_cubes[hand[1]], int(hand[0]))

    def check_set(game_set, required_cubes):
        for hand in game_set:
            check_hand(hand, required_cubes)

    def handle_line(line: str):
        sets = map(
            lambda x: x.strip(),
            line.split(':')[1].strip().split(';')
        )

        sets = map(
            lambda x: tuple(map(lambda j: j.strip().split(' '), x.split(','))),
            sets
        )

        required_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for s in sets:
            check_set(s, required_cubes)

        return reduce(lambda x, y: x * y, required_cubes.values())

    print(sum(map(lambda x: handle_line(x), read_input('input', strip=True, index=False))))

