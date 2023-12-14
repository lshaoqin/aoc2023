f = open("day14/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

def tilt():
    for line in lines:
        ceil = -1

        for index, char in enumerate(line):
            if char == "#":
                ceil = index
            if char == 'O':
                line[index] = '.'
                line[ceil + 1] = 'O'
                ceil += 1

def rev_tilt():
    for line in lines:
        floor = len(line)

        for index in range(len(line) - 1, -1, -1):
            char = line[index]
            if char == "#":
                floor = index
            if char == 'O':
                line[index] = '.'
                line[floor - 1] = 'O'
                floor -= 1

def score(iteration):
    
    height = len(lines)
    total = 0
    for line in lines:
        for char in line:
            if char == "O":
                total += height
        height -= 1

    print(iteration, total)
    return total

prev = 0
differences = []
for iteration in range(1000000):
    lines = list(zip(*lines))
    lines = [list(line) for line in lines]
    tilt()
    lines = list(zip(*lines))
    lines = [list(line) for line in lines]
    tilt()
    lines = list(zip(*lines))
    lines = [list(line) for line in lines]
    rev_tilt()
    lines = list(zip(*lines))
    lines = [list(line) for line in lines]
    rev_tilt()

    sc = score(iteration)
    differences.append(sc - prev)
    prev = sc

    if iteration % 100 == 0:
        print(iteration, differences[-100:])

# Pattern is 10, 5, -3, -4, -5, -2, 9, -3, -7

# 200 is 102500 (-5)

    