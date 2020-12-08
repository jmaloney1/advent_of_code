def search(value, expected_value, input_list):
    """

    :param value: int
    :param expected_value: int
    :param input_list: list
    """
    half = int(len(input_list) / 2)
    current_value = value + input_list[half]
    if current_value == expected_value:
        return input_list[half]
    elif len(input_list) <= 1 or current_value > expected_value:
        return None
    else:
        return search(value, expected_value, input_list[half:])


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line) for line in input]

    input_list.sort()

    print(input_list)

    for v_1 in input_list:
        copy = input_list.copy()
        copy.remove(v_1)
        for v_2 in copy:
            expected_value = 2020
            if v_1 + v_2 > expected_value:
                continue
            copy = copy.copy()
            copy.remove(v_2)
            value = search(v_1 + v_2, expected_value, copy)
            if value is not None:
                print(f"{v_1} * {value} * {v_2} = {v_1 * v_2 * value}")
                break
