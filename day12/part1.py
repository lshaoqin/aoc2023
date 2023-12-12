from itertools import product

f = open("day12/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(" ") for line in lines]

for line in lines:
    line[1] = line[1].split(",")
    line[1] = [int(x) for x in line[1]]

def is_valid(seq, key):
    seq = seq.split(".")
    seq = list(filter(lambda x: len(x) > 0 and x[0] == "#", seq))
    return len(seq) == len(key) and all([len(seq[i]) == key[i] for i in range(len(key))])

def generate_combinations(x):
    lst = [True, False]
    return [y for y in product(lst, repeat=x)]

total = 0

for lineno, line in enumerate(lines):
    indexes = []
    for i in range(len(line[0])):
        if line[0][i] == "?":
            indexes.append(i)
    combis = generate_combinations(len(indexes))
    for combi in combis:
        seq = line[0]
        for i in range(len(indexes)):
            if combi[i]:
                seq = seq[:indexes[i]] + "#" + seq[indexes[i]+1:]
            else:
                seq = seq[:indexes[i]] + "." + seq[indexes[i]+1:]
        if is_valid(seq, line[1]):
            total += 1
print(total)




