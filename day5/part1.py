f = open("day5/input.txt", "r")
lines = f.readlines()

seeds = lines[0].split(' ')
seeds.pop(0)

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

def getLocation(seed):
    soil = seed
    for key in SEED_TO_SOIL.keys():
        if seed in range(key[0], key[1] + 1):
            soil = SEED_TO_SOIL[key][0] + seed - key[0]
        
    fertilizer = soil
    for key in SOIL_TO_FERTILIZER.keys():
        if soil in range(key[0], key[1] + 1):
            fertilizer = SOIL_TO_FERTILIZER[key][0] + soil - key[0]

    water = fertilizer
    for key in FERTILIZER_TO_WATER.keys():
        if fertilizer in range(key[0], key[1] + 1):
            water = FERTILIZER_TO_WATER[key][0] + fertilizer - key[0]

    light = water
    for key in WATER_TO_LIGHT.keys():
        if water in range(key[0], key[1] + 1):
            light = WATER_TO_LIGHT[key][0] + water - key[0]

    temperature = light
    for key in LIGHT_TO_TEMPERATURE.keys():
        if light in range(key[0], key[1] + 1):
            temperature = LIGHT_TO_TEMPERATURE[key][0] + light - key[0]

    humidity = temperature
    for key in TEMPERATURE_TO_HUMIDITY.keys():
        if temperature in range(key[0], key[1] + 1):
            humidity = TEMPERATURE_TO_HUMIDITY[key][0] + temperature - key[0]

    location = humidity
    for key in HUMIDITY_TO_LOCATION.keys():
        if humidity in range(key[0], key[1] + 1):
            location = HUMIDITY_TO_LOCATION[key][0] + humidity - key[0]

    return location

min = 2**32

for seed in seeds:
    location = getLocation(int(seed))
    if location < min:
        min = location

print(min)
            
            
        
    
