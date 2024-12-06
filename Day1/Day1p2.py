with open("Day1.txt") as r:
    input = r.read().splitlines()

list1 = {}
list2 = {}

# Multiply the number in the left list times the times it appears in the right list
# Make a map of the right list2 and the occurance per number, if it ex
def map_insert(item, mylist):
    if item in mylist:
        mylist[item]+=1
    else:
        mylist[item]=1


for line in input:
    text = line.split()
    map_insert(text[0],list1)
    map_insert(text[1],list2)

count = 0

for number in list2:
    if list1.get(number) is not None:
        print(number)
        count += int(number) * int(list2.get(number))
        
print(count)