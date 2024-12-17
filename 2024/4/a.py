def main():
    with open("4/input/input") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    # Create a grid to mark found positions
    found_positions = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]

    def search_word(row, col, word):
        word_length = len(word)
        grid_height = len(lines)
        grid_width = len(lines[0])
        
        # Horizontal (left to right)
        found = 0
        if (row < grid_height and col + word_length <= grid_width):
            if lines[row][col:col + word_length] == word:
                for i in range(word_length):
                    found_positions[row][col + i] = True
                found += 1

        # Horizontal (right to left)
        if (row < grid_height and col >= word_length - 1):
            # Get the slice and reverse it to compare with the word
            slice_to_check = lines[row][col - word_length + 1:col + 1][::-1]
            if slice_to_check == word:
                for i in range(word_length):
                    found_positions[row][col - i] = True
                found += 1

        # Vertical (top to bottom)
        if (row + word_length <= grid_height and col < grid_width):
            if (lines[row][col] == word[0] and 
                lines[row + 1][col] == word[1] and 
                lines[row + 2][col] == word[2] and 
                lines[row + 3][col] == word[3]):
                for i in range(word_length):
                    found_positions[row + i][col] = True
                found += 1
        # Vertical (bottom to top)
        if (row >= word_length - 1  and col < grid_width):
            if (lines[row][col] == word[0] and 
                lines[row - 1][col] == word[1] and 
                lines[row - 2][col] == word[2] and 
                lines[row - 3][col] == word[3]):
                for i in range(word_length):
                    found_positions[row - i][col] = True
                found += 1

        # Diagonal (top-left to bottom-right)
        if (row + word_length <= grid_height and col + word_length <= grid_width):
            if (lines[row][col] == word[0] and 
                lines[row + 1][col + 1] == word[1] and 
                lines[row + 2][col + 2] == word[2] and 
                lines[row + 3][col + 3] == word[3]):
                for i in range(word_length):
                    found_positions[row + i][col + i] = True
                found += 1

        # Diagonal (bottom-right to top-left)
        if (row >= word_length - 1 and col >= word_length - 1):
            if (lines[row][col] == word[0] and 
                lines[row - 1][col - 1] == word[1] and 
                lines[row - 2][col - 2] == word[2] and 
                lines[row - 3][col - 3] == word[3]):
                for i in range(word_length):
                    found_positions[row - i][col - i] = True
                found += 1

        # Diagonal (top-right to bottom-left)
        if (row + word_length <= grid_height and col >= word_length - 1):
            if (lines[row][col] == word[0] and 
                lines[row + 1][col - 1] == word[1] and 
                lines[row + 2][col - 2] == word[2] and 
                lines[row + 3][col - 3] == word[3]):
                for i in range(word_length):
                    found_positions[row + i][col - i] = True
                found += 1

        # Diagonal (bottom-right to top-left)
        if (row >= word_length - 1 and col + word_length <= grid_width):
            if (lines[row][col] == word[0] and 
                lines[row - 1][col + 1] == word[1] and 
                lines[row - 2][col + 2] == word[2] and 
                lines[row - 3][col + 3] == word[3]):
                for i in range(word_length):
                    found_positions[row - i][col + i] = True
                found += 1

        return found

    found = 0
    for r, line in enumerate(lines):
        for c, _ in enumerate(line):
            f = search_word(r, c, 'XMAS')
            found += f
    
    # Print the grid with dots for unused characters
    print("\nFound words visualization:")
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if found_positions[r][c]:
                print(lines[r][c], end=' ')
            else:
                print('.', end=' ')
        print()
    
    print(f"\nTotal found: {found}")

if __name__ == "__main__":
    main()