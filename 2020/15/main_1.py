from collections import defaultdict

if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    numbers = list(map(int, input_list[0].split(',')))

    memory = defaultdict(lambda: 0)
    number = None
    for i in range(len(numbers) - 1):
        memory[numbers[i]] = i + 1
        number = numbers[i]
        print(f"Turn {i + 1}: {number}")

    number = numbers[-1]
    for i in range(len(memory) + 1, 2021):
        if number in memory:
            new_number = i - memory[number]
        else:
            new_number = memory[number]

        print(f"Turn {i}: {number}")
        memory[number] = i
        number = new_number
