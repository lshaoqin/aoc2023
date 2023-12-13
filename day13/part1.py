f = open("day13/input.txt", "r")
lines = f.readlines()

curr = []

def list_equals(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for index in range(len(lst1)):
        if lst1[index] != lst2[index]:
            return False
    return True

def process():
    for index in range(0, len(curr) - 1):
        currRow = index
        flag = False
        while index + index - currRow + 1 < len(curr) and currRow >= 0:
            if not list_equals(curr[currRow], curr[index + index - currRow + 1]):
                flag = True
            currRow -= 1
        if not flag:
            return 100*(index + 1)
    transposed = list(zip(*curr))
    for index in range(0, len(transposed) - 1):
        currRow = index
        flag = False
        while index + index - currRow + 1 < len(transposed) and currRow >= 0:
            if not list_equals(transposed[currRow], transposed[index + index - currRow + 1]):
                flag = True
            currRow -= 1
        if not flag:
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