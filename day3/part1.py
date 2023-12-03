f = open("day3/input.txt", "r")
lines = f.readlines()

for index in range(len(lines)):
    lines[index] = [char for char in lines[index] if char != '\n']

total = 0

def process(row, col):
    if row < 0 or row >= len(lines):
        return ''
    if col < 0 or col >= len(lines[row]):
        return ''
    if '0' <= lines[row][col] <= '9':
        num = lines[row][col]
        lines[row][col] = '.'
        return process(row, col - 1) + num + process(row, col + 1)
    return ''

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] != '.' and not lines[row][col].isdigit():
            for rowOffset in [-1, 0, 1]:
                for colOffset in [-1, 0, 1]:
                    ans = process(row + rowOffset, col + colOffset)
                    if ans.isdigit():
                        print(ans)
                        total += int(ans)
            

print(total)
