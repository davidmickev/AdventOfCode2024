with open("Day1.txt") as r:
    input = r.read().splitlines()


#Find difference between the min of list1 and min list2
#Add the difference between the lists as the answer

#First make two lists List a,b then sort the lists and find the difference

list1 = []
list2 = []

for line in input:
    text = line.split()
    list1.append(int(text[0]))
    list2.append(int(text[1]))
    
list1.sort()
list2.sort()

#print(type(list1[1]))

total = 0
for i in range(len(list1)):
    difference = int(list1[i])-int(list2[i])
    total += abs(difference)

print(total)
