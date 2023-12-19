f = open("day18/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(' ') for line in lines]

curr = (0, 0)
coordinates = [(0, 0)]
dirs = {0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)}

for line in lines:
    inst = line[2]

    steps = int(inst[2:7], 16)
    direction = int(inst[7])
    curr = (curr[0] + steps * dirs[direction][0], curr[1] + steps * dirs[direction][1])
    coordinates.append(curr)


area = 0
extras = 0
for index in range(len(coordinates)):
    c1 = coordinates[index]
    c2 = coordinates[(index + 1) % len(coordinates)]

    area += c1[0] * c2[1] - c1[1] * c2[0]
    extras += abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) 

print(1/2 * abs(area) + extras/2 + 1)


