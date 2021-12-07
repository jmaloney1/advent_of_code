import re


def mark_board(b, n):
    def is_found(x):
        if x == n:
            return None
        else:
            return x

    new_b = []
    for l in b:
        new_b.append(list(map(is_found, l)))

    return new_b


def check_bingo(b):
    for l in b:
        if all(map(lambda x: x is None, l)):
            return True

    for l in range(5):
        if all(map(lambda x: x[l] is None, b)):
            return True

    return False


if __name__ == '__main__':

    with open('input') as f:
        lines = f.readlines()

    bingo_numbers = list(map(int, lines[0].strip().split(',')))

    boards = []
    b = []
    lines.append('\n')
    for l in lines[2:]:
        s = l.strip()
        if s == '':
            boards.append(b)
            b = []
        else:
            b.append(list(map(int, re.split('\\s+', s))))

    for n in bingo_numbers:

        boards = list(map(lambda b: mark_board(b, n), boards))

        if len(boards) > 1:
            boards = list(filter(lambda b: not check_bingo(b), boards))
        else:
            print(sum(map(lambda x: sum(filter(lambda y: not (y is None), x)), boards[0])) * n)
            # < 17907
            # < 18709
            break
