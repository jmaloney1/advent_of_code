import sys
import math

def main():
    int_code = list(map(lambda s: int(s), sys.stdin.readline().split(',')))

    print(f"Input: {int_code}")

    position = 0
    while True:
        opcode = int_code[position]
        if opcode == 1:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
            int_code[output_posn] = int_code[input_posn_1] + int_code[input_posn_2]
        elif opcode == 2:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            int_code[output_posn] = int_code[input_posn_1] * int_code[input_posn_2]
            print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
        elif opcode == 99:
            break

        position = position + 4

    print(f"Output: {int_code}")


if __name__ == '__main__':
    main()

