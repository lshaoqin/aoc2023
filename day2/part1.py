f = open("day2/input.txt", "r")
lines = f.readlines()

targets = {"red": 12,
           "green": 13,
           "blue": 14}

total = 0
for gameNo, line in enumerate(lines):
    line = line.split(":")[1].strip()
    sets = line.split(";")
    valid = True
    for set in sets:
        set = set.strip()
        set = set.replace(",", "")
        words = set.split(" ")
        index = 1
        while index < len(words):
            if int(words[index - 1]) > targets[words[index]]:
                valid = False
                break
            index += 2

    if valid:
        total += gameNo + 1

print(total)