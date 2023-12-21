f = open("day20/input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line.split(" -> ") for line in lines]

# [fr, dest, pulse]
broadcast = []
# {moduleName: [moduleType, destinations[], state]}
# 0 is low pulse, 1 is high pulse
modules = {}

for line in lines:
    if line[0] == "broadcaster":
        broadcast = [(line[0], dest, 0) for dest in line[1].split(", ")]
    else:
        type = line[0][0]
        name = line[0][1:]
        destinations = line[1].split(", ")
        modules[name] = [type, destinations]

for module in modules:
    if modules[module][0] == "%":
        modules[module].append(0)
    if modules[module][0] == "&":
        inputs = {}
        for otherModule in modules:
            if modules[otherModule][1].count(module) > 0:
                inputs[otherModule] = 0
        modules[module].append(inputs)

low = 0
high = 0
pattern = {}
for i in range(10 ** 5):
    queue = broadcast.copy()
    low += 1
    while len(queue) > 0:
        curr = queue.pop(0)
        fr = curr[0]
        dest = curr[1]
        pulse = curr[2]

        if dest not in modules:
            if pulse == 1:
                high += 1
            if pulse == 0:
                low += 1
            continue

        if modules[dest][0] == "%":
            if pulse == 1:
                high += 1
                # Do nothing
            if pulse == 0:
                low += 1
                modules[dest][2] = not modules[dest][2]
                for destination in modules[dest][1]:
                    queue.append((dest, destination, modules[dest][2]))

        if modules[dest][0] == "&":
            if pulse == 1:
                high += 1

            if pulse == 0:
                low += 1

            modules[dest][2][fr] = pulse

            if all(modules[dest][2].values()):
                for destination in modules[dest][1]:
                    queue.append((dest, destination, 0))
            
            else:
                for destination in modules[dest][1]:
                    queue.append((dest, destination, 1))

        if dest == "rg":
            for input in modules[dest][2]:
                if modules[dest][2][input] == 1:
                    if input not in pattern:
                        pattern[input] = [i]
                    else:
                        pattern[input].append(i)

print(pattern)

# rg must be all satisfied.
# for rg to be all satisfied, kd, zf, vg, and gs must be all high

# kd occurs every 3767 iterations, zf every 3779, gs every 3889, vg every 4057
# Answer is LCM(3767, 3779, 3889, 4057)