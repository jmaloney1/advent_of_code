def run_program(program):
    accum = 0
    pc = 0
    run_list = []
    while pc < len(program):
        if pc in run_list:
             raise Exception()
        op, arg = program[pc]
        run_list.append(pc)
        if op == 'acc':
            accum += arg
        elif op == 'jmp':
            pc += arg - 1

        pc += 1

    return accum


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]
        program = []
        for line in input_list:
            s = line.split(' ')
            op = s[0]
            arg = int(s[1].replace('+', ''))
            program.append((op, arg))

    for i in range(len(program)):
        op, arg = program[i]
        if op == 'nop':
            op = 'jmp'
        elif op == 'jmp':
            op = 'nop'
        else:
            continue

        changed_program = program.copy()
        changed_program[i] = op, arg

        try:
            accum = run_program(changed_program)
            print(accum)
            break
        except Exception as e:
            print("Loop detected")
            continue
