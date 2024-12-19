import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    # Read the grid
    grid_original = []
    with open("input/input") as f:
        for line in f:
            grid_original.append(list(line.strip()))
    
    # Now grid is a 2D list where:
    # grid[y][x] gives you the character at position (x,y)
    # Example: print the dimensions
    height = len(grid_original)
    width = len(grid_original[0]) if grid_original else 0
    print(f"Grid dimensions: {width}x{height}")

    # Now we need to find the starting position
    guard_x, guard_y = 0, 0
    for y, row in enumerate(grid_original):
        for x, cell in enumerate(row):
            if cell == "^":
                guard_x, guard_y = x, y
                break

    posn_move = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    def print_grid(grid, posn_x, posn_y):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                print(cell, end='')
            print()

    def valid_move(grid, posn_x, posn_y):
        if posn_x < 0 or posn_y < 0 or posn_x >= width or posn_y >= height:
            return True
        return not (grid[posn_y][posn_x] == '#')
    
    def run_grid(grid, positions, known_loops):
        guard_x, guard_y, guard_char = positions[-1]
        while  guard_x >= 0 and guard_y >= 0 and guard_x < width and guard_y < height:
            if guard_char == '^' and not valid_move(grid, guard_x, guard_y-1):
                guard_char = '>'
            
            if guard_char == '>' and not valid_move(grid, guard_x+1, guard_y):
                guard_char = 'v'
            
            if guard_char == 'v' and not valid_move(grid, guard_x, guard_y+1):
                guard_char = '<'
            
            if guard_char == '<' and not valid_move(grid, guard_x-1, guard_y):
                guard_char = '^'
            
            guard_x, guard_y = guard_x + posn_move[guard_char][0], guard_y + posn_move[guard_char][1]
            if (guard_x, guard_y, guard_char) in known_loops:
                return True, positions, known_loops

            if (guard_x, guard_y, guard_char) in positions:
                loop = positions[positions.index((guard_x, guard_y, guard_char)):]
                return True, positions, loop
            positions = positions + [(guard_x, guard_y, guard_char)]
            #print(f"Guard position: {guard_x}, {guard_y}")
            #print_grid(grid, guard_x, guard_y)

        return False, positions[:-1], []

    


    grid = [row.copy() for row in grid_original]
    _, initial_positions, _ = run_grid(grid, [(guard_x, guard_y, '^')], set())
    print(len(initial_positions))

    known_loops = set()
    positions = []
    for i in range(1, len(initial_positions)):
        x, y, char = initial_positions[i]
        if (x, y) in positions:
            continue
        grid = [row.copy() for row in grid_original]
        grid[y][x] = '#'
        has_loop, _, loop = run_grid(grid, initial_positions[:i], known_loops)

        if has_loop:
            known_loops = known_loops.union(set(loop))
            positions.append((x, y, char))
            print(f"Found loop at {x}, {y}")

            grid = [row.copy() for row in grid_original]

    # unique positions
    print(f"Loop count: {len(set(positions))}")
        

if __name__ == "__main__":
    main()