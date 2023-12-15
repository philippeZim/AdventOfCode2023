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



with open("Save.txt", "r") as f:
    comp_res = [l.rstrip("\n") for l in f]

for i, x in enumerate(lines):
    ssol = solve(x[0], x[1])
    assert ssol == int(comp_res[i].split()[1])

res = 0
for i, line in enumerate(lines):
    print(i)
    str2 = ((line[0] + "?") * 5)[:-1]
    check2 = []
    for _ in range(5):
        for x in line[1]:
            check2.append(x)
    part2_line = (str2, tuple(check2))
    curRes = solve(part2_line[0], part2_line[1])
    res += curRes
print(res)


