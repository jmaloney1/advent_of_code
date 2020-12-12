if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line.strip()) for line in input]

    input_list.append(0)
    input_list.append(max(input_list) + 3)
    input_list.sort()
    print(input_list)

    single_jumps = 0
    triple_jumps = 0
    for i, rating in enumerate(input_list):
        if i == 0:
            continue

        else:
            diff = rating - input_list[i-1]
            if diff == 1:
                single_jumps += 1
            elif diff == 3:
                triple_jumps += 1

    print(f"{single_jumps} * {triple_jumps} = {single_jumps * triple_jumps}")
