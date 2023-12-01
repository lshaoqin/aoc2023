words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

f = open("day1/input.txt", "r")
lines = f.readlines()

def extract_value(line):
    first = 0
    last = 0
    for index in range(len(line)):
        if line[index] >= '0' and line[index] <= '9':
            first = int(line[index])
            break
        if line[index:index+3] in words:
            first = words[line[index:index+3]]
            break
        if line[index:index+4] in words:
            first = words[line[index:index+4]]
            break
        if line[index:index+5] in words:
            first = words[line[index:index+5]]
            break

    # Lazy method, just don't break to get the last one
    for index in range(len(line)):
        if line[index] >= '0' and line[index] <= '9':
            last = int(line[index])
        if line[index:index+3] in words:
            last = words[line[index:index+3]]
        if line[index:index+4] in words:
            last = words[line[index:index+4]]
        if line[index:index+5] in words:
            last = words[line[index:index+5]]
    return first * 10 + last

sum = 0
for line in lines:
    sum += extract_value(line)

print(sum)