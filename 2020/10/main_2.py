def search(adapters, results):
    if len(adapters) == 1:
        return 1

    for c in range(0, max(adapters)):
        for i in range(1, 4):
            if c + i in adapters:
                results[c + i] += results[c]


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line.strip()) for line in input]

    input_list.append(0)
    input_list.sort()
    print(input_list)

    results = [0] * (max(input_list) + 3)
    results[0] = 1
    search(input_list, results)
    print(results[-3:])
