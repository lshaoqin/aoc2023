import math

f = open("day6/input.txt", "r")
lines = f.readlines()

times = lines[0].split(':')[1].strip().split(' ')
time = ''.join(times)
time = int(time)
distance = lines[1].split(':')[1].strip().split(' ')
distance = ''.join(distance)
distance = int(distance)

def findCeil():
    low = 0
    high = time
    while low < high:
        mid = (low + high) // 2
        if mid * (time - mid) >= distance:
            low = mid + 1
        else:
            high = mid
    return high - 1

def findFloor():
    low = 0
    high = time
    while low < high:
        mid = (low + high) // 2
        if mid * (time - mid) >= distance:
            high = mid - 1
        else:
            low = mid
    return low + 1

print(findCeil() - findFloor() + 1)