with open("input.txt", "r") as f:
    sequence = f.read().split(",")


def hash(s):
    lres = 0
    for x in s:
        lres += ord(x)
        lres *= 17
        lres %= 256
    return lres


res = 0
for x in sequence:
    res += hash(x)
print(res)

# Part 2

boxes = [[] for _ in range(256)]
for x in sequence:
    key = hash(x[:x.find("=")])

    if "=" in x:
        value = x.split("=")
        wasIn = False
        for i, y in enumerate(boxes[key]):
            if value[0] == y[0]:
                boxes[key][i][1] = value[1]
                wasIn = True
                break
        if not wasIn:
            boxes[key].append(value)
    else:
        value = x[:-1]
        for i in range(len(boxes[key])):
            if boxes[key][i][0] == value:
                del boxes[key][i]
                break



res2 = 0

for i, x in enumerate(boxes):
    for j, y in enumerate(x):
        res2 += (i + 1) * (j + 1) * int(y[1])

print(res2)