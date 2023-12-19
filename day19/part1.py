f = open("day19/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]

instructions = {}

index = 0

def process(parts):
    curr = "in"
    while True:
        if curr == "A":
            sum = 0
            for key in parts:
                sum += parts[key]
            return sum
        if curr == "R":
            return 0
        for instruction in instructions[curr]:
            instruction = instruction.split(':')
            if len(instruction) == 1:
                curr = instruction[0]
                break
            else:
                instruction[0] = instruction[0].split('<')
                if len(instruction[0]) == 1:
                    instruction[0] = instruction[0][0].split('>')
                    comp = instruction[0][0]
                    num = instruction[0][1]
                    if parts[comp] > int(num):
                        curr = instruction[1]
                        break
                    else:
                        continue
                else:
                    comp = instruction[0][0]
                    num = instruction[0][1]
                    if parts[comp] < int(num):
                        curr = instruction[1]
                        break
                    else:
                        continue

while lines[index] != '':
    line = lines[index]
    parts = line.split('{')
    reqs = parts[1].split('}')[0]
    reqs = reqs.split(',')
    instructions[parts[0]] = reqs
    index += 1

index += 1

total = 0
while index < len(lines):
    line = lines[index]
    line = line.strip('{}')
    line = line.split(',')
    parts = {}
    for part in line:
        part = part.split('=')
        parts[part[0]] = int(part[1])
    print(parts)
    total += process(parts)
    print(total)
    index += 1

print(total)