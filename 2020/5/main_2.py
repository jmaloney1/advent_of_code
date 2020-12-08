if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    ids = set()
    for ticket in input_list:
        first_row = 0
        last_row = 127
        for c in ticket[:7]:
            half = int((first_row + last_row) / 2)
            if c == 'F':
                last_row = half
            else:
                if first_row == last_row:
                    first_row = last_row
                else:
                    first_row = half + 1

        row = first_row

        first_row = 0
        last_row = 7
        for c in ticket[7:]:
            half = int((first_row + last_row) / 2)
            if c == 'L':
                last_row = half
            else:
                if first_row == last_row:
                    first_row = last_row
                else:
                    first_row = half + 1

        seat = first_row
        id = row * 8 + seat
        ids.add(id)
        print(f"{row} * 8 + {seat} = {id}")

    for row in range(1, 127):
        for seat in range(8):
            i = row * 8 + seat
            if i - 1 in ids and i + 1 in ids and i not in ids:
                print(i)
