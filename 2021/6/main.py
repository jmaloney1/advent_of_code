class Point:
    def __init__(self, l):
        self.x = l[0]
        self.y = l[1]

    def __str__(self):
        return f"({self.x}, {self.y})"


def print_graph(g):
    for l in g:
        print(l.replace('0', '.'))


if __name__ == '__main__':

    with open('input') as f:

        segments = []
        max_x = 0
        max_y = 0
        for line in f:
            points = line.strip().split(' -> ')
            p1 = Point(list(map(int, points[0].split(','))))
            p2 = Point(list(map(int, points[1].split(','))))

            if p1.x == p2.x or p1.y == p2.y:
                max_x = max(max_x, p1.x, p2.x)
                max_y = max(max_y, p1.y, p2.y)
                segments.append((p1, p2))

        graph = ['0' * (max_x + 1)] * (max_y + 1)

        for s in segments:
            p1, p2 = s
            print(f"After segment: {p1} -> {p2}")
            m = 1
            if p1.x > p2.x:
                m = -1
            n = 1
            if p1.y > p2.y:
                n = -1
            for x in range(p1.x, p2.x + m, m):
                for y in range(p1.y, p2.y + n, n):
                    graph[y] = graph[y][:x] + str(int(graph[y][x]) + 1) + graph[y][x+1:]

            print_graph(graph)

        # print_graph(graph)

        print(sum(map(lambda x: len(x) - x.count('0') - x.count('1'), graph)))
