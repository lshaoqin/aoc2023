f = open("day5/input.txt", "r")
lines = f.readlines()

seeds = lines[0].split(' ')
seeds.pop(0)
seeds = [int(seed) for seed in seeds]

index = 3

SEED_TO_SOIL = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    SEED_TO_SOIL[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
SOIL_TO_FERTILIZER = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    SOIL_TO_FERTILIZER[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
FERTILIZER_TO_WATER = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    FERTILIZER_TO_WATER[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
WATER_TO_LIGHT = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    WATER_TO_LIGHT[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
LIGHT_TO_TEMPERATURE = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    LIGHT_TO_TEMPERATURE[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
TEMPERATURE_TO_HUMIDITY = {}
while lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    TEMPERATURE_TO_HUMIDITY[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

index += 2
HUMIDITY_TO_LOCATION = {}
while index < len(lines) and lines[index] != '\n':
    values = lines[index].split(' ')
    values = [int(value) for value in values]
    HUMIDITY_TO_LOCATION[(values[1], values[1] + values[2] - 1)] = (values[0], values[2] - 1)
    index += 1

maps = [SEED_TO_SOIL, SOIL_TO_FERTILIZER, FERTILIZER_TO_WATER, WATER_TO_LIGHT, LIGHT_TO_TEMPERATURE, TEMPERATURE_TO_HUMIDITY, HUMIDITY_TO_LOCATION]

def getLocationRange(ranges, mapNo):
    if mapNo == len(maps):
        return ranges
    
    currMap = maps[mapNo]
    def helper(start, end):
        ranges = []
        while start <= end:
            print(start, end)
            flag = False
            for key in currMap.keys():
                if start <= key[1] and end >= key[0]:
                    flag = True
                    e = max(start, key[0])
                    f = min(end, key[1])
                    ranges.append((e - key[0] + currMap[key][0], f - key[0] + currMap[key][0]))
                    start = f + 1
                    break
            if not flag:
                starts = [key[0] for key in currMap.keys()]
                starts = list(filter(lambda x: x >= start, starts))
                if len(starts) == 0:
                    ranges.append((start - key[0] + currMap[key][0], end - key[0] + currMap[key][0]))
                    start = end + 1
                    break
                ranges.append((start - key[0] + currMap[key][0], min(starts) - 1 - key[0] + currMap[key][0]))
                start = min(starts)
        return ranges
    
    newRanges = []

    for range in ranges:
        newRanges += helper(range[0], range[1])

    print(newRanges)
    return getLocationRange(newRanges, mapNo + 1) 

index = 0
mins = []

while index < len(seeds):
    ranges = getLocationRange([(seeds[index], seeds[index] + seeds[index + 1])], 0)
    mins.append(min(ranges, key = lambda x: x[0])[0])
    index += 2

print(min(mins))
            
            
        
    
