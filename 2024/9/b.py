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
    height = len(grid)
    width = len(grid[0]) if grid else 0
    print(f"Grid dimensions: {width}x{height}")

    # Find all non-dot characters and their positions
    char_positions = {}  # Dictionary to store sets of positions for each character
    for y in range(height):
        for x in range(width):
            char = grid[y][x]
            if char != '.':
                if char not in char_positions:
                    char_positions[char] = set()
                char_positions[char].add((x, y))
    
    # Print the positions for each character
    anti_nodes = set()
    for char, positions in char_positions.items():
        print(f"Character '{char}' found at positions: {positions}")

        for x, y in positions:
            for x2, y2 in positions:
                if x != x2 and y != y2:
                    x_offset = x2 - x
                    y_offset = y2 - y

                    # get all anti-nodes in range
                    for i in range(1, 100):
                        anti_nodes.add((x2 + x_offset * i, y2 + y_offset * i))
                    for i in range(1, 100):
                        anti_nodes.add((x2 - x_offset * i, y2 - y_offset * i))

    anti_nodes = set(filter(lambda x: 0 <= x[0] < width and 0 <= x[1] < height, anti_nodes))
    print(len(anti_nodes))

if __name__ == "__main__":
    main()
