f = open("day16/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

lines = list(zip(*lines))

def count_energised(config):
    
    energised = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    queue = config
    seen = set()

    while len(queue) > 0:
        curr = queue.pop(0)
        pos = curr[0]
        vel = curr[1]
        if (pos, vel) in seen:
            continue

        seen.add((pos, vel))

        if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
            continue

        energised[pos[0]][pos[1]] = 1

        if lines[pos[0]][pos[1]] == ".":
            queue.append(((pos[0] + vel[0], pos[1] + vel[1]), vel))

        elif lines[pos[0]][pos[1]] == "/":
            if vel == (1, 0):
                queue.append(((pos[0], pos[1] - 1), (0, -1)))
            elif vel == (-1, 0):
                queue.append(((pos[0], pos[1] + 1), (0, 1)))
            elif vel == (0, 1):
                queue.append(((pos[0] - 1, pos[1]), (-1, 0)))
            elif vel == (0, -1):
                queue.append(((pos[0] + 1, pos[1]), (1, 0)))
            
        elif lines[pos[0]][pos[1]] == '\\':
            if vel == (1, 0):
                queue.append(((pos[0], pos[1] + 1), (0, 1)))
            elif vel == (-1, 0):
                queue.append(((pos[0], pos[1] - 1), (0, -1)))
            elif vel == (0, 1):
                queue.append(((pos[0] + 1, pos[1]), (1, 0)))
            elif vel == (0, -1):
                queue.append(((pos[0] - 1, pos[1]), (-1, 0)))

        elif lines[pos[0]][pos[1]] == "-":
            if vel[1] == 0:
                queue.append(((pos[0] + vel[0], pos[1]), vel))
            else:
                queue.append(((pos[0] + 1, pos[1]), (1, 0)))
                queue.append(((pos[0] - 1, pos[1] ), (-1, 0)))
        
        elif lines[pos[0]][pos[1]] == "|":
            if vel[0] == 0:
                queue.append(((pos[0], pos[1] + vel[1]), vel))
            else:
                queue.append(((pos[0], pos[1] + 1), (0, 1)))
                queue.append(((pos[0], pos[1] - 1), (0, -1)))

    return sum([sum(row) for row in energised])

log = []

for x in range(len(lines[0])):
    log.append(count_energised([((x, 0), (0, 1))]))
    log.append(count_energised([((x, len(lines) - 1), (0, -1))]))

for y in range(len(lines)):
    log.append(count_energised([((0, y), (1, 0))]))
    log.append(count_energised([((len(lines[0]) - 1, y), (-1, 0))]))

print(max(log))