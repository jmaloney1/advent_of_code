import copy
import sys


def main():

    int_code = list(map(lambda s: int(s), sys.stdin.readline().split(',')))

    for noun in range(0, 100):
        for verb in range(0, 100):
            int_code_2 = copy.copy(int_code)
            int_code_2[1] = noun
            int_code_2[2] = verb 
            output = compute(int_code_2)
            print(output)
            if output == 19690720:
                print(f"100 * {noun} + {verb} = {100 * noun + verb}")
                return


def compute(int_code):
    print(int_code)
    position = 0
    while True:
        opcode = int_code[position]
        if opcode == 1:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            # print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
            int_code[output_posn] = int_code[input_posn_1] + int_code[input_posn_2]
        elif opcode == 2:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            int_code[output_posn] = int_code[input_posn_1] * int_code[input_posn_2]
            # print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
        elif opcode == 99:
            break

        position = position + 4

    return int_code[0]


if __name__ == '__main__':
    main()

