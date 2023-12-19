f = open("day18/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(' ') for line in lines]

curr = (500, 500)
grid = [['.' for i in range(1000)] for j in range(1000)]
directions = {'R':(0, 1),
              'L':(0, -1),
              'D':(1, 0),
              'U':(-1, 0)}

for line in lines:
    dir = line[0]
    steps = int(line[1])

    for i in range(steps):
        grid[curr[0]][curr[1]] = '#'
        curr = (curr[0] + directions[dir][0], curr[1] + directions[dir][1])

queue = [(0, 0)]
visited = set()

while len(queue) > 0:
    node = queue.pop(0)
    if node in visited:
        continue
    if node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
        continue

    if grid[node[0]][node[1]] == '#':
        continue

    visited.add(node)
    grid[node[0]][node[1]] = '@'
    queue.append((node[0] + 1, node[1]))
    queue.append((node[0] - 1, node[1]))
    queue.append((node[0], node[1] + 1))
    queue.append((node[0], node[1] - 1))

print(sum([row.count('#') for row in grid]) + sum([row.count('.') for row in grid]))