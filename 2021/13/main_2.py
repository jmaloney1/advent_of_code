class Node:
    def __init__(self, i):
        self.i = i
        self.adj = []

    def __str__(self):
        return f"{self.i}: {self.adj}"


def is_big_cave(i):
    return i.upper() == i


def is_small_cave(i):
    return i.lower() == i


def search(n, nodes, seen, small_cave_reuse):
    if n.i == 'end':
        return [seen + [n.i]]
    elif n.i == 'start' and len(seen) > 0:
        return []
    elif small_cave_reuse is True and is_small_cave(n.i) and n.i in seen:
        return []
    else:
        paths = []
        small_cave_reuse = small_cave_reuse or n.i in seen and is_small_cave(n.i)
        for i in n.adj:
            p = search(i, nodes, seen + [n.i], small_cave_reuse)
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

    paths = search(nodes['start'], nodes, [], False)
    print(paths)
    print(len(paths))
