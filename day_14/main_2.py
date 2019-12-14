import math


class Chem:
    def __init__(self, coeff, chem):
        self.coeff = coeff
        self.chem = chem

    def __repr__(self):
        return f"{self.coeff} {self.chem}"


class Reaction:
    def __init__(self, inp, output):
        self.input = [Chem(int(i.split(' ')[0]), i.split(' ')[1]) for i in inp.split(', ')]
        self.output = Chem(int(output.split(' ')[0]), output.split(' ')[1])


def lcm(x, y):
    return x * y // math.gcd(x, y)


def main():
    input_output = [line.rstrip().split(' => ') for line in open('input')]

    reactions = [Reaction(s[0], s[1]) for s in input_output]
    print('--------------------')
    for r in reactions:
        print(r.input, r.output)
    print('--------------------')

    reaction_output_dict = dict()
    for r in reactions:
        reaction_output_dict[r.output.chem] = r

    from_ore = set()
    for r in reactions:
        if r.input[0].chem == 'ORE':
            from_ore.add(r.output.chem)

    def get_ore(fuel):
        current_excess = dict()
        for r in reactions:
            current_excess[r.output.chem] = 0

        def reverse_reaction(out: Chem):
            if out.chem in from_ore:
                return [out]

            reaction = reaction_output_dict[out.chem]
            m = math.ceil(out.coeff / reaction.output.coeff)

            current_excess[out.chem] += reaction.output.coeff * m - out.coeff

            s = []
            for i in reaction.input:
                excess = current_excess[i.chem]
                used = min(i.coeff * m, excess)
                current_excess[i.chem] -= used
                needed = i.coeff * m - excess
                if used > 0:
                    print(f"We have excess: {i.chem}")
                if needed > 0:
                    s = s + reverse_reaction(Chem(needed, i.chem))
            return s

        reaction_cost = reverse_reaction(Chem(fuel, 'FUEL'))
        cost = dict()
        for c in reaction_cost:
            if c.chem not in cost:
                cost[c.chem] = 0
            cost[c.chem] += c.coeff

        print(cost)
        total = 0
        for c in cost:
            for r in reactions:
                if r.output.chem == c:
                    m = math.ceil(cost[c] / r.output.coeff)
                    total += r.input[0].coeff * m
                    print(f"Ore for {r.output.chem} = {r.input[0].coeff * m}")

        return total


    _min = 1
    _max = 1000000000000
    curr_max = 0
    while True:
        print(f"{_min}:{_max}")
        if _min == _max or _max < _min:
            break

        middle = (_max + _min) // 2
        #cost = ore_for_one * middle
        cost = get_ore(middle)
        print(f"Cost: {cost}")
        if cost > 1000000000000:
            _max = middle
        else:
            curr_max = max(curr_max, middle)
            _min = middle + 1

    print(curr_max)




if __name__ == '__main__':
    main()
