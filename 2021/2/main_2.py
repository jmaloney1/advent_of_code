if __name__ == '__main__':

    with open('input') as f:
        prev = None
        c = 0
        window_size = 3
        course = list(map(lambda line: line.strip().split(' '), f))

        depth = 0
        horizontal_position = 0
        aim = 0
        for c in course:
            print(c)

            movement = c[0]
            if movement == 'forward':
                horizontal_position += int(c[1])
                depth += aim * int(c[1])
            elif movement == 'down':
                aim += int(c[1])
            elif movement == 'up':
                aim -= int(c[1])

        print(depth * horizontal_position)
