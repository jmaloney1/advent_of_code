import util

if __name__ == '__main__':
    visited = set()
    h = (0, 0)
    t = (0, 0)
    for line in util.read_input('input'):
        direction, count = line.strip().split(' ')
        print(line.strip())
        for _ in range(int(count)):
            match direction:
                case 'R': h = h[0] + 1, h[1]
                case 'L': h = h[0] - 1, h[1]
                case 'U': h = h[0], h[1] + 1
                case 'D': h = h[0], h[1] - 1
            if abs(h[0] - t[0]) == 2 and h[1] != t[1]:
                t = t[0] + (-1, 1)[h[0] > t[0]], t[1] + (-1, 1)[h[1] > t[1]]
            elif abs(h[1] - t[1]) == 2 and h[0] != t[0]:
                t = t[0] + (-1, 1)[h[0] > t[0]], t[1] + (-1, 1)[h[1] > t[1]]
            elif abs(h[0] - t[0]) == 2:
                t = t[0] + (-1, 1)[h[0] > t[0]], t[1]
            elif abs(h[1] - t[1]) == 2:
                t = t[0], t[1] + (-1, 1)[h[1] > t[1]]

            visited.add(t)
            print(f"h: {h}")
            print(f"t: {t}")

    print(visited)
    print(len(visited))
