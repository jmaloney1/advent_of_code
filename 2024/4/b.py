def check_for_mas(row, col, lines):
    grid_height = len(lines)
    grid_width = len(lines[0])
    
    if lines[row][col] != 'A':
        return 0

    if row == grid_height - 1 or row == 0 or col == grid_width - 1 or col == 0:
        return 0
        
    found = 0
    if (lines[row-1][col-1] == 'M' and lines[row+1][col+1] == 'S') or (lines[row-1][col-1] == 'S' and lines[row+1][col+1] == 'M'):
        found += 1
        
    if (lines[row+1][col-1] == 'M' and lines[row-1][col+1] == 'S') or (lines[row+1][col-1] == 'S' and lines[row-1][col+1] == 'M'):
        found += 1
            
    return found

def main():
    with open("4/input/input") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        
    total = 0
    for r, line in enumerate(lines):
        for c, _ in enumerate(line):
            found = check_for_mas(r, c, lines)
            if found > 1:
                print(f"Found A at {r} {c} that's part of exactly 2 MAS patterns")
                total += 1

    print(f"Found {total} A's")

if __name__ == "__main__":
    main()