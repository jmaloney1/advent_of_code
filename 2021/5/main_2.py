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

    #0,9 -> 5,9
    #8,0 -> 0,8
    #9,4 -> 3,4
    #2,2 -> 2,1
    #7,0 -> 7,4
    #6,4 -> 2,0
    #0,9 -> 2,9
    #3,4 -> 1,4
    #0,0 -> 8,8
    #5,5 -> 8,2
    with open('input') as f:

        segments = []
        max_x = 0
        max_y = 0
        for line in f:
            points = line.strip().split(' -> ')
            p1 = Point(list(map(int, points[0].split(','))))
            p2 = Point(list(map(int, points[1].split(','))))

            max_x = max(max_x, p1.x, p2.x)
            max_y = max(max_y, p1.y, p2.y)
            segments.append((p1, p2))

        graph = ['0' * (max_x + 1)] * (max_y + 1)

        for s in segments:
            p1, p2 = s
            print(f"After segment: {p1} -> {p2}")
            m = 1
            if p1.x == p2.x:
                for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                    graph[y] = graph[y][:p1.x] + str(int(graph[y][p1.x]) + 1) + graph[y][p1.x + 1:]
            elif p1.y == p2.y:
                for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                    graph[p1.y] = graph[p1.y][:x] + str(int(graph[p1.y][x]) + 1) + graph[p1.y][x + 1:]
            else:
                n = 1
                if p1.y > p2.y:
                    n = -1
                m = 1
                if p1.x > p2.x:
                    m = -1

                y = p1.y
                for x in range(p1.x, p2.x + m, m):
                    graph[y] = graph[y][:x] + str(int(graph[y][x]) + 1) + graph[y][x + 1:]
                    y += n


            print_graph(graph)

        # print_graph(graph)

        print(sum(map(lambda x: len(x) - x.count('0') - x.count('1'), graph)))
