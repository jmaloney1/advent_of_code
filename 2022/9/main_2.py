import util

if __name__ == '__main__':
    visited = set()
    rope = [(0, 0) for _ in range(10)]
    for line in util.read_input('input'):
        direction, count = line.strip().split(' ')
        print(line.strip())
        for _ in range(int(count)):
            h = rope[0]
            match direction:
                case 'R': rope[0] = h[0] + 1, h[1]
                case 'L': rope[0] = h[0] - 1, h[1]
                case 'U': rope[0] = h[0], h[1] + 1
                case 'D': rope[0] = h[0], h[1] - 1

            for i in range(len(rope) - 1):
                h = rope[i]
                t = rope[i + 1]
                if abs(h[0] - t[0]) == 2 and h[1] != t[1]:
                    rope[i + 1] = t[0] + (-1, 1)[h[0] > t[0]], t[1] + (-1, 1)[h[1] > t[1]]
                elif abs(h[1] - t[1]) == 2 and h[0] != t[0]:
                    rope[i + 1] = t[0] + (-1, 1)[h[0] > t[0]], t[1] + (-1, 1)[h[1] > t[1]]
                elif abs(h[0] - t[0]) == 2:
                    rope[i + 1] = t[0] + (-1, 1)[h[0] > t[0]], t[1]
                elif abs(h[1] - t[1]) == 2:
                    rope[i + 1] = t[0], t[1] + (-1, 1)[h[1] > t[1]]

            visited.add(rope[-1])
        print(rope)

    print(visited)
    print(len(visited))
