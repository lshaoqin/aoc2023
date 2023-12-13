from itertools import product

f = open("day12/input.txt", "r")
lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(" ") for line in lines]

total = 0

for line in lines:
    line[0] = line[0] + "?" + line[0] + "?" + line[0] + "?" + line[0] + "?" + line[0]

    line[1] = line[1].split(",")
    line[1] = [int(x) for x in line[1]]
    line[1] = line[1] * 5

    solution = ""
    for key in line[1]:
        solution += "#" * key + "."
    dp = [0 for _ in range(len(solution))]
    dp.insert(0, 1)

    for char in line[0]:
        if char == "#":
            for index in range(len(solution) -1, -1, -1):
                key = solution[index]
                if key == "#":
                    dp[index+1] += dp[index]
                    dp[index] = 0
                if key == ".":
                    dp[index+1] = 0
                    dp[index] = 0

        if char == ".":
            for index in range(len(solution) -1, -1, -1):
                key = solution[index]
                if key == "#":
                    dp[index+1] = 0
                    if index != 0 and solution[index-1] == "#":
                        dp[index] = 0
                if key == ".":
                    dp[index+1] += dp[index]
                    dp[index] = 0

        if char == "?":
            for index in range(len(solution) -1, -1, -1):
                key = solution[index]
                if key == "#":
                    dp[index+1] += dp[index]
                    if index != 0 and solution[index-1] == "#":
                        dp[index] = 0

                if key == ".":
                    dp[index+1] += dp[index]
                    dp[index] = 0

    total += dp[-1] + dp[-2]

print(total)


