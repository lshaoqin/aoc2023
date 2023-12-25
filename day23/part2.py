f = open("day23/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

queue = [((0, 1), None, set())]
nextQueue = []
steps = 0

maxSteps = 0

while len(queue) > 0 or len(nextQueue) > 0:
    if len(queue) == 0:
        queue = nextQueue
        nextQueue = []
        steps += 1
        print(steps)
    curr = queue.pop()
    prev = curr[1]
    visited = curr[2]
    curr = curr[0]
    y = curr[0]
    x = curr[1]
    if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
        continue

    if y == len(lines) - 1 and x == len(lines[0]) - 2:
        maxSteps = steps
        continue

    viable = []

    for next in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
        if next[0] < 0 or next[1] < 0 or next[0] >= len(lines) or next[1] >= len(lines[0]):
            continue
        if lines[next[0]][next[1]] == '#':
            continue
        if next == prev:
            continue
        viable.append(next)
    
    if len(viable) >= 2:
        visited = visited.copy()
        visited.add((y, x))

    for next in viable:
        if next not in visited:
            nextQueue.append((next, (y, x), visited))

print(maxSteps)