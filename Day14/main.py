with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f]


def rollStones(m):
    res = []
    for x in m:
        lline = [y for y in x]
        lp = 0
        for i, x in enumerate(lline):
            if x == "O":
                lline[lp] = "O"
                lp += 1
                if lp - 1 != i:
                    lline[i] = "."
            elif x == "#":
                lp = i + 1
        res.append("".join(lline))
    return res


def transform_matrix(matrix):
    return [''.join(row) for row in zip(*matrix)]


rotate = transform_matrix(lines)
rolLeft = rollStones(rotate)
tL = transform_matrix(rolLeft)

res = 0

for i, x in enumerate(tL):
    res += x.count("O") * (len(tL) - i)
print(res)


# Part 2

def rollLeft(m):
    res = []
    for x in m:
        lline = [y for y in x]
        lp = 0
        for i, x in enumerate(lline):
            if x == "O":
                lline[lp] = "O"
                lp += 1
                if lp - 1 != i:
                    lline[i] = "."
            elif x == "#":
                lp = i + 1
        res.append("".join(lline))
    return res


def rollRight(m):
    res = []
    for x in m:
        lline = [y for y in x]
        lp = len(lline) - 1
        for i in range(len(lline) - 1, -1, -1):
            if lline[i] == "O":
                lline[lp] = "O"
                lp -= 1
                if lp + 1 != i:
                    lline[i] = "."
            elif lline[i] == "#":
                lp = i - 1
        res.append("".join(lline))
    return res


def rollDown(m):
    res = []
    resArr = [[""] * len(m[0]) for _ in range(len(m))]
    for i in range(len(m[0])):
        lp = len(m) - 1
        for j in range(len(m) - 1, -1, -1):
            if m[j][i] == "O":
                resArr[lp][i] = "O"
                lp -= 1
                if lp + 1 != j:
                    resArr[j][i] = "."
            elif m[j][i] == "#":
                resArr[j][i] = "#"
                lp = j - 1
            else:
                resArr[j][i] = "."
    for x in resArr:
        res.append("".join(x))
    return res


def rollUp(m):
    res = []
    resArr = [[""] * len(m[0]) for _ in range(len(m))]
    for i in range(len(m[0])):
        lp = 0
        for j in range(len(m)):
            if m[j][i] == "O":
                resArr[lp][i] = "O"
                lp += 1
                if lp - 1 != j:
                    resArr[j][i] = "."
            elif m[j][i] == "#":
                resArr[j][i] = "#"
                lp = j + 1
            else:
                resArr[j][i] = "."
    for x in resArr:
        res.append("".join(x))
    return res


def cycle(m):
    mup = rollUp(m)
    ml = rollLeft(mup)
    md = rollDown(ml)
    mr = rollRight(md)
    return mr

c = 0
save = []
dist = []
for i in range(300):
    lines = cycle(lines)
    if i == 200:
        save = lines.copy()
    if lines == save:
        dist.append(i)


target = 999999999

cicle_len = dist[1] - dist[0]
skip = (target - 200) // cicle_len

newStart = 200 + cicle_len * skip


for i in range(target - newStart):
    save = cycle(save)


res = 0

for i, x in enumerate(save):
    res += x.count("O") * (len(save) - i)
print(res)
