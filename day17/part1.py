f = open("day17/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [[int(char) for char in line] for line in lines]

# Coordinates: (y, x)
# ((currY, currX), currStep, loss, sameDir, (dirY, dirX))

queue = [((0, 1), 1, 0, 1, (0, 1)), ((1, 0), 1, 0, 1, (1, 0))]
visited = set()

while len(queue) > 0:
    node = queue.pop(0)
    if (node[0], node[3], node[4]) in visited:
        continue
    if node[0] == (len(lines) - 1, len(lines[0]) - 1):
        print(node[2] + lines[node[0][0]][node[0][1]])
        break
    if node[1] < lines[node[0][0]][node[0][1]]:
        queue.append((node[0], node[1] + 1, node[2], node[3], node[4]))
        continue

    visited.add((node[0], node[3], node[4]))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        next = (node[0][0] + direction[0], node[0][1] + direction[1])
        if direction == (-node[4][0], -node[4][1]):
            continue
        if next[0] >= 0 and next[0] < len(lines) and next[1] >= 0 and next[1] < len(lines[0]):
            if node[4] == direction and node[3] >= 3:
                continue
            if node[4] == direction and node[3] < 3:
                queue.append(((next[0], next[1]), 1, node[2] + lines[node[0][0]][node[0][1]], node[3] + 1, direction))
            else:
                queue.append(((next[0], next[1]), 1, node[2] + lines[node[0][0]][node[0][1]], 1, direction))


