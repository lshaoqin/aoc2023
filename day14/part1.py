f = open("day14/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = list(zip(*lines))

total = 0

for line in lines:
    height = len(line)
    heights = []
    minus = 0

    for char in line:
        if char == "#":
            heights.append(height)
            minus += height
        if char == 'O':
            if len(heights) == 0:
                heights.append(len(line))
            else:
                heights.append(heights[-1] - 1)
        height -= 1

    total += sum(heights) - minus

print(total)