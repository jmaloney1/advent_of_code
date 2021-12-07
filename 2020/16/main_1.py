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

        print(f"{nt} invalid_field: {invalid_field}")

        invalid_fields.append(invalid_field)

    print(sum(map(sum, invalid_fields)))

