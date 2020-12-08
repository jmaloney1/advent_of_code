import sys
import copy
import itertools


def main():
    int_code = list(map(int, sys.stdin.readline().split(',')))

    outputs = []
    for amp_setting in itertools.permutations(range(5, 10)):
        int_code_states = [initialize_computer(int_code) for _ in range(0, 5)]

        inputs = [[amp_setting[i]] for i in range(0, 5)]

        inputs[0].append(0)

        i = 0
        while True:
            (output, position) = compute(int_code_states[i][0], int_code_states[i][1], inputs[i])
            if i == len(int_code_states) - 1 and position < 0:
                print(f"Output for feedback loop: {output}")
                outputs.append((amp_setting, output))
                break
            
            int_code_states[i] = (int_code_states[i][0], position)
            
            i = (i + 1) % len(int_code_states)
            inputs[i].append(output)

    max_tuple = max(outputs, key=lambda x: x[1])
    print(f"Max output: {max_tuple}")


def initialize_computer(int_code):
    return (copy.copy(int_code), 0)


def compute(int_code, position, inputs, debug=False):
    if debug:
        print(int_code)

    while True:
        if debug:
            print(f"Position: {position}")
        inst = int_code[position]
        opcode = get_opcode(inst)

        # add
        if opcode == 1:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            if debug:
                print(f"Add: ({input_value_1}, {input_value_2}, {output_posn})")
            int_code[output_posn] = input_value_1 + input_value_2
            position = position + 4

        # multiply
        elif opcode == 2:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            if debug:
                print(f"Multiply: ({input_value_1}, {input_value_2}, {output_posn})")
            int_code[output_posn] = input_value_1 * input_value_2
            position = position + 4

        # input
        elif opcode == 3:
            output_posn = int_code[position + 1]
            inp = inputs.pop(0)
            int_code[output_posn] = inp 
            if debug:
                print(f"Input: {inp}")
            position = position + 2

        # output
        elif opcode == 4:
            output = int_code[position + 1]
            int_code[0] = int_code[output]
            if debug:
                print(f"Ouput: {int_code[output]}")
            position = position + 2
            return (int_code[output], position)

        # jump-if-true
        elif opcode == 5:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            if debug:
                print(f"Jump-If-True: ({input_value_1}, {input_value_2})")
            position = (position + 3, input_value_2)[input_value_1 != 0]

        # jump-if-false
        elif opcode == 6:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            if debug:
                print(f"Jump-If-False: ({input_value_1}, {input_value_2})")
            position = (input_value_2, position + 3)[input_value_1 == 0]

        # less than
        elif opcode == 7:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            if debug:
                print(f"Less Than: ({input_value_1}, {input_value_2})")
            int_code[output_posn] = (0, 1)[input_value_1 < input_value_2]
            position = position + 4

        # equal
        elif opcode == 8:
            input_value_1 = get_param_value(inst, position, 1, int_code)
            input_value_2 = get_param_value(inst, position, 2, int_code)
            output_posn = int_code[position + 3]
            if debug:
                print(f"Equal: ({input_value_1}, {input_value_2})")
            int_code[output_posn] = (0, 1)[input_value_1 == input_value_2] 
            position = position + 4

        # halt
        elif opcode == 99:
            if debug:
                print(f"Halting: {int_code[0]}")
            return (int_code[0], -1)


def get_param_value(inst, position, param_num, int_code):
    param = int_code[position + param_num]
    return (param, int_code[param])[get_parameter_modes(inst, param_num) == 0]


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

