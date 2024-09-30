with open("in.txt", "r", encoding="utf-8") as f:
    lines = [l.rstrip() for l in f]

# x, m, a, s
parts = []
instruct = []

second = False
for x in lines:
    if x == "":
        second = True
        continue
    if second:
        parts.append(x)
    else:
        instruct.append(x)


tp = []
for x in parts:
    t = x.replace("{", "").replace("}", "")
    t = t.split(",")
    t = [int(el[2:]) for el in t]
    tp.append(t)
parts = tp.copy()


inst = dict()
for x in instruct:
    k = x[:x.find("{")]
    v = x[x.find("{") + 1:-1].split(",")
    inst[k] = v


vm = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}
def val(part, instr):
    if instr == "R":
        return 0
    if instr == "A":
        return sum(part)
    b = inst[instr]
    for x in b:
        if x == "R":
            return 0
        if x == "A":
            return sum(part)
        if "<" not in x and ">" not in x:
            return val(part, x)

        if x[1] == "<":
            if part[vm[x[:1]]] < int(x[2:x.find(":")]):
                return val(part, x[x.find(":") + 1:])
        else:
            if part[vm[x[:1]]] > int(x[2:x.find(":")]):
                return val(part, x[x.find(":") + 1:])

res = 0
for x in parts:
    res += val(x, "in")
print(res)

# Part 2


paths = [["in"]]
accepted = []

while paths:
    cur = paths.pop()
    last = cur[-1]
    if ":" in last:
        last = last[last.find(":")+1:]
    if last == "R":
        continue
    if last == "A":
        accepted.append(cur + [last])
        continue
    for i, x in enumerate(inst[last]):
        befor = []
        if i > 0:
            for j in range(i):
                old = inst[last][j]
                nes = []
                if ">" in old:
                    nes.append(old[:2].replace(">", "<"))
                    nes.append(str(int(old[2:old.find(":")]) + 1))
                    nes.append(old[old.find(":"):])
                    befor.append("".join(nes))
                else:
                    nes.append(old[:2].replace("<", ">"))
                    nes.append(str(int(old[2:old.find(":")]) - 1))
                    nes.append(old[old.find(":"):])
                    befor.append("".join(nes))
        if x == "A":
            if befor:
                accepted.append(cur + befor + [x])
            else:
                accepted.append(cur + [x])
        elif x == "R":
            continue
        elif befor:
            paths.append(cur + befor + [x])
        else:
            paths.append(cur + [x])


clean_accepted = []

for x in accepted:
    t = []
    for y in x:
        if ":" in y:
            t.append(y)
    clean_accepted.append(t)

res = 0

for x in clean_accepted:
    cur_res = 1
    st = {
        "s": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "x": (1, 4000)
    }
    for y in x:
        n = int(y[2:y.find(":")])
        a, b = st[y[0]]
        if "<" in y:
            if b > n-1:
                st[y[0]] = (a, n-1)
        else:
            if n+1 > a:
                st[y[0]] = (n+1, b)

    for y in st:
        cur_res *= st[y][1] - st[y][0] + 1
    res += cur_res

print()
print(res)



















