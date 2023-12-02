f = open("day2/input.txt", "r")
lines = f.readlines()

total = 0
for line in lines:
    minimums = {"red": 1,
           "green": 1,
           "blue": 1}
    line = line.split(":")[1].strip()
    sets = line.split(";")
    for set in sets:
        set = set.strip()
        set = set.replace(",", "")
        words = set.split(" ")
        index = 1
        while index < len(words):
            if int(words[index - 1]) > minimums[words[index]]:
                minimums[words[index]] = int(words[index - 1])
            index += 2

    total += minimums["red"] * minimums["green"] * minimums["blue"]

print(total)