import re
with open("Day3.txt") as r:
    input = r.read().strip()

pattern = r"mul\((\d+),(\d+)\)"
pattern2 = r'do\(\)(.*?)don\'t\(\)'

# parse all do() commands
matches = re.findall(pattern2, input, re.DOTALL)

#parse all mul(x,x) operations 
refined = re.findall(pattern, str(matches))
print(refined)

numbers = [(int(x), int(y)) for x, y in refined]

count = 0

# # Calculate the total count 
count = sum(x * y for x, y in numbers)
# nicer way to write this above
# for set in numbers:
#     count += set[0]*set[1]

print(count)
 
