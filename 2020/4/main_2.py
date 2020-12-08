import re


def check_height(raw_value):
    if 'cm' in raw_value:
        return 150 <= int(raw_value[:-2]) <= 193
    elif 'in' in raw_value:
        return 59 <= int(raw_value[:-2]) <= 76
    return False


def check_passport(passport: dict):
    try:
        if not (1920 <= int(passport['byr']) <= 2002):
            return False

        if not (2010 <= int(passport['iyr']) <= 2020):
            return False

        if not (2020 <= int(passport['eyr']) <= 2030):
            return False

        if not check_height(passport['hgt']):
            return False

        if not re.match('#[0-9a-f]{6}', passport['hcl']):
            return False

        eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] not in eye_colours:
            return False

        if not re.match('^[0-9]{9}$', passport['pid']):
            return False

        return True
    except KeyError:
        return False


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    passport = {}
    valid_count = 0
    passport_count = 0
    input_list.append("")
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
