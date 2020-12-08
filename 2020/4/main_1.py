def check_passport(passport: dict):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required_keys:
        if key not in passport:
            return False
    return True


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    passport = {}
    valid_count = 0
    passport_count = 0
    input_list.append("")
    i: int
    for i, line in enumerate(input_list):
        if len(line) == 0 or i == len(input_list) - 1:
            valid = check_passport(passport)
            passport_count += 1
            if valid:
                valid_count += 1
            passport = {}
        else:
            for pair in line.split(' '):
                key, value = pair.split(':')
                passport[key] = value

    print(valid_count)
    print(passport_count)
