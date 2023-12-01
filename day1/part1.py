f = open("day1/input.txt", "r")
lines = f.readlines()

def extract_value(line):
    first = 0
    last = 0
    for char in line:
        if char >= '0' and char <= '9':
            first = int(char)
            break

    for char in line[::-1]:
        if char >= '0' and char <= '9':
            last = int(char)
            break
    
    return first * 10 + last

sum = 0
for line in lines:
    sum += extract_value(line)

print(sum)