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

class Posible:
    def __init__(self, s, groups, cur_chain, found, remaining):
        self.s = s
        self.groups = groups
        self.cur_chain = cur_chain
        self.found = found
        self.remaining = remaining

    def addGroup(self):
        self.groups.append(self.cur_chain)


def isValid2(posibleL, checkL):
    if len(posibleL.groups) > len(checkL):
        return False
    sum_check = sum(checkL)
    if posibleL.found > sum_check:
        return False
    if posibleL.remaining < sum_check - posibleL.found:
        return False
    if not len(posibleL.groups) > len(checkL) - 1 and posibleL.cur_chain > checkL[len(posibleL.groups)]:
        return False
    for li, lx in enumerate(posibleL.groups):
        if lx != checkL[li]:
            return False

    return True


def solve_part2(lline):
    cur_str = lline[0]

    check = lline[1]
    maxHash = cur_str.count("#") + cur_str.count("?")
    all_possible = []
    first = Posible("", [], 0, 0, maxHash)
    all_possible.append(first)

    for i, x in enumerate(cur_str):
        new_all_possible = []
        for j, y in enumerate(all_possible):
            if x == "#":
                y.s += "#"
                y.found += 1
                y.remaining -= 1
                if i == len(cur_str) - 1:
                    y.groups += [y.cur_chain + 1]
                    y.cur_chain = 0
                else:
                    y.cur_chain += 1
            elif x == ".":
                y.s += "."
                if y.cur_chain > 0:
                    if new_all_possible:
                        new_all_possible[j].addGroup()
                    else:
                        all_possible[j].addGroup()
                    y.cur_chain = 0
            else:
                if y.cur_chain > 0:
                    new_pos1 = Posible(y.s + ".", y.groups.copy() + [y.cur_chain], 0, y.found, y.remaining - 1)
                else:
                    new_pos1 = Posible(y.s + ".", y.groups.copy(), 0, y.found, y.remaining - 1)
                if i == len(cur_str) - 1:
                    new_pos2 = Posible(y.s + "#", y.groups.copy() + [y.cur_chain + 1], 0, y.found + 1, y.remaining - 1)
                else:
                    new_pos2 = Posible(y.s + "#", y.groups.copy(), y.cur_chain + 1, y.found + 1, y.remaining - 1)
                if isValid2(new_pos1, check):
                    new_all_possible.append(new_pos1)
                if isValid2(new_pos2, check):
                    new_all_possible.append(new_pos2)
            if not isValid2(y, check):
                all_possible.remove(y)

        if new_all_possible:
            all_possible = new_all_possible.copy()

    print(sorted([cstr.s for cstr in all_possible]))

    return len(all_possible)

"""
res2 = 0
for line in lines:
    solve_part2(line)
"""

res = 0

resSave = ""
for i, x in enumerate(lines):
    var_save = variations(x[0], x[1])
    resSave += str(i) + ", " + str(len(var_save)) + "\n"

with open("Save.txt", "w") as f:
    f.write(resSave)


