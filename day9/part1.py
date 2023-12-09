f = open("day9/input.txt", "r")
lines = f.readlines()

total = 0

for line in lines:
    line = line.strip().split(" ")
    line = [int(x) for x in line]
    seqs = [line]

    index = 0
    while True:
        seq = seqs[index]
        next = []
        for i in range(len(seq)-1):
            next.append(seq[i+1]-seq[i])

        seqs.append(next)

        if all(x == 0 for x in next):
            break
            
        index += 1

    while index > 0:
        seqs[index-1].append(seqs[index-1][-1] + seqs[index][-1])
        index -= 1

    total += seqs[0][-1]

print(total)

    
