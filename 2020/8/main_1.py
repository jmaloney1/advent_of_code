if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]
        program = []
        for line in input_list:
            s = line.split(' ')
            op = s[0]
            arg = int(s[1].replace('+', ''))
            program.append((op, arg))

    accum = 0
    pc = 0
    run_list = []
    while pc not in run_list:
        op, arg = program[pc]
        run_list.append(pc)
        if op == 'acc':
            accum += arg
        elif op == 'jmp':
            pc += arg - 1

        pc += 1

    print(accum)

