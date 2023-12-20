f = open("day19/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

instructions = {}

index = 0

while lines[index] != '':
    line = lines[index]
    parts = line.split('{')
    reqs = parts[1].split('}')[0]
    reqs = reqs.split(',')
    instructions[parts[0]] = reqs
    index += 1

total = 0
queue = [({'x': (1, 4000), 'm': (1, 4000), 'a':(1, 4000), 's':(1, 4000)}, 'in', 0)]

while len(queue) > 0:
    parts, curr, index = queue.pop(0)
    if curr == "A":
        sum = 1
        for key in parts:
            sum *= parts[key][1] - parts[key][0] + 1
        total += sum
        continue
    if curr == "R":
        continue
    if index >= len(instructions[curr]):
        continue
    instruction = instructions[curr][index]
    instruction = instruction.split(':')
    if len(instruction) == 1:
        queue.append((parts, instruction[0], 0))
    else:
        instruction[0] = instruction[0].split('<')
        if len(instruction[0]) == 1:
            instruction[0] = instruction[0][0].split('>')
            comp = instruction[0][0]
            num = instruction[0][1]
            if parts[comp][0] > int(num): # Condition is always true
                queue.append((parts, instruction[1], 0))
            elif parts[comp][1] < int(num): # Condition is always false
                queue.append((parts, curr, index + 1))
            else:
                p1 = parts.copy()
                p1[comp] = (int(num) + 1, parts[comp][1])
                queue.append((p1, instruction[1], 0))
                p2 = parts.copy()
                p2[comp] = (parts[comp][0], int(num))
                queue.append((p2, curr, index + 1))
        else:
            comp = instruction[0][0]
            num = instruction[0][1]
            if parts[comp][1] < int(num): # Condition is always true
                queue.append((parts, instruction[1], 0))
            elif parts[comp][0] > int(num): # Condition is always false
                queue.append((parts, curr, index + 1))
            else:
                p1 = parts.copy()
                p1[comp] = (parts[comp][0], int(num) - 1)
                queue.append((p1, instruction[1], 0))
                p2 = parts.copy()
                p2[comp] = (int(num), parts[comp][1])
                queue.append((p2, curr, index + 1))

print(total)