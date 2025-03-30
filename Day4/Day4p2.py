with open("Day4.txt") as r:
    # Read lines and convert each line to a list of characters
    grid = [list(line.strip()) for line in r]

# Read the grid from input
rows = len(grid)
if rows == 0:
    print(0)
    exit()

cols = len(grid[0])
count = 0

for i in range(rows - 2):
    for j in range(cols - 2):
        # Check main diagonal (top-left to bottom-right)
        main_diagonal = [
            grid[i][j],
            grid[i+1][j+1],
            grid[i+2][j+2]
        ]
        # Check anti-diagonal (top-right to bottom-left)
        anti_diagonal = [
            grid[i][j+2],
            grid[i+1][j+1],
            grid[i+2][j]
        ]
        s_main = ''.join(main_diagonal)
        s_anti = ''.join(anti_diagonal)
        
        if s_main in {'MAS', 'SAM'} and s_anti in {'MAS', 'SAM'}:
            count += 1

print(count)