from util_2023 import read_input

if __name__ == '__main__':

    def handle_line(line):
        first_num = None
        second_num = None
        for c in line:
            try:
                cast = int(c)
                if first_num is None:
                    first_num = cast

                second_num = cast
            except ValueError:
                pass

        return first_num * 10 + second_num

    print(sum(map(lambda x: handle_line(x), read_input('input'))))

