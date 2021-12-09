if __name__ == '__main__':

    with open('input') as f:
        fish = list(map(int, f.readline().strip().split(',')))

    fish_count = [0] * 9
    for i in fish:
        fish_count[i] = fish.count(i)

    print(f"Initial: {fish_count}")
    for d in range(256):
        zero = fish_count.pop(0)

        fish_count.append(zero)
        fish_count[6] += zero
        print(f"day {d+1}: {fish_count}")

    print(sum(fish_count))
