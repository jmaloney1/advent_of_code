import util


def run_cycle(cycle, cycle_delta):
    for c in range(cycle, cycle + cycle_delta):
        should_draw = abs(registers['x'] - ((c - 1) % 40)) <= 1
        print(('.', '#')[should_draw], end='')
        if c % 40 == 0:
            print()


if __name__ == '__main__':
    registers = {'x': 1}
    cycle = 1
    for line in util.read_input('input'):
        command = line.strip().split(' ')
        instruction = command[0]
        match instruction:
            case 'noop':
                run_cycle(cycle, 1)
                cycle += 1
            case 'addx':
                run_cycle(cycle, 2)
                cycle += 2
                registers['x'] += int(command[1])

    # print(signal_strength)
