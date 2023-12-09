with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]


# Part 1

def next_num(reihe):
    cur = []
    maps = [reihe]
    while True:
        onlyZeros = True
        for i in range(len(reihe) - 1):
            el = reihe[i + 1] - reihe[i]
            if el != 0:
                onlyZeros = False
            cur.append(el)
        maps.append(cur)
        reihe = cur
        cur = []
        if onlyZeros:
            break

    maps[-1].append(0)
    for i in range(len(maps) - 2, -1, -1):
        maps[i].append(maps[i + 1][-1] + maps[i][-1])

    return maps[0][-1]


sum = 0
for x in lines:
    arr = [int(el) for el in x.split()]
    sum += next_num(arr)
print(sum)

# Part 2

def prev_num(reihe):
    cur = []
    maps = [reihe]
    while True:
        onlyZeros = True
        for i in range(len(reihe) - 1):
            el = reihe[i + 1] - reihe[i]
            if el != 0:
                onlyZeros = False
            cur.append(el)
        maps.append(cur)
        reihe = cur
        cur = []
        if onlyZeros:
            break

    maps[-1].insert(0, 0)
    for i in range(len(maps) - 2, -1, -1):
        maps[i].insert(0, maps[i][0] - maps[i + 1][0])

    return maps[0][0]

sum = 0
for x in lines:
    arr = [int(el) for el in x.split()]
    sum += prev_num(arr)
print(sum)