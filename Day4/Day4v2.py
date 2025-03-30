with open("Day4.txt") as r:
    # Read lines and convert each line to a list of characters
    grid = [list(line.strip()) for line in r]

def find_x(grid):
    # Define the pattern to search for (XMAS)
    pattern = 'XMAS'
    pattern_length = len(pattern)
    
    # All 8 possible directions (row, column)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Down-right
        (1, -1),  # Down-left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, 1),  # Up-right
        (-1, -1)  # Up-left
    ]
    
    count = 0
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    
    visited = set()  # To track already-counted patterns

    for i in range(rows):
        for j in range(cols):
            # Check if current character starts the pattern
            if grid[i][j] == pattern[0]:
                # Check all directions
                for di, dj in directions:
                    # Check bounds for the full pattern
                    if (0 <= i + (pattern_length-1)*di < rows and 
                        0 <= j + (pattern_length-1)*dj < cols):
                        # Check remaining characters
                        match = True
                        for k in range(1, pattern_length):
                            if grid[i + k*di][j + k*dj] != pattern[k]:
                                match = False
                                break
                        if match:
                            # Track the starting position and direction
                            match_key = (i, j, di, dj)
                            if match_key not in visited:
                                visited.add(match_key)
                                count += 1
    print(count)

find_x(grid)