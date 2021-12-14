from collections import defaultdict

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

    polymer_count = defaultdict(lambda: 0)
    for w in [polymer[x:x+2] for x in range(len(polymer)-1)]:
        polymer_count[w] = 1

    for i in range(40):
        new_polymer_count = defaultdict(lambda: 0)
        for k in polymer_count.keys():
            t = polymer_template[k]
            new_polymer_count[k[0] + t] += polymer_count[k]
            new_polymer_count[t + k[1]] += polymer_count[k]

        polymer_count = new_polymer_count

        print(polymer_count)

    polymer_count[polymer[0]] = 1
    polymer_count[polymer[-1]] = 1

    sums = []
    for i in range(ord('A'), ord('Z')+1):
        c = chr(i)
        count = sum(map(lambda k: polymer_count[k] * (1, 2)[len(k) == 2 and k[0] == k[1]], filter(lambda k: c in k, polymer_count.keys())))
        if count > 0:
            print(f"{c}: {count // 2}")
            sums.append(count // 2)

    print(max(sums) - min(sums))
