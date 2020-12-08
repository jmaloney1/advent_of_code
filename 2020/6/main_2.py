if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    group_result = {}
    total_result = 0
    input_list.append("")
    group_len = 0
    for line in input_list:
        if line == "":
            for key in group_result:
                if group_result[key] == group_len:
                    total_result += 1
            print(group_result)
            group_result = {}
            group_len = 0
        else:
            for c in line:
                if c in group_result:
                    group_result[c] += 1
                else:
                    group_result[c] = 1

            group_len += 1

    print(total_result)
