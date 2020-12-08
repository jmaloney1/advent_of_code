def search(value, expected_value, input_list):
    """

    :param value: int
    :type input_list: list
    """
    half = int(len(input_list) / 2)
    current_value = value + input_list[half]
    if current_value == expected_value:
        return input_list[half]
    elif len(input_list) <= 1:
        return None

    if current_value < expected_value:
        return search(value, expected_value, input_list[half:])
    else:
        return search(value, expected_value, input_list[0:half])


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line) for line in input]

    input_list.sort()

    print(input_list)

    for v in input_list:
        copy = input_list.copy()
        copy.remove(v)
        value = search(v, 2020, copy)
        if value is not None:
            print(f"{v} * {value} = {v * value}")
            break
