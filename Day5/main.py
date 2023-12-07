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

# Part 2

# Brute Force -> to slow
"""
seed_ranges = [int(x) for x in lines[0].split()[1:]]

seeds = []
min_location = float('inf')
for i in range(0, len(seed_ranges), 2):
    print(i)
    for j in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]):
        seed = j
        for y in maps:
            seed = maper(y, seed)
        if seed < min_location:
            min_location = seed

res = min(seeds)
print(res)

# Smart approach with ranges
seed_ranges = [int(x) for x in lines[0].split()[1:]]

seeds = []
for i in range(0, len(seed_ranges), 2):
    seeds.append([seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1] - 1])
print(seeds)


def helper2(range1, range2):
    # range1 = [2, 8]
    # range2 = [4, 12]
    # return [4, 8], [2, 3] []
    interSec = [0, 0]
    if range1[1] < range2[0] or range2[1] < range1[0]:
        return []
    temp = [range1[0], range1[1], range2[0], range2[1]]
    temp.sort()

    re1 = temp[1:-1]

    left = [range1[0], re1[0] - 1]
    right = [re1[1] + 1, range1[1]]
    if left[0] > left[1]:
        left = []
    if right[0] > right[1]:
        right = []
    return [re1, left, right]

def create_new_ranges(range, transfer):
    if transfer[1] > range[1] or transfer[1] < range[0] and transfer[1] + (transfer[2] - 1) < range[0]:
        return [range]
    intermediate_result = helper2(range, [transfer[1], transfer[1] + (transfer[2] - 1)])
    res = [x for x in intermediate_result[1:] if x]
    lr = transfer[0] + (intermediate_result[0][0] - transfer[1])
    transfered = [lr, lr + (intermediate_result[0][1] - intermediate_result[0][0])]
    res.append(transfered)
    return res

def create_new_ranges_list(ranges, transfers):
    res = []
    for z1 in transfers:
        pre = []
        for x in ranges:

            cur = create_new_ranges(x, z1)

            for y2 in cur:
                pre.append(y2)

        cur = [tuple(el) for el in cur]
        cur = set(cur)
        res = list(res)
    res.sort(key=lambda z: z[0])
    return res


min_location2 = float('inf')
for cur_maps in maps:
    seeds = create_new_ranges_list(seeds, cur_maps)
    for x in cur_maps:
        print(x)
    print(seeds)
print(seeds)

"""

# Part 2


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


