import re
with open("Day3.txt") as r:
    input = r.read().strip()

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, input, re.DOTALL)

numbers = [(int(x), int(y)) for x, y in matches]

count = 0
for set in numbers:
    count += set[0]*set[1]

print(count)