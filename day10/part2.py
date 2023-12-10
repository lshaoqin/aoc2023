f = open("day10/input.txt", "r")
lines = f.readlines()

pipes = {'|': [(0, 1), (0, 1), (0, -1), (0, -1)],
         '-': [(1, 0), (1, 0), (-1, 0), (-1, 0)],
         'L': [(-1, 0), (0, -1), (0, 1), (1, 0)],
         'J': [(1, 0), (0, -1), (0, 1), (-1, 0)],
         '7': [(0, -1), (-1, 0), (1, 0), (0, 1)],
         'F': [(0, -1), (1, 0), (-1, 0), (0, 1)]
         }
# Find starting point
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == 'S':
            start = (col, row)
            break
moves = 0
curr = (start[0] + 1, start[1])
direction = (1, 0)
filled = set()
filled.add(start)
filled.add((start[0] + 0.5, start[1]))

while lines[curr[1]][curr[0]] != 'S':
    pipe = lines[curr[1]][curr[0]]
    if pipe == 'S':
        moves += 1
        break
    elif pipe not in pipes:
        print("Error: Invalid pipe encountered")
        break
    elif direction == pipes[pipe][0]:
        nextDir = pipes[pipe][1]
        moves += 1
        filled.add(curr)
        filled.add((curr[0]+nextDir[0]*0.5, curr[1]+nextDir[1]*0.5))
        curr = (curr[0]+nextDir[0], curr[1]+nextDir[1])
        direction = nextDir
    elif direction == pipes[pipe][2]:
        nextDir = pipes[pipe][3]
        moves += 1
        filled.add(curr)
        filled.add((curr[0]+nextDir[0]*0.5, curr[1]+nextDir[1]*0.5))
        curr = (curr[0]+nextDir[0], curr[1]+nextDir[1])
        direction = nextDir
    else:
        print("Error: Invalid pipe encountered")
        break

filled = set((x * 2, y *2) for (x, y) in filled)
filled = set((x + 1, y + 1) for (x, y) in filled)
filled = set((int(x), int(y)) for (x, y) in filled)

x_dim = len(lines[0]) * 2 + 2
y_dim = len(lines) * 2 + 2

empty = set()
all_squares = set((x, y) for x in range(x_dim) for y in range(y_dim))

stack = [(0, 0)]
def contagion(x, y):
    if x < 0 or y < 0 or x >= x_dim or y >= y_dim:
        return  # Out of bounds
    if (x, y) in filled or (x, y) in empty:
        return
    empty.add((x, y))
    stack.append((x + 1, y))
    stack.append((x - 1, y))
    stack.append((x, y + 1))
    stack.append((x, y - 1))

while len(stack) > 0:
    curr = stack.pop()
    contagion(curr[0], curr[1])
    
enclosed = all_squares - filled - empty
enclosed = set(filter(lambda p: p[0] % 2 == 1 and p[1] % 2 == 1, enclosed))

print(len(enclosed))
