f = open("day15/input.txt", "r")
lines = f.readlines()

line = lines[0]
seqs = line.strip().split(",")

dic = {}

for index in range(256):
    dic[index] = []

def hash(seq):
    curr = 0
    for char in seq:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    return curr

for seq in seqs:
    if '=' in seq:
        box = hash(seq.split('=')[0])
        for index, item in enumerate(dic[box]):
            if item[0] == seq.split('=')[0]:
                dic[box][index] = (seq.split('=')[0], seq.split('=')[1])
                break
        if seq.split('=')[0] not in [i[0] for i in dic[box]]:
            dic[box].append((seq.split('=')[0], seq.split('=')[1]))
    if '-' in seq:
        box = hash(seq.split('-')[0])
        dic[box] = [i for i in dic[box] if i[0] != seq.split('-')[0]]

total = 0

print(dic)

for box in dic:
    for index, item in enumerate(dic[box]):
        total += (box + 1) * (index + 1) * int(item[1])

print(total)