with open("Day1.txt") as r:
    input = r.read().splitlines()

list1 = []
list2 = []

for line in input:
    text = line.split()
    list1.append(int(text[0]))
    list2.append(int(text[1]))