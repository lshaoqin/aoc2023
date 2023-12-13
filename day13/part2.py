f = open("day13/input.txt", "r")
lines = f.readlines()

curr = []

def count_different(lst1, lst2):
    count = 0
    for index in range(len(lst1)):
        if lst1[index] != lst2[index]:
            count += 1
    return count

def process():
    for index in range(0, len(curr) - 1):
        count = 0
        currRow = index
        while index + index - currRow + 1 < len(curr) and currRow >= 0:
            count += count_different(curr[currRow], curr[index + index - currRow + 1])
            currRow -= 1
        if count == 1:
            return 100*(index + 1)
    transposed = list(zip(*curr))
    for index in range(0, len(transposed) - 1):
        currRow = index
        count = 0
        while index + index - currRow + 1 < len(transposed) and currRow >= 0:
            count += count_different(transposed[currRow], transposed[index + index - currRow + 1])
            currRow -= 1
        if count == 1:
            return index + 1

total = 0

for line in lines:
    if line == "\n":
        p = process()
        print(p)
        total += p
        curr = []
    else:
        curr.append(line.strip())

print(total)