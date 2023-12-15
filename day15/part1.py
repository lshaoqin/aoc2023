f = open("day15/input.txt", "r")
lines = f.readlines()

line = lines[0]
seqs = line.strip().split(",")

total = 0

for seq in seqs:
    curr = 0
    for char in seq:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    total += curr

print(total)