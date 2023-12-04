f = open("day4/input.txt", "r")
lines = f.readlines()

for index in range(len(lines)):
    lines[index] = lines[index].split(':')[1].split('|')

scratchcards = [1 for line in lines]

def countScore(card, target):
    score = 0
    for num in card:
        if num == '':
            continue
        if num in target:
            score += 1
    return score

for index, line in enumerate(lines):
    score = countScore(line[0].strip().split(' '), line[1].strip().split(' '))
    for num in range(score):
        if index + num + 1 < len(scratchcards):
            scratchcards[index + num + 1] += scratchcards[index]

print(sum(scratchcards))

