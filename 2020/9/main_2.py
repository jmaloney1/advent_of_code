if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line.strip()) for line in input]


    def contains_sum(nums, s):
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if num_i + num_j == s and i != j:
                    return True

        return False


    invalid_number = None
    window_size = 25
    nums = input_list[:window_size]
    for i in range(window_size, len(input_list)):
        if not contains_sum(nums, input_list[i]):
            print(input_list[i])
            invalid_number = input_list[i]
            break
        else:
            nums.pop(0)
            nums.append(input_list[i])

    for i in range(0, len(input_list)):
        window = input_list[i:i+2]
        j = i + 2
        while sum(window) < invalid_number:
            window.append(input_list[j])
            j += 1

        if sum(window) == invalid_number:
            print(window)
            max1 = max(window)
            print(f"max: {max1}")
            min1 = min(window)
            print(f"min: {min1}")
            print(f"sum: {max1 + min1}")
            break
