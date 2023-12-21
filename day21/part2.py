#Attempted but realised method doesn't work
f = open("day21/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

oddCount = 0
evenCount = 0
oddVisited = set()
evenVisited = set()

total = 0

for rowNo, row in enumerate(lines):
    for colNo, char in enumerate(row):
        if char == 'S':
            evenVisited.add((rowNo, colNo))

def checkValid(row, col):
    if row < 0:
        row = len(lines) - 1
    if col < 0:
        col = len(lines[row]) - 1
    if row >= len(lines):
        row = 0
    if col >= len(lines[row]):
        col = 0
    if lines[row][col] == '#':
        return False
    return (row, col)

for generation in range(26501365):
    visited = evenVisited if generation % 2 == 0 else oddVisited
    prev = oddVisited if generation % 2 == 0 else evenVisited
    for row, col in prev:
        nextSquares = [checkValid(row - 1, col), checkValid(row + 1, col), checkValid(row, col - 1), checkValid(row, col + 1)]
        if checkValid(row - 1, col):
            nextQueue.add(checkValid(row - 1, col))
        if checkValid(row + 1, col):
            nextQueue.add(checkValid(row + 1, col))
        if checkValid(row, col - 1):
            nextQueue.add(checkValid(row, col - 1))
        if checkValid(row, col + 1):
            nextQueue.add(checkValid(row, col + 1))
    currQueue = nextQueue
    nextQueue = set()
    generation += 1

print(len(currQueue))
