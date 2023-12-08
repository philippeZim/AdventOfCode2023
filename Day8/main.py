with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

lr = lines[0]

lines = lines[2:]

d = dict()
for x in lines:
    sp = x.split()
    key = sp[0]
    val = sp[2][1:-1] + " " + sp[3][:-1]
    d[key] = val


cur = "AAA"
ind = 0
steps = 0
while cur != "ZZZ":
    if ind == len(lr):
        ind = 0
    val = d[cur]
    if lr[ind] == "L":
        cur = val.split()[0]
    elif lr[ind] == "R":
        cur = val.split()[1]
    steps += 1
    ind += 1
print(steps)


# Part 2

starts = []
for x in d:
    if x[2] == "A":
        starts.append(x)

ind = 0
steps = 0
found_Z = 0
distances = [[] for _ in range(len(starts))]
while found_Z < len(starts):
    found_Z = 0
    if ind == len(lr):
        ind = 0
    for i in range(len(starts)):
        val = d[starts[i]]
        if lr[ind] == "L":
            starts[i] = val.split()[0]
        elif lr[ind] == "R":
            starts[i] = val.split()[1]
        if starts[i][2] == "Z":
            distances[i].append(steps)
            found_Z += 1
    if steps == 100_000:
        break
    steps += 1
    ind += 1

patterns = [[] for _ in range(len(starts))]
for i in range(len(distances)):
    for j in range(0, 2, 2):
        patterns[i].append(distances[i][j + 1] - distances[i][j])


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


patterns = [x[0] for x in patterns]

final_lcm = patterns[0]
for i in range(1, len(patterns)):
    final_lcm = lcm(final_lcm, patterns[i])

print(final_lcm)
