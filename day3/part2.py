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
        # This assumes that there are no numbers next to two gears at once
        lines[row][col] = '.'
        return process(row, col - 1) + num + process(row, col + 1)
    return ''

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == '*':
            ans = []
            for rowOffset in [-1, 0, 1]:
                for colOffset in [-1, 0, 1]:
                    result = process(row + rowOffset, col + colOffset)
                    if result.isdigit():
                        ans.append(result)
            if len(ans) == 2:
                total += int(ans[0]) * int(ans[1])
            

print(total)
