if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    max_id = 0
    for ticket in input_list:
        first_row = 0
        last_row = 127
        for c in ticket[:8]:
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
        for c in ticket[8:]:
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
        max_id = max(id, max_id)
        print(f"{row} * 8 + {seat} = {id}")

    print(max_id)
