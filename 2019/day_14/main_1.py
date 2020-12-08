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

    from_ore = []
    for r in reactions:
        if r.input[0].chem == 'ORE':
            from_ore.append(r.output.chem)

    print(from_ore)

    current_excess = dict()
    for r in reactions:
        current_excess[r.output.chem] = 0

    def reverse_reaction(out: Chem):
        if out.chem in from_ore:
            return [out]

        for reaction in reactions:
            if reaction.output.chem == out.chem:
                # print(reaction.output)
                m = 1
                while reaction.output.coeff * m < out.coeff:
                    m += 1

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

    #print(reverse_reaction((1, 'FUEL')))
    #reaction_cost = reverse_reaction((3, 'JNWZP'))
    #reaction_cost = reverse_reaction((17, 'NVRVD'))
    # reaction_cost = reverse_reaction((8, 'VPVL'))
    reaction_cost = reverse_reaction(Chem(1, 'FUEL'))
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
                m = 1
                while m * r.output.coeff < cost[c]:
                    m += 1
                total += r.input[0].coeff * m
                print(f"Ore for {r.output.chem} = {r.input[0].coeff * m}")

    print(total)


if __name__ == '__main__':
    main()
