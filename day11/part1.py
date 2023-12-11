f = open("day11/input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

index = 0
while index < len(lines):
    line = lines[index]
    if all({s == '.' for s in line}):
        lines.insert(index, line)
        index += 1
    index += 1

index = 0
while index < len(lines[0]):
    column = [line[index] for line in lines]
    if all({s == '.' for s in column}):
        for lindex in range(len(lines)):
            line = lines[lindex]
            lines[lindex] = line[:index] + '.' + line[index:]
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
        total += abs(coordinate[0] - other[0]) + abs(coordinate[1] - other[1])

print(total)
