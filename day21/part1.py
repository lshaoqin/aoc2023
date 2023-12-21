f = open("day21/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

currQueue = set()
nextQueue = set()
generation = 1

for rowNo, row in enumerate(lines):
    for colNo, char in enumerate(row):
        if char == 'S':
            currQueue.add((rowNo, colNo))

def checkValid(row, col):
    if row < 0 or row >= len(lines):
        return False
    if col < 0 or col >= len(lines[row]):
        return False
    if lines[row][col] == '#':
        return False
    return True

while generation <= 64:
    for row, col in currQueue:
        if checkValid(row - 1, col):
            nextQueue.add((row - 1, col))
        if checkValid(row + 1, col):
            nextQueue.add((row + 1, col))
        if checkValid(row, col - 1):
            nextQueue.add((row, col - 1))
        if checkValid(row, col + 1):
            nextQueue.add((row, col + 1))
    currQueue = nextQueue
    nextQueue = set()
    generation += 1

print(len(currQueue))
