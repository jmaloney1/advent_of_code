from itertools import count


def trajectory(x, y, x_range, y_range):
    t = [(0, 0)]
    x_v = x
    y_v = y
    for i in count(0):
        t_i1 = t[i][0] + x_v, t[i][1] + y_v
        x_v = max(x_v - 1, 0)
        y_v -= 1
        t.append(t_i1)
        if x_range[0] <= t_i1[0] <= x_range[1] and y_range[0] <= t_i1[1] <= y_range[1]:
            return t, True
        elif y_range[0] > t_i1[1] or x_range[1] < t_i1[0]:
            return t, False

    return t, None


if __name__ == '__main__':
    with open('input') as f:
        l = f.readline().strip()
        t = l.replace('target area: ', '').split(', ')
        x_range = tuple(map(lambda x: int(x.replace('x=', '')), t[0].split('..')))
        y_range = tuple(map(lambda y: int(y.replace('y=', '')), t[1].split('..')))

        print(x_range)
        print(y_range)

        t, valid = trajectory(30, -7, x_range, y_range)
        print(f"{30}, {-7}: {valid} {t}")

        ts = []
        for y in range(y_range[0], 1000):
            for x in range(1, x_range[1] + 1):
                t, valid = trajectory(x, y, x_range, y_range)
                if valid:
                    ts.append((x, y))

        print(len(ts))
