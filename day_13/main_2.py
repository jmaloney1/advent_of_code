import copy

from day_13.IntCode import IntCode, compute


def main():
    int_code = list(map(int, open('input').readline().split(',')))
    # int_code = list(map(int, sys.stdin.readline().split(',')))

    game_board = dict()
    def get_input():
        ball = get_ball_x(game_board)

        paddle = get_paddle_x(game_board)

        if ball is not None and paddle is not None:
            if ball[0] < paddle[0]:
                return -1
            elif ball[0] > paddle[0]:
                return 1
            else:
                return 0

    code = IntCode(copy.copy(int_code), get_input)
    score = 0
    while code.position >= 0:
        x = compute(code, debug=False)
        if code.position < 0:
            break
        y = compute(code, debug=False)
        if code.position < 0:
            break
        tile_id = compute(code, debug=False)
        if code.position < 0:
            break

        if x == -1 and y == 0:
            score = tile_id
        else:
            game_board[(x, y)] = tile_id

        print_board(game_board, score)


def get_paddle_x(game_board):
    for key in game_board:
        if game_board[key] == 3:
            return key


def get_ball_x(game_board):
    for key in game_board:
        if game_board[key] == 4:
            return key


def print_board(game_board, score):
    if len(game_board) == 0:
        return

    max_x = max(game_board.keys(), key=lambda x: x[0])[0]
    min_x = min(game_board.keys(), key=lambda x: x[0])[0]
    max_y = max(game_board.keys(), key=lambda x: x[1])[1]
    min_y = min(game_board.keys(), key=lambda x: x[1])[1]
    print(f"Score: {score}")
    for y in range(min_y, max_y + 1):
        s = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in game_board:
                tile_id = game_board[(x, y)]
                if tile_id == 0:
                    n = ' '
                elif tile_id == 1:
                    n = str(1)
                elif tile_id == 2:
                    n = str('x')
                elif tile_id == 3:
                    n = str('-')
                elif tile_id == 4:
                    n = str('0')
                s = s + n
            else:
                s = s + ' '
        print(s)
    # print(list(game_board.values()).count(2))


if __name__ == '__main__':
    main()
