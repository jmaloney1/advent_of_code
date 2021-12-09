if __name__ == '__main__':

    with open('input') as f:
        fish = list(map(int, f.readline().strip().split(',')))

    print(f"Initial: {fish}")
    for d in range(80):
        fish = list(map(lambda x: (x - 1, None)[x == 0], fish))
        spawns = len(list(filter(lambda x: x is None, fish)))
        fish = list(map(lambda x: (x, 6)[x is None], fish))
        fish += [8] * spawns
        print(f"day {d+1}: {fish}")

    print(len(fish))
