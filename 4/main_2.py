import sys
import math

def main():
    min = 382345
    max = 843167

    numbers = filter(check_num, range(min, max))

    numbers = list(filter(check_num_2, numbers))

    print(numbers)

    print(f"Numbers in range: {len(numbers)}")


def check_num(num):
        digits = [int(d) for d in str(num)]
        cons = False
        for i in range(0, len(digits) - 1):
            if digits[i] == digits[i+1]:
                cons = True
            if digits[i] > digits[i+1]:
                return False

        return cons


def check_num_2(num):
        digits = [int(d) for d in str(num)]
        cons_len = 1
        for i in range(0, len(digits) - 1):
            if digits[i] == digits[i+1]:
                cons_len = cons_len + 1
            elif cons_len == 2:
                return True
            else:
                cons_len = 1

        return cons_len == 2


if __name__ == '__main__':
    main()

