from enum import IntEnum


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSE = 1
    DRAW = 2
    WIN = 3


win_map = {
    Shape.ROCK: Shape.PAPER,
    Shape.PAPER: Shape.SCISSORS,
    Shape.SCISSORS: Shape.ROCK
}

lose_map = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER
}


def get_score(o_shape: Shape, shape: Shape):
    if o_shape == shape:
        return 3 + shape
    elif lose_map[o_shape] == shape:
        return shape
    else:
        return 6 + shape


def get_shape(o_shape: Shape, outcome: Outcome):
    if outcome == Outcome.DRAW:
        return Shape(o_shape)
    elif outcome == Outcome.LOSE:
        return lose_map[o_shape]
    else:
        return win_map[o_shape]


if __name__ == '__main__':
    with open('input') as f:
        total_score = 0
        for line in f:
            o_shape, outcome = line.strip().split(' ')
            o_shape = Shape(ord(o_shape) - ord('A') + 1)
            outcome = Outcome(ord(outcome) - ord('X') + 1)
            shape = get_shape(o_shape, outcome)
            total_score += get_score(o_shape, shape)

    print(total_score)
