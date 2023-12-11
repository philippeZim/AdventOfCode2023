with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]


def expandMatrixHorizontal(m):
    expand = []
    for x in m:
        s = set(x)
        if len(s) == 1 and "#" not in s:
            expand.append(x)
            expand.append(x)
        else:
            expand.append(x)
    return expand


def invertMatrix(m):
    invert = ["" for _ in range(len(m[0]))]
    for i in range(len(m[0])):
        line = ""
        for j in range(len(m)):
            line += m[j][i]
        invert[i] = line
    return invert


hz = expandMatrixHorizontal(lines)
iv = invertMatrix(hz)
vc_ex = expandMatrixHorizontal(iv)
ex = invertMatrix(vc_ex)

galaxies = []
for i in range(len(ex)):
    for j in range(len(ex[0])):
        if ex[i][j] == "#":
            galaxies.append((i, j))

pairs = []

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        pairs.append((galaxies[i], galaxies[j]))

res = 0
for x in pairs:
    res += abs(x[0][0] - x[1][0])
    res += abs(x[0][1] - x[1][1])

print(res)


# Part 2

def getHorizontalLines(m):
    res = []
    for i in range(len(m)):
        s = set(m[i])
        if len(s) == 1 and "#" not in s:
            res.append(i)
    return res


horizontalLines = getHorizontalLines(lines)
verticalLines = getHorizontalLines(invertMatrix(lines))

galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append((i, j))

pairs = []

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        pairs.append((galaxies[i], galaxies[j]))


def expand(n):
    res = 0
    for x in pairs:
        hl = 0
        vl = 0
        for y in horizontalLines:
            if max(x[0][0], x[1][0]) > y > min(x[0][0], x[1][0]):
                hl += 1
        for y in verticalLines:
            if max(x[0][1], x[1][1]) > y > min(x[0][1], x[1][1]):
                vl += 1
        dif1 = abs(x[0][0] - x[1][0]) + (hl * n)
        dif2 = abs(x[0][1] - x[1][1]) + (vl * n)
        res += dif2 + dif1
    return res


final_res = expand(999999)
print(final_res)
