f = open("day4/input.txt", "r")
lines = f.readlines()

for index in range(len(lines)):
    lines[index] = lines[index].split(':')[1].split('|')

totalScore = 0

def countScore(card, target):
    score = 0
    for num in card:
        if num == '':
            continue
        if num in target:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score

for line in lines:
    totalScore += countScore(line[0].strip().split(' '), line[1].strip().split(' '))

print(totalScore)

