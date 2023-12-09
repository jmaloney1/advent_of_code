from util_2023 import read_input

if __name__ == '__main__':

    input = read_input('test_input_1', strip=True, index=False)

    schematic = [list(i) for i in input]

    for y, row in enumerate(schematic):
        for x, c in enumerate(row):
