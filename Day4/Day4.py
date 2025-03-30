#TLDR this code is for a different "solution" variant if the input could have completely scrambled letters, initially i thought that words could be in any order and this solution is still very interesting in terms of just creating a occurence map of letters in the grid and returning minimum count which would equal the number of times the full word appeared.

data = []

with open("Day4.txt") as r:
    for line in r:
        data.append(line.strip())
    #input = r.read().splitlines()


# print(len(data))
# print(len(data[0]))
# 140,140 array 

### This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
### you don't merely need to find one instance of XMAS - you need to find all of them
# Idea as you are traversing O(n), add all matching letters (X,M,A,S) entries in map:
# 1) horrizontal ()
# 2) vertical (x,0+y)
# 3) diagonal top-right,
# 4) diagonal bottom-left

horizontal_map = {}
vertical_map = {}
diagonal_map_tl = {}
diagonal_map_tr = {}

x = len(data[0])
y = len(data)

print(x,y)

letters = {'X', 'M', 'A', 'S'}

for row in range(x):
    for col in range(y):
        value = data[row][col]  # Get the letter at (row, col)

        # Only process if the letter is one of X, M, A, S
        if value in letters:
            # Update horizontal map (count per row)
            if row not in horizontal_map:
                horizontal_map[row] = {'X': 0, 'M': 0, 'A': 0, 'S': 0}
            horizontal_map[row][value] += 1

            # Update vertical map (count per column)
            if col not in vertical_map:
                vertical_map[col] = {'X': 0, 'M': 0, 'A': 0, 'S': 0}
            vertical_map[col][value] += 1

            # Update diagonal map (top-left to bottom-right)
            diagonal_id_top_left = row - col
            if diagonal_id_top_left not in diagonal_map_tl:
                diagonal_map_tl[diagonal_id_top_left] = {'X': 0, 'M': 0, 'A': 0, 'S': 0}
            diagonal_map_tl[diagonal_id_top_left][value] += 1

            # Update diagonal map (top-right to bottom-left)
            diagonal_id_top_right = row + col
            if diagonal_id_top_right not in diagonal_map_tr:
                diagonal_map_tr[diagonal_id_top_right] = {'X': 0, 'M': 0, 'A': 0, 'S': 0}
            diagonal_map_tr[diagonal_id_top_right][value] += 1


count = 0

def print_min_letters(map_name, map_data):
    #print(f"Minimum letters for {map_name}:")
    for index, letter_counts in map_data.items():
        min_letter = min(letter_counts, key=letter_counts.get)  # Find the letter with the smallest count

# Print minimum letters for each map
print_min_letters("Horizontal Map", horizontal_map)
print_min_letters("Vertical Map", vertical_map)
print_min_letters("Diagonal Map (Top-Left to Bottom-Right)", diagonal_map_tl)
print_min_letters("Diagonal Map (Top-Right to Bottom-Left)", diagonal_map_tr)

combined_map = horizontal_map | vertical_map | diagonal_map_tl | diagonal_map_tr
for index, letter_counts in combined_map.items():
    # Find the minimum value in the dictionary for the current index
    min_value = min(letter_counts.values())  # Get the smallest count
    count += min_value
    
print(count)    
