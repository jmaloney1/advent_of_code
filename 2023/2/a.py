from util_2023 import read_input

if __name__ == '__main__':

    def is_hand_possible(hand):
        required_cubes = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        return required_cubes[hand[1]] >= int(hand[0])


    def is_game_possible(game_set):
        return all(is_hand_possible(hand) for hand in game_set)

    def handle_line(e: str):
        i = e[0] + 1
        line = e[1]

        sets = map(
            lambda x: x.strip(),
            line.split(':')[1].strip().split(';')
        )

        sets = map(
            lambda x: tuple(map(lambda j: j.strip().split(' '), x.split(','))),
            sets
        )

        for g in sets:
            if not is_game_possible(g):
                return 0

        print(i)

        return i

    print(sum(map(lambda x: handle_line(x), read_input('input', strip=True))))

