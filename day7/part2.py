f = open("day7/input.txt", "r")
lines = f.readlines()

# Element 0 is the hand, element 1 is the bid
lines = [line.strip().split(" ") for line in lines]
mappings = {line[0] : line[1] for line in lines}

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def sort(arr):
    return sorted(arr, key=lambda x: order.index(x[0]) * 14**4 + order.index(x[1]) * 14**3 + order.index(x[2]) * 14**2 + order.index(x[3]) * 14 + order.index(x[4]))

buckets = [[], [], [], [], [], [], []]

for line in lines:
    hand = line[0]
    counts = [0 for i in range(len(order))]

    joker = 0

    for card in hand:
        if card == "J":
            joker += 1
        else:
            counts[order.index(card)] += 1

    counts.sort(reverse=True)

    if counts[0] + joker == 5:
        buckets[0].append(hand)

    elif counts[0] + joker == 4:
        buckets[1].append(hand)

    elif counts[0] + joker == 3 and counts[1] == 2:
        buckets[2].append(hand)

    elif counts[0] + joker == 3:
        buckets[3].append(hand)

    elif counts[0] == 2 and counts[1] + joker == 2:
        buckets[4].append(hand)

    elif counts[0] + joker == 2:
        buckets[5].append(hand)

    else:
        buckets[6].append(hand)

for i in range(len(buckets)):
    buckets[i] = sort(buckets[i])

total = 0
rank = len(lines)

for bucket in buckets:
    for hand in bucket:
        total += rank * int(mappings[hand])
        rank -= 1

print(total)

