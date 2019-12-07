import sys
import copy
import itertools

def main():

    int_code = list(map(lambda s: int(s), sys.stdin.readline().split(',')))

    outputs = []
    for amp_setting in itertools.permutations([0, 1, 2, 3, 4]):
        output = 0
        for amp in amp_setting:
            output = compute(copy.copy(int_code), [amp, output])
            print(output)
        outputs.append((amp_setting, output))

    max_tuple = max(outputs, key=lambda x: x[1])
    print(f"Max output: {max_tuple}")


def compute(int_code, inputs):
    print(int_code)
    position = 0
    while True:
        print(f"position: {position}")
        inst = int_code[position]
        opcode = get_opcode(inst)

        # add
        if opcode == 1:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            print(f"Add: ({opcode}, {input_value_1}, {input_value_2}, {output_posn})")
            int_code[output_posn] = input_value_1 + input_value_2
            position = position + 4

        # multiply
        elif opcode == 2:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            print(f"Multiply: ({opcode}, {input_value_1}, {input_value_2}, {output_posn})")
            int_code[output_posn] = input_value_1 * input_value_2
            position = position + 4

        # input
        elif opcode == 3:
            output_posn = int_code[position + 1]
            inp = inputs.pop(0)
            int_code[output_posn] = inp 
            print(f"Input: {inp}")
            position = position + 2

        # output
        elif opcode == 4:
            output = int_code[position + 1]
            int_code[0] = int_code[output]
            print(f"Ouput: {int_code[output]}")
            position = position + 2

        # jump-if-true
        elif opcode == 5:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            print(f"Jump-If-True: ({opcode}, {input_value_1}, {input_value_2})")
            if input_value_1 != 0:
                position = input_value_2
            else:
                position = position + 3

        # jump-if-false
        elif opcode == 6:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            print(f"Jump-If-False: ({opcode}, {input_value_1}, {input_value_2})")
            if input_value_1 == 0:
                position = input_value_2
            else:
                position = position + 3

        # less than
        elif opcode == 7:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            print(f"Less Than: ({opcode}, {input_value_1}, {input_value_2})")
            int_code[output_posn] = (0, 1)[input_value_1 < input_value_2]
            position = position + 4

        # equal
        elif opcode == 8:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            print(f"Equal: ({opcode}, {input_value_1}, {input_value_2})")
            int_code[output_posn] = (0, 1)[input_value_1 == input_value_2] 
            position = position + 4

        elif opcode == 99:
            return int_code[0]


def get_param_value(inst, position, param_num, int_code):
    param = int_code[position + param_num]
    return int_code[param] if get_parameter_modes(inst, param_num) == 0 else param


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

