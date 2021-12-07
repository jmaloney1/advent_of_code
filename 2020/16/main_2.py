import itertools


def parse_rule(line):
    parts = line.split(': ')
    field = parts[0]
    rules = []
    for l in parts[1].split(' '):
        if l != 'or':
            s = l.split('-')
            rule = int(s[0]), int(s[1])
            rules.append(rule)

    return field, rules


def parse_ticket(line):
    return list(map(int, line.split(',')))


def match_rule(value, rule):
    for r in rule[1]:
        if r[0] <= value <= r[1]:
            return True

    return False


if __name__ == '__main__':
    with open('input', 'r') as input:
        ticket_rules = []
        ticket = None
        nearby_tickets = []

        line = input.readline().strip()
        while line != '':
            ticket_rules.append(parse_rule(line))
            line = input.readline().strip()

        input.readline()
        ticket = parse_ticket(input.readline().strip())

        input.readline()
        input.readline()
        line = input.readline().strip()
        while line != '':
            nearby_tickets.append(parse_ticket(line))
            line = input.readline().strip()

    print(ticket_rules)
    print(ticket)
    print(nearby_tickets)

    invalid_fields = []
    valid_tickets = []

    for nt in nearby_tickets:
        invalid_field = []
        for field in nt:
            valid = False
            for rule in ticket_rules:
                if match_rule(field, rule):
                    valid = True
                    break
            if not valid:
                invalid_field.append(field)

        invalid_fields.append(invalid_field)
        if len(invalid_field) == 0:
            valid_tickets.append(nt)

    # print(valid_tickets)

    invalid_rules = [[]] * len(ticket_rules)

    permutations = itertools.permutations(ticket_rules)

    valid_rules = [[] for _ in ticket_rules]
    for i in range(len(ticket_rules)):
        for r in ticket_rules:
            valid = True
            for v in valid_tickets:
                if not match_rule(v[i], r):
                    valid = False
                    break

            if valid:
                valid_rules[i].append(r)

    while True:
        thinned = False
        for r in valid_rules:
            if len(r) == 1:
                for x in valid_rules:
                    if x != r and r[0] in x:
                        x.remove(r[0])
                        thinned = True

        if not thinned:
            break

    print(valid_rules)

    s = 1
    for i, r in enumerate(valid_rules):
        if 'departure' in r[0][0]:
            s *= ticket[i]

    print(s)
