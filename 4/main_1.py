import sys
import math

def main():
    min = 382345
    max = 843167

    numbers = list(filter(check_num, range(min, max)))

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


if __name__ == '__main__':
    main()

