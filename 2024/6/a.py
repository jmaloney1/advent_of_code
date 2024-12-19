import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    # Read the grid
    grid = []
    with open("input/input") as f:
        for line in f:
            grid.append(list(line.strip()))
    
    # Now grid is a 2D list where:
    # grid[y][x] gives you the character at position (x,y)
    # Example: print the dimensions
    height = len(grid)
    width = len(grid[0]) if grid else 0
    print(f"Grid dimensions: {width}x{height}")

    # Now we need to find the starting position
    guard_x, guard_y = 0, 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                guard_x, guard_y = x, y
                break
    
    print(f"Guard position: {guard_x}, {guard_y}")

    posn_move = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    guard_char = '^'
    moves = 0

    def print_grid():
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if (x, y) == (guard_x, guard_y):
                    print(guard_char, end='')
                else:
                    print(cell, end='')
            print()

    def check_move(posn_x, posn_y):
        if posn_x < 0 or posn_y < 0 or posn_x >= width or posn_y >= height:
            return True
        return not (grid[posn_y][posn_x] == '#')


    while  guard_x >= 0 and guard_y >= 0 and guard_x < width and guard_y < height:
        if guard_char == '^' and not check_move(guard_x, guard_y-1):
            guard_char = '>'
        
        if guard_char == '>' and not check_move(guard_x+1, guard_y):
            guard_char = 'v'
        
        if guard_char == 'v' and not check_move(guard_x, guard_y+1):
            guard_char = '<'
        
        if guard_char == '<' and not check_move(guard_x-1, guard_y):
            guard_char = '^'

        moves += 1
        grid[guard_y][guard_x] = guard_char
        guard_x, guard_y = guard_x + posn_move[guard_char][0], guard_y + posn_move[guard_char][1]
        print(f"Guard position: {guard_x}, {guard_y}")
        #print_grid()

    print(f"Moves: {moves}")
    arrow_count = 0
    for row in grid:
        arrow_count += sum(1 for cell in row if cell in ['^', '>', 'v', '<'])
    print(f"Arrow count: {arrow_count}")
        

if __name__ == "__main__":
    main()