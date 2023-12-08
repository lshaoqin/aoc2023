from functools import reduce


f = open("day8/input.txt", "r")
lines = f.readlines()

instructions = lines[0].strip()

mapping = {}

for line in lines[2:]:
    line = line.strip().split("=")
    node = line[0].strip()
    dest1 = line[1][2:5]
    dest2 = line[1][7:10]
    mapping[node] = (dest1, dest2)

currNodes = [key for key in mapping.keys() if key[2] == "A"]
index = 0
count = 0
store = [[] for i in range(len(currNodes))]

while count < 100000:
    if index >= len(instructions):
        index = 0
    if instructions[index] == "L":
        for n in range(len(currNodes)):
            currNodes[n] = mapping[currNodes[n]][0]
    else:
        for n in range(len(currNodes)):
            currNodes[n] = mapping[currNodes[n]][1]
    index += 1
    count += 1
    
    for i in range(len(currNodes)):
        if currNodes[i][2] == "Z":
            store[i].append(count)
    
# Found out from this that the cycle length is constant
for s in store:
    for j in range(len(s) - 1, 0, -1):
        s[j] = s[j] - s[j-1]

def LCM(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, arr)

print(LCM(map(lambda x: x[0], store)))