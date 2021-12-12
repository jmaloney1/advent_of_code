class Node:
    def __init__(self, i):
        self.i = i
        self.adj = []

    def __str__(self):
        return f"{self.i}: {self.adj}"


def is_big_cave(i):
    return i.upper() == i


def search(n, nodes, seen):
    if n.i == 'end':
        return [seen + [n.i]]
    elif not is_big_cave(n.i) and n.i in seen:
        return []
    else:
        paths = []
        for i in n.adj:
            p = search(i, nodes, seen + [n.i])
            if len(p) > 0:
                paths += p

        return paths


if __name__ == '__main__':
    nodes = dict()
    with open('input') as f:
        for line in f:
            edge = line.strip().split('-')[:2]
            n_0 = nodes.get(edge[0])
            if n_0 is None:
                n_0 = Node(edge[0])
                nodes[edge[0]] = n_0
            n_1 = nodes.get(edge[1])
            if n_1 is None:
                n_1 = Node(edge[1])
                nodes[edge[1]] = n_1
            n_1 = nodes.get(edge[1], Node(edge[0]))
            n_0.adj.append(n_1)
            n_1.adj.append(n_0)

    paths = search(nodes['start'], nodes, [])
    print(paths)
    print(len(paths))
