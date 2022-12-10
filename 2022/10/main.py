import util


def run_cycle(cycle, cycle_delta):
    signal_strength = 0
    for c in range(cycle, cycle + cycle_delta):
        if (c - 20) % 40 == 0:
            signal_strength = c * registers['x']
            print(f'{c}: {signal_strength}')
    return signal_strength


if __name__ == '__main__':
    registers = {'x': 1}
    cycle = 1
    signal_strength = 0
    for line in util.read_input('input'):
        command = line.strip().split(' ')
        instruction = command[0]
        match instruction:
            case 'noop':
                signal_strength += run_cycle(cycle, 1)
                cycle += 1
            case 'addx':
                signal_strength += run_cycle(cycle, 2)
                cycle += 2
                registers['x'] += int(command[1])

    print(signal_strength)
