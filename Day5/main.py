with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]

seeds = [int(x) for x in lines[0].split()[1:]]

maps = []
for i in range(2, len(lines)):
    if lines[i] == "":
        continue
    elif "-" in lines[i]:
        maps.append([])
    else:
        ins = lines[i].split()
        maps[-1].append([int(ins[0]), int(ins[1]), int(ins[2])])


def maper(map, num):
    for x in map:
        if x[1] + x[2] > num >= x[1]:
            return x[0] + (num - x[1])
    return num


for i in range(len(seeds)):
    for y in maps:
        seeds[i] = maper(y, seeds[i])

res1 = min(seeds)
print(res1)

# Part 2 (Brute Force to slow)


seed_ranges = [int(x) for x in lines[0].split()[1:]]
seeds = []
for i in range(0, len(seed_ranges), 2):
    seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1] - 1))


def update(inital_Seeds, transforms):
    # seeds = list of tuples [(a, b), ... , (c, d)]
    # transform = list of transforms [[a, b, c], [d, e, f]]
    newRanges = []
    oldRanges = inital_Seeds
    t = []
    for transform in transforms:
        t = []
        for seed in oldRanges:


            m = (max(seed[0], transform[1]), min(seed[1], transform[1] + (transform[2] - 1)))

            if m[0] > seed[1] or m[1] < seed[0]:
                t.append(seed)
                continue
            l = (-1, -1) if m[0] - 1 < seed[0] else (seed[0], m[0] - 1)
            r = (-1, -1) if m[1] + 1 > seed[1] else (m[1] + 1, seed[1])
            newRange = (transform[0] + (m[0] - transform[1]), transform[0] + (m[0] - transform[1]) + (m[1] - m[0]))
            newRanges.append(newRange)
            if not l == (-1, -1):
                t.append(l)
            if not r == (-1, -1):
                t.append(r)
        oldRanges = t
    return newRanges + oldRanges


for cur_maps in maps:
    seeds = update(seeds, cur_maps)
min_location2 = seeds[0][0]
for x in seeds:
    if x[0] < min_location2:
        min_location2 = x[0]
print(min_location2)


