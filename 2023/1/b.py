from util_2023 import read_input

if __name__ == '__main__':

    numbers = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]

    def handle_line(line):
        first_num = None
        second_num = None
        for i, c in enumerate(line):
            temp_word = ''
            word = None
            x = i
            while x < i + 6 and x < len(line):
                temp_word += line[x]
                if temp_word in numbers:
                    word = temp_word
                x += 1

            number = None
            if word is not None:
                number = numbers.index(word) + 1
            else:
                try:
                    number = int(c)
                except ValueError:
                    pass

            if number is None:
                continue

            if first_num is None:
                first_num = number

            second_num = number

        print(first_num * 10 + second_num)
        return first_num * 10 + second_num

    print(sum(map(lambda x: handle_line(x), read_input('input', True))))

