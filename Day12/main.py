with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]


def valid(s, b):
    if not s.count("#") == sum(b):
        return False
    ind = 0
    bs = b.copy()
    for i, x in enumerate(s):
        if x == "#":
            bs[ind] -= 1
            if bs[ind] < 0:
                return False
            if i < len(s) - 1:
                if s[i + 1] == ".":
                    if not bs[ind] == 0:
                        return False
                    ind += 1
    if not bs[-1] == 0:
        return False
    else:
        return True


def variations(s, b):
    res = []
    for i, x in enumerate(s):
        if x == "?" and not res:
            el1 = s[:i] + "#" + s[i + 1:]
            el2 = s[:i] + "." + s[i + 1:]
            res.append(el1)
            res.append(el2)
        elif x == "?":
            new_res = []
            for y in res:
                el1 = y[:i] + "#" + y[i + 1:]
                el2 = y[:i] + "." + y[i + 1:]
                new_res.append(el1)
                new_res.append(el2)
            res = new_res

    return list(filter(lambda el: valid(el, b), res))


strings = []
checks = []
for x in lines:
    see = x
    strings.append(x.split()[0])
    checks.append([int(toint) for toint in x.split()[1].split(",")])

lines = list(zip(strings, checks))
# lines[0] = ("??????#?#?#?..???#?.", [6, 2])



# Part 2

def getLines():
    with open("input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f]

    strings = []
    checks = []
    for x in lines:
        see = x
        strings.append(x.split()[0])
        checks.append(tuple([int(toint) for toint in x.split()[1].split(",")]))

    return list(zip(strings, checks))


lines = getLines()

cache = {}
def solve(strSq, check):
    if strSq == "":
        return 1 if check == () else 0
    if check == ():
        return 0 if "#" in strSq else 1
    key = (strSq, check)
    if key in cache:
        return cache[key]
    res = 0
    if strSq[0] in ".?":
        res += solve(strSq[1:], check)
    if strSq[0] in "#?":
        if len(strSq) >= check[0] and "." not in strSq[:check[0]] \
                and (check[0] == len(strSq) or strSq[check[0]] != "#"):
            res += solve(strSq[check[0] + 1:], check[1:])
    cache[key] = res
    return res

res = 0
respart1 = 0
for i, line in enumerate(lines):
    respart1 += len(variations(line[0], list(line[1])))
    str2 = ((line[0] + "?") * 5)[:-1]
    check2 = []
    for _ in range(5):
        for x in line[1]:
            check2.append(x)
    part2_line = (str2, tuple(check2))
    curRes = solve(part2_line[0], part2_line[1])
    res += curRes

print(respart1)
print(res)


