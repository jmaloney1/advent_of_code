from collections import Counter

if __name__ == '__main__':
    polymer_template = {}
    polymer = None
    with open('input') as f:
        for line in f:
            if line == '\n':
                continue
            elif ' -> ' not in line:
                polymer = line.strip()
            else:
                l = line.strip().split(' -> ')[:2]
                polymer_template[l[0]] = l[1]

    for i in range(10):
        new_polymer = polymer[0]
        windows = [polymer[x:x+2] for x in range(len(polymer)-1)]
        for w in windows:
            if w in polymer_template:
                new_polymer = new_polymer + polymer_template[w] + w[1]
            else:
                new_polymer = new_polymer + w

        polymer = new_polymer
        print(new_polymer)

    print(polymer)

    counter = Counter(polymer)
    print(max(counter.values()) - min(counter.values()))

