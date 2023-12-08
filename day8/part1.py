f = open("day8/input.txt", "r")
lines = f.readlines()

instructions = lines[0].strip()

mapping = {}

for line in lines[2:]:
    line = line.strip().split("=")
    node = line[0].strip()
    dest1 = line[1][2:5]
    dest2 = line[1][7:10]
    mapping[node] = (dest1, dest2)

currNode = "AAA"
index = 0
count = 0

while currNode != "ZZZ":
    if index >= len(instructions):
        index = 0
    if instructions[index] == "L":
        currNode = mapping[currNode][0]
    else:
        currNode = mapping[currNode][1]
    index += 1
    count += 1

print(count)