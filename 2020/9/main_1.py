if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [int(line.strip()) for line in input]

    def contains_sum(nums, s):
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if num_i + num_j == s and i != j:
                    return True

        return False


    window_size = 25
    nums = input_list[:window_size]
    for i in range(window_size, len(input_list)):
        if not contains_sum(nums, input_list[i]):
            print(input_list[i])
            break
        else:
            nums.pop(0)
            nums.append(input_list[i])
