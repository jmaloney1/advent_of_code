if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    group_result = {}
    unique_result = 0
    for line in input_list:
        if line == "":
            unique_result += len(group_result)
            print(group_result)
            group_result = {}
        else:
            for c in line:
                group_result[c] = True

    print(unique_result)
