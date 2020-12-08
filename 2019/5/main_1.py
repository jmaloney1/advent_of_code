import sys
import copy

def main():

    int_code = list(map(lambda s: int(s), sys.stdin.readline().split(',')))

    output = compute(copy.copy(int_code), 1)
    print(output)


def compute(int_code, user_id):
    print(int_code)
    position = 0
    while True:
        opcode = get_opcode(int_code[position])
        #opcode = int_code[position]
        if opcode == 1:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
            input_value_1 = int_code[input_posn_1] if get_parameter_modes(int_code[position], 1) == 0 else input_posn_1
            input_value_2 = int_code[input_posn_2] if get_parameter_modes(int_code[position], 2) == 0 else input_posn_2
            int_code[output_posn] = input_value_1 + input_value_2
            position = position + 4
        elif opcode == 2:
            input_posn_1 = int_code[position + 1]
            input_posn_2 = int_code[position + 2]
            output_posn = int_code[position + 3]
            input_value_1 = int_code[input_posn_1] if get_parameter_modes(int_code[position], 1) == 0 else input_posn_1
            input_value_2 = int_code[input_posn_2] if get_parameter_modes(int_code[position], 2) == 0 else input_posn_2
            int_code[output_posn] = input_value_1 * input_value_2
            print(f"Read: ({opcode}, {input_posn_1}, {input_posn_2}, {output_posn})")
            position = position + 4
        elif opcode == 3:
            output_posn = int_code[position + 1]
            int_code[output_posn] = user_id
            position = position + 2
        elif opcode == 4:
            output = int_code[position + 1]
            print(f"Ouput: {int_code[output]}")
            int_code[0] = int_code[output]
            position = position + 2
        elif opcode == 99:
            break

    return int_code[0]

def get_opcode(inst):
    digits = [int(d) for d in str(inst)]
    l = len(digits)
    return get_digit(digits, l - 2) * 10 + get_digit(digits, l - 1)


def get_parameter_modes(inst, param_posn):
    digits = [int(d) for d in str(inst)]
    l = len(digits)
    return get_digit(digits, l - param_posn - 2)


def get_digit(digits, i):
    return digits[i] if i < len(digits) and i >= 0 else 0


if __name__ == '__main__':
    main()

    #print(read_parameter_mode(1002, 0))
    #print(read_parameter_mode(1002, 1))
    #print(read_parameter_mode(1002, 2))

