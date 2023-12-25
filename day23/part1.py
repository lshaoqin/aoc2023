f = open("day23/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

queue = [((0, 1), [])]
nextQueue = []
steps = 0

maxSteps = 0

while len(queue) > 0 or len(nextQueue) > 0:
    if len(queue) == 0:
        queue = nextQueue
        nextQueue = []
        steps += 1
    curr = queue.pop()
    visited = curr[1]
    curr = curr[0]
    y = curr[0]
    x = curr[1]
    if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
        continue
    if lines[y][x] == '#':
        continue

    if y == len(lines) - 1 and x == len(lines[0]) - 2:
        maxSteps = steps
        continue

    v = visited.copy()
    v.append((y, x))

    if lines[y][x] == '>':
        if (y, x + 1) not in visited:
            nextQueue.append(((y, x + 1), v))
        continue
    if lines[y][x] == '<':
        if (y, x - 1) not in visited:
            nextQueue.append(((y, x - 1), v))
        continue
    if lines[y][x] == '^':
        if (y - 1, x) not in visited:
            nextQueue.append(((y - 1, x), v))
        continue
    if lines[y][x] == 'v':
        if (y + 1, x) not in visited:
            nextQueue.append(((y + 1, x), v))
        continue

    if (y, x + 1) not in visited:
        nextQueue.append(((y, x + 1), v))
    if (y, x - 1) not in visited:
        nextQueue.append(((y, x - 1), v))
    if (y + 1, x) not in visited:
        nextQueue.append(((y + 1, x), v))
    if (y - 1, x) not in visited:
        nextQueue.append(((y - 1, x), v))

print(maxSteps)