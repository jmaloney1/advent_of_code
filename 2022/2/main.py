from enum import IntEnum


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


rules = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER
}


def get_score(o_shape: Shape, shape: Shape):
    if o_shape == shape:
        return 3 + shape
    elif rules[o_shape] == shape:
        return shape
    else:
        return 6 + shape


if __name__ == '__main__':
    with open('input') as f:
        total_score = 0
        for line in f:
            o_shape, shape = line.strip().split(' ')
            o_shape = Shape(ord(o_shape) - ord('A') + 1)
            shape = Shape(ord(shape) - ord('X') + 1)
            total_score += get_score(o_shape, shape)

    print(total_score)
