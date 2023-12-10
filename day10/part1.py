f = open("day10/input.txt", "r")
lines = f.readlines()

pipes = {'|': [(0, 1), (0, 1), (0, -1), (0, -1)],
         '-': [(1, 0), (1, 0), (-1, 0), (-1, 0)],
         'L': [(-1, 0), (0, 1), (0, -1), (1, 0)],
         'J': [(1, 0), (0, 1), (0, -1), (-1, 0)],
         '7': [(0, 1), (-1, 0), (1, 0), (0, -1)],
         'F': [(0, 1), (1, 0), (-1, 0), (0, -1)]
         }
# Find starting point
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == 'S':
            start = (col, row)
            break
moves = 0
curr = start[0] + 1, start[1]
direction = (1, 0)

while lines[curr[1]][curr[0]] != 'S':
    pipe = lines[curr[1]][curr[0]]
    if pipe == 'S':
        moves += 1
        break
    elif pipe not in pipes:
        break
    elif direction == pipes[pipe][0]:
        nextDir = pipes[pipe][1]
        moves += 1
        curr = (curr[0]+nextDir[0], curr[1]-nextDir[1])
        direction = nextDir
    elif direction == pipes[pipe][2]:
        nextDir = pipes[pipe][3]
        moves += 1
        curr = (curr[0]+nextDir[0], curr[1]-nextDir[1])
        direction = nextDir
    else:
        break

print((moves + 1)/2)
