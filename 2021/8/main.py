if __name__ == '__main__':

    with open('input') as f:

        segments = []
        max_x = 0
        max_y = 0

        input_values = []
        for line in f:
            s = line.strip().split(' | ')
            signal_pattern = s[0].split(' ')
            output_values = s[1].split(' ')

            input_values.append((signal_pattern, output_values))

        digits = [0] * 10
        for i in input_values:
            signal_pattern = i[0]
            output_values = i[1]

            for o in output_values:
                if len(o) == 2:
                    digits[1] += 1
                elif len(o) == 4:
                    digits[4] += 1
                elif len(o) == 3:
                    digits[7] += 1
                elif len(o) == 7:
                    digits[8] += 1

        print(sum(digits))
