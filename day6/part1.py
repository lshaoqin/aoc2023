import numpy as np

f = open("day6/input.txt", "r")
lines = f.readlines()

times = lines[0].split(':')[1].strip().split(' ')
times = [int(i) for i in times if i != '']
distance = lines[1].split(':')[1].strip().split(' ')
distance = [int(i) for i in distance if i != '']
ways = [0 for i in range(len(times))]

for index in range(len(times)):
    for way in range(times[index]):
        if (times[index] - way) * way > distance[index]:
            ways[index] += 1
            
print(np.prod(ways))
