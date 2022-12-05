import functools
import re
from textwrap import wrap


def move(stacks, amount_to_move, from_stack_id: int, to_stack_id: int):
    moved = stacks[from_stack_id][-amount_to_move:]
    stacks[to_stack_id] += moved[::-1]
    stacks[from_stack_id] = stacks[from_stack_id][:-amount_to_move]

    return stacks


if __name__ == '__main__':
    with open('input') as f:

        stacks = []
        skip_line = False
        for line in f:
            if skip_line:
                skip_line = False
                continue

            # read moves
            if line.strip().startswith('move'):
                amount_to_move, from_stack, to_stack = re.findall('\\d+', line.strip())[:3]
                stacks = move(stacks, int(amount_to_move), int(from_stack) - 1, int(to_stack) - 1)

                continue

            # box lines
            if line.strip().startswith('1'):
                skip_line = True
                continue

            for i, val in enumerate(wrap(line, 4, drop_whitespace=False)):

                if len(stacks) == i:
                    stacks.append('')
                stacks[i] = val.replace(']', '').replace('[', '').strip() + stacks[i]

        print(stacks)
        print(functools.reduce(lambda a, b: a + b, map(lambda s: s[-1], stacks)))

