f = open("day22/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines.sort(key=lambda x: int(x.split('~')[0].split(',')[2]))

grid = [[(0, -1) for row in range(10)] for col in range(10)]
dependencies = {}

for index, line in enumerate(lines):
    start = line.split('~')[0]
    end = line.split('~')[1]

    start = start.split(',')
    start = [int(x) for x in start]
    
    end = end.split(',')
    end = [int(x) for x in end]

    diff = [end[0] - start[0], end[1] - start[1], end[2] - start[2]]

    blocks = [(start[0], start[1], start[2])]

    for x in range(diff[0]):
        blocks.append((start[0] + x + 1, start[1], start[2]))

    for y in range(diff[1]):
        blocks.append((start[0], start[1] + y + 1, start[2]))

    maximum = max([grid[x][y][0] for x, y, z in blocks])
    deps = set()
    for x, y, z in blocks:
        if grid[x][y][0] == maximum:
            if grid[x][y][1] != -1:
                deps.add(grid[x][y][1])
        grid[x][y] = (maximum + diff[2] + 1, index)

    dependencies[index] = deps
    
total = 0
for blockNo in range(len(lines)):
    disintegrated = {blockNo}
    for dep in dependencies:
        if len(dependencies[dep]) == 0:
            continue
        if all([x in disintegrated for x in dependencies[dep]]):
            disintegrated.add(dep)

    total += len(disintegrated) - 1

print(total)