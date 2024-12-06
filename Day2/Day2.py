with open("Day2.txt") as r:
    input = r.read().strip().split('\n')

# idea is to not have the current input line abs(a-b) > 3 or = 0. Also for the input to be strictly increasing or decreasing
# can accomplish this by having a set to represent negative and positive outputs, if outside of this bound continue
count = 0
for line in input:
    values = list(map(int, line.split()))
    set1 = set([1, 2, 3])
    set2 = set([-1, -2, -3])
    for i in range(1, len(values)):
        set1.add(values[i] - values[i - 1])
        set2.add(values[i] - values[i - 1])
        
    print("set1: " , set1, "set2: ", set2)

    if len(set1) == 3 or len(set2) == 3:
        count += 1

print(count)
