import copy
import sys


class IntCode:

    def __init__(self, int_code, inputs):
        self.int_code = {position: code for position, code in enumerate(int_code)}
        self.position = 0
        self.inputs = inputs
        self.relative_base = 0

    def read(self, position):
        if position in self.int_code:
            return self.int_code[position]
        else:
            self.int_code[position] = 0
            return 0


def main():
    #int_code = list(map(int, open('input').readline().split(',')))
    int_code = list(map(int, sys.stdin.readline().split(',')))

    code = IntCode(copy.copy(int_code), [2])

    outputs = []
    for output in compute(code, debug=True):
        print(f"Output for feedback loop: {output}")
        outputs.append(output)

    print(outputs)


def compute(int_code: IntCode, debug=False):
    if debug:
        print(int_code.int_code)

    while True:
        if debug:
            print(f"Position: {int_code.position}")

        op_code = get_opcode(int_code)

        # add
        if op_code == 1:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            posn = get_memory_value(3, int_code)
            if debug:
                print(f"Add: ({input_value_1}, {input_value_2}, {posn})")
            int_code.int_code[posn] = input_value_1 + input_value_2
            int_code.position = int_code.position + 4

        # multiply
        elif op_code == 2:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            posn = get_memory_value(3, int_code)
            if debug:
                print(f"Multiply: ({input_value_1}, {input_value_2}, {posn})")
            int_code.int_code[posn] = input_value_1 * input_value_2
            int_code.position = int_code.position + 4

        # input
        elif op_code == 3:
            output_posn = get_memory_value(1, int_code)
            inp = int_code.inputs.pop(0)
            int_code.int_code[output_posn] = inp
            if debug:
                print(f"Input: {inp}")
            int_code.position = int_code.position + 2

        # output
        elif op_code == 4:
            output = get_param_value(1, int_code)
            if debug:
                print(f"Output: {output}")
            int_code.position = int_code.position + 2
            yield output

        # jump-if-true
        elif op_code == 5:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            if debug:
                print(f"Jump-If-True: ({input_value_1}, {input_value_2})")
            int_code.position = (int_code.position + 3, input_value_2)[input_value_1 != 0]

        # jump-if-false
        elif op_code == 6:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            if debug:
                print(f"Jump-If-False: ({input_value_1}, {input_value_2})")
            int_code.position = (int_code.position + 3, input_value_2)[input_value_1 == 0]

        # less than
        elif op_code == 7:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            posn = get_memory_value(3, int_code)
            if debug:
                print(f"Less Than: ({input_value_1}, {input_value_2})")
            int_code.int_code[posn] = (0, 1)[input_value_1 < input_value_2]
            int_code.position = int_code.position + 4

            # equal
        elif op_code == 8:
            input_value_1 = get_param_value(1, int_code)
            input_value_2 = get_param_value(2, int_code)
            output_posn = get_memory_value(3, int_code)
            if debug:
                print(f"Equal: ({input_value_1}, {input_value_2})")
            int_code.int_code[output_posn] = (0, 1)[input_value_1 == input_value_2]
            int_code.position = int_code.position + 4

        # relative base
        elif op_code == 9:
            input_value_1 = get_param_value(1, int_code)
            if debug:
                print(f"Relative base: ({input_value_1})")
            int_code.relative_base = int_code.relative_base + input_value_1
            int_code.position = int_code.position + 2

        # halt
        elif op_code == 99:
            if debug:
                print(f"Halting: {int_code.int_code[0]}")
            return int_code.int_code[0], -1


def get_memory_value(param_num, int_code: IntCode):
    inst = int_code.read(int_code.position)
    param = int_code.read(int_code.position + param_num)

    mode = get_parameter_mode(inst, param_num)
    if mode == 0:
        return param
    elif mode == 2:
        return param + int_code.relative_base


def get_param_value(param_num, int_code: IntCode):
    inst = int_code.read(int_code.position)
    param = int_code.read(int_code.position + param_num)

    mode = get_parameter_mode(inst, param_num)
    if mode == 0:
        return int_code.read(param)
    elif mode == 1:
        return param
    elif mode == 2:
        return int_code.read(int_code.relative_base + param)


def get_opcode(int_code: IntCode):
    inst = int_code.read(int_code.position)
    digits = [int(d) for d in str(inst)]
    l = len(digits)
    return get_digit(digits, l - 2) * 10 + get_digit(digits, l - 1)


def get_parameter_mode(inst, param_posn):
    digits = [int(d) for d in str(inst)]
    l = len(digits)
    return get_digit(digits, l - param_posn - 2)


def get_digit(digits, i):
    return digits[i] if len(digits) > i >= 0 else 0


if __name__ == '__main__':
    main()
