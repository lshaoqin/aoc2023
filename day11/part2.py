f = open("day11/input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

index = 0
while index < len(lines):
    line = lines[index]
    if all({s == '.' for s in line}):
        lines.insert(index, str('1' * len(line)))
        index += 1
    index += 1

index = 0
while index < len(lines[0]):
    column = [line[index] for line in lines]
    if all({s == '.' or s == '1' for s in column}):
        for lindex in range(len(lines)):
            line = lines[lindex]
            lines[lindex] = line[:index] + '1' + line[index:]
        index += 1
    index += 1

coordinates = []
total = 0

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '#':
            coordinates.append((row, col))
    
for index, coordinate in enumerate(coordinates):
    for other in coordinates[index + 1:]:
        low, high = sorted([coordinate[1], other[1]])
        for col in range(low, high):
            if lines[coordinate[0]][col] == '1':
                total += 10 ** 6 - 1
            else:
                total += 1
        low, high = sorted([coordinate[0], other[0]])
        for row in range(low, high):
            if lines[row][coordinate[1]] == '1':
                total += 10 ** 6 - 1
            else:
                total += 1


print(total)
